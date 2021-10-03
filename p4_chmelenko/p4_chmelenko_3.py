age = float(input("Enter how many years:"))

first_year = 10.5
second_year = first_year + 10.5
after_year = 4
n = age - 2
m = n * 4


if ( age == 0 ):
    print("dog",age,"years old")
elif ( age == 1 ):
    print("dog",first_year,"years old")
elif ( age == 2 ):
    print("dog",second_year,"years old")
elif( age > 2):
    print("dog",second_year + m,"years old")
elif ( age < 0): 
    print("Negative value, try again")