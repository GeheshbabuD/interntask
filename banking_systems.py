import sys
import os

def get_hidden_input(prompt=""):
    print(prompt, end='', flush=True)
    if os.name == 'nt':
        import msvcrt
        chars = []
        while True:
            char = msvcrt.getch()
            if char in (b'\r', b'\n'):
                print()
                break
            elif char == b'\x08':  
                if chars:
                    chars.pop()
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()
            else:
                chars.append(char.decode('utf-8'))
                sys.stdout.write('*')
                sys.stdout.flush()
        return ''.join(chars)

class banking_system:
    def __init__(self):
        self.accounts = {}

    def transaction_history(self, account_id, pin):
        if account_id not in self.accounts:
            return "Account not found."
        if self.accounts[account_id]['pin'] != pin:
            return "Incorrect PIN."
        return self.accounts[account_id]['transactions']
        
    def create_account(self, account_id, account_holder, pin, initial_balance=0):
        if account_id in self.accounts:
            return "Account already exists."
        if len(pin) < 4:
            return "PIN must be at least 4 digits."
        self.accounts[account_id] = {
            'account_holder': account_holder,
            'balance': initial_balance,
            'pin': pin,
            'transactions': []
        }
        return f"Account created successfully for {account_holder}."
    
    def deposit(self, account_id, pin, amount):
        if account_id not in self.accounts:
            return "Account not found."
        if self.accounts[account_id]['pin'] != pin:
            return "Incorrect PIN."
        if amount <= 0:
            return "Deposit amount must be positive."
        self.accounts[account_id]['balance'] += amount
        self.accounts[account_id]['transactions'].append(f"Deposited: {amount}")
        return f"Deposited {amount}. New balance: {self.accounts[account_id]['balance']}"
     
    def withdraw(self, account_id, pin, amount):
        if account_id not in self.accounts:
            return "Account not found."
        if self.accounts[account_id]['pin'] != pin:
            return "Incorrect PIN."
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if self.accounts[account_id]['balance'] < amount:
            return "Insufficient funds."
        self.accounts[account_id]['balance'] -= amount
        self.accounts[account_id]['transactions'].append(f"Withdrew: {amount}")
        return f"Withdrew {amount}. New balance: {self.accounts[account_id]['balance']}"
    
    def get_balance(self, account_id, pin):
        if account_id not in self.accounts:
            return "Account not found."
        if self.accounts[account_id]['pin'] != pin:
            return "Incorrect PIN."
        return f"Current balance: {self.accounts[account_id]['balance']}"
    
    def pin_change(self, account_id, old_pin, new_pin):
        if account_id not in self.accounts:
            return "Account not found."
        if self.accounts[account_id]['pin'] != old_pin:
            return "Old PIN is incorrect."
        if len(new_pin) < 4:
            return "New PIN must be at least 4 digits."
        self.accounts[account_id]['pin'] = new_pin
        return "PIN changed successfully."
    
    def account_info(self, account_id, pin):
        if account_id not in self.accounts:
            return "Account not found."
        if self.accounts[account_id]['pin'] != pin:
            return "Incorrect PIN."
        info = {
            'account_holder': self.accounts[account_id]['account_holder'],
            'account_id': account_id,
            'balance': self.accounts[account_id]['balance'],
            'transactions': self.accounts[account_id]['transactions']
        }
        return info

if __name__ == "__main__":
    bank = banking_system()
    while True:
        print("\n=== Banking System ===")
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check balance")
        print("5. Transaction history")  
        print("6. Change PIN")
        print("7. Account info")
        print("8. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            acc_id = input("Enter account ID: ")
            acc_holder = input("Enter account holder name: ")
            pin = get_hidden_input("Set your PIN (min 4 digits): ")
            initial_balance = float(input("Enter initial balance: "))
            print(bank.create_account(acc_id, acc_holder, pin, initial_balance))
            
        elif choice == '2':
            acc_id = input("Enter account ID: ")
            pin = get_hidden_input("Enter PIN: ")
            amount = float(input("Enter deposit amount: "))
            print(bank.deposit(acc_id, pin, amount))
            
        elif choice == '3':
            acc_id = input("Enter account ID: ")
            pin = get_hidden_input("Enter PIN: ")
            amount = float(input("Enter withdrawal amount: "))
            print(bank.withdraw(acc_id, pin, amount))
            
        elif choice == '4':
            acc_id = input("Enter account ID: ")
            pin = get_hidden_input("Enter PIN: ")
            print(bank.get_balance(acc_id, pin))
            
        elif choice == '5':
            acc_id = input("Enter account ID: ")
            pin = get_hidden_input("Enter PIN: ")
            transactions = bank.transaction_history(acc_id, pin)
            if isinstance(transactions, list):
                for transaction in transactions:
                    print(transaction)
            else:
                print(transactions)
                
        elif choice == '6':
            acc_id = input("Enter account ID: ")
            old_pin = get_hidden_input("Enter old PIN: ")
            new_pin = get_hidden_input("Enter new PIN (min 4 digits): ")
            print(bank.pin_change(acc_id, old_pin, new_pin))
            
        elif choice == '7':
            acc_id = input("Enter account ID: ")
            pin = get_hidden_input("Enter PIN: ")
            info = bank.account_info(acc_id, pin)
            if isinstance(info, dict):
                for key, value in info.items():
                    print(f"{key}: {value}")
            else:
                print(info)
            
        elif choice == '8':
            print("Thank you for using our banking system!")
            break
            
        else:
            print("Invalid choice. Please try again.")