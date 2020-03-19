# GetItem controller
import os
from get_item_wrapper import get_item_wrapper
from responses import get_success_response, get_error_response

def handle_get_item(event, client, response, user_id):
    item_name = event['request']['intent']['slots']['item']['value']
    
    res = get_item_wrapper(client, item_name, user_id)
      
    if(res['ResponseMetadata']['HTTPStatusCode'] == 200 and ('Item' in res)):
        location = res['Item']['location']['S']
        quantity = res['Item']['quantity']['N']
        
        response = get_success_response(quantity, item_name, location)
    else:
        response = get_error_response(item_name)
    
    return response