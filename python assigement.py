#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q1. Write a Python program that defines a function called "add_numbers" that takes two arguments (i.e.,
#numbers) and returns their sum. Within the function, add the two numbers together and return the result
#using the return statement. Call the function with the values 5 and 6, and print out the returned result.
#This will result in the addition of 5 and 6, with the output of the program being the sum of these two
#numbers.


# In[1]:


def add_numbers(a,b):
    sum=a+b
    return sum
a=add_numbers(5,6)


# In[2]:


a


# In[ ]:


#Q2. Write a Python program that calculates the square root of a given number using a built-in function.
#Specifically, the program should take an integer or float input from the user, calculate its square root
#using the 'sqrt()' function from the 'math' module, and print out the result to the user. As an example,
#calculate the square root of the number 625 using this program, which should output the value of 25.


# In[3]:


import math as mm


# In[5]:


a=int(input("The square root of the number "))
sq=mm.sqrt(a)
print("Square of this number",sq)



# In[6]:


#Q3.Write a program that prints all prime numbers between 0 to 50.
for i in range(2,51):
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
            break
    if prime:    
        print(i)


# In[7]:


#4. How can we swap the values of three variables (let's say a, b, and c) without using a fourth 
#variable? For example, if we have a=5, b=8, and c=9, how can we obtain a=9, b=5, and c=8? The challenge
#is to perform this operation without using an additional variable to store any of the values during
#the swapping process.
a=5
b=8
c=9
a,b,c=c,a,b
print("a =",a)
print("b =",b)
print("c =",c)
    


# In[8]:


#5.Can you write a program that determines the nature of a given number (in this case, 87) as being 
#positive, negative, or zero? The program should be designed to take the number as input and perform 
#the necessary calculations to determine if the number is positive (i.e., greater than zero), negative
#(i.e., less than zero), or zero (i.e., equal to zero). The output of the program should indicate which
#of these three categories the given number falls into.
num=int(input("Enter a number"))
if num>0:
    print("The number is positive")
elif num<0:
    print("The number is negative")
elif num==0:
    print("The number is Zero")
else:
    print("None")


# In[9]:


#6.How can you create a program that determines whether a given number (in this case, 98) is even or 
#odd? The program should be designed to take the number as input and perform the necessary calculations
#to determine whether it is divisible by two. If the number is divisible by two without leaving a remainder,
#it is an even number, and if there is a remainder, it is an odd number. The output of the program should 
#indicate whether the given number is even or odd.
num=int(input("Enter a number"))
if num%2==0:
    print("The number is Even")
else:
    print("The number is Odd")
    


# In[ ]:


#7.Write a program for sum of digits.the digits are 76543 and the output should be 25.
a=76543
num=0
while a>0:
    num=num+a
print("The sum of digit is ")    


# In[ ]:


8.Write a program for reversing the given number  5436 and the output  should be 6345.
num=5436
num.


# In[ ]:


#10.Write a program the given year is 1996  a leap year.
year=1996
if (year%4==0 and year%100!=0)or(year%400==0)
print("It is a leap year")
else:
    ("it is not a leap year")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




