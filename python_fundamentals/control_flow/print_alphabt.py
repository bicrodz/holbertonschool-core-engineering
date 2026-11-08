#!/usr/bin/env python3
letters = ""
for code in range(97, 123):
    char = chr(code)
    if char != "e" and char != "q":
        letters += char
print(letters)
