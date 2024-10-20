import unittest
from src.binary_tree import BinaryTree

class BinaryTreeTest(unittest.TestCase):

    # yeah im not asserting everything because i am lazy
    def test_append_node(self):
        tree = BinaryTree()

        tree.insert_recursive(10)
        tree.insert_recursive(15)
        tree.insert_recursive(6)
        tree.insert_recursive(21)
        tree.insert_recursive(20)
        tree.insert_recursive(3)
        tree.insert_recursive(7)

        self.assertEqual(tree.search(15).data, 15)
        self.assertEqual(tree.search(77), None)
    
    def test_inorder(self):
        # Setup
        tree = self.get_basic_tree()
        expected_inorder = [1, 3, 4, 5, 9 ,10, 13, 17, 18, 20, 25, 30]
        
        # Run
        result = tree.inorder()

        # Validate
        self.assertEqual(len(result), 12)
        self.assertEqual(len(result), 12)
        for i, node in enumerate(result):
            self.assertEqual(expected_inorder[i], node.data)

    def test_preorder(self):
        # Setup
        tree = self.get_basic_tree()
        expected_preorder = [10, 5, 3, 1, 4, 9, 20, 18, 13, 17, 25, 30]
        
        # Run
        result = tree.preorder()

        # Validate
        self.assertEqual(len(result), 12)
        for i, node in enumerate(result):
            self.assertEqual(expected_preorder[i], node.data)

    def test_postorder(self):
        # Setup
        tree = self.get_basic_tree()
        expected_postorder = [1, 4, 3, 9, 5, 17, 13, 18, 30, 25, 20, 10]
        
        # Run
        result = tree.postorder()

        # Validate
        self.assertEqual(len(result), 12)
        self.assertEqual(len(result), 12)
        for i, node in enumerate(result):
            self.assertEqual(expected_postorder[i], node.data)

    def test_delete(self):
        # Setup
        tree = self.create_tree([100, 75, 125, 65, 85, 115, 150, 60, 70, 80, 95, 110, 120, 135, 175])
        expected = [60, 65, 70, 75, 80, 85, 95, 110, 115, 120, 125, 135, 150, 175]

        # Run
        tree.delete(100)

        # Validate 
        result = tree.inorder()
        result_data = []
        for node in result:
            result_data.append(node.data)

        self.assertEqual(expected, result_data)
        


    # Helpers

    def get_basic_tree(self):
        inputs = [10, 5, 20, 18, 25, 3, 9, 4, 13, 17, 30, 1]
        tree = BinaryTree()
        for x in inputs:
            tree.insert_iterative(x)
        return tree
    
    def create_tree(self, data):
        tree = BinaryTree()
        for x in data:
            tree.insert_iterative(x)
        return tree

    

        

