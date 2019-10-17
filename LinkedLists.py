class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=node()#used to point 

    def append(self,data):
        new_node=node(data) #sets data point in the node
        current=self.head #starts at the left most point
        while current.next!=None:#while the next node has value
            current=current.next
        current.next=new_node#addes to the end when the next value is none
    def length(self):
        current=self.head
        total=0
        while current.next!=None:
            total+=1
            current=current.next
        return total
    def display(self):
        elems=[]
        current_node = self.head
        while current_node.next!=None:
            current_node=current_node.next
            elems.append(current_node.data)
        print (elems)
    def get(self,index):
        if index>=self.length():
            return "error"
        current_index=0
        current_node=self.head
        while True:
            current_node=current_node.next
            if current_index==index:return current_node.data
            current_index+=1
    def erase(self,index):
        if index>=self.length():
            return "error"
        current_index=0
        current_node=self.head
        while True:
             last_node=current_node
             current_node=current_node.next
             if current_index==index:
                 last_node.next=current_node.next
                 return 
             current_index+=1


my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
my_list.erase(1)
my_list.display()
