"""
This script uses IBM Watson Language Translator to translate text between English and French.

Before using the script, ensure that the necessary IBM Cloud API credentials are saved as 
environment variables with the names 'apikey' and 'url'.

"""

import enum
import json
import os

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3, ApiException
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
VERSION = "2018-05-01"

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)
language_translator.set_service_url(URL)

class Language(enum.Enum):
    """An enumeration of the supported languages."""
    ENGLISH = 'en'
    FRENCH = 'fr'

    def __str__(self) -> str :
        return self.value

def translate(text : str, source : Language, target : Language) -> str :
    """Translates text from one language to another."""
    
    if text is None: 
        return None

    try:
        translation = language_translator.translate(
            text=text,
            source=str(source),
            target=str(target)
        ).get_result()

        # ensure_ascii is set to False to avoid escaping non-ASCII characters.
        # This is necessary for accented characters used in French, Spanish, etc.
        translated_text = json.dumps(
            translation['translations'][0]['translation'],
            ensure_ascii=False
        )

        # removing double quotes from the output
        return translated_text[1:-1]

    except ApiException as ex:
        return f"Method failed with status code {ex.code}: {ex.message}"

def english_to_french(english_text : str) -> str :
    """Translates English text to French."""
    return translate(english_text, Language.ENGLISH, Language.FRENCH)

def french_to_english(french_text : str) -> str :
    """Translates French text to English."""
    return translate(french_text, Language.FRENCH, Language.ENGLISH)
