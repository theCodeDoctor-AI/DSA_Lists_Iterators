from abc import ABC, abstractmethod

class PositionalInterface(ABC):
    
    @abstractmethod
    def __len__(self):
        '''Return the number of elements in the list.'''
        pass

    @abstractmethod
    def is_empty(self):
        '''Return True if list is empty.'''
        pass

    @abstractmethod
    def first(self):
        '''Return the first Position in the list (or None if the list is empty).'''
        pass

    @abstractmethod
    def last(self):
        '''Return the last Position in the list (or None if the list is empty).'''
        pass

    @abstractmethod
    def before(self, p):
        '''Return the Position just before Position p (or None if the list is empty).'''
        pass

    @abstractmethod
    def after(self, p):
        '''Return the Position just after Position p (or None if p is the last).'''
        pass

    @abstractmethod
    def add_last(self, element):
        '''Insert element at the back of the list and return new Position.'''
        pass

    @abstractmethod
    def add_before(self, element):
        '''Insert element into list before Position pp and return new Position.'''
        pass

    @abstractmethod
    def replace(self, p, element):
        '''Replace the element at Position p with element.
        
        Return the element formerly at Position p.
        '''
        pass

    @abstractmethod
    def delete(self, p):
        '''Remove and return the element at Position p.'''
        pass

    @abstractmethod
    def __iter__(self):
        '''Generate a forward iteration for the elements in the list.'''
        pass

    @abstractmethod
    def find_position(self, element):
        '''Returns a new position object pointing to node containing element or None if not found.'''
        pass


        