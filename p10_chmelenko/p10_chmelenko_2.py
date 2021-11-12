import numpy as np

global year
global years
global months

years = np.arange(1900, 2020 + 3, 1)

try:
    year = input("Enter year from range (1900 to 2022): ")
    while year.isalpha() or int(year) < 1900:
        year = input("Enter year from range (1900 to 2022): ")
    while year.isalpha() or int(year) > 2022:
        year = input("Enter year from range (1900 to 2022): ")

    months = input("Enter month from range (1 to 12): ")
    while months.isalpha() or int(months) < 1:
        months = input("Enter month from range (1 to 12): ")
    while months.isalpha() or int(months) > 12:
        months = input("Enter month from range (1 to 12): ")
except ValueError: 
    print('Error, try again')

def function(all):
    return list(filter(lambda i: (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0, all)))


def day(months):
    if months == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        return 31
    elif months == 2:
        if year in function(years):
            return 29
        else:
            return 28
    else:
        return 30

print('Days in a month:', day(months))