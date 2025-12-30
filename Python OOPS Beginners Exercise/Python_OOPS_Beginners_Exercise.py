class BankAccount:
  def display_details(self): 
    print(self.account_number,self.account_holder,self.balance)
  def setData(self, account_number, account_holder, initial_balance):
    self.account_number = account_number
    self.account_holder = account_holder
    self.balance = initial_balance
  def __init__(self,account_number,account_holder,initial_bal):
    self.account_number = account_number
    self.account_holder = account_holder
    self.balance = initial_bal

  def deposit(self, amount):
    if amount >= 0:
      self.balance += amount
  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance -= amount
  def get_balance(self):
    return self.balance   

number = int(input())
holder = input()
initial_bal = int(input())

account = BankAccount(number, holder, initial_bal)

ch = int(input())

if ch==1:
  amount = int(input())
  account.deposit(amount)
  account.display_details()
  
elif ch==2:
  amount = int(input())
  account.withdraw(amount)
  print(account.get_balance())