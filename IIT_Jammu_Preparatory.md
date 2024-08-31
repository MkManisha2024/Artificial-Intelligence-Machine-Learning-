```python
#prepatory classes
#1. Variables
A storage container which holds some data
```


```python

```


```python
x=30 #shortcut shift+enter
```


```python
x #asking Python the value of x
```




    30




```python
y=40
```


```python
y
```




    40




```python
x
y 
```




    40




```python
#above only last value is considered
```


```python
print(x)
print(y)
```

    30
    40
    


```python
X
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-9-b5fec669aca1> in <module>
    ----> 1 X
    

    NameError: name 'X' is not defined



```python
#python is a case sensitive language
```


```python
x=1
y=2
z=3
```


```python
print(x)
print(y)
print(z)
```

    1
    2
    3
    


```python
print(x,y,z)
```

    1 2 3
    

2. Data types


```python
# 1,2,3,4,5 --> int
# 3.4, 5.6 ---> float
# 'Hello World', "Name " ---> str
# True or False ---> bool
```


```python
x=70
```


```python
type(x)
```




    int




```python
c = False
```


```python
type(c)
```




    bool




```python
d=true
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-17-8500cedbf841> in <module>
    ----> 1 d=true
    

    NameError: name 'true' is not defined



```python
d=True
```


```python
type(d)
```




    bool



1. Variables in python are case sensitive.
2. A variable name cannot start with a number.
3. A variable name can consist of alphanumeric characters.
4. A variable name can start with a character or an underscore.
5. No keywords can be a variable name.


```python
3ac=6
```


      File "<ipython-input-21-afc0a13c6468>", line 1
        3ac=6
          ^
    SyntaxError: invalid syntax
    



```python
a3c=7
```


```python
_2ab=4
```


```python
if=6 #if is a keyword
```


      File "<ipython-input-24-c51fa6c597f4>", line 1
        if=6 #if is a keyword
          ^
    SyntaxError: invalid syntax
    



```python
IF = 5 #this will work as it is in capital
```


```python
#user input
```


```python
age = input()
```

    77
    


```python
age #by default input is only going to be string
```




    '77'




```python
type(age)
```




    str




```python
age = int(input())
```


```python
type(age)
```




    int




```python
age = int(input())
```

    34.7
    


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-33-fd1c10bad766> in <module>
    ----> 1 age = int(input())
    

    ValueError: invalid literal for int() with base 10: '34.7'



```python
pi = float(input())
```

    43.5
    


```python
age =int(input('Enter your age:'))
```


```python
#can add integer + integer or string + string
```


```python
#Typecasting
d = str(d)
```


```python
x="Hello"
```


```python
d="7"
```


```python
type(d)
```

Operators


```python
#tuple,list etc. later
```


```python
#arithmetic operators
a=10
b=20
```


```python
a+b
```




    30




```python
b-a
```




    10




```python
a = 10
b=20

if a==b :
    print ('a and b are equal')
else:
    print ('Not equal')
```

    Not equal
    


```python
b/a #on division gets float values
```




    2.0




```python
a**b #exponential a to the power of b 10 raise to 20
```


```python
4**2
```




    16




```python
#floor division
b//a #removes point values
```




    2




```python
15//2
```




    7




```python
15/2
```




    7.5




```python
10%3 #modulus which is the remainder
```




    1




```python
8%2
```




    0



Assignment operator


```python
x=50
```


```python
x+=5 #x=x+5
```


```python
x
```




    55




```python
x-=5 #x-5
```


```python
x
```




    50




```python
x*=5
```


```python
x
```




    250




```python
x/=5
```


```python
x
```




    50.0




```python
#comparison operators
```


```python
x=20
y=10
```


```python
x>y
```




    True




```python
x>=y
```




    True




```python
x<=y
```




    False




```python
x==y #checking the equality
```




    False




```python
x!=y
```




    True




```python
#Logical operator
```


```python
x=True
y=False
```


```python
#or and condition
```


```python
x or y
```




    True




```python
y or y
```




    False




```python
x and y
```




    False




```python
not x
```




    False




```python
not y
```




    True




```python
#Identity operator (it's like comparison)
```


```python
x=20
y=10
```


```python
x is y
```




    False




```python
x is not y
```




    True




```python
#membership operator (only in or not in)
```


```python
x=[0,1,3,4,5,6]
```


```python
3 in x
```




    True




```python
7 in x
```




    False




```python
3 not in x
```




    False




```python
a=[1,2,3]
b=[1,2,3]
```


```python
a is b #different objects
```




    False




```python
a == b #checking numeric value
```




    True



**Conditional statements** if, else (Day 2) - Preparatory Classes


```python
#types
#--> simple if
#--> if else
#--> if elif else
#--> nested if else
```


```python
a=10
b=20

if a==b:
    print('a and b are Equal')
    
else:
    print('not equal')
```

    not equal
    


```python
a=10
b=10

if a==b:
    print('a and b are Equal')
    
else:
    print('not equal')
```

    a and b are Equal
    


```python
a=int(input('Enter the number :'))
b=int(input('Enter the number :'))

if a==b:
    print('a and b are Equal')
    
else:
    print('not equal')
```

    Enter the number :10
    Enter the number :12
    not equal
    


```python
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
```

    Enter the number :3
    Enter the number :4
    Enter the number :3
    b is greater
    


```python
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
```

    Enter the number :10
    Enter the number :5
    Enter the number :200
    200 is greater
    


```python
#tillControlflowandfunctions_1hour
```


```python

```


```python

```


```python
a=5
if a>0:
    print('Positive')
    
else:
    print('Not positive')
```

    Positive
    


```python
a=int(input('Enter the number :'))
if a>0:
    print('Positive')
    
else:
    print('Not positive')
```

    Enter the number :0
    Not positive
    


```python
#when entering 0 first condition since 0 is not greater than 0
```


```python
#elif mix of else and if always added before else and if
```


```python
a=int(input('Enter the number :'))
if a>0:
    print('Positive')
elif a==0:
    print('Zero')   
else:
    print('Not positive')
```

    Enter the number :0
    Zero
    


```python
a = 10

if a >0:
    print('Positive')
else:
    print ('Negative')  
```

    Positive
    


```python
#give user input & restrict it to integer
a = int(input('Enter the number :'))
if a >0:
    print('Positive')
else:
    print ('Negative') 

```

    Enter the number :10
    Positive
    


```python
#give user input & restrict it to integer
a = int(input('Enter the number :'))
if a >0:
    print('Positive')
elif a==0:
    print('Zero')
else:
    print ('Negative') 

```

    Enter the number :0
    Zero
    


```python
a = int(input('Enter the number : '))
b = int(input('Enter the number : '))
if a ==b:
    print ('a and b are equal')
else:
    print ('Not equal')
```


```python
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
```


```python
a = int(input('Enter 1st number : '))
if a/2 
```
