#!/usr/bin/env python
# coding: utf-8

# In[1]:


def print_pattern(rows):
    for i in range(rows):
        print("$" * (rows - i - 1) + "*" * (i + 1))

# Example usage with 5 rows
print_pattern(5)


# In[7]:


def print_pattern():
    for i in range(5):
        for j in range(7):
            if i == 0 or i == j or j == 6:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Call the function to print the pattern
print_pattern()


# In[ ]:




