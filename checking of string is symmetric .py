#!/usr/bin/env python
# coding: utf-8

# In[2]:


def symmetric_chk(data):
    n= len(data)
    start=0
    last=n
    flag=0
   
    if n%2:
        middle=n//2+1
    else:
        middle=n//2
    while(start<middle and middle<last):
        if(data[start]==data[middle]):
            start+=1
            middle+=1
        else:
            flag=1
            break
    if(flag==0):
        print('string is symmetric')
    else:
        print('string is asymmetric')
symmetric_chk("abcabc")


# In[ ]:




