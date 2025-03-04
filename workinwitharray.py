#!/usr/bin/env python
# coding: utf-8

# In[2]:


#a create a 1d array
#working with arrays 
import numpy as np
nd=np.random.randint(1,100,size=10)
print("ID data")
print("Content of nd",nd)
print("type of nd",type(nd))
print("Dimension of nd",nd.ndim)
print("dtype of nd",nd.dtype)
print("shape of nd",nd.shape)
print("size of nd",nd.size)


# In[3]:


#b Create a boolean array
lst=[0,1,2,3,0,6,7,8,0]
ndo=np.array(lst,dtype=bool)
print(ndo)
ndo=ndo.reshape(3,3)
print(ndo)
print("Dimension of ndo",ndo.ndim)
print("shape of ndo",ndo.shape)
print("Size of ndo",ndo.size)
print("dtype of ndo",ndo.dtype)


# In[4]:


#c extract items that staisfy a given condition from 1d arary
import numpy as np
ndo=np.random.randint(1,10,size=10)
print(ndo)
ind=np.where(ndo>5)
print(ind)
print(ndo[ind])


# In[5]:


#d. Replace items that satisfy a condition with another value in numpy
tstate=[10,20,15,18,25,70,56]
andhs=[25,19,30,45,67,89,90]
t=np.array(tstate)
a=np.array(andhs)
poll=np.where(t>18,t,a)
print(poll)


# In[6]:


#e Replace items that satisfy a condition without affecting the original 
sal=np.array([1000,2000,3000,4000,5000,6000])
comm=np.array([10,20,30,None,None,None])
#netsal=sal+comm
newcomm=np.where(comm==None,0,comm)
print(newcomm)
netsal=sal+newcomm
print("Netsalary")
print(netsal)


# In[8]:


#f Reshape an array
ndo=np.random.randint(1,50,size=(3,3))
print(ndo)
ndo1=ndo.reshape(9,)
print(ndo1)


# In[9]:


#g Extract all numbers btwn a given range from a numpy array
ndo=np.random.randint(5,10,size=8)
print(ndo)
out=np.extract(ndo>5,ndo)
print(out)


# In[26]:


#binary file-save
import numpy as np
lst=[10,20,30,40,50,60]
i=np.array
res=np.save("out",i)
print("File is saved successfully.....")


# In[28]:


#binary file-load
result=np.load("out.npy")
print("File is loaded Successfully...")
print(result)


# In[30]:


lst=[100,200,300,400,500]
a=np.array(lst)
result=np.savetxt("outt.txt",a)
print("My text File is saved successfully")
print(result)


# In[31]:


r=np.loadtxt("outt.txt")
print("My text file is loaded successfully")
print(r)


# In[32]:


lst=[15,25,50,75.100]
c=np.array(lst)
r=np.savetxt("outc.csv",c,delimiter=',')
print("csv files saved successfully")


# In[ ]:




