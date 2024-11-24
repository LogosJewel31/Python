print("Hello,World!")
x = 5
print(type(x))
x = "Hello,Wolrd!"
print(type(x))
x = 20.5
print(type(x))
x = 1j
print(type(x))
# in code 11 and 13 the differnce is in the bracket
x = ["apple", "banana", "cherry"]
print(type(x))
x = ("apple", "banana", "cherry")
print(type(x))
x = range(6)
print(type(x))
x = {"name" : "john", "age" : "36"}
print(type(x))
x = {"apple", "banana", "cherry"}
print(type(x))
x= True
print(type(x))
x = b"Hello"
print(type(x))
x = None
print(type(x))
x = 1               #int
y = 2.8             #float
z= 1j                #complex
print(type(x))
print(type(y))
print(type(z))
x = 1
y = 2.8
z = 1j
# CONVERT FROM INT TO FLOAT
a =float(x)

#CONVERT FRON FLOAT TO INT
b =int(y)

# CONVERT FROM INT TO COMPLEX
c =complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
#YOU CANNOT CONVERT COMPLEX INTO ANOTHER TYPE

import random

print(random.randrange(1,10))

#INTEGERS
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)
a = "Hello"
print(a)
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqu."""
# STRINGS ARE ARRAYS ALWAYS WITH A ZERO
print(a)
a = "Hello Wold!"
print(a[1])
# loop through a string 
for x in "banana":
    print(x)

#STRING LENGTH USE LEN FUNCTION
a = "Hello, World!"
print(len(a))
# to check if a certain phrase is in a text
txt = "The best things in life are free!"
print("free" in txt)
# use of if in a txt statement
txt = "The best things in life are free!"
if  "free" in txt:
    print("Yes, 'free' is present.")

#to check if a phrase or character is not present in a string make use of "not in"
txt = "The best things in life are free!"  
print("expensive" not in txt)
txt = "The bests yhings in life are free"  
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
# slice from a certain character to the another one
b = "Hello, World!"
print(b[2:5]) 
#slice from the start to a certain character
b = "Hello,World!" 
print(b[:5]) 
#slice to the end 
b = "Hello, World!"
print(b[2:])
# negative indexing
b = "Hello, World!"
print(b[-5:-2])
# uppercase
a = "Hello, Wolrd!"
print(a.upper())
#lowercase
a = "Hello, World!"
print(a.lower())
a = " Hello, World! "
# remove white space
print(a.strip())    #returns hello world
# replace strings
a = "Hello, World!"
print(a.replace("H", "J"))
#split srings
a = "Hello, World!"
print(a.split(","))
a = "Hello"
b = "World"
c = a + b
print(c)
a = "Hello"
b = "World"
c = a + " " + b
print(c)
age = 36
txt =f"My name is John, I am {age} "
print(txt)
price = 59
txt = f"The price is {price} dollars"
print(txt)
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
txt = f"The price is {20 + 59} dollars"
print(txt)
# escape character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
# boolean values to know whether its true or false
a = 200
b = 30

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
class myclass():
    def _len_(self):
        return 0
myobj = myclass()
print(bool(myobj))
def myFunction() :
    return True
print(myFunction())