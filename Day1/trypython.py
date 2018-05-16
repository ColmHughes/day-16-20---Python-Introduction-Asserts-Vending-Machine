# print('Hello World')
# print('Welcome To Python')

# s = 'Whaddup?'
# print(s)
# x=10
# print(2**x)
# fname = input("What is your name? ")
# country = input("Where are you from? ")
# print("Hello " + fname + " from " + country)

# x = int(input("Pick a number: "))
# y = int(input("Pick a second number: "))
# z = x+y
# print(x, " plus " , y , " = " , z)
# print(str(x) + " plus " + str(y) + " = " + str(z))


# text = input("Enter some text: ")
# print(text.upper())
# print(text.lower())
# print(text.title())


# text = input("Enter some text: ")
# print(text[::-1])

# x = int(input("Enter a number: "))

# if x > 10:
#     print("Big")
# else:
#     print("Small")
    
# y = int(input("Enter a number: "))
# z = int(input("Enter a number: "))

# if y == z:
#     print("Same")
# else:
#     print("Different")


# x = int(input("Enter a number: "))
# if x == 1:
#     name = input("Please enter your name: ")
#     print("Hello " + name)
# elif x == 2:
#     age = input("What is your age? ")
#     print("You're " + age + " years old.")
# else:
#     print("TBD")

total = 0
for i in range(10):
    i = int(input("Pick Number " + str(i+1) + "? "))
    total += i
    
print(total)
    


# max = 0
# for i in range(4):
#     num = int(input("Pick Number " + str(i+1) + "? "))
#     if i == 0:
#         max = num
#     if num > max:
#         max = num
 
# print(max)

def add(a, b):
    return a + b
    
print(add(5,8))

c = int(input("Pick a number: "))
d = int(input("Pick a number: "))
def add2(c, d):
    return c + d
    
print(add2(c,d))


def odd(n):
    if n%2 == 0:
        return True
    else:
        return False
        
print(odd(3))
print(odd(999))
print(odd(888))
print(odd(-9999991))
def message():
    return "This is the message"
    
with_parens = message()
without_parens = message

print(with_parens)
print(without_parens)

print(type(message))
print(type(message()))
