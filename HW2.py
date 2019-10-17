#Code is for a startup bank that just got off the ground, the bank only has access from the government to hold two accounts per each user of their platform.
import random 
from abc import *

class Account(ABC):#Parent abstract class
    def __init__(self,person,holder):
        self.person=person
        self.holder=holder
        self.balance=0
    @abstractmethod #both are used to define abstract methods used in the subclasses
    def deposit(self,amount):
        raise NotImplementedError
    @abstractmethod
    def withdraw(self):
        raise  NotImplementedError
class CheckingAccount(Account):
    def __init__(self,person,holder):#Inits the CheckingAcount class with the vars
        self.person=person
        self.holder=holder
        self.__holder=holder
        self.balance=0
        self.__id=self.__createID()
    def deposit(self,holder,amount):# Can only deposit if the deposit amount is over 5$
        if amount < 5:
            return "We don't except deposits under 5$"
        if amount >=5:
                self.balance+=amount
                return 'your new balance is {}'.format(self.balance)
    def withdraw(self,holder,account,amount):#Checks if the person withdrawing is the user of their account and has enough money
        if self.__holder==holder:
            if amount <= self.balance:
                self.balance -= amount
                return "you have withdrawn {} your remaining balance is {}".format(amount,self.balance)
            if amount > self.balance:
                return 'You do not have enough funds, your balance is {}'.format(self.balance)
        else: 
            return "the account you are accessing is not yours,you have been reported for fraud" 
    def __createID(self):#called when the account is made to make a private ID 
        return random.randint(1,10)*7
    def getAmount(self,holder):#
        if self.__holder==holder:
            return self.balance
        else:
            return "you don't have access to this account"
        return self.__id
    def setID(self,holder,new_id):
        if self.__holder==holder:
            self.__id=new_id
            return "your new id is {}".format(self.__id)
        else:
            return "you don't have access to this account"
   
class SavingAccount(Account):

    def __init__(self,person,holder):
        self.person=person
        self.holder=holder
        self.__holder=holder
        self.balance=0
        self.__id=self.__createID()
    def deposit(self,holder,account,amount):
        if amount < 100:
            return "We don't except deposits under 100$"
        if amount >=5:
                self.balance+=amount
                return 'your new balance is {}'.format(self.balance)
    def withdraw(self,holder,account,amount):
        if self.__holder==holder:
            if amount < 1000:
                return 'you deposit {} more $ before you are able to withdraw'.format(1000-self.balance)
            else:
                return "you most have 1000$ in your account before you can withdraw"
        else:
            return "You are trying to access the wrong account, you have been reported for fraud"
    def __createID(self):
        return random.randint(1,10)*7
    def getID(self):
        return self.__id
    def getAmount(self,holder):#
        if self.__holder==holder:
            return self.balance
        else:
            return "you don't have access to this account"
    def setID(self,holder,new_id):
        if self.__holder==holder:
            self.__id=new_id
            return "your new id is {}".format(self.__id)
        else:
            return "you don't have access to this account"

        

