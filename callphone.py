#!/usr/bin/env python3
from twilio.rest import Client
import sys

def make_call():
    # Twilio credentials (replace with actual values or use environment variables)
    account_sid = 'YOUR_TWILIO_ACCOUNT_SID'  # Your Account SID from Twilio
    auth_token = 'YOUR_TWILIO_AUTH_TOKEN'  # Your Auth Token from Twilio
    twilio_number = 'YOUR_TWILIO_PHONE_NUMBER'  # Your Twilio phone number
    to_phone_number = sys.argv[1]  # Destination phone number (from command line argument)

    # Initialize Twilio client
    client = Client(account_sid, auth_token)

    try:
        # Make the call
        call = client.calls.create(
            to=to_phone_number,
            from_=twilio_number,
            url='http://demo.twilio.com/docs/voice.xml'  # This URL provides the default voice response
        )
        print(f"Call initiated! Call SID: {call.sid}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./callphone.py <destination_phone_number>")
    else:
        make_call()
