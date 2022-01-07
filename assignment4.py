Jan 5, 2022

# PYTHON WEEKLY ASSIGNMENT 4

## if we list all numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these numbers is 23.
## Write some code to find the sum of all  multiples of 3 and 5 between 0 and 1000.

for num in range(1000):
         if num % 3 == 0 or num % 5 == 0:
             print(num)

while i<1000:
         if i%3==0 or i%5==0:
             print(num)
         i+=1
     print("Total is: ")I

## Write a python program to count the number of occuring characters in a given string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

from collections import Counter
string = "google.com"
Counter(string)

## Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'

custom_string = "$"
print(f"Saturd{custom_string}y")

## Given the following list, list1 = [100, 200, 300, 400, 500], reverse the list
expected result: [500, 400, 300, 200, 100]

list = [100, 200, 300, 400, 500]
list.reverse()
print(list)

## Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
so if given:
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
Expected output should be: ['My', 'name', 'is', 'Kelly']

listA = ["M", "na", "i", "Ke"]
listB = ["y", "me", "s", "lly"]
listC = [i + x for i, x in zip(listA, listB)]
print (listC)


## Write a Python program to iterate over dictionaries using for loops.

thisdict = {"candy": "lollipop", "soup": "pepper soup", "school": "humber"}
for i in thisdict:
         print(i)

## Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n = 15
for i in range(1, n+1):
    numbers[i] = i * i
print (numbers)


## Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

y = 10
numbers = {}
for i in range(1, y+1):
        numbers[i] = i * i
print(numbers)

## Assign the first number of lst to answer _1 and print it. I have helped  you with some of the code
lst=[11, 100, 99, 1000, 999]
answer_1=

_1, x, y, z, a = [11, 100, 99, 1000, 999]
print(_1)


## Now print the second item directly. again I am helping you with some of the code
lst=[11, 100, 99, 1000, 999]
print()

_1, x, y, z, a = [11, 100, 99, 1000, 999]
print(x)
