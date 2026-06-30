'''#insertion at begiining
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


new_data = int(input("enter new data:"))
new  = node(new_data)

head_data = int(input("enter head node:"))
head = node(head_data)

middle_data = int(input("enter middle node:"))
middle = node(middle_data)

tail_data = int(input("enter tail node:"))
tail = node(tail_data)



print("forward connection:")
new.next = head
head.next = middle
middle.next = tail
tail.next = None

print("backward connection:")
tail.prev = middle
middle.prev = head
head.prev = None


print("forward traversal:")
temp = new
while temp is not None:
    print(f"{temp.data}-->", end = "")
    temp = temp.next
print("None")

print("backward traversal:")
temp = tail
while temp is not None:
    print(f"{temp.data}-->", end = "")
    temp = temp.prev
print("None")'''




#insertion at end
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


new_data = int(input("enter new data:"))
new  = node(new_data)

head_data = int(input("enter head node:"))
head = node(head_data)

middle_data = int(input("enter middle node:"))
middle = node(middle_data)

tail_data = int(input("enter tail node:"))
tail = node(tail_data)


print("forward connection:")
head.next = middle
middle.next = tail
tail.next = new
new.next = None

print("backward connection:")
new.prev = tail
tail.prev = middle
middle.prev = head
head.prev = None


print("forward traversal:")
temp = head
while temp is not None:
    print(f"{temp.data}-->", end = "")
    temp = temp.next
print("None")

print("backward traversal:")
temp = new
while temp is not None:
    print(f"{temp.data}-->", end = "")
    temp = temp.prev
print("None")'''




'''#insertion at specific position
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


new_data = int(input("enter new data:"))
new  = node(new_data)

head_data = int(input("enter head node:"))
head = node(head_data)

middle_data = int(input("enter middle node:"))
middle = node(middle_data)

tail_data = int(input("enter tail node:"))
tail = node(tail_data)


print("forward connection:")
head.next = middle
middle.next = new
new.next = tail
tail.next = None


print("backward connection:")
tail.prev = new
new.prev = middle
middle.prev = head
head.prev = None


print("forward traversal:")
temp = head
while temp is not None:
    print(f"{temp.data}-->", end = "")
    temp = temp.next
print("None")

print("backward traversal:")
temp = tail
while temp is not None:
    print(f"{temp.data}-->", end = "")
    temp = temp.prev
print("None")'''




'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


new_data = int(input("enter new data:"))
new  = node(new_data)

head_data = int(input("enter head node:"))
head = node(head_data)

middle_data = int(input("enter middle node:"))
middle = node(middle_data)

tail_data = int(input("enter tail node:"))
tail = node(tail_data)


print("forward connection:")
head.next = middle
middle.next = tail
tail.next = new
new.next = None

print("backward connection:")
new.prev = tail
tail.prev = middle
middle.prev = head
head.prev = None


print("forward traversal:")
temp = head
while temp is not None:
    print(f"{temp.data}-->", end = "")
    temp = temp.next
print("None")

print("backward traversal:")
temp = new
while temp is not None:
    print(f"{temp.data}-->", end = "")
    temp = temp.prev
print("None")'''





class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


new_data1 = int(input("enter new data1:"))
new1  = node(new_data1)

head_data = int(input("enter head node:"))
head = node(head_data)

middle_data = int(input("enter middle node:"))
middle = node(middle_data)

tail_data = int(input("enter tail node:"))
tail = node(tail_data)

specific_data = int(input("enter specific data:"))
specific = node(specific_data)

new_data2 = int(input("enter new data2:"))
new2  = node(new_data2)


print("forward connection:")
new1.next = head
head.next = middle
middle.next = tail
tail.next = specific
specific.next = new2
new2.next = None


print("backward connection:")

new2.prev = specific
specific.prev = tail
tail.prev = middle
middle.prev = head
head.prev = new1
new1.prev = None


print("forward traversal:")
temp = new1
while temp is not None:
    print(f"{temp.data}-->", end = "")
    temp = temp.next
print("None")

print("backward traversal:")
temp = new2
while temp is not None:
    print(f"{temp.data}-->", end = "")
    temp = temp.prev
print("None")