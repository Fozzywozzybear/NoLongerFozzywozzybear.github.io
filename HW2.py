
"""class ATM(Person):#Deposit or withdraw at an atm function 
    def __init__(self):

    
    def deposit(self):
    depositAmount=float(input('Please enter the amount of money you would like to deposit into your account'))
    self.balance +=depositAmount 
    return " you have deposited {} $".format(self.balance)

    def withdraw(self):
        withdrawAmount=float(input('Please enter the amount of money you would like to withdraw'))
        if self.balance >= withdrawAmount:
            self.balance -= withdrawAmount
            return "Your remaining balance is {}".format(self.balance)"""
import random 
from abc import *
class BankOfAaron(ABC):

    def __init__(self,person,id):
        self.person = person 
        self.id = random.randint(0,10)*7
        
class Account(ABC):

    def __init__(self,person,holder,id):
        self.person=person
        self.balance=0
        self.__id=random.randint(0,10)*7
        self.__holder=person
    def deposit(self,amount):
        self.balance += amount
        return 'your new balance is {}'.format(self.balance)
    @abstractmethod
    def withdraw(self):
        raise  NotImplementedError
class CheckingAccount(Account):

    def deposit(self,holder,id,amount):
        if amount < 5:
            return "We don't except deposits under 5$"
        if amount >=5:
            if holder == self.__holder:
                self.balance+=amount
                return 'your new balance is {}'.format(self.balance)
    def withdraw(self,holder,account,amount):#Checks if the person withdrawing is the user of their account
        if holder == self.__holder:
            if amount <= self.balance:
                self.balance -= amount
                return "you have withdrawn {} your remaining balance is {}".format(amount,self.balance)
            if amount > self.balance:
                return 'You do not have enough funds, your balance is {}'.format(self.balance)
        else: 
            return "the account you are accessing is not yours" 
    def createID(self):
        return random.randint(0,10)*7
class SavingAccount(Account):
    
    def deposit(self,holder,account,amount):
        if amount < 100:
            return "We don't except deposits under 100$"
        if amount >=5:
            if holder == self.__holder:
                self.balance+=amount
                return 'your new balance is {}'.format(self.balance)
    def withdraw(self,holder,account,amount):
        if amount < 1000:
            return 'you deposit {} more $ before you are able to withdraw'.format(1000-self.balance)
class ChangeId(Account):

    def getid(self):
        return self.__id
    def setID(self,holder,new_id):
        if holder == self.__holder:
            self.__id=new_id
        else:
            return "you do not have access to change the id of this account"

        

