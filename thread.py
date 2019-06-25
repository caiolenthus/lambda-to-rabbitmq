# -*- coding: utf-8 -*-
import time
import json
import logging
import requests.exceptions
from boto3.session import Session
import multiprocessing
import pika
import sys
import glob
import errno

#AWS credentials
ACCESS_KEY='myAccess'
SECRET_KEY='mySecret'

#Boto3 session S3
session = Session(aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY)
s3 = session.resource('s3')
bucket = s3.Bucket('myBucket')

#Send to Rabbit
def torabbit(a):
    
#Connect with RabbitMQ
    credentials = pika.PlainCredentials('myLogin', 'myPass')
    parameters = pika.ConnectionParameters('myHost',
                                               5672, 'myChannel', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='myQueue')
    
    #To bytes
    a = bytes(a, 'utf-8')
    channel.basic_publish(exchange='', routing_key='myRoute', body=a)
    #print(str(a.decode('UTF-8')))


#Json Formater
def prepJson(x):
    try:
        fields = {}

        for (k, v) in x.items():
            tmp_dict = {}

            tmp_dict[ str( k ) ] = str( v )
            fields.update( tmp_dict )
            
        torabbit(str(fields))

    except Exception as e:
          
        print(e)

#Obtain files in S3 and pass, 1 to 1, for the preparation of Json
def getList(pre):
    for s3_file in bucket.objects.filter(Prefix="my/folder/"+str(pre)):
        #key = s3_file.key
    
        fp = "[" + s3_file.get()['Body'].read().decode('utf-8') + "]"
    
        j = json.loads(fp)

        for x in j:
            prepJson(x)


processes = []
maxProc = 0

def lambda_handler(event, context):

    maxProc = event['maxProc']
    listRange = event['listRange']
    aux = 0

    for unit in listRange:
        
        if (aux != maxProc):
            p = multiprocessing.Process(target=getList, args=(unit,))
            processes.append(p)
            p.start()
            aux += 1

        for process in processes:
            process.join()

        time.sleep(2)

    return True