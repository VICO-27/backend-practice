num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
op = input('Enter Operator ')


if op == '+':
    print("the sum is: ", num1 +num2)
elif op ==  '-':
     print("the differece is: ", num1 - num2)
elif op ==  '*':
     print("the multiplication is: ", num1 * num2)
elif op == '/':
     print('The division is: ', abs(num1/num2))
else:
     print('invalid opration input')
