from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionShow(Action):

    def name(self) -> Text:
        return "action_show"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("action file called : action_show")
        #dispatcher.utter_message("leave type details:")
        tmp = tracker.get_slot("department_name")
        dispatcher.utter_message(tmp)
        tmp = next(tracker.get_latest_entity_values("department_name"), None)
        #print(tmp)
        return







class ActionLocation(Action):

    def name(self) -> Text:
        return "action_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("action file called : action_location")
        #department = tracker.get_slot("department_name")
        dispatcher.utter_message(text="Bengaluru")

        return 

       







"""

        department = tracker.get_slot('department_name')
        dispatcher.utter_message("you want to know something related to {} team".format(department))

        return [SlotSet("department_name",department)]



      cuisine = tracker.get_slot('cuisine')
      q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)
      result = db.query(q)

      return [SlotSet("matches", result if result is not None else [])]













"""
