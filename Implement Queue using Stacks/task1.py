class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        self.head = Node(item, self.head)

    def pop(self):
        item = self.head.item
        self.head = self.head.next
        return item

    @property
    def peek(self):
        return self.head.item

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count +=1
            current = current.next
        return count

    def __str__(self):
        s = ''
        cur = self.head
        while cur is not None:
            s = str(cur.item) + ' ' +s
            cur = cur.next
        return 'bottom -> '+ s+'<- top'

class MyQueue:
    def __init__(self):
        self.stack_push = Stack()
        self.stack_pop = Stack()

    def push(self, x):
        self.stack_push.push(x)

    def pop(self):
        if self.stack_pop.is_empty():
            while not self.stack_push.is_empty():
                self.stack_pop.push(self.stack_push.pop())
        return self.stack_pop.pop()

    def peek(self):
        if self.stack_pop.is_empty():
            while not self.stack_push.is_empty():
                self.stack_pop.push(self.stack_push.pop())
        return self.stack_pop.peek
    
    def empty(self):
        return self.stack_push.is_empty() and self.stack_pop.is_empty()