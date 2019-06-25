import boto3, json

lambda_client = boto3.client('lambda')

maxProc=[5]
maxFunc = 101
startValue = 15535382
finishValue = 15607037
v1 = startValue
v2 = 0

try:
    while(v2 < finishValue):

        aux = 0
        
        while(aux < maxFunc):
            v2 = v1 + 2 
            
            listRange = list(range(v1, v2 + 1))
            x = {"maxProc" : maxProc, "listRange" : listRange}
            invoke_response = lambda_client.invoke(FunctionName="myLambdaFunction",
                                            InvocationType='Event',
                                            Payload=json.dumps(x))

            v1 = v2
            aux += 1
                       
except Exception as e:
    print(e)
