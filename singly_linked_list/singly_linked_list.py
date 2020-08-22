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

    # insertion method
    def add_to_tail(self, value):
        newNode = Node(value)
        if self.head is None and self.tail is None:
            self.head = newNode
            self.tail = newNode
        self.tail.set_next(newNode)
        self.tail = newNode

    # deletion methods
    def remove_node(self, value):
        if self.head is None and self.tail is None:
            return
        byeNode = self.head
        while(byeNode):  
            if byeNode.value == value:  
                break
            prev = byeNode  
            byeNode = byeNode.get_next()
            prev.next = byeNode.get_next()

    def remove_head(self):
        if self.head is None and self.tail is None:
            return
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value
            
    def remove_tail(self):
        if self.head is None and self.tail is None:
            return
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
        return value

    # print method
    def printMe(self):
        current = self.head
        while(current):
            print(current.value)
            current = current.next
