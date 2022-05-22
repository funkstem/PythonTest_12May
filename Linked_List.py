



class node:
    def __init__(self,val) -> None:
        self.val=val
        self.next=None


class linkList:
    def __init__(self) -> None:
        self.head_val=None

    def dayin(self):
        first=self.head_val
        while first:
            print(first.val)
            first=first.next

    def begin(self,dataFront):
        NewNode=node(dataFront)
        NewNode.next=self.head_val
        self.head_val=NewNode

    def end(self,dataBehind):
        NewNode=node(dataBehind)
        if self.head_val is None:
            self.head_val=NewNode
        dd=self.head_val
        while dd.next:
            dd=dd.next
        dd.next=NewNode
        # self.head_val=NewNode

    def inBetween(self,middleNode,dataInsert):
        if not middleNode:
            print("This mode is none.")
        NewNode=node(dataInsert)
        NewNode.next=middleNode.next
        middleNode.next=NewNode
        
        

    def willDelete(self,Removekey):
        HeadVal=self.head_val
        if not HeadVal:
            if HeadVal.val==Removekey:
                self.head_val=HeadVal.next
                HeadVal=None
                return
        
        while(HeadVal):
            if HeadVal.val==Removekey:
                break
            previous=HeadVal
            HeadVal=HeadVal.next

        if (HeadVal==None):
            return

        previous.next=HeadVal.next
        HeadVal=None
        
        


        


        







e1=node(1)
e2=node(2)
e3=node(3)
e1.next=e2
e2.next=e3

# e0=node(-11)
# e8=node()
list1=linkList()
list1.head_val=e1
# list1.head_val.next=e2
# list1.dayin()

list1.begin(-11)

# list1.dayin()
list1.end(11)
list1.dayin()
print("------------------------------")
list1.inBetween(e2,12221)
list1.dayin()

print("------------------------------")
list1.willDelete(3)

list1.dayin()

# dd=e1

# while dd:
#     print(dd.val) 
#     dd=dd.next


