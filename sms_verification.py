from twilio.rest import Client

class SMSVerification:
    def __init__(self, account_sid, auth_token):
        self.client = Client(account_sid, auth_token)

    def get_latest_sms(self, from_number):
        messages = self.client.messages.list(from_=from_number)
        if messages:
            return messages[0].body  # Return the most recent SMS body
        return None

# Example usage
if __name__ == '__main__':
    # Replace with your Twilio credentials
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    sms_verifier = SMSVerification(account_sid, auth_token)
    latest_sms = sms_verifier.get_latest_sms('your_twilio_number')
    print(latest_sms)
