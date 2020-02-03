class QueueWithList(object):
    """Queue implementation with list"""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def front(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    a_queue = QueueWithList()
    a_queue.enqueue(1)
    a_queue.enqueue(2)
    a_queue.enqueue(3)
    a_queue.enqueue(4)
    a_queue.enqueue(5)
    print(a_queue.items)
    print(a_queue.dequeue())
    print(a_queue.items)
    print(a_queue.front())
    print(a_queue.size())
