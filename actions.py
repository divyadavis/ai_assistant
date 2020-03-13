from typing import Any, Text, Dict, List
import requests, json
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
        #tmp = tracker.get_slot("department_name")
        
        tmp = next(tracker.get_latest_entity_values("department_name"), None)

        print("tmp", tmp)

        dispatcher.utter_message(text="you want to know something related to {}".format(tmp))
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

       




class ActionWeather(Action):
     def name(self) -> Text:
        return "action_weather"
     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         print("action file called : action_weather")
        

         location = next(tracker.get_latest_entity_values("city_name"), None)

         print("location", location)

         url = "http://api.openweathermap.org/data/2.5/weather?q=" + "Bengaluru" + "&APPID=3a1460156ae6d16dc1fa7cc8e986e94e"

         print("url :", url)

         response = requests.get(url)

         #print(response)

         data = response.json()

         #print(data["cod"])

         r = data["main"]

         #print("temperature:", r["temp"])
         #print("pressure:", r["pressure"])
         #print("humidity:", r["humidity"])


         response = """ The temperature is {} , The pressure is {}, The humidity is {} %.""".format(r["temp"], r["pressure"], r["humidity"])
        
         dispatcher.utter_message(response)









































"""

        department = tracker.get_slot('department_name')
        dispatcher.utter_message("you want to know something related to {} team".format(department))

        return [SlotSet("department_name",department)]



      cuisine = tracker.get_slot('cuisine')
      q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)
      result = db.query(q)

      return [SlotSet("matches", result if result is not None else [])]



"""
