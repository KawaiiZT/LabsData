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

PNEW = DataNode(input())
print(PNEW.get_data())  # Use the get_data() method to access the data
print(PNEW.get_next())  # Use the get_next() method to access the next node
