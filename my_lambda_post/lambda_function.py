import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Student')

def lambda_handler(event, context):

    trans = {}

    try :
        query  = event['body']

        data = json.loads(query)

        for keys, val in data.items():
            trans[keys] = val

        table.put_item(Item=trans)

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
        'body':json.dumps({"msg":"Item Inserted Successfully"})
    }
