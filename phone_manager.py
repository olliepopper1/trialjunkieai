from twilio.rest import Client

class PhoneManager:
    def __init__(self, account_sid, auth_token, twilio_number):
        self.client = Client(account_sid, auth_token)
        self.twilio_number = twilio_number

    def send_sms(self, to, message):
        message = self.client.messages.create(
            body=message,
            from_=self.twilio_number,
            to=to
        )
        return message.sid

# Example usage
if __name__ == '__main__':
    # Replace with your Twilio credentials
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    twilio_number = 'your_twilio_number'
    phone_manager = PhoneManager(account_sid, auth_token, twilio_number)
    print(phone_manager.send_sms('+1234567890', 'Hello from Twilio!'))
