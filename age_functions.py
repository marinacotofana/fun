def till_80(age):
  print(f"in {80-int(age)} years time you will be 80")
def age_category(age):

  if age < 20:
   print ("You are young!")
  elif age < 40 :
   print ("You are adult")
  else:
    print("You are old!")
age_category (43)
def ages():
  age_list = []
  repeat = True 
  while repeat: 
    age = input("Enter your age or type 'quit' to end ") # keep asking for age until types 'quit'
    if age == 'quit': 
      repeat = False
    else:
      age_list.append(int(age))
  print(age_list)
  return age_list
list_ages = ages()

oldest_age = max(list_ages)
youngest_age = min(list_ages)
age_gap = oldest_age - youngest_age
print("Oldest age is " , oldest_age)
print("Youngest age is " , youngest_age)
print ("Age gap between " , age_gap )

# define a function that takes no arguments and returns a dictionary of names and ages

  # initiate the dict

  # run a while loop taking in names and ages that quits when the user enters quit

    # check if the user has quit

      #if they have end the loop

      # if they havent update the dict with their name and age
  
  # return the dict

# using a for loop return a print stating each person's name along with their age

# change the dict to instead contain a dict for each name within the dict that has their email and age, all ages should be in the form name@lewagon.com and in lower case

# print a line for each person stating their name, email and time till retirement (assume a retirement age of 64)
