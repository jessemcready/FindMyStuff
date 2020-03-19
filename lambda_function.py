import boto3
import constants
from get_item import handle_get_item
from put_item import handle_put_item
from remove_item import handle_remove_item
from event_types import handle_launch_request, handle_session_end_request

def lambda_handler(event, context):
    if (event['session']['application']['applicationId'] != os.APPLICATION_ID):
      raise ValueError("Invalid Application ID")
    
    req_type = event['request']['type']
        
    if req_type == constants.LAUNCH_REQUEST:
      return handle_launch_request()
    if req_type == constants.SESSIONS_END_REQUEST:
      return handle_session_end_request()
    
    client = boto3.client('dynamodb')
    response = {}
    intent = event['request']['intent']['name']
    user_id = event['session']['user']['userId']
    
    if intent == constants.GET_ITEM_INTENT:
      response = handle_get_item(event, client, response, user_id)
    elif intent == constants.PUT_ITEM_INTENT:
      response = handle_put_item(event, client, response, user_id)
    elif intent == constants.REMOVE_ITEM_INTENT:
      response = handle_remove_item(event, client, response, user_id)
    else:
      response = handle_launch_request()
  
    return response
