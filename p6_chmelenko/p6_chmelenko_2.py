#Task 2

index = input(("Enter the post index (example: A2B): ").upper()).upper()

if len(index) != 3 or not index[0].isalpha() or not index[-1].isalpha() or not index[1].isdigit():
    print(("error").upper())
    exit()

indexes = {
    'Newfoundland': 'A',
    'Nova Scotia': 'B',
    'Prince Edward Island': 'C',
    'New Brunswick': 'E',
    'Quebec': ('G', 'H', 'J'),
    'Ontario': ('K', 'L', 'M', 'N', 'P'),
    'Manitoba': 'R',
    'Saskatchewan': 'S',
    'Alberta': 'T',
    'British Columbia': 'V',
    'Nunavut': 'X',
    'Northwest Territories': 'X',
    'Yukon': 'Y'
}
a = ''
for i in indexes.keys():
    if isinstance(indexes[i], str):
        if indexes[i] == index[0]:
            a += i + " "
    else:
        if index[0] in indexes[i]:
            a += i + " "
if a == " ":
    print(("Sorry, we haven`t the same index").upper())
    exit()
print(("The name of the province(s): " + a).upper())
if index[1] == 0:
    print(("Type of terrain : Village").upper())
else:
    print(("Type of terrain : City").upper())