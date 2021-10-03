print("Practice 4. Chmelenko Sophia KM-14")

print("Please, enter the following details:\n")

# Block input
a = input("First name:")      
b = input("Second name:")
c = input("Phone number (format: +380)")
e = input("Enter your street:(Str.)")
f = input("Enter your house number:")
g = input("Enter your apartment number:")
d = input("Enter your city:") 
h = input("Enter your index:")
j = input("Enter your country:\n")

# Block output
print(a, b)     
print(c)
print("Str.",e,f,"," "ap.",g,",",d)
print(h)
print(j,"\n")                                  


v = input("Is this data correct? (yes/no):\n")
if v == 'yes':
    print("Data was entered, thank you.\nYour Ukrposhta:)")
elif v == 'no':
    print("Restart the application:(")   
else:
    print("Error")
