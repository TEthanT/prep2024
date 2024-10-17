import unittest
from src.hello_world import helloWorld

class TestHelloWorld(unittest.TestCase):

    def set_up(self):
        self.hw = helloWorld()

    def test_hello_world(self):
        expected = "Hello World!"
        actual = self.hw.say_hello()
        self.assertEqual(expected, actual)