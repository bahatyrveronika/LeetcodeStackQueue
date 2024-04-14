class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def pop(self):
        if self.head:
            item = self.head
            self.head = self.head.next
            return item
        raise ValueError('Queue is empty.')

    @property
    def peek(self):
        return self.head.item

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        s = ''
        current = self.head
        while current is not None:
            s += str(current.item)+' '
            current = current.next
        return f'start -> {s}<- end'
        
class MyStack:
    def __init__(self):
        self.q_push = Queue()
        self.q_pop = Queue()

    def push(self, x: int) -> None:
        while not self.q_push.is_empty():
            self.q_pop.add(self.q_push.pop().item)
        self.q_push.add(x)
        while not self.q_pop.is_empty():
            self.q_push.add(self.q_pop.pop().item)

    def pop(self) -> int:
        if self.q_push.is_empty():
            raise ValueError('Stack is empty')
        return self.q_push.pop().item

    def top(self) -> int:
        if self.q_push.is_empty():
            raise ValueError('Stack is empty')
        return self.q_push.peek

    def empty(self) -> bool:
        return self.q_push.is_empty()
