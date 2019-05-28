#!/usr/bin/env python
# coding: utf-8

# In[2]:


print('hello world')


# In[2]:


x = 5
y = 4
x+y


# In[5]:


'creating string with single quotes'


# In[6]:


"creating string with double quotes"


# In[4]:


"we have lot's of other quotes,let's wrap in double quotes"


# In[7]:


x = 'string'
print(x)


# In[51]:


a = 3
b = 5
print(a+b)


# In[53]:


a1 = 'hello'
b1 = 'world'
helloworld = a1+ " "+b1
print(helloworld)


# In[55]:


print(a+b+a1)


# In[11]:


name = 'jeff'
age = 36


# In[12]:


print('my name is {},and my age is {}'.format(name,age))


# In[13]:


print('my name is {one},and my age is {two}'.format(one=name,two=age))


# In[14]:


print('my name is {one},and my age is {two}'.format(two=age,one=name))


# In[15]:


print('my name is {one} and my age is {two},{one} again {two},{two}'.format(two=age,one=name))


# In[18]:


x[0]


# In[19]:


x[-1]


# In[21]:


x[0:4]


# In[22]:


s = 'Hi I am jeff'


# In[23]:


print(s.lower())


# In[24]:


print(s.split())


# In[25]:


tweet = 'go flames go! #hockey'


# In[27]:


print(tweet.split('#'))


# In[28]:


print(tweet.split('#')[1])


# # LIST

# In[4]:


my_list = ['a','b','c']
print(my_list)


# In[5]:


my_list.append('d')


# In[36]:


my_list.pop()


# pop - removed the last item from the list

# In[ ]:


my_list


# In[7]:


a = [123,'xyz','luci']
b = [220, 'john']
a.extend(b)
print("extended list: " , a)


# In[9]:


a.index('xyz')


# In[13]:


b.insert(2,234)
print(b)


# In[16]:


list = [12,234,'a','b']
list.remove(234)
print(list)


# In[19]:


s = [23,56,43,78,45,32]
s.sort()
print(s)


# In[70]:


nest = [1,2,3,[4,5,6]]
nest[3]


# In[49]:


nest[3][1]


# In[73]:


nest[1]=3
nest


# In[50]:


nest = [1,2,3,[4,5,6],['a','b']]
nest


# # DICTIONARY

# In[61]:


d1 = {'k1':'v1','k2':'v2','k3':'v3'}
d1


# In[62]:


d1['k1']


# In[75]:


d1['k1'] = 'k4'
d1


# In[63]:


d2 = {'k1': [1,2,3],'k2':['a','b']}
d2


# In[64]:


d2['k1']


# In[65]:


d2['k2'][1]


# In[66]:


d1.values()


# In[25]:


dict = {'name': 'mark', 'age': 34, 'class': 'first'}
print(dict['name'])


# In[ ]:


del dict['name']  ##remove entry with key name
dict.clear()  ##removes all entry in dict
del dict  ##delete entire dictionary


# In[27]:


t = {'state' : 'Delhi', 'Age': 45, 'state' : 'Haryana'}
print("State :" , t['state'])  ##More than one entry per key is not allowed,which means no duplicate key is allowed.


# In[30]:


dict1 = {'name': 'mark', 'age': 34, 'class': 'first'}
dict2 = {'name': 'john', 'age': 34, 'class': 'second'}
dict1.update(dict2)
print(dict1)


# # TUPLES

# In[67]:


t = (1,2,3)
print(t)


# In[68]:


t[0]


# In[20]:


tup1 = (12,34,56)
tup2 = ('abc','xyz')
tup3 = tup1 + tup2
print(tup3)


# In[23]:


tup = ('physics' , 'chemistry' ,1997,2000)
print(tup)


# In[22]:


del tup


# # SETS

# In[76]:


{1,2,3,4,5,6}


# In[77]:


{1,2,2,3,3,3,3,4,5,5}


# In[79]:


s = {1,2,3}
s.add(4)
s


# In[ ]:





# In[ ]:




