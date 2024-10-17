import unittest
from src.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def test_append_one_node(self):
        list = LinkedList()

        list.insert(0)
        
        self.assertEqual(list.is_empty(), False)
        list.to_string()

    def test_create_list(self):
        list = LinkedList()

        list.insert(0)
        list.insert(99)
        list.insert(12)
        list.insert(52)
        list.insert(78)

        self.assertEqual(list.search(12).val, 12)
        self.assertEqual(list.search(12).next.val, 52)
        self.assertEqual(list.head.val, list.search(0).val)
        self.assertEqual(list.tail, list.search(78))
        self.assertEqual(list.tail.next, None)
        list.to_string()