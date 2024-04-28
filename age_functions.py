def till_80(age):
  print(f"in {80-int(age)} years time you will be 80")
def age_category(age):

  if age < 20:
   print ("You are young!")
  elif age < 40 :
   print ("You are adult")
  else:
    print("You are old!")
# age_category ()
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
# list_ages = ages()

# oldest_age = max(list_ages)
# youngest_age = min(list_ages)
# age_gap = oldest_age - youngest_age
# print("Oldest age is " , oldest_age)
# print("Youngest age is " , youngest_age)
# print ("Age gap between " , age_gap )

# define a function that takes no arguments and returns a dictionary of names and ages
def names_and_ages():  #initiate the dict
  names_ages_dict = {}


  # run a while loop taking in names and ages that quits when the user enters quit

  repeat = True 
  while repeat:  #checks if the user has quit 
    name = input("Enter name or type 'quit' to end ") # keep asking for agea and name until types 'quit'
    if name.lower() == "quit":   # if they have ended the loop 
      repeat = False
    else:                
      age = (input("Enter age or type 'quit' to end"))
      if age == "quit":
       repeat = False 
      else:
        names_ages_dict.update({name: int(age)})
  return names_ages_dict # return the dictionaryquit

# using a for loop return a print stating each person's name along with their age

dictionary_result = names_and_ages() 
print(dictionary_result)
for name, age in dictionary_result.items():
    print ("Name:", name, " Age:", age)
  

      

      # if they havent update the dict with their name and age
  
  # return the dict



# change the dict to instead contain a dict for each name within the dict that has their email and age, all ages should be in the form name@lewagon.com and in lower case

# print a line for each person stating their name, email and time till retirement (assume a retirement age of 64)
