class node:
    def __init__(self, data):
        self.data = data
        self.next = None
new_data = int(input("new1 data:"))  
new1 = node(new_data)     


head_data = int(input("enter head data:"))
head = node(head_data)


middle_data = int(input("enter middle data:"))
middle = node(middle_data)


tail_data = int(input("enter tail data:"))
tail = node(tail_data)


new_data2 = int(input("enter new2 data:"))
new2 = node(new_data2)


specific_position = int(input("enter specific data:"))
specific = node(specific_position)


new1.next = head
head.next = middle
middle.next = specific
specific.next = tail
tail.next = new2
new2.next = None


temp = new1
while temp is not None:
    print(f"{temp.data},-->", end="")
    temp = temp.next
