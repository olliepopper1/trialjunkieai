# Trial Junkie

## Overview
Trial Junkie is a web application designed to help users manage and track their trial subscriptions effectively. The application provides an intuitive interface for users to connect their wallets, search for integrations, and manage their subscriptions seamlessly.

## Features
- **User-friendly Interface**: A modern design that enhances user experience.
- **Wallet Connection**: Easily connect your wallet to manage subscriptions.
- **Integration Search**: Find various integrations to manage your subscriptions.
- **Payment Routing**: Route payments to your wallet seamlessly.
- User-friendly interface with modern design
- Wallet connection functionality
- Search for integrations
- Payment routing to user wallets

## Installation
To run the application locally, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/olliepopper1/trialjunkie.git
   ```
2. Navigate to the project directory:
   ```bash
   cd trialjunkie/automated-trial-platform
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To start the application, run:
```bash
python main.py
```

## Account Creation Flow
The application allows users to create accounts for various services, including Netflix and Hulu. Here’s how the flow works:
1. **User Input**: The user is prompted to enter the service they want to create an account for (e.g., Netflix or Hulu), along with their username and password.
2. **Service Selection**: The application determines which service the user wants to create an account for based on their input.
3. **Account Creation Logic**: The application uses the `AccountCreator` class to handle the account creation process, navigating to the respective signup pages and submitting the required information.
4. **Trial Management**: After successfully creating the account, the application adds a trial for the user using the `TrialManager`.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
