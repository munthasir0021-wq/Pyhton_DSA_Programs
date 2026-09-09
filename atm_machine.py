def atm_machine():
    balance=10000
    pin=1234


    print("welcome to ATM machine")
    enter_pin = int(input("Enter your pin:"))
    if enter_pin!=pin:
        print("Incorrect pin")
        return
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print("balance is:", balance)
        
        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print("amount deposited successfully.")
        
        elif choice == 3:
            amount = int(input("Enter amount to withdraw: "))

            if amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print("amount withdrawn successfully.")
        
        elif choice == 4:
            print("Thank you for using the ATM.")
            break
        
        else:
            print("Invalid choice. Please try again.")
atm_machine()