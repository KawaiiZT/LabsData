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
class BST:
    """Docstring"""
    def __init__(self):
        """Announced Initation"""
        self.root = None
    def get_root(self):
        return self.root
    def set_root(self, data):
        self.root = data
    def insert(self, data):
        self.root = self._insert_recursive(self.root, data)
    def _insert_recursive(self, node, data):
        """Helper function for recursive insertion"""
        # If the tree is empty, create a new node with the given data
        if node is None:
            return BSTNode(data)

        # If the data is smaller than the current node, go to the left subtree
        if data < node.get_data():
            node.set_left(self._insert_recursive(node.get_left(), data))
        # If the data is larger than the current node, go to the right subtree
        elif data > node.get_data():
            node.set_right(self._insert_recursive(node.get_right(), data))

        # If the data is eq ual to the current node, do nothing (avoid duplicates)

        return node 
    def preorder(self):
        """Traverse the tree in Pre-Order and print node values"""
        result = self._preorder_recursive(self.root)
        print(result, end="")

    def _preorder_recursive(self, node):
        """Helper function for recursive Pre-Order traversal"""
        if node is None:
            return ""

        # Process the current node
        result = "-> " + str(node.get_data()) + " "

        # Recursively traverse the left and right subtrees
        result += self._preorder_recursive(node.get_left())
        result += self._preorder_recursive(node.get_right())

        return result

def main():
        my_bst = BST()
        for i in range(int(input())):
            my_bst.insert(int(input()))

        print("Preorder: ", end="")
        my_bst.preorder()

main()
