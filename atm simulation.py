PIN = int(input("ENTER YOUR PIN: "))

if PIN == 1234:
    balance = 10000  # initial balance

    print("Welcome!")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. EXIT")

    option = int(input("Enter your choice from options 1–4: "))

    if option == 1:
        print("Your current balance is ₹", balance)

    elif option == 2:
        deposit_money = int(input("Enter amount to deposit: "))
        balance += deposit_money
        print("Deposit successful.")
        print("Updated balance: ₹", balance)

    elif option == 3:
        withdrawal_money = int(input("Enter amount to withdraw: "))
        if withdrawal_money > balance:
            print("Insufficient funds.")
        else:
            balance -= withdrawal_money
            print("Withdrawal successful.")
            print("Remaining balance: ₹", balance)

    elif option == 4:
        print("Thank you for using our ATM!")

    else:
        print("Invalid option. Please choose between 1 and 4.")

else:
    print("Incorrect PIN. Access Denied.")

