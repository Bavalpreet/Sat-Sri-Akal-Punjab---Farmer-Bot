# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from typing import Any, Text, Dict, List
import urllib.request, json
import os
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# from fuzzywuzzy import fuzz
# from textblob import TextBlob

# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

class ActionGeneral(Action):

    def name(self) -> Text:
        return "action_general"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("_"*10 + "Method: action_general" + "_"*10 + "\n")
        _intent=tracker.latest_message['intent'].get('name')
        print(f"Name of the intent is: {_intent}")
        if _intent == "nlu_fallback":
            dispatcher.utter_message(response="utter_please_rephrase", buttons=[{"payload": "", "title": ""}])
        else:
            dispatcher.utter_message(response="utter_" + str(_intent), buttons=[{"payload": "", "title": ""}])
        return []

# class ActionSlotSetter(Action):
#     def name(self) -> Text:
#         return "action_slot_setter"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         buttons = [
#             {"payload":'/ok{"intent_button":"faq-agriculture"}',"title":"Agriculture"},
#             {"payload":'/ok{"intent_button":"faq-horticulture"}',"title":"Horticulture"}
#         ]
#         print(tracker.slots['intent_button'], "------------------------------")
#         if tracker.slots['intent_button'] == None:
#             print("\n","slots value is ",tracker.slots['intent_button'])
#             dispatcher.utter_message(text="Hi! Welcome to Farmerapp chatbot. For any queries related to crop, vegetation, etc, please select a topic from the below options.",buttons=buttons)
#         else:
#             print("\n","Now slots value is ",tracker.slots['intent_button'])
#             dispatcher.utter_message(text="Yes you are good to go")
#         return []

## this code is commented since there is no use of slots in the current architecture
# class ActionSlotSetter(Action):

#     def name(self) -> Text:
#         return "action_slot_setter"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         buttons = [
#             {"payload":'/ok{"intent_button":"faq-agriculture"}',"title":"Agriculture"},
#             {"payload":'/ok{"intent_button":"faq-horticulture"}',"title":"Horticulture"}
#         ]
#         print("_"*10 + "Method: action_slot_setter" + "_"*10 + "\n")
#         print(f"intent_button slot value: {tracker.slots['intent_button']}")
#         dispatcher.utter_message(text="Hi! Welcome to Farmerapp chatbot. For any queries related to crop, vegetation, etc, please select a topic from the below options.",buttons=buttons)
#         return []


class ActionVizFaq(Action):

    def name(self) -> Text:
        return "action_viz_faq"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("_"*10 + "Method: action_faq" + "_"*10 + "\n")

        # To get intent of user message
        _intent = tracker.latest_message['intent'].get('name')
        # To find retrival intent with max confidence
        intent_found = json.dumps(tracker.latest_message['response_selector'][_intent]['ranking'][0]['intent_response_key'], indent=4)
        retrieval_intent_confidence = tracker.latest_message['response_selector'][_intent]['response']['confidence']*100
        print(f"User text: {tracker.latest_message['text']}") # to get user typed message 
        print(f"User Intent: {_intent}")
        print(f"Retrieval intent: {intent_found}")
        print(f"retrieval_intent_confidence: {retrieval_intent_confidence}")

        second_intent_found = json.dumps(tracker.latest_message['response_selector'][_intent]['ranking'][1]['intent_response_key'], indent=4)
        second_retrieval_intent_confidence = tracker.latest_message['response_selector'][_intent]['ranking'][1]['confidence']*100        
        
        if retrieval_intent_confidence < 80:
            dispatcher.utter_message(text="I couldn't understand. Can you please rephrase it?", buttons=[{"payload": "", "title": ""}])
            return []

        intent_found = f'utter_{eval(intent_found)}'
        print(f"After adding utter: {intent_found}")
        dispatcher.utter_message(response = intent_found, buttons=[{"payload": "", "title": ""}]) # use response for defining intent name
        
        # print(retrieval_intent_confidence - second_retrieval_intent_confidence)
        if retrieval_intent_confidence - second_retrieval_intent_confidence <= 5:
            dispatcher.utter_message(text="One more possible solution could be as below", buttons=[{"payload": "", "title": ""}])
            dispatcher.utter_message(response=f'utter_{eval(second_intent_found)}', buttons=[{"payload": "", "title": ""}])
            dispatcher.utter_message(text="Take decison as per your choice", buttons=[{"payload": "", "title": ""}])

        return [] # setting slot values