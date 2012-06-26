#2
#A function that takes an integer and returns the factorial of
#that number
def factorial(a):
    n=1
    while a>0:
        n=n*a
    a=a-1
    return n

#3
# A function that takes an integer n and returns a list of
# containing the first n fibonacci numbers

def fibonacci(n):
    fib_list=[]
    for i in range(1,n+1):
        fib_list.append(fibon(i))
    return fib_list

print fibonacci(10)
def fibon(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fibon(x-1)+fibon(x-2)

#4
# A function that takes an integer and returns true if
# the integer is prime and false otherwise    
def prime(p):
    count=0
    if i in range(1,p+1):
        count+=1
    if count==2:
        return True
    else:
        return False
print prime(13)    

#CHALLENGING PROBLEMS:

#4
# A function that tests if a string is a Palindrome
# and returns true, otherwise returns false
def isPalindrome(x):
    if x==x[::-1]:
        return True
    else:
        return False    
    
isPalindrome('able was I ere I saw elba')


#5
""" A function that takes two strings as input and
returns true if the first string is a substring of the
second string, else returns false """
def isSubstring(a,b):
    if b.find(a)>=0:
        return True
    elif b.find(a)==(-1):
        return False

print isSubstring('fs','barfoobar')





























