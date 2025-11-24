"""
pydefine.i18n
~~~~~~~~~~~~~

Internationalization (i18n) support for pyDefine.

Provides translation capabilities for error explanations.
Currently includes stub for Hinglish (Hindi + English mix) translation.

Usage:
    from pydefine.i18n import set_language, translate_explanation
    
    set_language('hi')  # Hinglish
    translated = translate_explanation(explanation, 'hi')
"""

import re
from typing import Dict, Optional

# Current language (default: English)
_current_language = "en"

# Supported languages
SUPPORTED_LANGUAGES = {
    "en": "English",
    "hi": "Hinglish (Hindi + English)",
}


def set_language(language_code: str) -> bool:
    """
    Set the current language for translations.
    
    Args:
        language_code: Language code ('en', 'hi', etc.)
        
    Returns:
        True if language is supported, False otherwise
        
    Example:
        >>> set_language('hi')
        True
        >>> set_language('fr')
        False
    """
    global _current_language
    
    if language_code in SUPPORTED_LANGUAGES:
        _current_language = language_code
        return True
    else:
        print(f"⚠️  Warning: Language '{language_code}' not supported. Using English.")
        return False


def get_language() -> str:
    """
    Get the current language code.
    
    Returns:
        Current language code (e.g., 'en', 'hi')
    """
    return _current_language


def translate_explanation(text: str, target_language: str) -> str:
    """
    Translate an error explanation to target language.
    
    Args:
        text: English explanation text
        target_language: Target language code
        
    Returns:
        Translated text (or original if translation not available)
        
    Example:
        >>> text = "You tried to divide by zero"
        >>> translate_explanation(text, 'hi')
        "Aapne zero se divide karne ki koshish ki"
    """
    if target_language == "en":
        return text
    
    if target_language == "hi":
        return _translate_to_hinglish(text)
    
    # Fallback to English
    return text


def _translate_to_hinglish(text: str) -> str:
    """
    Translate English text to Hinglish (Hindi + English mix).
    
    This is a stub implementation with basic word replacements.
    For production, integrate with a proper translation API.
    
    Args:
        text: English text
        
    Returns:
        Hinglish text
    """
    # Basic word-level replacements (stub implementation)
    replacements = {
        # Common programming terms (keep English)
        "Python": "Python",
        "code": "code",
        "function": "function",
        "variable": "variable",
        "file": "file",
        "error": "error",
        "exception": "exception",
        
        # Verbs and actions
        "You tried": "Aapne koshish ki",
        "You wrote": "Aapne likha",
        "You pressed": "Aapne press kiya",
        "tried to": "koshish ki",
        "doesn't exist": "exist nahi karta",
        "doesn't follow": "follow nahi karta",
        "couldn't find": "nahi mil saka",
        "can't find": "nahi mil sakta",
        "doesn't have": "ke paas nahi hai",
        
        # Nouns
        "the language rules": "language ke rules",
        "the wrong type": "galat type",
        "a dictionary": "ek dictionary",
        "a list": "ek list",
        "a file": "ek file",
        "a folder": "ek folder",
        "the program": "program",
        "the computer": "computer",
        
        # Descriptors
        "wrong": "galat",
        "correct": "sahi",
        "invalid": "invalid",
        "missing": "missing",
        "too big": "bahut bada",
        "too long": "bahut lamba",
        
        # Common phrases
        "It's like": "Yeh aisa hai jaise",
        "This is": "Yeh hai",
        "Something went wrong": "Kuch galat ho gaya",
        "Check": "Check karein",
        "Make sure": "Pakka karein",
        "Use": "Use karein",
        "Install": "Install karein",
    }
    
    translated = text
    
    # Apply replacements (longer phrases first to avoid partial matches)
    for english, hinglish in sorted(replacements.items(), key=lambda x: -len(x[0])):
        translated = translated.replace(english, hinglish)
    
    return translated


def get_supported_languages() -> Dict[str, str]:
    """
    Get dictionary of supported language codes and names.
    
    Returns:
        Dictionary mapping language codes to full names
        
    Example:
        >>> langs = get_supported_languages()
        >>> print(langs['hi'])
        'Hinglish (Hindi + English)'
    """
    return SUPPORTED_LANGUAGES.copy()


def is_language_supported(language_code: str) -> bool:
    """
    Check if a language is supported.
    
    Args:
        language_code: Language code to check
        
    Returns:
        True if supported, False otherwise
    """
    return language_code in SUPPORTED_LANGUAGES


# Translation templates for common error messages
# This can be expanded with full translations in future versions
TRANSLATION_TEMPLATES = {
    "hi": {
        "SyntaxError": {
            "simple_explanation": (
                "Aapne Python code likha jo language ke rules follow nahi karta. "
                "Python samajh nahi saka ki aapne kya type kiya. "
                "Yeh aisa hai jaise galat grammar ke saath sentence likhna 📝"
            ),
            "fix_suggestion": (
                "Missing colons (:), unmatched parentheses/brackets check karein, "
                "ya keywords jaise 'if', 'for', 'def' mein typos dekhe"
            )
        },
        
        "NameError": {
            "simple_explanation": (
                "Aapne ek variable ya function name use karne ki koshish ki jo abhi tak exist nahi karta. "
                "Python ko samajh nahi aa raha aap kya bol rahe ho. "
                "Yeh aisa hai jaise kisi ko bulana jo kamre mein nahi hai 🤷"
            ),
            "fix_suggestion": (
                "Spelling check karein, pakka karein ki aapne pehle variable define kiya hai, "
                "ya module import karein jisme yeh hai"
            )
        },
        
        "ZeroDivisionError": {
            "simple_explanation": (
                "Aapne ek number ko zero se divide karne ki koshish ki, jo math mein impossible hai. "
                "Zero se division universe ke math rules ko tod deta hai. "
                "Python infinity calculate nahi kar sakta ➗"
            ),
            "fix_suggestion": (
                "Divide karne se pehle check karein ki divisor zero toh nahi hai, "
                "ya zero values handle karne ke liye condition add karein"
            )
        },
        
        "FileNotFoundError": {
            "simple_explanation": (
                "Python ko woh file nahi mili jise aap open ya use karne ki koshish kar rahe ho. "
                "File aapke diye gaye path par exist nahi karti. "
                "Yeh aisa hai jaise ek book dhundhna jo shelf par nahi hai 📁"
            ),
            "fix_suggestion": (
                "File path ki spelling check karein, verify karein ki file exist karti hai, "
                "ya file create karein agar honi chahiye"
            )
        },
        
        "TypeError": {
            "simple_explanation": (
                "Aapne galat type ke data ke saath kuch karne ki koshish ki. "
                "Jaise ek number ko ek word ke saath add karna - yeh mix nahi hote. "
                "Python ko compatible types chahiye saath kaam karne ke liye 🔢➕📝"
            ),
            "fix_suggestion": (
                "Data ko sahi type mein convert karein (e.g., int(), str(), list()), "
                "ya check karein ki aap sahi operation use kar rahe ho"
            )
        },
        
        "ValueError": {
            "simple_explanation": (
                "Data type toh sahi hai par actual value sense nahi bana rahi. "
                "Jaise 'hello' word ko number mein convert karne ki koshish karna. "
                "Format ya content galat hai 🎯"
            ),
            "fix_suggestion": (
                "Check karein ki input value valid hai jo aap karne ki koshish kar rahe ho. "
                "Bad values handle karne ke liye validation ya try/except add karein"
            )
        },
        
        "KeyError": {
            "simple_explanation": (
                "Aapne ek dictionary se ek key use karke value lene ki koshish ki jo exist nahi karti. "
                "Yeh aisa hai jaise dictionary mein ek word dhundhna jo hai hi nahi. "
                "Aapne jo key maangi woh missing hai 🔑"
            ),
            "fix_suggestion": (
                "dict[key] ke bajaye dict.get(key, default) use karein, "
                "ya 'key in dict' se pehle check karein ki key exist karti hai"
            )
        },
        
        "IndexError": {
            "simple_explanation": (
                "Aapne list mein ek position access karne ki koshish ki jo exist nahi karta. "
                "Jaise 10th item lena jab sirf 5 items hain. "
                "Index range se bahar hai 📊"
            ),
            "fix_suggestion": (
                "Access karne se pehle len() se length check karein, "
                "ya end se count karne ke liye negative indices use karein"
            )
        },
        
        "ImportError": {
            "simple_explanation": (
                "Python aapke request kiye gaye module ko import nahi kar saka. "
                "Package shayad installed nahi hai ya naam galat hai. "
                "Import fail ho gaya 📦"
            ),
            "fix_suggestion": (
                "Package ko pip install se install karein, spelling check karein, "
                "ya verify karein ki module aapke environment mein exist karta hai"
            )
        },
        
        "AttributeError": {
            "simple_explanation": (
                "Aapne ek property ya method access karne ki koshish ki jo object par exist nahi karta. "
                "Jis cheez ke saath aap kaam kar rahe ho uske paas woh feature nahi hai. "
                "Yeh aisa hai jaise car ka door kholna jo hai hi nahi 🚗"
            ),
            "fix_suggestion": (
                "dir(object) use karke sahi attribute name check karein, "
                "ya verify karein ki object type wahi hai jo aap expect kar rahe ho"
            )
        },
    }
}


def get_translated_template(error_type: str, language_code: str) -> Optional[Dict[str, str]]:
    """
    Get translated template for an error type.
    
    Args:
        error_type: Exception class name
        language_code: Target language code
        
    Returns:
        Dictionary with translated explanation and fix, or None
    """
    if language_code in TRANSLATION_TEMPLATES:
        return TRANSLATION_TEMPLATES[language_code].get(error_type)
    return None


# Export public API
__all__ = [
    'set_language',
    'get_language',
    'translate_explanation',
    'get_supported_languages',
    'is_language_supported',
    'get_translated_template',
    'SUPPORTED_LANGUAGES',
]
