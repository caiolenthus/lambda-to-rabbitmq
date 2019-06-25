
# lambda-to-rabbitmq [![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)  [![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)
Script to extract and process files in S3 and send to a RabbitMQ host, using AWS Lambda Function

**Problem:**
Extract N files from S3 bucket and send them to some database; each file containing at least 14 rows in json unformatted.

**Structure of the project**
**tolambda.py** Standalone script python. Invokes lambda function, passing as parameters maximum amount of processes and prefix list S3
**lambda.py** Python script for AWS Lambda. Receives Json containing list of S3 prefix and number of processes allowed per function call, connects to S3 and processes file by file from the list received.

**Requiriments:**
- Python 3.7.3
- pip3

**Relevants links**v
- [ AWS Lambda Deployment Package in Python](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html) 
- [Multiprocessing ](https://docs.python.org/3/library/multiprocessing.html)
