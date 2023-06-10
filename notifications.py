from twilio.rest import Client

# Twilio account credentials
account_sid = 'AC0639fdc23e17c0a8a9f82478d2230012'
auth_token = 'cd98711a3083638d5614c1d47ba104f0'
from_phone_number = '+13613019593'

# Create a Twilio client
client = Client(account_sid, auth_token)    

# Function to send a text message
def send_text_message(to_phone_number, message):
    message = client.messages.create(
        body=message,
        from_=from_phone_number,
        to=to_phone_number
    )
    print(f"Message sent: {message.sid}")
