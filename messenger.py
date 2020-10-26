import random, schedule, time

from twilio.rest import Client

msg = ["Time to get up",
       "Good morning"
        ]

afternoon = ["Time to take a break",
             "Lunch time remember to eat",
             "Wow look at the time"
            ]

night = ["Getting late now maybe you should sleep",
         "It's nap nap time"
        ]

def send_message(quote_list = msg):
    account_sid = "YOUR_ACCOUNT_SID"
    auth_token = "YOUR_AUTH_TOKEN"
    client = Client(account_sid, auth_token)
    quote = quote_list[random.randint(0, len(quote_list)-1)]
    
    client.messages.create(to="PHONE_NUMBER_YOU_WANT_TO_SEND_TO",
                           from_="YOUR_TWILIO_PHONE_NUMBER",
                           body=quote
                           )

def send_message_afternoon(quote_list = afternoon):
    account_sid = "ACCOUNT_SID"
    auth_token = "YOUR_AUTH_TOKEN"
    client = Client(account_sid, auth_token)
    quote = quote_list[random.randint(0, len(quote_list)-1)]
    
    client.messages.create(to="PHONE_NUMBER_YOU_WANT_TO_SEND_TO",
                           from_="YOUR_TWILIO_PHONE_NUMBER",
                           body=quote
                           )

def send_message_night(quote_list = night):
    account_sid = "YOUR_ACCOUNT_SID"
    auth_token = "YOUR_AUTH_TOKEN"
    client = Client(account_sid, auth_token)
    quote = quote_list[random.randint(0, len(quote_list)-1)]
    
    client.messages.create(to="PHONE_NUMBER_YOU_WANT_TO_SEND_TO",
                           from_="YOUR_TWILIO_PHONE_NUMBER",
                           body=quote
                           )

schedule.every().day.at("09:30").do(send_message, msg)

schedule.every().day.at("12:30").do(send_message_afternoon, afternoon)

schedule.every().day.at("01:30").do(send_message_night, night)

while True:
    schedule.run_pending()
    time.sleep(2)
