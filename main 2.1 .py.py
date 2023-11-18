class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
      self._account_number = account_number
      self._account_holder_name = account_holder_name
      self._account_balance = initial_balance

  def deposit(self, amount):
      if amount > 0:
          self._account_balance += amount
          print(f"Deposited ${amount}. New balance is ${self._account_balance}.")
      else:
          print("Please enter a valid amount to deposit.")

  def withdraw(self, amount):
      if 0 < amount <= self._account_balance:
          self._account_balance -= amount
          print(f"Withdrew ${amount}. New balance is ${self._account_balance}.")
      else:
          print("Insufficient funds or invalid amount to withdraw.")

  def display_balance(self):
      print(f"Account Balance for {self._account_holder_name}: ${self._account_balance}")


# Example usage:

# Creating an instance of BankAccount
account = BankAccount("123456789", "John Doe", 1000.0)

# Display initial balance
account.display_balance()

# Deposit some money
account.deposit(500.0)

# Withdraw some money
account.withdraw(200.0)

# Display the updated balance
account.display_balance()
