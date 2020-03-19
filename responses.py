# acceptable responses

def get_success_response(quantity, item_name, location):
    return {
            "version": "1.0",
            "response": {
                "outputSpeech": {
                  "type": "PlainText",
                  "text": f"You have {quantity} {item_name} located in {location}!"            
                },
              "shouldEndSession": "false"
            }
          }
          
def get_error_response(item_name):
    return {
          "version": "1.0",
          "response": {
              "outputSpeech": {
                "type": "PlainText",
                "text": f"{item_name} not found, please try another item."            
              },
            "shouldEndSession": "false"
          }
        }

def get_quantity_response(quantity, item_name):
    return {
                "version": "1.0",
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": f"There are only {quantity} {item_name} left, try again."            
                    },
                "shouldEndSession": "false"
                }
            }
            
def put_success_response(quantity, item_name, location):
    return {
          "version": "1.0",
          "response": {
              "outputSpeech": {
                "type": "PlainText",
                "text": f"{quantity} {item_name} has been placed in {location}!"            
              },
            "shouldEndSession": "false"
          }
        }
        
def put_error_response(item_name, location):
    return {
          "version": "1.0",
          "response": {
              "outputSpeech": {
                "type": "PlainText",
                "text": f"Could not add {item_name} to {location}, please try again."            
              },
            "shouldEndSession": "false"
          }
        }
        
def remove_success_response(quantity_removed, item_name, location, quantity):
    return {
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": f"{quantity_removed} {item_name} has been removed from {location}! You have {quantity} left."            
                },
                "shouldEndSession": "false"
            }
        }
        
def remove_error_response(quantity_removed, item_name):
    return {
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": f"Could not remove {quantity_removed} {item_name}, please try again later."            
                },
                "shouldEndSession": "false"
            }
        }