import unittest
from src.hello_world import helloWorld

class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        hw = helloWorld()
        expected = "Hello World!"
        actual = hw.say_hello()
        self.assertEqual(expected, actual)