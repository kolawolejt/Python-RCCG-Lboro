print('Hello, what is your name?')
name=input()
print('And what is your year of birth?')
yob=input()
#above is the year of birth 'yob'
age = 2022 - int(yob) + 10
#'age' is the age 10 years from now
print('Hello, ' + name + '. You will be ' + str(age) + ' years old in 10 years.')
