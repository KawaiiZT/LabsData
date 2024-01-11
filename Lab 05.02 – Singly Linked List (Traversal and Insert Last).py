"""Docstring"""
class DataNode:
    """Docstring"""
    def __init__(self, data, next=None):
        """Docstring"""
        self._data = data
        self._next = next

    def get_data(self):
        """Docsitrng"""
        return self._data

    def set_data(self, data):
        """Docstring"""
        self._data = data

    def get_next(self):
        """Docsitrng"""
        return self._next

    def set_next(self, next):
        """Docstring"""
        self._next = next

class SinglyLinkedList: 
    """Docstring"""
    def __init__(self):
        """Initialize an empty singly linked list."""
        self.head = None
        
    def traverse(self):
        """Traverse the linked list and print each element with arrows."""
        current = self.head
        if not current:
            print("This is an empty list.")
            return

        while current.get_next():
            print(current.get_data(), end=" -> ")
            current = current.get_next()
        print(current.get_data())

    def insert_last(self, data):
        new_node = DataNode(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.get_next():
            current = current.get_next()
        current.set_next(new_node)

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input())
    mylist.traverse()

main()