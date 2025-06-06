class Stack:
    def __init__(self):
        self.items = []


    def push(self, value):
        self.items.append(value)


    def pop(self):
        if Stack.size() == 0:
            return None
        return self.items.pop(-1)


    def peek(self):
        if Stack.size() == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)



