class _DoublyLinkedBase:
    '''A base class providing a doubly linked list representation.'''

    class _Node:
        '''Lightweight, nonpublic class for storing a soubly linked node.'''
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element,
            self._prev = prev,
            self._next = next

    def __init__(self):
        '''Creates an empty list.'''
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        '''Return the number of elements in the list.'''
        return self._size

    def is_empty(self):
        '''Return True if list is empty.'''
        return self._size == 0

    def _insert_between(self, element, predecessor, successor):
        '''Add element betweeen two existing nodes and return new node.'''
        newest = self._Node(element, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        '''Delete nonsentinal node form the list and return its element.'''
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None # Depracate the node
        return element