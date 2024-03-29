#!/usr/bin/env python
# coding: utf-8

# ### 1. Develop a text-to-speech project using Python. Your program should take input text and convert it into speech output. Ensure that the program is able to handle various text inputs and produce clear and understandable speech output.

# In[1]:


pip install pyttsx3


# In[2]:


import pyttsx3


# In[13]:


def Text_to_speech(n):
    engine = pyttsx3.init()
    engine.say(n)
    engine.runAndWait()


# In[17]:


Text_to_speech("you are amazing")


# In[19]:


Text_to_speech("you are very good at playing cricket")


# In[20]:


Text_to_speech("today is a plesant day")

