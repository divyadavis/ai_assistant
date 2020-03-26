from typing import Any, Text, Dict, List
import requests, json, custom.conversion, custom.evaluation, custom.weather_action
import array as arr
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class ActionWeather(Action):
    def name(self) -> Text:
        return "action_weather"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("action file called : action_weather")
        res = []
        location = next(tracker.get_latest_entity_values("city_name"), None)
        #obj = custom.weather_action.Weather()
        #res = obj.weatherReports(location)
        #print(res)

        if location is None:
            send_url = "https://api.ipfind.com?ip=49.15.196.100&auth=1741d3b4-a220-4041-9df3-d1e6e6e6c76a"
            response = requests.get(send_url)
            data = response.json()
            lat = data["latitude"]
            lon = data["longitude"]
            url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&APPID=3a1460156ae6d16dc1fa7cc8e986e94e"
            location = data["city"]
        else:
            print("location", location)
            url = "http://api.openweathermap.org/data/2.5/weather?q=" + location + "&APPID=3a1460156ae6d16dc1fa7cc8e986e94e"
        response = requests.get(url)
        data = response.json()
        r = data["main"]
        w = data["wind"]
        
        response = """ Temperature: {} celsius\n\nHumidity: {} %\n\nWind: {} mph\n\nLocation: {}.""".format(round(r["temp"] - 273.15, 3), r["humidity"], w["speed"], location)
        dispatcher.utter_message(response)





class ActionCalculation(Action):

    def name(self) -> Text:
        return "action_calculation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("action file called : action_calculation")
        #print(tracker.latest_message.get("text"))
        #operands = next(tracker.get_latest_entity_values("number"), None)
        #print(operands)
        a = arr.array('d')
        stack = []
        evaluate = []
        i = 96
        j = 0
        prediction = tracker.latest_message["entities"]
        print(prediction)
        #entity_type = prediction['entities'][0]['entity']
        #print(entity_type)
        #print(next((e for e in tracker.latest_message["entities"] if e['entity'] == 'number'), None))
        for x in tracker.latest_message["entities"]:
            if x['value'] in "*-+/()":
                #operator = x['value']
                #print("operator.......", operator)
                stack.append(x['value'])

            else:
                #print(float(x['value']))
                a.append(float(x['value']))
                i = i+1
                stack.append(chr(i))
        #print(a)
        #print(stack)
        obj = custom.conversion.Conversion(len(stack))
        postfix = obj.infixToPostfix(stack)
        #print(postfix)

        for i in postfix:
            if i in "*-+/":
                evaluate.append(i)   
            else:
                #print(i)
                i = a[j]
                j = j + 1
                evaluate.append(i)
       # print(evaluate)
        obj = custom.evaluation.Evaluate(len(evaluate)) 
        result = obj.evaluatePostfix(evaluate)
        dispatcher.utter_message(text="calculating...........")
        dispatcher.utter_message(format(result))
        return 
          
       





































