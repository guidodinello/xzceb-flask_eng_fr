import unittest
from translator import english_to_french, french_to_english

class TestMachineTranslation(unittest.TestCase):

    def test_english_to_french(self):
        f = english_to_french
        self.assertEqual(f("Hello"), "Bonjour")
        self.assertNotEqual(f("Hello"), "Hello")
        self.assertIsNone(f(None))

    def test_french_to_english(self):
        f = french_to_english
        self.assertEqual(f("Bonjour"), "Hello")
        self.assertNotEqual(f("Bonjour"), "Bonjour")
        self.assertIsNone(f(None))

if __name__ == '__main__':
    unittest.main()
