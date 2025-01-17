import imaplib
import email

class EmailVerification:
    def __init__(self, email_user, email_pass):
        self.email_user = email_user
        self.email_pass = email_pass

    def check_verification_email(self, subject_filter):
        mail = imaplib.IMAP4_SSL('imap.gmail.com')  # Change to your email provider's IMAP server
        mail.login(self.email_user, self.email_pass)
        mail.select('inbox')

        result, data = mail.search(None, 'UNSEEN')
        email_ids = data[0].split()

        for e_id in email_ids:
            result, msg_data = mail.fetch(e_id, '(RFC822)')
            msg = email.message_from_bytes(msg_data[0][1])
            if subject_filter in msg['Subject']:
                return msg.get_payload(decode=True).decode()  # Return the email body

        return None

# Example usage
if __name__ == '__main__':
    verifier = EmailVerification('your_email@example.com', 'your_password')
    verification_email = verifier.check_verification_email('Verify your email')
    print(verification_email)
