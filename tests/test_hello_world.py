import unittest
from PACKAGE_NAME_HERE.hello_world_module import return_hello

class TestHelloWorld(unittest.TestCase):
    def test_return_hello(self):
        self.assertEqual(return_hello(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()