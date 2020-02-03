from main import Node


class QueueWithContainer(object):
    """Implementing Queues with a node container"""

    def __init__(self):
        self.top = None
        self.bottom = None
        self.__size = 0

    def enqueue(self, item):
        new_item = Node(item)
        if self.bottom is None:
            self.top = self.bottom = new_item
        else:
            self.bottom.next = new_item
            self.bottom = self.bottom.next
        self.__size += 1

    def dequeue(self):
        if self.top is not None:
            temp = self.top
            self.top = temp.next
            self.__size -= 1
            return temp.item
        raise Exception("Queue is empty")

    def front(self):
        if self.top is not None:
            return self.top.item
        raise Exception("Queue is empty")

    @property
    def size(self):
        return self.__size


if __name__ == "__main__":
    a_queue = QueueWithContainer()
    a_queue.enqueue(0)
    a_queue.enqueue(1)
    a_queue.enqueue(2)
    a_queue.enqueue(3)
    a_queue.enqueue(4)
    a_queue.enqueue(5)
    print("=============== Size")
    print(a_queue.size)
    print("=============== Dequeue")
    print(a_queue.dequeue())
    print("=============== Size")
    print(a_queue.size)
    print("=============== Front")
    print(a_queue.front())
    print("===============")
