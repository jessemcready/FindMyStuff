# remove item intent 
import os
from get_item_wrapper import get_item_wrapper
from put_item_wrapper import put_item_wrapper
from responses import get_quantity_response, remove_success_response, remove_error_response

def handle_remove_item(event, client, response, user_id):
    item_name = event['request']['intent']['slots']['item']['value']
    quantity_removed = int(event['request']['intent']['slots']['quantity']['value'])
    
    res = get_item_wrapper(client, item_name, user_id)
    
    if(res['ResponseMetadata']['HTTPStatusCode'] == 200 and ('Item' in res)):
        quantity = int(res['Item']['quantity']['N'])
        location = res['Item']['location']['S']
        if quantity >= quantity_removed:
            quantity -= quantity_removed
        else:
            return get_quantity_response(quantity, item_name)
    
    put_res = put_item_wrapper(client, user_id, item_name, quantity, location)
    
    if(res['ResponseMetadata']['HTTPStatusCode'] == 200):
        response = remove_success_response(quantity_removed, item_name, location, quantity)
    else:
        response = remove_error_response(quantity_removed, item_name)
    
    return response