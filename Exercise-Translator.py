"""
Translate from a file
"""

from translate import Translator
translator = Translator(to_lang="ja")
# Sets the translated language
# See https://en.wikipedia.org/wiki/ISO_639-1 for language choices.

try:
    with open("Translate.txt", mode='r') as my_file:
        text = my_file.read()  # Reads the txt file
        translated_file = translator.translate(text)  # Translates the the "text" file.
        print(translated_file)  # Prints the translated text file
except FileNotFoundError as err:
    print('Check your file-path, idiot')

