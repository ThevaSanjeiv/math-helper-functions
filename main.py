from evens import evens
from palindrome import palindrome
from factorial import factorial
from squares import squares

num = int(input("Enter a number: "))
even_nmbers = evens(num)
for i in even_nmbers:
    print(i)

c=input()
if palindrome(c):
    print("Its a palindrome number")
else:
    print("Its not a palindrome number")


a=int(input("Enter the number: "))
print(factorial(a))

a=int(input("Enter the number:"))
r=squares(a)
for i in range(a):
    print(i**2)
