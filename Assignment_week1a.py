Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
12-10+3**2*2
20
(8+3-5)*((2*3)/(5-3))
18.0
9-2*7%3
7
'I ate'+' '+'3'+' '+'burgers'
'I ate 3 burgers'
name=input()
Martins
YearOfBirth=input()
1987
age=10+YearOfBirth
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    age=10+YearOfBirth
TypeError: unsupported operand type(s) for +: 'int' and 'str'
age=10+int(YearOfBirth)
age
1997
del age
int(YearOfBirth)
1987
age=2022-YearOfBirth
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    age=2022-YearOfBirth
TypeError: unsupported operand type(s) for -: 'int' and 'str'
del age
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    del age
NameError: name 'age' is not defined
age=2022-int(YearOfBirth)
age
35
Print('Hello,'+' '+str(name)+'.'+' '+'You are'+' '+str(age)+' '+'years old'+'.'+' '+'You will be'+' '+str(age+10)+' '+'years old in 10 years'+'.')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    Print('Hello,'+' '+str(name)+'.'+' '+'You are'+' '+str(age)+' '+'years old'+'.'+' '+'You will be'+' '+str(age+10)+' '+'years old in 10 years'+'.')
NameError: name 'Print' is not defined. Did you mean: 'print'?
print('Hello,'+' '+str(name)+'.'+' '+'You are'+' '+str(age)+' '+'years old'+'.'+' '+'You will be'+' '+str(age+10)+' '+'years old in 10 years'+'.')
Hello, Martins. You are 35 years old. You will be 45 years old in 10 years.
