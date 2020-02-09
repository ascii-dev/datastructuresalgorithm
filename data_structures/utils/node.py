class Node(object):
    """A single node element for use with containers"""

    def __init__(self, item, next=None, previous=None):
        self.item = item
        self.__next = next
        self.__previous = previous

    @property
    def next(self):
        return self.__next

    @property
    def previous(self):
        return self.__previous

    @next.setter
    def next(self, item):
        self.__next = item

    @previous.setter
    def previous(self, item):
        self.__previous = item
