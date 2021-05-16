#!/usr/bin/env python
# coding: utf-8

# In[9]:


import nltk


# In[11]:


nltk.download()


# In[12]:


from nltk.book import *


# # LISTS

# #### How do we represent text in Python?

# In[1]:


sent1=['Hello','Mr','.','Bell','!']
sent1


# In[2]:


len(sent1)


# In[4]:


def lexical_diversity(text):
    return len(text)/len(set(text))
lexical_diversity(sent1)


# #### Hence, all the list operations are applicable. For example,

# In[5]:


sent2=['My','name','is','Mukut','.']
sent1+sent2


# In[6]:


sent2.append(':)')


# In[7]:


sent2


# #### Indexing Lists

# In[13]:


text4[173]


# In[14]:


text4.index('awaken')


# #### Slicing

# In[15]:


text5[16715:16735]


# In[18]:


text4[:3] #goes till index 3


# In[19]:


text2[141525:]


# #### Variable

# In[20]:


my_sent = ['Bravely', 'bold', 'Sir', 'Robin', ',', 'rode',
'forth', 'from', 'Camelot', '.']


# In[21]:


noun_phrase=my_sent[1:4]


# In[22]:


noun_phrase


# In[25]:


wOrDs = sorted(noun_phrase)
#apitalized words appear before 
#lowercase words in sorted lists
wOrDs


# In[27]:


vocab=set(text1)
vocab_size=len(vocab)
vocab_size


# # Strings

# In[34]:


name = 'Monty'
name[0]


# In[35]:


name[:3]


# In[36]:


name*2


# In[37]:


name+'!'


# In[38]:


''.join(['Monty','Python'])


# In[39]:


'Monty Python'.split() 


# # Simple Statistics

# In[41]:


saying = ['After', 'all', 'is', 'said', 'and', 'done','more', 'is', 'said', 'than', 'done']
tokens=set(saying)
tokens=sorted(tokens)


# In[42]:


tokens[-2:]


# #### To find 50 most frequent words of Moby Dick.  

# In[43]:


fdist1= FreqDist(text1)
fdist1


# In[51]:


vocabulary1 = fdist1.keys()


# In[53]:


vocabulary1


# In[55]:


fdist1['whale']


# In[56]:


fdist1.plot(50, cumulative=True)


# #### Let's check for hapaxes, i.e., the words that occur once only.

# In[58]:


hap=fdist1.hapaxes()


# In[62]:


hap


# ## Difference between word type and hapaxes.

# ### To find the words from the vocabulary of the text that are more than 15 characters long.

# In[64]:


V= set(text1)
long_words=[w for w in V if len(w) > 15]
sorted(long_words)


# ### All words from the chat corpus that are longer than seven characters, that occur more than seven times.

# In[67]:


fdist5= FreqDist(text5)


# In[69]:


sorted([w for w in set(text5) if len(w)>7 and fdist5[w]>7])


# # Collocations and Bigrams

# ### Collocations: sequence of word occuring together usually often. Example: "Red wine".
# 
# ##### To handle collocations, extraction from word pairs ,i.e,
# # BIGRAMS
# #### is used.

# In[74]:


from nltk import bigrams


# In[77]:


list(bigrams(['more','is','said','than','done']))


# In[72]:


text4.collocations()


# In[78]:


list(bigrams(text4))


# ### Code for the distribution of word lengths in a text, by creating a FreqDist out of a long list of numbers, where each number is the length of the corresponding word in the text.

# In[80]:


[len(w) for w in text1]


# In[83]:


fdist=FreqDist([len(w)for w in text1])
fdist


# In[84]:


fdist.keys()


# In[85]:


fdist.items()


# In[86]:


fdist.max()


# In[87]:


fdist[3]


# In[88]:


fdist.freq(3)

