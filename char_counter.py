#!/usr/bin/env python
#-*- coding: utf-8 -*-

try:
    from argparse import ArgumentParser
    from codecs import open as open_coding
    from string import ascii_lowercase as ALPHABET
except ImportError as error:
    print(str(error))
    exit(1)


def supplement_alphabet(diacritics_letters, basic_alphabet = ALPHABET):
    """Supplement the latin alphabet by diacritics letters of a given language

    Parameters
    ---------
    diacritics_letters : str
        an unicode string containing
        additional lowercase letters
    basic_alphabet : str
        must contain lowercase letters
        the default value is "abc...xyz"

    Return
    ------
    A string with all letters.

    Examples
    --------
    >>> from char_counter import supplement_alphabet
    >>> german_alphabet = supplement_alphabet(u"äöüß")
    >>> for ga in german_alphabet:
    ...     print ga
    ...
    a
    b
    ...
    ü
    ß
    """
    return basic_alphabet + diacritics_letters

def count_letters(filename, alphabet = ALPHABET):
#   description
    letters_dict = init_letters_dictionary(alphabet)

    try:
        with open_coding(filename, "r", "utf-8") as input_file:
            for text_line in input_file:
                for letter in text_line.lower():
                    if letter in alphabet:
                        letters_dict[letter] += 1
    except IOError:
        print("Cannot open '%s' file." % (filename,))
        return

    return letters_dict

def init_letters_dictionary(alphabet):
    """Initialize a dictionary for a given alphabet

    Parameters
    ----------
    alphabet : str
        a set of letters

    Return
    ------
    A dictionary with letters as
    keys and zeros as values.

    Examples
    --------
    >>> from char_counter import init_letters_dictionary
    >>> letters_dict = init_letters_dictionary('abcdef')
    >>> letters_dict
    >>> {'a': 0, 'c': 0, 'b': 0, 'e': 0, 'd': 0, 'f': 0}
    """
#   body of function

#def sort_polish_alphabet(alphabet):
#    ...
#    return alphabet


if __name__ == "__main__":
    argparser = ArgumentParser(prog='char_counter.py', description='Program calculates statistical \
    values of used characters for data from a text file', epilog='Copyright (c) 2017 Jakub21 & pbrus | GitHub')
    argparser.add_argument('filename', help='name of a file containing a text to parse')
    args = argparser.parse_args()

    polish_alphabet = supplement_alphabet(u"ąęćłńóśźż")
    count_letters(args.filename, polish_alphabet)

