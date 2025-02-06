**Banking Management System**

Project Description:

The Banking System is a Python-based console application that simulates basic banking operations. It provides functionality for account creation, login, and performing essential banking transactions such as balance inquiry, deposit, and withdrawal. The program maintains user account details and balances in memory for the duration of its execution.

<hr/>

Features:
1. Account Creation:

* Users can create an account by providing their name and a unique 4-digit PIN.
* Each account is initialized with a balance of $0.
2. Login System:

* Users can securely log in using their name and PIN.
* Only valid credentials allow access to banking features.
3. Banking Operations:

4. View Balance: Check the current account balance.
5. Deposit: Add money to the account balance.
6. Withdraw: Deduct money from the account balance (within limits).
7. Logout: Securely exit the account session.
8. Error Handling:

Validates user inputs for choices, deposit amounts, and withdrawal limits.
Prevents invalid operations such as negative deposits or withdrawals exceeding balance.
9. Exit System:

Users can exit the application at any time.

<hr/>

How to Use:

1. Run the program in any Python environment.
2. The program displays a main menu with three options:
* 1. Create Account
* 2. Login
* 3. Exit
3. Follow on-screen instructions to:
* Create an account.
* Log in to an existing account.
* Perform banking operations or exit the application.

Example Usage -

<hr/>

Main Menu:

Welcome to Our Bank.
1. Create Account
2. Login
3. Exit
   
Create Account:

Select an option(1/2/3): 1

Please enter your name: John

Please enter your pin: 1234

Account created Successfully!!, Login to continue.

Login:

Select an option(1/2/3): 2

Please enter your name: John

Please enter your pin: 1234

Login Successful!

Logged-In Options:

Logged In Options:
1. View Balance
2. Deposit
3. Withdraw
4. Logout

<hr/>

Requirements:

* Python 3.x
