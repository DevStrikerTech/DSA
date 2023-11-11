class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_result(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append_node(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1

    def prepend_node(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1
        
    def pop_node(self):
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head

        while(temp.next):
            pre = temp
            temp = temp.next
        
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        
        return temp
    
    def pop_first_node(self):
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp
    
    def get_node(self, index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head

        for _ in range(index):
            temp = temp.next
        
        return temp
    
    def set_node(self, index, value):
        temp = self.get_node(index)

        if temp:
            temp.value = value
            return True
        
        return False
    
    def insert_node(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend_node(value)
        
        if index == self.length:
            return self.append_node(value)
        
        new_node = Node(value)
        temp = self.get_node(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

        return True
    
    def remove_node(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first_node()
        
        if index == self.length - 1:
            return self.pop_node()
        
        pre = self.get_node(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1

        return temp
    
    def reverse_node(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


# Create objects
linked_list = LinkedList(1)
linked_list.append_node(2)
linked_list.append_node(3)
linked_list.append_node(4)

# (2) Items - Returns 2 Node
# print(linked_list.pop_node())
# (1) Item -  Returns 1 Node
# print(linked_list.pop_node())
# (0) Item - Return None
# print(linked_list.pop_node())

# (2) Items - Returns 2 Node
# print(linked_list.pop_first_node())
# (1) Item -  Returns 1 Node
# print(linked_list.pop_first_node())
# (0) Item - Return None
# print(linked_list.pop_first_node())

# print(linked_list.get_node(2))

# linked_list.set_node(1, 4)

# linked_list.insert_node(1, 1)

# print(linked_list.remove_node(2), '\n')

# linked_list.reverse_node()

linked_list.print_result()