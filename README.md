# Banking Management System

## Project Description
The Banking System is a Python-based console application that simulates basic banking operations. It provides functionality for account creation, login, and performing essential banking transactions such as balance inquiry, deposit, and withdrawal. The program maintains user account details and balances in memory for the duration of its execution.

## Features
- **Create Account:** Users can create a new bank account with a name and PIN.
- **Login:** Users can log in using their name and PIN.
- **View Balance:** Displays the current balance of the logged-in user.
- **Deposit Money:** Allows users to deposit money into their account.
- **Withdraw Money:** Enables users to withdraw money from their account, ensuring sufficient balance.
- **Logout:** Users can securely log out of their accounts.

## Prerequisites
- Python 3.x

## Installation
1. Clone the repository or copy the script.
2. Run the script using Python:
   ```bash
   python banking_system.py
   ```

## How to Use
1. Run the script and choose an option:
   - **Option 1:** Create an account (enter name and PIN).
   - **Option 2:** Login using an existing account.
   - **Option 3:** Exit the program.
2. If logged in, additional options will be available:
   - View balance
   - Deposit money
   - Withdraw money
   - Logout

## Notes
- The script does not store account data persistently; all data is lost when the script stops running.
- PINs are stored in plaintext; for security, consider encrypting them.
- Enhancements like database integration, transaction history, and security improvements can be added.

