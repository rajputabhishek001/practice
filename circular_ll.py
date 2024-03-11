class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CLinkedList:
    def __init__(self):
        # new_node = Node(value)
        # new_node.next=new_node
        self.head = None
        self.tail = None
        self.length = 0


liked_list = CLinkedList()
print(liked_list.head)