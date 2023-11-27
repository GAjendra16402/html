#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def least_frequent_character(input_string):
    char_frequency = {}
    
    # Count the frequency of each character
    for char in input_string:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    # Find the character with the minimum frequency
    least_frequent_char = min(char_frequency, key=char_frequency.get)

    return least_frequent_char

# Example usage:
input_str = "hello world"
result = least_frequent_character(input_str)

print(f"The max frequent character in the string '{input_str}' is: {result}")

