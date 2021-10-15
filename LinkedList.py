class LinkedList:
    def __init__(self):
        self.head = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

l_list = LinkedList()

number = [7,6,4,8,2,10,9,20,1,3]
first = True
for i in number:
    if first:
        l_list.head = Node(i)
        curNode = l_list.head
        first = not(first)
    else:
        curNode.next = Node(i)
        curNode = curNode.next

string_repr = ""
node = l_list.head

while node is not None:
    string_repr += str(node.data)
    string_repr += " -> "
    node = node.next
string_repr += "None"

print(string_repr)