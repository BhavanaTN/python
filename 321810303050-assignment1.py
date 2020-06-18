#!/usr/bin/env python
# coding: utf-8

# write a program to design a simple calculator

# In[3]:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulus(x,y):
    return x % y

def exponent(x,y):
    return x ** y

def floordivision(x,y):
    return x // y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulus")
print("6.exponent")
print("7.floor division")

while True:
    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    if choice in ('1', '2', '3', '4','5','6','7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            
        elif choice == '5':
            print(num1, "%", num2, "=", modulus(num1, num2))
            
        elif choice == '6':
            print(num1, "**", num2, "=", exponent(num1, num2))
            
        elif choice == '7':
            print(num1, "//", num2, "=", floordivision(num1, num2))



        break
    else:
        print("Invalid Input")


# write a python program to calculate simple interest

# In[6]:


def simple_interest(p,t,r): 
    print('The principal is', p) 
    print('The time period is', t) 
    print('The rate of interest is',r) 
      
    si = (p * t * r)/100
      
    print('The Simple Interest is', si) 
    return si
a=float(input("enter principal"))
b=float(input("enter time"))
c=float(input("enter interest"))
simple_interest(a,b,c) 


# write a python program to calculate area of circle
# 

# In[4]:


PI = 3.14
r = float(input("Enter the radius of the circle: "))
area = PI * r * r
print("area of circle:" +str(area))


# write a program to calculate area of triangle

# In[7]:


a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is' +str(area))


# write a program to conver celsius to fahrenheit

# In[10]:


celsius = 32
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))


# write a program to find area of rectangle

# In[21]:


l = float(input("enter length:"))
b = float(input("enter breadth:"))
def area(a,b):
    print( a * b)
area(l,b)
 


# write a program to find perimeter of square

# In[24]:


def perimeter(a): 
        return (4 * a)  
a = float(input("side:"))
c = perimeter(a) 
print("perimeter"+str(c)) 


# write a program to calculate circumference of a circle

# In[2]:


PI = 3.14
r = float(input("Enter the radius of the circle: "))
c = 2 * PI * r
print("circumference of circle:" +str(c))


#  write a program to swap two numbers

# In[10]:


num1=int(input("enter a:"))
num2=int(input("enter b:"))
print("before swap")
print('a=',num1)
print('b=',num2)
t=num1
num1=num2
num2=t
print("after swap")
print('a=',str(num1))
print('b=',str(num2))


# In[ ]:





# In[ ]:




