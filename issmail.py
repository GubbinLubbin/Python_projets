from datetime import datetime
import requests
import time
import smtplib
my_gmail=#"Your gmail"
password=#"Create password with app passwords in gmail"
my_lat=#YOur latitude
my_lng=#YOur longitude
def is_night():
    parameters={
        "lat":my_lat,
        "lng":my_lng,
        "formatted":0}
    response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data=response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now=datetime.now()
    if(sunrise>=time_now.hour()>=sunset):
        return True


def is_iss_overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()

    iss_lng=float(data["iss_position"]["longitude"])
    iss_lat=float(data["iss_position"]["latitude"])

    if(my_lng-5<=iss_lng<=my_lng+5 or my_lat-5<=iss_lat<=my_lat+5):
        return True
while True:
    time.sleep(60)
    if(is_iss_overhead() and is_night()):
        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_gmail,password=password)
        connection.sendmail(from_addr=my_gmail,to_addrs=#"Target gmail",msg="Subject:Regarding iss position\n\nLook up iss is up ")
