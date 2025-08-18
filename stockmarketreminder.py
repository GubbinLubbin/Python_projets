#mv main.py stockmarketreminder.pyFill the commented information according to you
import requests
import datetime
from twilio.rest import Client

# account_ssid=
# auth_token=

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STOCK_API_KEY=
# NEWS_API_KEY=
# STOCK_ENDPOINT = 
# NEWS_ENDPOINT = 

alphavantage_parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":STOCK_API_KEY,
    "outputsize":"compact"
}

alphavantage_response=requests.get(url=STOCK_ENDPOINT,params=alphavantage_parameters)
alphavantage_data=alphavantage_response.json()["Time Series (Daily)"]

Main_data=[values for (keys,values) in alphavantage_data.items()]

opening_value=Main_data[0]["1. open"]
closing_value=Main_data[1]["4. close"]
change=abs(float(opening_value)-float(closing_value))
change_percentage=round((change/float(closing_value))*100)
if(opening_value>closing_value):
    string="Went up by"
else:
    string="Went down by"
if(change_percentage>0.5):
    news_parameters={
        #"apiKey":
        "q":COMPANY_NAME,
    }
    news_data=requests.get(url=NEWS_ENDPOINT,params=news_parameters).json()["articles"][:3]
    all_articles=[f"{string} {change_percentage} \nHeadline:{article['title']}\n\nBrief:{article['description']}" for article in news_data]
    for articles in all_articles:
        client=Client(account_ssid,auth_token)
        message=client.messages.create(body=articles,from_=#,to=#"ur num")
