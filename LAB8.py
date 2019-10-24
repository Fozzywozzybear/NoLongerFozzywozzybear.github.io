#Lab #8
#Due Date: 10/25/2019, 11:59PM 
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
                        
                          
class Queue:
    '''
        >>> x=Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        'Queue is empty'
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> x.dequeue()
        1
        >>> x.reverse()
        >>> x
        Head:Node(3)
        Tail:Node(2)
        Queue:3 2
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
        return f'Head:{self.head}\nTail:{self.tail}\nQueue:{out}'

    __repr__=__str__

    def isEmpty(self):
        if self.count==0:
            return True
        else:
            return False

    def enqueue(self, x):
        new_node=Node(x)
        if self.isEmpty()==False:
            self.head=new_node
        else:
            self.head.next=new_node
            self.head=new_node
        self.count+=1
        return 
            



    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty'
        if self.count==1:
            value=self.head.value
            self.tail==None
            self.head==None
            return value
        else:
            while self.head != None:
                if self.head.next==None:
                    value=self.head.next.value
                    self.head=self.head.next
                    self.head.next=None
                    return value
                self.head=self.head.next




    def __len__(self):
        return self.count 

    def reverse(self): 
        pass
