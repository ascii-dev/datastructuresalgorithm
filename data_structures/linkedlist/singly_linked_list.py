from main import Node


class SinglyLinkedList(object):
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def first(self):
        if self.is_empty():
            return None
        return self.__head.item

    def last(self):
        if self.is_empty():
            return None
        return self.__tail

    def add_first(self, item):
        self.__head = Node(item, self.__head)
        if not self.__tail:
            self.__tail = self.__head
        self.__size += 1

    def add_last(self, item):
        item = Node(item)
        if self.__tail:
            self.__tail.next = item
        else:
            self.__tail = self.__head = item
        self.__size += 1

    def remove_first(self):
        if self.is_empty():
            return None
        temp = self.__head
        self.__head = self.__head.next
        self.__size -= 1
        if self.is_empty():
            self.__tail = None
        return temp
