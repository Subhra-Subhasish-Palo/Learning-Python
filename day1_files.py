print("calculator")
print("==============")

ask = input('choose( * , + , - , / ):')

print("==============")

if ask == '+':
 print('addition')
elif ask == '*':
 print('multiplication')
elif ask == '/':
 print('division')
elif ask =='-':
 print('subtraction')
else:
 print('nothing')

print("==============")

if ask in ['+', '-', '*','/']:

    try:
     x = int(input('X = '))
     y = int(input('Y = '))
   
     if ask == '+':
      print(x + y)
     elif ask == "-":
      print(x - y)
     elif ask == "*":
      print(x * y)
     elif ask == "/":
      print(x/y)
    
    except ValueError:
     print("please enter integers")
    except ZeroDivisionError:
     print("Error: Cannot divide by zero!")

else:
    print("please enter valid sign")
     


