import unittest
import xmlrunner
from main import add, is_even

class TestMainFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertNotEqual(add(2, 2), 5)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(3))
        self.assertTrue(is_even(0))

if __name__ == '__main__':
    with open('test-results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False
        )
