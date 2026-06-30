class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


head_data = int(input("enter head node:"))
head = node(head_data)

middle_data = int(input("enter middle node:"))
middle = node(middle_data)

tail_data = int(input("enter tail node:"))
tail = node(tail_data)


head.next = middle
middle.next = tail
tail.next = None

tail.prev = middle
middle.prev = head
head.prev = None


print("forward connection:")
temp = head
while temp is not None:
    print(f"{temp.data}-->", end = "")
    temp = temp.next
print("None")

print("backward connection:")
temp = tail
while temp is not None:
    print(f"{temp.data}-->", end = "")
    temp = temp.prev
print("None")