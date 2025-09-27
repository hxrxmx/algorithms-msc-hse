class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            print("pop from empty stack")
            return None
        val = self.top.value
        self.top = self.top.next
        return val

    def peek(self):
        if self.is_empty():
            print("peek from empty stack")
            return None
        return self.top.value


class Queue:
    def __init__(self):
        self.top = None
        self.bottom = None

    def is_empty(self):
        return self.top is None

    def enqueue(self, value):
        node = Node(value)
        if self.bottom is None:
            self.top = node
            self.bottom = node
        else:
            self.bottom.next = node
            self.bottom = node

    def dequeue(self):
        if self.is_empty():
            print("dequeue from empty queue")
            return None
        val = self.top.value
        self.top = self.top.next
        if self.top is None:
            self.bottom = None
        return val

    def peek(self):
        if self.is_empty():
            print("peek from empty queue")
            return None
        return self.top.value
