Question of the day for Thursday January 13th 2022
#Write a shut_down functioon that takes one argument. if the argument is yes, the function should return shutting down, if no it should return shut down aborted. if the argument is neither yes or no, the function should return sorry.

 def shut_down():
         #This function defines the action to be taken, given certain conditions
         arguments = ("yes", "no", "yes or no")
         for i in arguments:
             if i == yes:
                 print("shutting down")
             if i == no:
                 print("abort")
             else:
                 print("sorry")


#Define a function called hotel_cost with one argument nights as input. The hotel costs $140 per night. So, the function hotel_cost should return 140 * nights.
#Define a function called plane_ride_cost that takes a string, city, as input. The function should return a different price depending on the location.
#define a function called rental_car_cost with an argument called days. Calculate the cost of renting the car: Every day you rent the car costs $40.(cost=40*days) if you rent the car for 7 or more days, you get $50 off your total(cost-=50). Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total. You cannot get both of the above discounts. Return that cost.
#Now define a function called trip cost that takes the output from the three functions above and prints the total cost of the trip
#First, def a function called distance_from_zero, with one argument (choose any argument name you like). If the type of the argument is either int or float, the function should return the absolute value of the function input. Otherwise, the function should return "Nope". Check if it works calling the function with -5.6 and "what?".
