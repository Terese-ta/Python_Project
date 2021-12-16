Name: Terez
Subject: Python_Assignment_1
Proff: Willy

Date: Dec 16, 2021

Requirements
# 1. Make a shopping list of 5 things you need at the grocery store
# put each item on a line by itself
#2 Your items ring up as 9.45, 5.67, 3.20, 7.47 and 20.23. Use python as a handy
# calculator to calculate the total of your shopping.
#3. But wait, you decide to buy five more of the last item. Recalculate the total
#4. Uinsg a built in function, determine the length of this phrase: 'Blood oxygenation level dependant functional magnetic resource imaging '
#5. Pick your favorite snack, use the * operator to print it a 100 times.
# Modify the code to print it with spaces in between.
#Challenge: run 'dir('any_string')' Pick any two interesting methods and
#run 'help('any_string'.interesting_method)' Can you figure out how to use these
#methods
#Bonus Challenge Can you figure out how to do the same thing on exercise 1 with just one line



First Attempt

In [56]: list1_coffee = 9.45

In [57]: list2_sugar = 5.67

In [58]: list3_milk = 3.20

In [59]: list4_bread = 7.47

In [60]: list5_butter = 20.23

In [61]: print(list1_coffee + list2_sugar + list3_milk + list4_bread + list5_butter)
46.019999999999996

In [62]: print(list1_coffee + list2_sugar + list3_milk + list4_bread + list5_butter * 5)
126.94

In [63]: phrase = 'Blood oxygenation level dependant functional magnetic resource imaging '

In [64]: print(len(phrase))
71

In [72]: favorite_snack = "bread  "

In [73]: print(favorite_snack * 100)
bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread  bread



