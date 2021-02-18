from twilio.rest import Client
from tohide import InfoHiden

account_sid = InfoHiden["NT_SID"]
auth_token = InfoHiden["NT_AUTH_TOKEN"]
PHONE_TWILIO = InfoHiden["NT_PHONE_TWILIO"]
MY_PHONE = InfoHiden["NT_MY_PHONE"]


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, city_from, city_to, price, departure, returned):
        self.client = Client(account_sid, auth_token)
        self.message = self.client.messages \
            .create(
            body=f"\nOnly {price}€ travel from {city_from} to {city_to} Date to go:{departure} Date to return:{returned}.",
            from_=PHONE_TWILIO,
            to=MY_PHONE
        )
        print(self.message.status)
