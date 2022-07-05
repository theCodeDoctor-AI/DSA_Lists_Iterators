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

class LinkedStack:
    '''LIFO Stack implementation using a singly linked list for storage'''

    # nested Node class
    class _Node:
        '''Lightweight, nonpublic class for storing a singly linked node'''
        __slots__ = '_element', '_next' # streamlines memory usage

        def __init__(self, element = None, next = None):
            self._element = element
            self._next = next

        # Stack methods
    
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self) -> int:
        '''Return the number of elements in the stack.'''
        return self._size
    
    def is_empty(self) -> bool:
        '''Return True if stack is empty.'''
        return self._size == 0

    def push(self, element) -> None:
        '''Add element to the top of the stack'''
        self._head = self._Node(element, self._head)
        self._size += 1

    def top(self) -> _Node._element:
        '''Return (but do not remove) the element at the top of the stack.
        
        Raise Empty exeption if the stack is empty
        '''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element # top of stack is the head of the list

    def pop(self) -> _Node._element:
        '''Remove and return the element from the top of the stack
        
        Raise Empty exception if the stack is empty
        '''
        if self.is_empty():
            raise Empty('The stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
    
    # def __str__(self):
    #     temp = self._head
    #     string = ''
    #     while True:
    #         string += str(temp._element)
    #         temp = temp._next
    #         if temp._element is None:
    #             break
    #         #string += ' --> ' if temp._next._element else ''
    #     return string

'''Write a recursive method for removing all the elements from a stack S. Write the necessary code to test the method.'''

def empty_stack(stack: 'LinkedStack'):
    if len(stack) == 0:
        return
    stack.pop()
    empty_stack(stack)

if __name__ == '__main__':
    stack = LinkedStack()
    stack.push('Mark')
    stack.push('Bibi')
    stack.push('Megan')
    stack.push('Marcus')
    print(len(stack))

    empty_stack(stack)
    print(len(stack))