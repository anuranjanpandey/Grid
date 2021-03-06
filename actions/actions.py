# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_recommended_product"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product = self.get_product()
        dispatcher.utter_message(text=f"You might be interested in buying {product}")

        return [SlotSet('recommended_product', product)]
    
    def get_product(self):
        #geting product from recomender system
        return "Apple M1 chip macbook is at 70% Discount get it prebooked now!!!"
