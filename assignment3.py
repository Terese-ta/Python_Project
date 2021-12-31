#1)Assignment 3
#write some code that randomly picks a price from your price list (9.42, 5.67, 3.25, 13.40, 7.50) and prints True if the price is greater than 10 or false if its not.
list = [9.42, 5.67, 3.25, 13.40, 7.50]

import random

print(random.choice(list))
9.42

print(random.choice(list))
5.67
price = random.choice(list)
if price > 10:
    print(True)
else:
    print(False)
                           
False



#2) #You are provided with the following list ['bread', 'butter', 'groundnuts', 'sugar', 'garri', 'egusi', 'ogboono', 'eru']. 
#Write code to print True if the following items ['bread', 'rice', 'okra', 'water', 'egusi'] are found in the list. Can you do this with a for loop?

list = ['bread', 'butter', 'groundnuts', 'sugar', 'garri', 'egusi', 'ogboono', 'eru']
    print(any(item==['bread', 'rice', 'okra', 'water', 'egusi'] for item in list))
False

    print(any(item==['bread'] for item in list))
False
#https://www.tutorialspoint.com/check-if-one-list-is-subset-of-other-in-python



#3)#Write a for loop that prints every letter in the phrase "Blood-oxygenation level dependent functional magnetic resource imaging" 

phrase = "Blood-oxygenation level dependent functional magnetic resource imaging"
for x in phrase:
    print(x)


#4) #Create a grocery list. Now use a for loop to print the words "Note to self, buy" and the grocery item.

grocery_list = ["apple" "egg" "peas" "orange"]
for i in grocery_list:
    print("Note to self, buy", i)
#https://www.webucator.com/article/how-to-use-enumerate-to-print-a-numbered-list-in-p/


#5.) #Now create a for loop that prints a numbered list of your grocery items.

grocery_list = ["apple" "egg" "peas" "orange"]
for i, item in enumerate(grocery_list,1):
    print(i, ". " + item, sep="")


#6.) #Evidently your favorite snack is more important than anything else in your grocery list. 
#Modify the last exercise to stop if and when it finds your favorite snack in your grocery list.

favorite_snack = "peas"
for i in grocery_list:
    if i == favorite_snack:
break
    print(i)
apple
egg

#https://www.w3schools.com/python/python_for_loops.asp


#7) #Use the string split method, to segment all the words in the 
    #phrase ""Blood-oxygenation level dependent functional magnetic resource imaging" using a for loop                                

phrase = "Blood-oxygenation level dependent functional magnetic resource imaging"
i  = phrase.split()
   print(i)
['Blood-oxygenation', 'level', 'dependent', 'functional', 'magnetic', 'resource', 'imaging']

                                                                                                                                    
#8.) Use the range method to write a for loop to print out a numbered grocery list. #If you have not created a groucery list, create it.

grocery_list = ["candy", "peach", "lemon", "coffee", "apple"]
                                                                                                                                        
grocery_list[1] 
'peach'

grocery_list = ["candy", "peach", "lemon", "coffee", "apple"]
range = [0,1,2,3,4]
for i in grocery_list:
                                                                                                                                        
for x in range:
                                                                                                                                        
    print(i,x)
    

# 9)#Use enumerate to print out a numbered grocery list. if you don't have a grocery list, create one.


grocery_list = ["candy", "peach", "lemon", "coffee"]

for i, item in enumerate(grocery_list)
print(i, ". " + item, sep="")
