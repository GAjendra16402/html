#!/usr/bin/env python
# coding: utf-8

# In[1]:


def contains_all_vowels(input_string):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        if vowel not in input_string:
            return False
    return True

# Example usage:
input_str = "Hello, World!"
result = contains_all_vowels(input_str)

if result:
    print(f"The string '{input_str}' contains all the vowels.")
else:
    print(f"The string '{input_str}' does not contain all the vowels.")


# In[ ]:




