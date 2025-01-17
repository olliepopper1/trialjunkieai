import random

class EmailManager:
    def __init__(self, domain):
        self.domain = domain

    def generate_unique_email(self, identifier):
        return f'user+{identifier}@{self.domain}'

    def get_disposable_email(self):
        # Placeholder for disposable email logic
        return 'temp_email@example.com'  # Replace with actual disposable email logic

# Example usage
if __name__ == '__main__':
    email_manager = EmailManager('example.com')
    print(email_manager.generate_unique_email(1))
