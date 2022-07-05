'''
    Mark Randall #301178066
    Data Structures and Algorithms
    COMP254 Sec.003
    Assignment #4
    For Professor Salima Alim
    July 2nd, 2022
'''

class Empty(Exception):
    '''Error attempting to access an element from an empty container.'''
    pass

class LinkedQueue:
    '''FIFO queue implementation using a singly linked list for storage.'''

    class _Node:
        '''Lightweight, nonpublic class for storing a singly linked node.'''
        __slots__ = '_element', '_next' # streamlines memory usage

        def __init__(self, element = None, next = None):
            self._element = element
            self._next = next

    def __init__(self):
        '''Create an empty queue.'''
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self) -> int:
        '''Return True if the queue is empty.'''
        return self._size

    def is_empty(self):
        '''Returns True if Stack is empty'''
        return self._size == 0

    def first(self):
        '''Return (but do not remove) the element at the front of the queue.'''
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def dequeue(self):
        '''Remove and return the first element of the queue
        
        Raise Empty exception if the queue is empty.
        '''
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, element):
        '''Add an element to the back of the Queue'''
        newest = self._Node(element, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        

    def __str__(self):
        string = ''
        temp = self._head
        while temp:
            string += f'{str(temp._element)}' 
            string += ' --> ' if temp._next else ''
            temp = temp._next
        return string

    def concatenate(self, other: 'LinkedQueue') -> None:
        '''Removes all elements from LinkedQueue other and appends them to LinkedQueue self'''
        self._tail._next = other._head
        self._size += len(other)
        other._head = other._tail = None
        other._size = 0

    

if __name__ == '__main__':
    linked_queue = LinkedQueue()
    linked_queue.enqueue('C#')
    linked_queue.enqueue('Python')
    linked_queue.enqueue('JavaScript')
    linked_queue.enqueue('Java')
    print(linked_queue)
    print(len(linked_queue))

    linked_queue2 = LinkedQueue()
    linked_queue2.enqueue('.NET')
    linked_queue2.enqueue('Django')
    linked_queue2.enqueue('React')
    linked_queue2.enqueue('JUnit')
    print(linked_queue2)
    print(len(linked_queue2))

    linked_queue.concatenate(linked_queue2)
    print(linked_queue)
    print(len(linked_queue))
    print(linked_queue2)
    print(len(linked_queue2))
