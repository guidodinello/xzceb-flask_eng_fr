import unittest
from translator import english_to_french, french_to_english
from typing import TypeVar

TranslationFunction = TypeVar('TranslationFunction', english_to_french, french_to_english)
AssertionMethod = TypeVar('AssertionMethod', unittest.TestCase.assertEqual, unittest.TestCase.assertNotEqual)

class TestMachineTranslation(unittest.TestCase):

    def _test_translate(self, 
        assert_func : AssertionMethod,
        trans_func : TranslationFunction, 
        samples : "list[tuple[str, str]]"
        ) : 
        for (input, expected) in samples:
            assert_func(trans_func(input), expected)

    def test_english_to_french(self):

        self._test_translate( 
            self.assertEqual,
            english_to_french,
        [
            ("My name is Foo", "Mon nom est Foo"),
            ("This is a test", "Il s'agit d'un test"),
            ("Hello", "Bonjour")
        ])

        self._test_translate( 
            self.assertNotEqual,
            english_to_french,
        [
            ("My name is Foo", "My name is Foo"),
            ("This is a test", "This is a test"),
            ("Hello", "Hello")
        ])

        self.assertIsNone(english_to_french(None))

    def test_french_to_english(self):

        self._test_translate( 
            self.assertEqual,            
            french_to_english,
        [
            ("Mon nom est Foo", "My name is Foo"),
            ("Il s'agit d'un test", "This is a test"),
            ("Bonjour", "Hello")
        ])

        self._test_translate( 
            self.assertNotEqual,            
            english_to_french,
        [
            ("Mon nom est Foo", "Mon nom est Foo"),
            ("Il s'agit d'un test", "Il s'agit d'un test"),
            ("Bonjour", "Bonjour")
        ])

        self.assertIsNone(french_to_english(None))

if __name__ == '__main__':
    unittest.main()
