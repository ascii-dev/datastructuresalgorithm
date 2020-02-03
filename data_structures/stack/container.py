from main import Node


class StackWithNodes(object):
    """Implementing stacks with a node container"""

    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, item):
        new_node = Node(item)
        if self.top:
            new_node.set_next(self.top)
        self.top = new_node
        self.length += 1

    def pop(self):
        if self.top:
            temp = self.top
            if self.top.next:
                self.top = self.top.next
            self.length -= 1
            return temp.item
        return Exception("Stack is empty")

    def peek(self):
        if self.top:
            return self.top.item
        return Exception("Stack is empty")

    def print_stack(self):
        next_item = self.top
        while next_item:
            print(next_item.item)
            next_item = next_item.next


if __name__ == "__main__":
    new_stack = StackWithNodes()
    new_stack.print_stack()
    new_stack.push(1)
    new_stack.push(2)
    new_stack.push(3)
    new_stack.push(4)
    new_stack.push(5)
    new_stack.print_stack()
    print(new_stack.pop())
    print(new_stack.peek())
    new_stack.print_stack()
