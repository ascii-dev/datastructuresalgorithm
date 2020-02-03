class Node(object):
    """A single node element for use with containers"""

    def __init__(self, item):
        self.item = item
        self.__next = None
        self.__previous = None

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
