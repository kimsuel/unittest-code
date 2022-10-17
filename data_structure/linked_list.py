class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# 1
node1 = Node(1)

print(node1.data)
print(node1.next)


# 2
node1 = Node(1)
node2 = Node(3)

node1.next = node2
head = node1

print(node1.next.data)
print(node2.data)


# 3
def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)


node1 = Node(1)
head = node1

add(3)

print(node1.next.data)


# 4
node1 = Node(1)
head = node1

add(3)
add(4)
add(5)

node = head

while node.next:
    print(node.data)
    node = node.next

print(node.data)
