
# lambda-to-rabbitmq
Script to extract and process files in S3 and send to a RabbitMQ host, using AWS Lambda Function

**Problem:**
Extract N files from S3 bucket and send them to some database; each file containing at least 14 rows in json unformatted.

**Structure of the project**
**tolambda.py** - standalone script python that invokes lambda function, passing as parameters maximum amount of processes and prefix list S3
**lambda.py** - python script for AWS Lambda which receives json containing list of S3 prefix and number of processes allowed per function call, connects to S3 and processes file by file from the list received.
