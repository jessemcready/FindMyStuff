# put_item_wrapper 
import os

def put_item_wrapper(client, user_id, item_name, quantity, location):
    return client.put_item(
        TableName=os.environ['DYNAMODB_TABLE_NAME'],
        Item={
            "userId":{
              "S": user_id
            },
            "item_name": {
              "S": item_name,
            },
            "quantity": {
              "N": f"{quantity}"
            },
            "location":{
              "S": location,
            },
          }
      )