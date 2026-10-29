# Python Banking Program

def show_balance(balance):
    print(f"Balance is £{balance:.2f}")

def deposit():
    amount =float(input("Enter an amount to deposit: "))

    if amount < 0:
        print("£££££££££££££££££££££££")
        print("Please enter a positive amount")
        print("£££££££££££££££££££££££")
        return 0
    else:
        return amount

def withdraw(balance):
    amount =float(input("Enter an amount to withdraw: "))

    if amount > balance:
        print("£££££££££££££££££££££££")
        print("Insufficient funds")
        print("£££££££££££££££££££££££")
        return 0
    elif amount < 0:
        print("£££££££££££££££££££££££")
        print("Amount must be greater than 0")
        print("£££££££££££££££££££££££")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("£££££££££££££££££££££££")
        print("   Banking Program    ")
        print("£££££££££££££££££££££££")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("£££££££££££££££££££££££")

        choice = input("Enter your choice: (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
          balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("£££££££££££££££££££££££")
            print("Please enter a valid choice")
            print("£££££££££££££££££££££££")

    print("£££££££££££££££££££££££")
    print("Thank you for using this program")
    print("£££££££££££££££££££££££")

if __name__ == "__main__":
    main()