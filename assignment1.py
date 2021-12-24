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

Continuation
Dec 16, 2021

#Challenge: run 'dir('any_string')' Pick any two interesting methods and
#run 'help('any_string'.interesting_method)' Can you figure out how to use these
#methods

In [1]: dir('any_string')
Out[1]:
['__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getnewargs__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rmod__',
 '__rmul__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'capitalize',
 'casefold',
 'center',
 'count',
 'encode',
 'endswith',
 'expandtabs',
 'find',
 'format',
 'format_map',
 'index',
 'isalnum',
 'isalpha',
 'isascii',
 'isdecimal',
 'isdigit',
 'isidentifier',
 'islower',
 'isnumeric',
 'isprintable',
 'isspace',
 'istitle',
 'isupper',
 'join',
 'ljust',
 'lower',
 'lstrip',
 'maketrans',
 'partition',
 'replace',
 'rfind',
 'rindex',
 'rjust',
 'rpartition',
 'rsplit',
 'rstrip',
 'split',
 'splitlines',
 'startswith',
 'strip',
 'swapcase',
 'title',
 'translate',
 'upper',
 'zfill']
In [2]: values = "Today is Thursday, Dec 16, 2021. We are looking forward to Christmas. We need a break."

In [3]: print(values)
Today is Thursday, Dec 16, 2021. We are looking forward to Christmas. We need a break.

In [4]: x = values.find("Christmas")

In [5]: print(x)
59

In [6]: txt = "Today is Thursday, Dec 16, 2021. We are looking forward to Christmas. We need a break."

In [7]: x =txt.endswith(".")

In [8]: print(x)
True

In [9]: x =txt.endswith("break")

In [10]: print(x)
False

In [13]: help("Today is Thursday, Dec 16, 2021. We are looking forward to Christmas. We need a break.".find)

Help on built-in function find:

find(...) method of builtins.str instance
    S.find(sub[, start[, end]]) -> int

    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Return -1 on failure.
(END)
In [19]: list1_coffee = 9.45

In [20]: list2_sugar = 5.67

In [21]: list3_milk = 3.20

In [22]: list4_bread = 7.47

In [23]: list5_butter = 20.23


#Bonus Challenge Can you figure out how to do the same thing on exercise 1 with just one line

In [25]: shopping_list = {"list1_coffee":9.45, "list2_sugar":5.67, "list3_milk":3.20, "list4_bread":7.47, "list5_butt    ...: er":20.23}

In [26]: print(shopping_list)
{'list1_coffee': 9.45, 'list2_sugar': 5.67, 'list3_milk': 3.2, 'list4_bread': 7.47, 'list5_butter': 20.23}


