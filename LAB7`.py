#Lab #7
#Due Date: 10/11/2019, 11:59PM 
########################################
#                                      
# Name:
# Collaboration Statement:             
#
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class OrderedLinkedList:
    '''
        >>> x=OrderedLinkedList()
        >>> x.pop()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.remDuplicates()
        >>> x.pop()
        8.76
        >>> x
        Head:Node(1)
        Tail:Node(5)
        List:1 3 5
    '''

    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out) 
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__

    def isEmpty(self):
        return self.head == None

    def __len__(self):
        return self.count


    def add(self, value):
        temp=self.head
        while temp != None:
            if value < temp.next.value:
                temp=self.next
        self.next=temp
        temp.next=value

      


    def pop(self):
        pass


    def remDuplicates(self):
        # --- Your code starts here
        pass





