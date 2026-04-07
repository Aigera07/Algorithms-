"""Algorithms and Data Structures 1 AI - Linked Lists."""

from dataclasses import dataclass
import sys
from typing import Any, Iterator, Sequence, overload, override


@dataclass
class MyListNode:
    value: int
    prev_node: "MyListNode | None" = None
    next_node: "MyListNode | None" = None

class MySortedDoublyLinkedList(Sequence[int]):
    """A base class providing a doubly linked list representation."""

    @overload
    def __init__(self) -> None:
        """Initializes a new SortedDoublyLinkedList."""
        ...

    @overload
    def __init__(self, head: MyListNode, tail: MyListNode, size: int):
        """Initializes a new SortedDoublyLinkedList using predefined `head` and `tail`.

        Used for testing.
        """
        ...

    def __init__(
        self,
        head: "MyListNode | None" = None,
        tail: "MyListNode | None" = None,
        size: int = 0,
    ) -> None:
        self._head = head
        self._tail = tail
        self._size = size

    @override
    def __len__(self) -> int:
        """Return the number of elements in the list."""
        return self._size

    @override
    def __iter__(self) -> Iterator[int]:
        node = self._head
        while node:
            yield node.value
            node = node.next_node

    @override
    def __reversed__(self) -> Iterator[int]:
        node = self._tail
        while node:
            yield node.value
            node = node.prev_node

    @overload
    def __getitem__(self, index: int) -> int:
        ...

    @overload
    def __getitem__(self, index: slice) -> Sequence[int]:
        ...

    @override
    def __getitem__(self, index: int | slice) -> int | Sequence[int]:
        # proper implementation of Sequence interface
        if isinstance(index, slice):
            rv = []
            for idx in range(*index.indices(len(self))):
                rv.append(self[idx])
            return rv
        if isinstance(index, int) and index < 0:
            index = len(self) - index
        return self._get_value(index)

    def _get_value(self, index: int) -> int:
        """Return the value (elem) at position "index" without removing the node.

        Args:
            index (int): 0 <= index < length of list

        Returns:
            int: Retrieved value.

        Raises:
            IndexError: If the passed index out of range.
        """
        # TODO
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")

        # startinf from the beginning
        current = self._head
        
        # starting our search
        for _ in range(index):
            if current:
                current = current.next_node
        
        # if condition was true and we found the point, then return
        if current:
            return current.value
        raise IndexError("Node not found")
    

    @override
    def index(self, value: Any, start: int = 0, stop: int = sys.maxsize) -> int:
        """Return the index of the first occurrence of `value` in the list.

        Args:
            val (Any): Value to be searched.
            start (int): A number representing where to start the search.
            stop (int): A number representing where to end the search.

        Raises:
            ValueError: If the given value isn't found.
            
        Returns:
            int: Retrieved index.
        """
        if not isinstance(value, int):
            raise ValueError(f"{value} is not in list.")
        # TODO
        
        stop = min(stop, self._size)
        # limiting our search
        current = self._head
        current_index = 0
        # startinf from the very first index
        while current and current_index < start:  
                current = current.next_node
                current_index += 1
                # we have to find our start
        while current and current_index < stop: # searching from strat till stop
                if current.value == value:
                    return current_index  # if found then return it
                current = current.next_node
                current_index += 1
        raise ValueError(f"{value} is not in list.")
        # if didnt find then its error        

    def insert(self, val: int) -> None:
        """Add a new node containing "val" to the list, keeping the list in ascending order.

        Args:
            val (int): Value to be added.

        Raises:
            TypeError: If val is not an int.
        """
        # TODO
        if not isinstance(val, int):
            raise TypeError("Value must be an integer") 
        # value must be integer
        new_node = MyListNode(val) # creating new node for our value
        # in the case below if there are no nodes or our value <= selg.head
        if self._head is None or val <= self._head.value:
            new_node.next_node = self._head # according to our condition making new head
            if self._head:
                self._head.prev_node = new_node #link new node with self.head
            self._head = new_node
            if self._tail is None: # if there are no nodes
                self._tail = new_node
            self._size += 1
            return
        
        # in the case below: if everything its okay, then try to insert it between nodes
        current = self._head
        while current.next_node and current.next_node.value < val:
            current = current.next_node
            # searching place untill our condition will be true
        new_node.next_node = current.next_node
        new_node.prev_node = current # inserting new node and linking them 

        if current.next_node: # if inserting in the middle of the nodes 
            current.next_node.prev_node = new_node
        else: # if inserting in the end
             self._tail = new_node
        current.next_node = new_node
        self._size += 1 # increasing our size
        return
    
        

    def remove(self, val: int) -> None:
        """Remove the first occurrence of the parameter "val".

        Args:
            val (int): Value to be removed.

        Raises:
            ValueError: If `val` is not present.
        """
        if not isinstance(val, int):
            raise ValueError(f"{val} is not in list.")
        # TODO
        else: # if val is int
            current = self._head # starting from the head of the node
            while current:
                if current.value == val:
                    # starting to search value
                    if current.prev_node: # inserting our value with left neighbor nodes 
                        current.prev_node.next_node = current.next_node
                    else:
                        # if there are no node, then its head
                        self._head = current.next_node

                    if current.next_node:
                        current.next_node.prev_node = current.prev_node
                    else: # if there are no nodes in the right side, then its tail
                        self._tail = current.prev_node

                    self._size -= 1 # decreasing the size
                    return 
                
                # if current.value != val
                else:
                    current = current.next_node # move forward
            
        # if value is not present
        raise ValueError(f"{val} is not in list.") 


    def remove_all(self, val: int) -> int:
        """Remove all occurrences of the parameter "val".

        Args:
            val (int): Value to be removed.

        Returns:
            int: the number of elements removed.
        """
        # TODO
        count = 0  # this is our cointig point
        current = self._head # this is our starting point

        while current:
            next_node = current.next_node # before removing it should know the next node values

            if current.value == val: # giving a condition, if its true then link nodes with each other
                if current.prev_node:
                    current.prev_node.next_node = current.next_node
                else:
                    self._head = current.next_node 
                    
                if current.next_node:
                    current.next_node.prev_node = current.prev_node
                else:
                    self._tail = current.prev_node # repeating the same condition but for tail 
                self._size -= 1 # dereasing the size 
                count += 1 # counts the removings
            current = next_node
            
        return count

    def remove_duplicates(self) -> None:
        """Remove all duplicate occurrences of values from the list."""
        # TODO
        current = self._head
        while current:
            next_node = current.next_node # comparing our starting point with the next node and if condition is true, then remove prev.value
            if next_node is not None and current.value == current.next_node.value:
                self.remove(current.value)
            current = next_node
            

    def filter_n_max(self, n: int) -> None:
        """Filter the list to only contain the "n" highest values.

        Args:
            n (int): 0 < n <= length of list

        Raises:
            TypeError: If the passed value n is not an int.
            ValueError: If the passed value n is out of range.
        """
        # TODO
        if not isinstance(n, int):
            raise TypeError("n must be int")
        if n <= 0  or n > self._size:
            raise ValueError("n is out of range")
        if n== self._size:
            return 
        steps_to_skip = self._size - n # we have to find new first node
        current = self._head 
        for _ in range(steps_to_skip): 
            current = current.next_node 
        self._head = current
        self._head.prev_node = None # remoning the other nodes and making our current - self._head 
        self._size = n 

    def filter_odd(self) -> None:
        """Filter the list to only contain odd values."""
        # TODO
        current = self._head 
        while current:
            next_node = current.next_node
            if current.value % 2 == 0: #removing all even values
                self.remove(current.value)
            current = next_node





    def filter_even(self) -> None:
        """Filter the list to only contain even values."""
        # TODO
        current = self._head 
        while current:
            next_node = current.next_node
            if current.value % 2 == 1: #removing all odd values
                self.remove(current.value)
            current = next_node
