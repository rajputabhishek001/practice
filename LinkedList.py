class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
         
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    #str method to print in a presented format
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '-->'
            temp_node = temp_node.next
        return result
    
    #add end of linked list
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    #add element at bignning
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def any_location(self, value, index):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current=current.next
    
    def search(self, target):
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return index
            current =  current.next
            index += 1
        return -1
    
    def get_value_of_index(self, index):
        if index == -1:
            return self.tail
        if index < 0 or index >= self.length:
            return None
        current=self.head
        for _ in range(index):
            current = current.next
        return current

    def set_value(self, index, value):
        temp = self.get_value_of_index(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_linked(self):
        if self.length == 0:
            return None
        popped_ele= self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_ele.next = None
        self.length -= 1
        return popped_ele
    
    def pop_end(self):
        if self.length == 0:
            return None
        poped_ele=self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length-=1
        return poped_ele
    
    def remove(self, index):
        if index >= self.length or index < -1:
            return None
        if index == 0:
            self.pop_linked()
        if index == self.length-1 or index == -1:
            return self.pop_end()
        pre_node = self.get_value_of_index(index-1)
        poped_ele = pre_node.next
        pre_node.next = poped_ele.next
        poped_ele.next = None
        self.length -=1
        return poped_ele
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0    

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head  

    def is_pallindrome(self):
        reverse = reverse(self)
 

    def remove_duplicates(self):
        if self.head is None:
            return
        node_values = set()  # set to store unique node values
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next:
            if current_node.next.value in node_values:  # duplicate found
                current_node.next = current_node.next.next
                self.length -= 1

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode(-1)
    
        prev = res
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next
 
        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2
 
        return res.next
    
    def deleteDuplicates(self, head):
        if not head:
            return None
        
        seen = set()
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy
        current_node = head
 
        while current_node:
            if current_node.val in seen:
                prev_node.next = current_node.next
                current_node = current_node.next
            else:
                seen.add(current_node.val)
                prev_node = current_node
                current_node = current_node.next
        return dummy.next

new_element = LinkedList()
new_element1 = LinkedList()
new_element.append(3)
new_element.append(4)
# new_element.any_location(2,2)
new_element.append(8)
new_element.append(10)
# new_element.traverse()
# print(new_element.search(3))
# new_element.set_value(1,4)
# new_element.pop_linked()
# new_element.pop_end()
# new_element.remove(3)
# new_element.delete_all()

# new_element.reverse()
new_element1.append(5)
new_element1.append(7)
new_element1.append(9)

print(new_element)
print(new_element1)
sl = Solution()
sl.mergeTwoLists(new_element, new_element1)
print(sl)
