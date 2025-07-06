#loops control statements(y loops)

count = 0

while count < 5:
  print(count)
  count += 1
  if count ==3:
    break #exits  the loop when the count is reached - 3




#loop Control statements

fruits = ["apple","banana","cherry","data"]

for fruit in fruits:
  if fruit == "charry":
      break # Exit the loop if cherry is found
  print(fruit)

print()

fruits = ["apple","banana","cherry","data"]

for fruit in fruits:
  if fruit == "charry":
      continue # Skips cherry and moves to the next iteration
  print(fruit)




print()

fruits = ["apple","banana","cherry","data"]

for fruit in fruits:
  if fruit == "charry":
      pass # placeholder , no action is needed for cherry
  print(fruit)





#Loops
#Using a while loop to count from 1 to 5
count = 1

while count <= 5:
  print(count)
  count += 1 #increment the count by 1


#loops

fruits = ["apple","banana","cherry"]

for fruit in fruits:
  print(fruit)
  

numbers = [1, 2, 3, 5, 7]

for number in numbers:
  print(number)



#control statements
  
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))

if num1 > num2:
  print(num1, "is greater than ",num2)
elif num2 > num1:
   print(num2 ,"is greater than" ,num1)
else:
  print("both number are equal")






#control statements

num = 0

if num > 0: 
    print("This number is positive")
elif num == 0:
  print("This number is zero")
else:
  print("This number is  negative")





#Operator with strings

str1 = 'Hello'
str2 = 'World'

print(str1 + " " + str2 + " " + str2)

print(str1 * 3)





#Operators

#Addition (+)
#Subtraction (-)
#multiplecation (*)
#division (/)
#modulus (%)
#exponent (**)

X = 10
Y = 2

print(X+Y)
print(X-Y)
print(X*Y)
print(X/Y)
print(X%Y)

print(X**Y)

X = 10
X+= 2

print(X)





#Variables

my_variable  = 10
total_count = 0
user = 'John'

#Invalid
second_variable = 10
user_name = 20





#Numeric Data

num = 3

print(type(num))

num2 = 3.14

print(type(num2))

# int num = 3
# float num = 3