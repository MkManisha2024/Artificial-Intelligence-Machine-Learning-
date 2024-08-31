#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#prepatory classes
#1. Variables
A storage container which holds some data


# In[ ]:





# In[2]:


x=30 #shortcut shift+enter


# In[3]:


x #asking Python the value of x


# In[5]:


y=40


# In[6]:


y


# In[7]:


x
y 


# In[ ]:


#above only last value is considered


# In[8]:


print(x)
print(y)


# In[9]:


X


# In[ ]:


#python is a case sensitive language


# In[10]:


x=1
y=2
z=3


# In[11]:


print(x)
print(y)
print(z)


# In[12]:


print(x,y,z)


# 2. Data types

# In[ ]:


# 1,2,3,4,5 --> int
# 3.4, 5.6 ---> float
# 'Hello World', "Name " ---> str
# True or False ---> bool


# In[13]:


x=70


# In[14]:


type(x)


# In[15]:


c = False


# In[16]:


type(c)


# In[17]:


d=true


# In[19]:


d=True


# In[20]:


type(d)


# 1. Variables in python are case sensitive.
# 2. A variable name cannot start with a number.
# 3. A variable name can consist of alphanumeric characters.
# 4. A variable name can start with a character or an underscore.
# 5. No keywords can be a variable name.

# In[21]:


3ac=6


# In[22]:


a3c=7


# In[23]:


_2ab=4


# In[24]:


if=6 #if is a keyword


# In[25]:


IF = 5 #this will work as it is in capital


# In[ ]:


#user input


# In[28]:


age = input()


# In[29]:


age #by default input is only going to be string


# In[30]:


type(age)


# In[ ]:


age = int(input())


# In[32]:


type(age)


# In[33]:


age = int(input())


# In[34]:


pi = float(input())


# In[ ]:


age =int(input('Enter your age:'))


# In[ ]:


#can add integer + integer or string + string


# In[ ]:


#Typecasting
d = str(d)


# In[ ]:


x="Hello"


# In[ ]:


d="7"


# In[ ]:


type(d)


# Operators

# In[ ]:


#tuple,list etc. later


# In[2]:


#arithmetic operators
a=10
b=20


# In[3]:


a+b


# In[4]:


b-a


# In[3]:


a = 10
b=20

if a==b :
    print ('a and b are equal')
else:
    print ('Not equal')


# In[5]:


b/a #on division gets float values


# In[ ]:


a**b #exponential a to the power of b 10 raise to 20


# In[6]:


4**2


# In[7]:


#floor division
b//a #removes point values


# In[8]:


15//2


# In[9]:


15/2


# In[10]:


10%3 #modulus which is the remainder


# In[11]:


8%2


# Assignment operator

# In[18]:


x=50


# In[19]:


x+=5 #x=x+5


# In[20]:


x


# In[21]:


x-=5 #x-5


# In[22]:


x


# In[23]:


x*=5


# In[24]:


x


# In[25]:


x/=5


# In[26]:


x


# In[27]:


#comparison operators


# In[28]:


x=20
y=10


# In[29]:


x>y


# In[30]:


x>=y


# In[31]:


x<=y


# In[32]:


x==y #checking the equality


# In[33]:


x!=y


# In[34]:


#Logical operator


# In[35]:


x=True
y=False


# In[ ]:


#or and condition


# In[36]:


x or y


# In[37]:


y or y


# In[38]:


x and y


# In[39]:


not x


# In[40]:


not y


# In[ ]:


#Identity operator (it's like comparison)


# In[41]:


x=20
y=10


# In[42]:


x is y


# In[43]:


x is not y


# In[ ]:


#membership operator (only in or not in)


# In[45]:


x=[0,1,3,4,5,6]


# In[46]:


3 in x


# In[47]:


7 in x


# In[48]:


3 not in x


# In[49]:


a=[1,2,3]
b=[1,2,3]


# In[50]:


a is b #different objects


# In[51]:


a == b #checking numeric value


# **Conditional statements** if, else (Day 2) - Preparatory Classes

# In[ ]:


#types
#--> simple if
#--> if else
#--> if elif else
#--> nested if else


# In[52]:


a=10
b=20

if a==b:
    print('a and b are Equal')
    
else:
    print('not equal')


# In[53]:


a=10
b=10

if a==b:
    print('a and b are Equal')
    
else:
    print('not equal')


# In[64]:


a=int(input('Enter the number :'))
b=int(input('Enter the number :'))

if a==b:
    print('a and b are Equal')
    
else:
    print('not equal')


# In[4]:


#Q out of these 3 which number is greater ?

a=int(input('Enter the number :'))
b=int(input('Enter the number :'))
c=int(input('Enter the number :'))

if a>b and a>c:
    print('a is greater')
elif b>a and b>c:
    print('b is greater') 
elif a==b and a==c:
    print('All are equal')
elif a==b and a>c:
    print('a and b are greater')
elif b==c and a<c:
    print('b and c are greater')
elif a==c and a>b:
    print('a and c are greater')   
else:
    print('c is greater')    


# In[5]:


#formatted string
a=int(input('Enter the number :'))
b=int(input('Enter the number :'))
c=int(input('Enter the number :'))

if a>b and a>c:
    print(f'{a} is greater')
elif b>a and b>c:
    print(f'{b} is greater') 
elif a==b and a==c:
    print('All are equal')
elif a==b and a>c:
    print(f'{a} and {b} are greater')
elif b==c and a<c:
    print(f'{b}and {c} are greater')
elif a==c and a>b:
    print(f'{a} and{c} are greater')   
else:
    print(f'{c} is greater') 


# In[ ]:


#tillControlflowandfunctions_1hour


# In[ ]:





# In[ ]:





# In[56]:


a=5
if a>0:
    print('Positive')
    
else:
    print('Not positive')


# In[60]:


a=int(input('Enter the number :'))
if a>0:
    print('Positive')
    
else:
    print('Not positive')


# In[ ]:


#when entering 0 first condition since 0 is not greater than 0


# In[61]:


#elif mix of else and if always added before else and if


# In[63]:


a=int(input('Enter the number :'))
if a>0:
    print('Positive')
elif a==0:
    print('Zero')   
else:
    print('Not positive')


# In[54]:


a = 10

if a >0:
    print('Positive')
else:
    print ('Negative')  


# In[8]:


#give user input & restrict it to integer
a = int(input('Enter the number :'))
if a >0:
    print('Positive')
else:
    print ('Negative') 


# In[9]:


#give user input & restrict it to integer
a = int(input('Enter the number :'))
if a >0:
    print('Positive')
elif a==0:
    print('Zero')
else:
    print ('Negative') 


# In[ ]:


a = int(input('Enter the number : '))
b = int(input('Enter the number : '))
if a ==b:
    print ('a and b are equal')
else:
    print ('Not equal')


# In[ ]:


a = int(input('Enter 1st number : '))
b = int(input('Enter 2nd number : '))
c = int(input('Enter 3rd number : '))
if a>b and a>c:
    print ('a is greater')
elif b>a and b>c:
    print ('b is greater')
elif a==b and a==c: 
    print ('all are equal')
elif a==b and a>c:  
    print ('a and b are greater')
elif b==c and a<c: 
    print ('b and c are greater')

else print ('c is greater')


# In[ ]:


a = int(input('Enter 1st number : '))
if a/2 

