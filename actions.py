# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, SlotSet, Restarted


class ActionSearchRestaurant(Action):

    def name(self) -> Text:
        return "action_search_restaurants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        budgetmin = tracker.get_slot("budgetmin")
        budgetmax = tracker.get_slot("budgetmax")
        
        location = tracker.get_slot("location")
        cuisine = tracker.get_slot("cuisine")

        dispatcher.utter_message(text="Hello World!")
        dispatcher.utter_message(text=budgetmin)
        dispatcher.utter_message(text=budgetmax)
        dispatcher.utter_message(text=location)
        dispatcher.utter_message(text=cuisine)
        return [SlotSet("restaurant_exists", True)]


class ActionSendEmail(Action):

    def name(self) -> Text:
        return "action_send_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Please check you inbox")

        return []


class ActionVerfiyLocation(Action):

    def name(self) -> Text:
        return "action_verify_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        location = tracker.get_slot("location")

        if location == "Mumbai":
            return [SlotSet("location_ok", True)]
        else:
            return [SlotSet("location_ok", False)]



class ActionVerfiyCuisine(Action):

    def name(self) -> Text:
        return "action_verify_cuisine"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        return [SlotSet("cuisine_ok", True)]

class ActionVerfiyBudget(Action):

    def name(self) -> Text:
        return "action_verify_budget"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        return [SlotSet("budget_ok", True)]

class ActionRestarted(Action): 	
	def name(self):
		return 'action_restart'

	def run(self, dispatcher, tracker, domain):
		return[Restarted()] 