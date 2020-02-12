import os
import dialogflow_v2 as dialogflow
from dialogflow_v2.types import TextInput, QueryInput
from google.api_core.exceptions import InvalidArgument
from google.protobuf.json_format import MessageToDict

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/Users/aarondelossantos/Documents/DialogueflowKey/SimpleassistantKey.json'

DIALOGFLOW_PROJECT_ID = 'simpleassistant-mwxwbe'
DIALOGFLOW_LANGUAGE_CODE = 'en-US'
SESSION_ID = 'me'

text_to_be_analyzed = "testing"

session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

def askBotResponse(text):
    text_input = dialogflow.types.TextInput(text=text, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
        # Allow the variables to be called from outside
        global detectedIntent, confidence, reply, action, requiredParamsPresent, replyParams
        detectedIntent = response.query_result.intent.display_name
        confidence = response.query_result.intent_detection_confidence
        reply = response.query_result.fulfillment_text
        action = response.query_result.action
        requiredParamsPresent = response.query_result.all_required_params_present
        replyParams = MessageToDict(response.query_result.parameters)
    except InvalidArgument:
        # raise exception
        return("Unable to process")