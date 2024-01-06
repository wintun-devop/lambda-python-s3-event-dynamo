import json
import urllib.parse
import boto3
import csv
import os

def main(event,context):
    print("eventTesting>>",event)
    body = {
        "message": "Serverless python deployment testing ok!",
    }
    response = {"statusCode": 200, "body": json.dumps(body)}
    print("functionBodyTesting>>",response)
    print("env variable testing>>",os.environ["PROCESS_REGION"])
    print("env variable testing db>>",os.environ["DATABASE_NAME"])
    return response