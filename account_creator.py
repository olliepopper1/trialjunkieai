from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class AccountCreator:
    def __init__(self, proxy=None):
        options = webdriver.ChromeOptions()
        if proxy:
            options.add_argument(f'--proxy-server={proxy}')
        self.driver = webdriver.Chrome(options=options)

    def create_account(self, service_url, user_data):
        self.driver.get(service_url)
        time.sleep(2)  # Wait for the page to load

        # Example for filling out a registration form
        self.driver.find_element(By.NAME, 'username').send_keys(user_data['username'])
        self.driver.find_element(By.NAME, 'email').send_keys(user_data['email'])
        self.driver.find_element(By.NAME, 'password').send_keys(user_data['password'])

        # Submit the form
        self.driver.find_element(By.NAME, 'submit').click()
        time.sleep(5)  # Wait for the account creation to process

        # Handle any verification logic here
        print('Account created successfully!')

    def close(self):
        self.driver.quit()

# Example usage
if __name__ == '__main__':
    creator = AccountCreator()
    user_info = {'username': 'testuser', 'email': 'testuser@example.com', 'password': 'securepassword'}
    creator.create_account('https://example.com/signup', user_info)
    creator.close()
