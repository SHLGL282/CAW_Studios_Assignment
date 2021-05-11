import boto3
#from botocore.vendored import requests
import requests
from requests_aws4auth import AWS4Auth

es_host = "https://search-es-instance-new-qpr7u2gcrhz46x6mwduhihjc2a.us-east-2.es.amazonaws.com"
es_index = "metadata"
es_type = "Students"

url = es_host + '/' + es_index + '/' + es_type + '/'

region = 'us-east-2'
service = 'es'

credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

def lambda_handler(event, context):
    print("Event is :", event)
    print("requests has below methods: ", dir(requests))
    for record in event['Records']:
        id = str(record['dynamodb']['Keys']['Name']['S'])
        if record['eventName'] == 'REMOVE':
            res = requests.delete(url + id, auth=awsauth)
        else:
            print("Entered")
            document = record['dynamodb']['NewImage']
            print("document value is:", document)
            print("id value is:", id)
            print("url :", url)
            res = requests.put(url + id, auth=awsauth, json=document, headers={"Content-Type": "application/json"})
            print("Sahil Res is : ", res)

    return {
        'statusCode': 200,
        'body': json.dumps(res)
    }
