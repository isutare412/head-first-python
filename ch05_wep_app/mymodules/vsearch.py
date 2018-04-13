#!/usr/bin/env python3


def search_for_letters(phrase: str, letters: str='aeiou') -> set:
    return set(letters).intersection(set(phrase))
