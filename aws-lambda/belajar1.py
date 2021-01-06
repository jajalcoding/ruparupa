import json


def lambda_handler(event, context):
    # TODO implement
    nilai1 = event.get('key1')
    nilai2 = event.get('key2')    
    return {
        'statusCode': 200,
        'body': "So you put nilai1="+nilai1+" and nilai2="+nilai2
        
    }

'''
saved test event data :

{
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}

Execution Result :

Response:
{
  "statusCode": 200,
  "body": "So you put nilai1=value1 and nilai2=value2"
}

Request ID:
"0c303512-d55c-495a-bc5d-fc8a711e2b10"

Function logs:
START RequestId: 0c303512-d55c-495a-bc5d-fc8a711e2b10 Version: $LATEST
END RequestId: 0c303512-d55c-495a-bc5d-fc8a711e2b10
REPORT RequestId: 0c303512-d55c-495a-bc5d-fc8a711e2b10	Duration: 2.16 ms	Billed Duration: 100 ms	Memory Size: 128 MB	Max Memory Used: 48 MB	Init Duration: 124.41 ms	


'''
