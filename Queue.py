class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def en_queue(self, data):
        if self.front is None:
            self.front = self.rear = Node(data)
        else:
            temp = Node(data)
            self.rear.next = temp
            self.rear = temp

    def de_queue(self):
        data = self.front.data
        self.front = self.front.next
        return data

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

    def display(self):
        temp = self.front
        while temp is not None:
            print(temp.data)
