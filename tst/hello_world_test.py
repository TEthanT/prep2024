import unittest
from src.hello_world import helloWorld

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.hw = helloWorld()

    def testHelloWorld(self):
        expected = "Hello World!"
        actual = self.hw.say_hello()
        self.assertEqual(expected, actual)