import requests

'''
# part 1
request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
print(response["value"])
'''

location_name = input("Please enter city name: ")
request2 = "https://api.openweathermap.org/data/2.5/weather?q=" + location_name + "&appid=" + "My_API_Key" + "&units=metric"

try:
    response2 = requests.get(request2)
    if response2.status_code == 200:
        json_response2 = response2.json()
        for a in json_response2["weather"]:
            print(
                f"The weather in {location_name} is {a['description']} and the temperature is {json_response2['main']['temp']} degrees")

except requests.exceptions.RequestException as e:
    print("Request could not be completed.")