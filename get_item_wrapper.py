# client.get_item wrapper file
import os

def get_item_wrapper(client, item_name, user_id):
    return client.get_item(
        TableName=os.environ['DYNAMODB_TABLE_NAME'],
        Key={
          "item_name":{
            "S": item_name
          },
          "userId": {
            "S": user_id
          }
        }
    )