print('Please enter two numbers')
a=int(input())
b=int(input())
if a<5 or b%2==0:
    print('At least one condition has been satisfied')
elif a>=5 or b%2==1:
    print('No condition has been satisfied')
