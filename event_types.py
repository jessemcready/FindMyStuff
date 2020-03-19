# LaunchRequest controller
def handle_launch_request():
    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
              "type": "PlainText",
              "text": "What can I help you find?"            
            },
          "shouldEndSession": "false"
        }
      }
      
def handle_session_end_request():
    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
              "type": "PlainText",
              "text": "Have a great day."            
            },
          "shouldEndSession": "true"
        }
      }