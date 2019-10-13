
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

class Account(ABC):

    def __init__(self,person,holder):
        self.person=person
        self.holder=holder
        self.balance=0
    @abstractmethod
    def deposit(self,amount):
        raise NotImplementedError
    @abstractmethod
    def withdraw(self):
        raise  NotImplementedError
class CheckingAccount(Account):

    def __init__(self,person,holder):
        self.person=person
        self.holder=holder
        self.__holder=holder
        self.balance=0
        self.__id=self.__createID()
        id=self.__id
        


    def deposit(self,holder,amount):
        if amount < 5:
            return "We don't except deposits under 5$"
        if amount >=5:
                self.balance+=amount
                return 'your new balance is {}'.format(self.balance)
    def withdraw(self,holder,account,amount):#Checks if the person withdrawing is the user of their account
            if amount <= self.balance:
                self.balance -= amount
                return "you have withdrawn {} your remaining balance is {}".format(amount,self.balance)
            if amount > self.balance:
                return 'You do not have enough funds, your balance is {}'.format(self.balance)
            else: 
                return "the account you are accessing is not yours" 
    def __createID(self):
        return random.randint(1,10)*7
    def getammount(self,holder):
        if self.__holder==holder:
            return self.balance
        else:
            return "you dont have access to this account"
        return self.__id
    def setID(self,holder,new_id):
        if self.__holder==holder:
            self.__id=new_id
            return "your new id is {}".format(self.__id)
        else:
            return "you dont have access to this account"
   
class SavingAccount(Account):

    def __init__(self,person,holder):
        self.person=person
        self.holder=holder
        self.__holder=holder
        self.balance=0
        self.__id=self.__createID()
        id=self.__id

    
    def deposit(self,holder,account,amount):
        if amount < 100:
            return "We don't except deposits under 100$"
        if amount >=5:
                self.balance+=amount
                return 'your new balance is {}'.format(self.balance)
    def withdraw(self,holder,account,amount):
        if amount < 1000:
            return 'you deposit {} more $ before you are able to withdraw'.format(1000-self.balance)
    def __createID(self):
        return random.randint(1,10)*7
    def getid(self):
        return self.__id
    def setID(self,holder,new_id):
        if self.__holder==holder:
            self.__id=new_id
            return "your new id is {}".format(self.__id)
        else:
            return "you don't have access to this account"

        

