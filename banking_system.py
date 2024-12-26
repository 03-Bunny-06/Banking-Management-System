def banking_system():
    print('Welcome to Our Bank.\n1. Create Account\n2. Login\n3. Exit')

    accounts = []
    while True:
        options = [1,2,3]
        choice = int(input('Select an option(1/2/3): '))
        if choice not in options:
            print(f'The {choice} that you have entered is invalid.')
        else:
            if (choice == 1):
                name = input('Please enter you name: ')
                pin = int(input('Please enter your pin: '))
                accounts.append({'name':name, 'pin':pin, 'balance': 0})
                print('Account created Successfully!!, Login to continue.')
            elif (choice == 2):
                name = input('Please enter you name: ')
                pin = int(input('Please enter your pin: '))
                for account in accounts:
                    if account['name'] == name and account['pin'] == pin:
                        is_logged = True
                        logged_account = account
                        print('Login Successful!')
                        while is_logged:
                            print('\nLogged In Options:\n1. View Balance\n2. Deposit\n3. Withdraw\n4. Logout')
                            choices = [1,2,3,4]
                            sub_choice = int(input('Select an option (1/2/3/4): '))
                            if sub_choice not in choices:
                                print(f'The {sub_choice} that you have entered is invalid.')
                            else:
                                if (sub_choice == 1):
                                    print(f"Your current balance is: ${logged_account['balance']:.2f}")
                                elif (sub_choice == 2):
                                    amount = float(input('Enter the amount to deposit: '))
                                    if amount > 0:
                                        logged_account['balance'] += amount
                                        print(f"${amount:.2f} has been deposited. New balance: ${logged_account['balance']:.2f}")
                                    else:
                                        print('Invalid deposit amount.')
                                elif (sub_choice == 3):
                                    amount = float(input('Enter amount to withdraw: '))
                                    if 0 < amount <= logged_account['balance']:
                                        logged_account['balance'] -= amount
                                        print(f"${amount:.2f} has been withdrawn. New balance: ${logged_account['balance']:.2f}")
                                    else:
                                        print('Invalid withdrawl amount.')
                                elif (sub_choice == 4):
                                    print('You have been logged out.')
                                    is_logged = False
                                else:
                                    print('Invalid option. Please try again.')
                                
                    else:
                        print('No Account Found!, Create an account.')
                        break
                
            else:
                print('Thank you for using our banking system. Goodbye!')
                break

banking_system()