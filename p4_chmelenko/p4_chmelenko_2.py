  
try:
    x = float(input('Enter wind speed (km/h): '))
    
    if ( 0 <= x <= 137 ):
        print("Minor hazard")
    elif ( 137 < x <= 177 ):
        print("Moderate hazard")
    elif ( 177 < x <= 217 ):
        print("Considerable hazard")
    elif ( 217 < x <= 266 ):
        print("Severe hazard")
    elif ( 266 < x <= 322 ):
        print("Devastating hazard")
    elif ( x > 322 ):
        print("Incredible hazard")
    else: 
        print("Value error, try again")
except ValueError:
    print("Please, enter a number")
