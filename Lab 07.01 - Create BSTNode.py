"""SSS"""
class BSTNode:
    """Docstring"""
    def __init__(self, data=None):
        """Announced Initation"""
        self.data = data
        self.left = None
        self.right = None
    def get_data(self):
        """T"""
        return self.data
    def set_data(self, data):
        """D"""
        self.data = data
    def get_left(self):
        """X"""
        return self.left
    def set_left(self, data):
        """S"""
        self.left = data
    def get_right(self):
        """S"""
        return self.right
    def set_right(self, data):
        """S"""
        self.right = data
p_new = BSTNode(int(input()))
print(p_new.get_data())
print(p_new.get_left())
print(p_new.get_right())
