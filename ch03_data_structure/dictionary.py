#!/usr/bin/env python3

input_str = input("Provide a word to search for vowelds: ")

vowel_count = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0,
        }

for ch in input_str:
    if ch in vowel_count.keys():
        vowel_count[ch] += 1

for k, v in sorted(vowel_count.items()):
    print('%s was found %d time(s).' % (k, v))
