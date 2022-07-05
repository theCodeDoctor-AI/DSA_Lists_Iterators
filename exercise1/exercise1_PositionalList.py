'''
    Mark Randall #301178066
    Data Structures and Algorithms
    COMP254 Sec.003
    Assignment #4
    For Professor Salima Alim
    July 2nd, 2022
'''

from typing import Union, Any
from exercise1_mock_interface import PositionalInterface
from exercise1_doubly_linked import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase, PositionalInterface):
    '''A sequential container of elements allowing positional access.'''

    class Position:
        '''An abstraction representing the location of a single element.'''

        def __init__(self, container, node):
            '''Constructor should not be invoked by user.'''
            self._container = container
            self._node = node

        def element(self) -> Any:
            '''Return the element stored at this Position.'''
            return self._node._element

        def __eq__(self, other) -> bool:
            '''Return True if other is a Position representing the same location.'''
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other) -> bool:
            '''Return True if other does not represent the same location.'''
            return not(self == other)

    # utility fucntion
    def _validate(self, p) -> Union[Any, TypeError, ValueError]:
        '''Return position's node, or raise appropriate error if invalid.'''
        if not isinstance(p, self.Position):
            raise TypeError('p must be a proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node) -> Union['Position', None]:
        '''Return Position instance for given node (or None if sentinal).'''
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self) -> Union['Position', None]:
        '''Return the first Position in the list (or None if the list is empty).'''
        return self._make_position(self._header._next)

    def last(self) -> Union['Position', None]:
        '''Return the last Position in the list (or None if the list is empty).'''
        return self._make_position(self._trailer._prev)

    def before(self, p) -> Union['Position', None]:
        '''Return the Position just before Position p (or None if the list is empty).'''
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p) -> Union['Position', None]:
        '''Return the Position just after Position p (or None if p is the last).'''
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self) -> iter:
        '''Generate a forward iteration for the elements in the list.'''
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)


    ## Mutators
    #override ingerited version to return Position instead of a Node
    def _insert_between(self, element, predecessor, successor) -> None:
        '''Add element between existing nodes and return new Position.'''
        node = super()._insert_between(element, predecessor, successor)
        return self._make_position(node)

    def add_first(self, element) -> None:
        '''Insert element at the front of the list and return new Position.'''
        return self._insert_between(element, self._header, self._header._next)

    def add_last(self, element) -> None:
        '''Insert element at the back of the list and return new Position.'''
        return self._insert_between(element, self._trailer._prev, self._trailer)
    
    def add_before(self, p, element) -> None:
        '''Insert element into list before Position pp and return new Position.'''
        original = self._validate(p)
        return self._insert_between(element, original._prev, original)

    def add_after(self, p, element) -> None:
        '''Insert element into list after Position p and return new Position.'''
        original = self._validate(p)
        return self._insert_between(element, original, original._next)

    def delete(self, p) -> Union[Any, None]:
        '''Remove and return the element at Position p.'''
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, element) -> Any:
        '''Replace the element at Position p with element.
        
        Return the element formerly at Position p.
        '''
        original = self._validate(p)
        old_value = original._element
        original._element = element
        return old_value

    def find_position(self, element) -> Union['Position', None]:
        '''Returns a new Position object pointing to the Node containing element, or None if not found.'''
        current_pos = self.first()
                
        while current_pos is not None:
            current_ele = current_pos.element()[0]
            if current_ele == element:
                return current_pos # found a match
            current_pos = self.after(current_pos)
                
        return None # no match was found so return None


if __name__ == '__main__':
    test = PositionalList()

    mark_pos = test.add_first('Mark')
    bibi_pos = test.add_first('Bibi')
    megan_pos = test.add_first('Megan')
    marcus_pos = test.add_first('Marcus')

    print('\nOriginal position objects:')
    print(f'position -> {mark_pos} has element -> {mark_pos.element()[0]}')
    print(f'position -> {bibi_pos} has element -> {bibi_pos.element()[0]}')
    print(f'position -> {megan_pos} has element -> {megan_pos.element()[0]}')
    print(f'position -> {marcus_pos} has element -> {marcus_pos.element()[0]}')

    print('\nNew position object for element "Mark":')
    mark_test_pos = test.find_position('Mark')
    print(f'position -> {mark_test_pos} has element -> {mark_test_pos.element()[0]}')

    print('\nValidate... Is new position equal to original position:')
    print(mark_test_pos == mark_pos)

    print('\nTesting searching for a non-existant element (should return None):')
    none_test = test.find_position('Zippety-do-dah')
    print(f'Searched for "Zippety-do-dah"... Returned value => {none_test}')
    



