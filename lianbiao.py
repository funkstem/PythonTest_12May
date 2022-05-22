class daynames:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

e1 = daynames('Mon')
e2 = daynames('Wed')
e3 = daynames('Tue')
e4 = daynames('Thu')

e1.nextval = e3
e3.nextval = e2
e2.nextval = e4

thisvalue = e1

while thisvalue:
        # print(thisvalue)  #该节点内存地址
        if thisvalue.dataval=="Wed":
            break
        print(thisvalue.dataval) #该节点数值
        # print(thisvalue.nextval) #下一个节点内存地址
        thisvalue = thisvalue.nextval

print("haha")
# xx=0
# if not xx:
#     print("Yes")
# else:
#     print("No")


# class Node:
#     def __init__(self, dataval=None):
#         self.dataval = dataval
#         self.nextval = None

# class SLinkedList:
#     def __init__(self):
#         self.headval = None

# list1 = SLinkedList()
# list1.headval = Node(1)
# e2 = Node(2)
# e3 = Node(4)
# # Link first Node to second node
# list1.headval.nextval = e2
# # Link second Node to third node
# e2.nextval = e3

# list2 = SLinkedList()
# list2.headval = Node(1)
# f2 = Node(3)
# f3 = Node(4)
# # Link first Node to second node
# list2.headval.nextval = f2
# # Link second Node to third node
# f2.nextval = f3


# print("DFSDFS")

# class Solution:
#     # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#     def mergeTwoLists(self, l1, l2):
#         if not l1:
#             return l2
#         if not l2:
#             return l1
#         if not l1 and not l2:
#             return l1
#         node1, node2 = None, None
#         if l1.val <= l2.val:
#             node1, node2 = l1, l2
#         else:
#             node1, node2 = l2, l1
#         temp_node1, temp_node2 = node1, node2
#         pre_temp1 = None
#         while temp_node1 and temp_node2:
#             if temp_node2.val >= temp_node1.val:
#                 pre_temp1 = temp_node1
#                 temp_node1 = temp_node1.next
#             else:
#                 temp2 = temp_node2.next
#                 pre_temp1.next = temp_node2
#                 temp_node2.next = temp_node1
#                 pre_temp1 = temp_node2
#                 temp_node2 = temp2
#         if temp_node2:
#             pre_temp1.next = temp_node2
 
#         return node1
        
# list1 = [1,2,4]
# list2 = [1,3,4]
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    def mergeTwoLists(sekf,l1, l2):
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        
        return dummy.next

class SLinkedList:
    def __init__(self):
        self.headval = None

list1 = SLinkedList()
list1.headval = ListNode(1)
e2 = ListNode(2)
e3 = ListNode(4)
# Link first Node to second node
list1.headval.next = e2
# Link second Node to third node
e2.next = e3

list2 = SLinkedList()
list2.headval = ListNode(1)
f2 = ListNode(3)
f3 = ListNode(4)
# Link first Node to second node
list2.headval.next= f2
# Link second Node to third node
f2.next = f3


print(list1)
c1=Solution()
print(c1.mergeTwoLists(list1,list2))


# class Solution1:
#     def isPalindrome(self, x: int) -> bool:
#         strx=str(x)
#         lenNum=len(strx)
#         lenNum_half=lenNum//2+1
#         boolNum=1
#         for num_loop in range(lenNum_half):
#             if strx[num_loop]==strx[(-1-num_loop)]:
#                 boolNum=1*boolNum
#             else:
#                 boolNum=0*boolNum
#                 break
#         if boolNum==1:
#             return True
#         else:
#             return False

# ss=Solution1()
# print(ss.isPalindrome(123))'''