#!/usr/bin/env python
# coding: utf-8

# In[1]:


def palandrom_check(data):
    
    mid = (len(data)-1)//2
    start = 0
    last = len(data)-1
    flag = 0
    
    while(start<=mid):
        
        if (data[start]== data[last]):
            start+=1
            last-=1
        else:
            flag= 1
            break;
        if flag==0:
            print('string is palindrom')
        else:
            print('string is not palindrome')
            
palandrom_check("saras")


# In[ ]:




