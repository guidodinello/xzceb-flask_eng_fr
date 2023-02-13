import unittest
from translator import english_to_french, french_to_english
from typing import TypeVar

TranslationFunction = TypeVar('TranslationFunction', english_to_french, french_to_english)

class TestMachineTranslation(unittest.TestCase):

    def _test_translate(self, 
        func : TranslationFunction, 
        samples : "list[tuple[str, str]]"
        ) : 
        for (input, expected) in samples:
            self.assertEqual(func(input), expected)

    def test_english_to_french(self):

        self._test_translate( english_to_french,
        [
            ("My name is Foo", "Mon nom est Foo"),
            ("This is a test", "Il s'agit d'un test"),
            ("Hello", "Bonjour"),
            (None, "Method failed with status code 400: Bad Request, text must be provided.")
        ])

    def test_french_to_english(self):

        self._test_translate( french_to_english,
        [
            ("Mon nom est Foo", "My name is Foo"),
            ("Il s'agit d'un test", "This is a test"),
            ("Bonjour", "Hello"),
            (None, "Method failed with status code 400: Bad Request, text must be provided.")
        ])

if __name__ == '__main__':
    unittest.main()