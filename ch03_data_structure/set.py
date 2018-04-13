#!/usr/bin/env python3

vowels = set('aeiou')
word = 'hello'

print(vowels.union(set(word)))
print(vowels.difference(set(word)))
print(vowels.intersection(set(word)))
