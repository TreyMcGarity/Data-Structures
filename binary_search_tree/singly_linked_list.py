class Node:
  # constructor
  def __init__(self, value = None): 
    self.value = value
    self.next = None

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next

  def set_next(self, new_next):
    self.next = new_next

# A Linked List class with a single head node
class LinkedList:
    def __init__(self):  
        self.head = None
        self.tail = None
        self.length = 0

    # insertion methods
    def add_to_tail(self, value):
        new_node = Node(value)
        self.length += 1
        if not self.head:
            self.head = new_node
            self.tail = new_node
        if self.tail:
            current = self.tail #10
            current.set_next(new_node) #20
            self.tail = new_node 
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
        self.tail.set_next(None)

    def add_to_head(self, value):
        self.length += 1
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        self.head.set_next(new_node)
        self.head = new_node

    # deletion methods
    def remove_head(self):
        if self.head is None and self.tail is None:
            return None
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value
        self.length -= 1

            
    def remove_tail(self):
        self.length -= 1
        if self.head is None and self.tail is None:
            return None
        current = self.head
        if self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        while current.get_next() is not self.tail:
            current = current.get_next()
        value = self.tail.get_value()
        self.tail = current
        current = None
        return value

    def remove_at_value(self, value):
        self.length -= 1
        if self.head is None and self.tail is None:
            return
        bye_node = self.head
        while(bye_node):  
            if bye_node.value == value:  
                break
            prev = bye_node  
            bye_node = bye_node.get_next()
            prev.next = bye_node.get_next()

    def remove_at_index(self, index):
        self.length -= 1
        if index > self.length:
            return None
        if self.length == 1 and index == 0:
            target = self.head
            self.head = None
            self.tail = None
            return target.get_value()
        prev_node = self.head
        for i in range(index - 1):
            prev_node = prev_node.get_next()
        target = prev_node.get_next()
        prev_node.next = target.get_next()
        target.next = None

    # print method
    def print_list(self):
        # print(self.tail.value)
        current = self.head
        while(current):
            print(current.value)
            current = current.next