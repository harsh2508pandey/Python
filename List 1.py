#!/usr/bin/env python
# coding: utf-8

# In[2]:


i=0
while i>20:
    print(i*'X')
    i=i+1
while i<0:
    print(i*'X')
    i=i-1


# In[5]:


n=int(input('Enter number'))
i=1
y=0
while i<=n:
    y=y+i
    print(y)
    i=i+1
print('Final result is',y)


# In[2]:


def numpat(n):
    num=1
    for i in range(0,n):
        num=1
        for j in range(0,i+1):
            print(num,end=" ")
            num=num+1
        print("\r")


# In[ ]:


n=int(input("Number of rows= "))

i=0
for i in range (1,n+1):
    for j in range(i):
        print(i,end=" ")
    
    print()
    


# In[ ]:





# In[1]:


n=int(input("Number of rows= "))

i=0
for i in range(1,n+1):
    for j in range(j,end)


# In[14]:


a="harsh"
b=['www','google','com']
print(a.join(b))
print(a.isupper())
print(a.islower())
print(a.isalpha())
print(a.isdigit())
print(a.isalnum())


# In[ ]:


a=""
b=int(input())
c=int(input())
d=int(input())
e=[b,c,d]
print(a.join(e))


# In[2]:


print("hello world!\ntoday is friday")


# In[5]:


a='Hello World\nToday is friday'
print(a)
print(repr(a))


# In[1]:





# In[2]:


result=" "
str="List"
for i in str:
    result=result+(i*2)
print(result)
  


# In[8]:


a="Python"
print(a[:3])


# In[14]:


a=['LOvely','harsh']
print(a[::5])


# In[15]:


l=['Krishna','harsh','nitin','manish']
print(type(1))
a[:2]


# In[2]:


x=[1,2,3,4,5,6,7,8,9,10]
print(list(x[3:8]))
print(list(x[1:9:2]))


# In[8]:


x=[2,4,6]
print(x*4)
print(list(x[1:9:2])*4)


# In[15]:


x=[1,2,3,4,5,6,7,8,9,10]
a=x[1:6:2]*4
print(a)
print(x==a)
x[3]=100
print(x,a)
x[4:]=[]
print(x,a)


# In[3]:


a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
a[5:9]=[]
del a[5:9]
a.remove(5:9)


# In[4]:


a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
b=a.pop(4)
print(b)


# In[6]:


a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
b=list(enumerate(a))
print(b)


# In[8]:


a=[789654]
b=list(enumerate(a))
print(b)


# In[7]:


x='alresdy'
list(x)


# In[8]:


a=[1,2,3,4,6,7,8,9,10]
a.insert(3,50)
print(a)


# In[6]:


a=[1,2,3,4,5,6,7,8,9,10]
a.remove(5)
print(a)


# In[10]:


a=[1,2,3,4,6,7,8,9,10]
a.count(3)


# In[12]:


a=[1,2,3,4,6,7,8,9,10]
a.sort(key=None, reverse=True)
print(a)
a.sort(key=None, reverse=False)
print(a)


# In[16]:


a=[1,2,3,4,6,7,8,9,10]
b=a.copy()
print(b)
print(a is b)


# In[27]:


i=ord('A')
j=ord('a')
alpha=[ ]
for k in range(26):
    alpha.append(chr(i))
    alpha.append(chr(j))
    i=i+1
    j=j+1
print(alpha)


# In[28]:


a=[1,2,3,4,6,7,8,9,10]
a=tuple(a)
print(a)


# In[36]:


t1=(1,2,3,[4,5],6,7,8,9)
t1[3][0]=42
print(t1)

ti=list(t1)
print(ti)
a=[1,2,3,4,5,6,7,8,9,10]
b=tuple(a)
print(b)
print(type(ti))
print(type(b))


# In[3]:


n=int(input())
x=['even' if(n%2==0) else 'odd']
print(x)


# s="Harsh"
# x=[i for i in s]
# print(x)

# In[4]:


s="harsh"
x=[i for i in s]
print(x)


# In[5]:


dict1={i:i**2 for i in range(1,21) if (i%2==0)}
print(dict1)


# In[6]:


m=int(input())
n=int(input())
print("Enter elements:")
mat=[[int(input()) for x in range(n)] for y in range(m)]
print("Sparse matrix is:")
for i in range(m):
    for j in range(n):
        print(mat[i][j],end=" ")
    print()


# In[3]:


class greatestnumber():
    def number(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        return max(a,b,c)
    a,b,c=int(input()),int(input()),int(input())
    print(greatestnumber.number())


# In[ ]:




