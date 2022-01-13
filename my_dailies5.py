
Question of the day for January 10th 2022.
# 1. write a python function to find the max of 3 numbers.

 def maximum(a, b, c):
    #This function finds the max of 3 numbers
    if (a >= b) and (a >= c):
        largest = a
        
    elif (b >= a) and (b >= c):
        largest = b
    else: 
        largest = c
        return largest
    a = 10
    b = 14
    c = 12
    print(maximum(a, b, c)) 


# 2. Write a python function to sum all the numbers in a list.

  list = [2, 4, 6, 8, 10]
  # function is to find sum of the list
  total_list = sum(list)
  print(total_list)

# 3. Write a python function to multiply all numbers in a list

  def multiply_list(list):
  # function to multiply all numbers in a list
     mul_num = 1
     for i in list:
         mul_num *= i
     return mul_num

# 4. Write a python function to reverse a given string.

    def reverse_string(str):
          #function to reverse string
          string = "apple", "cheese", "orange"
          for i in str:
              string = i + string
              return string 

# 5. Write a python function that takes a string and displays the number of upper case letters and the number of lower case letters.
    list = "i Am a Developer"
    len(list)
