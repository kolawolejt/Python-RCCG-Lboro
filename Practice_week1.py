Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
6
6
python -V
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    python -V
NameError: name 'python' is not defined
py
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    py
NameError: name 'py' is not defined

2+3
5
2+3+5
10
2+3*5
17
(2+3)*5
25
2+3**2*4
38
(5-1)*((7+1)/(3-1))
16.0
1+1
2
'a'+'b'
'ab'
'5'+'20'
'520'
'1'+2
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    '1'+2
TypeError: can only concatenate str (not "int") to str
'John'*3
'JohnJohnJohn'
3*'John'
'JohnJohnJohn'
'Tim'+'Tom'
'TimTom'
spam=42
a=10
name='John'
name
'John'
name='Kolawole'
name
'Kolawole'
del
SyntaxError: invalid syntax
del name
name
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    name
NameError: name 'name' is not defined
name='John'
type(name)
<class 'str'>
len(name)
4
len(spam)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    len(spam)
TypeError: object of type 'int' has no len()
type(spam)
<class 'int'>
str(name)
'John'
print(John)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(John)
NameError: name 'John' is not defined
print(name)
John
'we are in the year'+str(2022)
'we are in the year2022'
'we are in the year'+' '+str(2022)
'we are in the year 2022'
year='we are in the year'+' '+str(2022)
print(year)
we are in the year 2022
apples=5
oranges=4
bananas=8
total=apples+oranges+bananas
print(total)
17
total
17
age=input()
22
age
'22'
ask_age='what is your age'
print(ask_age)
what is your age
age=input()
23
