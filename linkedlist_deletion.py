#deletion at beginning
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
     


head_data = int(input("enter head data:"))
head = node(head_data)


middle_data = int(input("enter middle data:"))
middle = node(middle_data)


tail_data = int(input("enter tail data:"))
tail = node(tail_data)




head.next = middle
middle.next = tail
tail.next = None
head = head.next



temp = head
while temp is not None:
    print(f"{temp.data}-->", end="")
    temp = temp.next
print("None")'''


#deletion at end
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
     


head_data = int(input("enter head data:"))
head = node(head_data)


middle_data = int(input("enter middle data:"))
middle = node(middle_data)


tail_data = int(input("enter tail data:"))
tail = node(tail_data)





head.next = middle
middle.next = None



temp = head
while temp is not None:
    print(f"{temp.data}-->", end="")
    temp = temp.next
print("None")'''


#delete at specific position
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
     


head_data = int(input("enter head data:"))
head = node(head_data)


middle_data = int(input("enter middle data:"))
middle = node(middle_data)


tail_data = int(input("enter tail data:"))
tail = node(tail_data)





head.next = tail

tail.next = None



temp = head
while temp is not None:
    print(f"{temp.data}-->", end="")
    temp = temp.next
print("None")
