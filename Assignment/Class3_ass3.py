# Baggage processing program
print('Welcome to John baggage handling enterprise')
print('Please enter the weight of your baggage in kg')
weight=float(input())
if weight<=50:
    price=2*weight
    print('The price for handling is £',str(price))
else:
    excess=weight%50
    price1=2*50+5*excess
    print('The price for handling your baggage is £',str(price1))
print(' ')
print('The break down of your price is as follows:')
if weight>50:
    print('You have an excess baggage of',str(weight-50))
    print('We charge £2/kg if baggage is less than 50 kg and £5/kg of baggage in excess')
else:
    print('You do not have an excess baggage! We charge £2/kg of baggage')
