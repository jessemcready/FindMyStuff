# PutItem controller
import os
from put_item_wrapper import put_item_wrapper
from responses import put_success_response, put_error_response

def handle_put_item(event, client, response, user_id):
    item_name = event['request']['intent']['slots']['item']['value']
    location = event['request']['intent']['slots']['location']['value']
    quantity = event['request']['intent']['slots']['quantity']['value']
    
    res = put_item_wrapper(client, user_id, item_name, quantity, location)
    
    if(res['ResponseMetadata']['HTTPStatusCode'] == 200):
        response = put_success_response(quantity, item_name, location)
    else:
        response = put_error_response(item_name, location)
    
    return response