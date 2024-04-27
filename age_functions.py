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
