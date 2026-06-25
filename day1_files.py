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


# GUESSING NUMKBER

print ("guessing number")
sec_no = 50 

try:
  user_no = int(input("guess number: "))
  if user_no > sec_no :
    print ("too high")
  elif user_no < sec_no :
    print ("too low")
  elif user_no == sec_no:
    print("perfect")

    
except ValueError:
    print("please enter a number")


# avenger if else

print("====Avengers secret party=====")

age = 18
banned = ["loki", "thanos","ultron"]

user_name = input("avenger name: ")

if user_name in banned:
  print(f"{user_name},is a notorious villian not allowned")

else:
  
  try:
   user_age = int(input("avenger age: "))
   
   if user_age < age:
    print("baby avengers are not allowled")
   elif user_age>=age :
    print(f"Welcome to the club,{user_name}!") 
  
  except ValueError:
   print("enter a valid age")



# grades

print("your grades")

user_name = input("enter your id name: ")

try:
    yo_grd = int(input("enter your score: "))

    if yo_grd < 0 or yo_grd > 100:
        print("enter your score in between 0-100")
    elif yo_grd>=90 :
        print("grade a")
    elif yo_grd >=80:
        print("grade b")
    elif yo_grd >= 70:
        print("grade c")
    elif yo_grd < 70:
        print("grade f")

except ValueError:
    print("enter score in numbers")

# some sort of password page

name = "subhra"
pass_ = "Password123"

user = input("username: ")

if user != name:
    print("please enter valid user name")

else:
    pass_input = input("password: ")
    if pass_input == pass_: 
     print(f"welcome, {name}")
    elif pass_input != pass_:
     print("Access Denied!")

# may be a incomple caclulator


print("   calculator")
print("================")

ask = input('choose( * , + , - , / ):')


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

     
# odd even


print("odd even calculator")

try:
    yo_no = int(input("your number: "))

    if yo_no % 2 == 0:
        print("number is even")

    else:
        print("number is odd")

except ValueError:
    print("please enter integers only")
  
   


