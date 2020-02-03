class StackWithList(object):
    """Implementing stack data structure with list"""

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()
        raise Exception("Stack is empty")

    def peek(self):
        if len(self.items) != 0:
            return self.items[-1]
        raise Exception("Stack is empty")

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    a_stack = StackWithList()
    a_stack.push(1)
    a_stack.push(2)
    a_stack.push(3)
    a_stack.push(4)
    print(a_stack)
    print(a_stack.size())
    print(a_stack.peek())
    print(a_stack.pop())
    print(a_stack.peek())
