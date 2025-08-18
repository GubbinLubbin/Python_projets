import requests
from twilio.rest import Client
account_sid=#acount sid
auth_token=#accnt token
parameters={
    "lat":#ur lat,
    "lon":#ur  lon,
    "appid":"4b7a7935643335817fdaf63004c5a46e",
    "cnt":4
}
response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
data=response.json()
id_list=[]
for i in range (0,4):
    weather_id=data["list"][i]["weather"][0]["id"]
    id_list.append(weather_id)
for id in id_list:
    if(id<=700):
        will_rain=True
        break
if will_rain:
    client=Client(account_sid,auth_token)
    message=client.messages.create(
        body="It is going to rain",
        from_=#your nuumber,
        to=#target no )
else:
    client=Client(account_sid,auth_token)
    message=client.messages.create(
        body="Hey it aint gonna rain so chill",
        from_=#your number,
        to=#Target number)
print(message.status)