# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, Restarted

from actions.mail.mail_api import send_email
from actions.utils.city_check import check_location
from actions.zomato.search_restaurants import SearchRestaurants


class ActionSearchRestaurant(Action):

    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        budgetmin = tracker.get_slot("budgetmin")
        budgetmax = tracker.get_slot("budgetmax")
        location = tracker.get_slot("location")
        cuisine = tracker.get_slot("cuisine")
        dispatcher.utter_message(text="Hello World!")
        dispatcher.utter_message(text=budgetmin)
        dispatcher.utter_message(text=budgetmax)
        dispatcher.utter_message(text=location)
        dispatcher.utter_message(text=cuisine)

        global response
        zomato = SearchRestaurants()
        restaurants_length, response = zomato.search_restaurants(location, cuisine, budgetmin, budgetmax)
        dispatcher.utter_message(str(response))


class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        recipient = tracker.get_slot('email')
        top10 = response.head(10)
        print("got this correct")
        send_email(recipient, top10)
        dispatcher.utter_message(text="Please check you inbox")
        return []


class ActionVerfiyLocation(Action):

    def name(self):
        return 'action_verify_location'

    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot("location")
        check = check_location(location)
        return [SlotSet('location', check['location_new']), SlotSet('location_ok', check['location_f'])]


class ActionVerfiyCuisine(Action):
    def name(self):
        return 'action_verify_cuisine'

    def run(self, dispatcher, tracker, domain):
        cuisines_dict = {'american': 1, 'chinese': 25, 'north indian': 50, 'italian': 55, 'mexican': 73,
                         'south indian': 85,
                         'thai': 95}
        cuisine = tracker.get_slot("cuisine")
        return [SlotSet("cuisine_ok", cuisines_dict.has_key(cuisine))]


class ActionVerfiyBudget(Action):

    def name(self):
        return 'action_verify_budget'

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("budget_ok", True)]


class ActionRestarted(Action):
    def name(self):
        return 'action_restart'

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]
