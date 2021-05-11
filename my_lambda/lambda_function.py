import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Student')

def lambda_handler(event, context):
    try :
        query  = event['queryStringParameters']['query']
        response = table.get_item(Key={'Name':query})
        value = (response['Item'])

    except KeyError as kErr:
        return {
        'statusCode':400,
        'body':json.dumps({"msg":"Item is not availavle in dynamobd"})
        }

    except Exception as err:
        return {
        'statusCode':400,
        'body':json.dumps({"msg":"Something went wrong"})
        }

    return {
        'statusCode':200,
        'body':json.dumps(value)
    }
