class Node(object):
    """A single node element for use with containers"""

    def __init__(self, item):
        self.item = item
        self.next = None
        self.previous = None

    def set_next(self, item):
        self.next = item

    def set_previous(self, item):
        self.previous = item
