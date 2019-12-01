#ask user their choice of operation
print('select operation')
print('1.addition')
print('2.subtraction')
print('3.division')
print('4.multiplication')
choice=input('Enter your choice:  ')
#ask user to enter number to operation with that operation
num1=float(input('Enter first number: '))
num2=float(input('Enter second number: '))
#conditional functioning
if choice == '1':
    print(num1,'+',num2,'=',num1+num2)
elif choice == '2':
        print(num1, '-', num2, '=', num1 - num2)
elif choice == '3':
        print(num1, '/', num2, '=', num1 / num2)
elif choice == '4':
        print(num1, 'x', num2, '=', num1 * num2)
else:
    print('Invalid Input')
