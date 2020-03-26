import requests

class Weather:
    def _init_(self):
        self.lst = []

    def weatherReports(self, location):
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
        lst.append(r["temp"]).append(r["humidity"]).append(w["speed"]).append(location)
        return lst
