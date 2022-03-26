print('Welcome to John Loan financial services, please enter the following details)')
print('What is your name')
name=input()
print('Enter your year of birth')
yob=int(input())
age= 2022-yob
print('Enter the amount of loan you are interested in')
loan=int(input())
print('Enter your anual salary')
salary=int(input())
print('Enter your current debt amount')
debt=int(input())
if age>18 and loan<=0.5*salary and debt<0.2*loan:
    print('Congratulations '+name+'! '+'Your loan application for '+str(loan)+' has been approved.')
else:          
    print('Sorry',name,'. Your loan application for ',str(loan),' has been rejected.')
