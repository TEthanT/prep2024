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

        self.assertEqual(tree.search(15), True)
        self.assertEqual(tree.search(77), False)
    
    def test_inorder(self):
        # Setup
        tree = self.get_basic_tree()
        expected_inorder = [1, 3, 4, 5, 9 ,10, 13, 17, 18, 20, 25, 30]
        
        # Run
        result = tree.inorder()

        # Validate
        self.assertEqual(len(result), 12)
        self.assertEqual(result, expected_inorder)

    def test_preorder(self):
        # Setup
        tree = self.get_basic_tree()
        expected_preorder = [10, 5, 3, 1, 4, 9, 20, 18, 13, 17, 25, 30]
        
        # Run
        result = tree.preorder()

        # Validate
        self.assertEqual(len(result), 12)
        self.assertEqual(result, expected_preorder)

    def test_postorder(self):
        # Setup
        tree = self.get_basic_tree()
        expected_postorder = [1, 4, 3, 9, 5, 17, 13, 18, 30, 25, 20, 10]
        
        # Run
        result = tree.postorder()

        # Validate
        self.assertEqual(len(result), 12)
        self.assertEqual(result, expected_postorder)


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

    

        

