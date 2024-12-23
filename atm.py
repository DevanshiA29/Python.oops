class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    
    def menu(self):
        while True:  # Keep showing the menu until the user exits
            user_input = input("""
                                         ENTER 1 FOR PIN GENERATION
                                         ENTER 2 FOR CREDIT
                                         ENTER 3 FOR WITHDRAW
                                         ENTER 4 FOR CHECK BALANCE
                                         ENTER 5 FOR EXIT
""")
            if user_input == '1':
                self.generate_pin()
            elif user_input == '2':
                self.credit()
            elif user_input == '3':
                self.withdraw()
            elif user_input == '4':
                self.check_balance()
            elif user_input == '5':
                print("Bye!")
                break
            else:
                print("Invalid choice. Try again.")
    
    def generate_pin(self):
        self.pin = input("Enter your new PIN: ")
        print("PIN set successfully!")
    
    def credit(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            amount = int(input("Enter amount to credit: "))
            self.balance += amount
            print(f"₹{amount} credited successfully. New balance: ₹{self.balance}")
        else:
            print("Invalid PIN.")
    
    def withdraw(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount > self.balance:
                print("Insufficient balance.")
            else:
                self.balance -= amount
                print(f"₹{amount} withdrawn successfully. New balance: ₹{self.balance}")
        else:
            print("Invalid PIN.")
    
    def check_balance(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            print(f"Your current balance is: ₹{self.balance}")
        else:
            print("Invalid PIN.")
