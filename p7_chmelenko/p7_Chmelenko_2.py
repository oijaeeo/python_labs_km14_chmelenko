#test 2

def func(f):
    error = "Range of values: [0;255]"
    if f.isdigit():
        if 0 < int(f) < 255:
            return True
    print(error)
    return False

def defunc(f):
    f = int(f)
    fanc = [i for i in range(9)]
    fanc += ['A', 'B', 'C', 'D', 'E', 'F']
    a = str(fanc[f // 16])
    a += str(fanc[f % 16])
    return a

defunc_number = ' #'
inputing = 'Enter the {} number to convert [0;255] (Example: 158)  : \n'
for n in ('first', 'second', 'third'):
    while True:
        f = input(inputing.format(n))
        if func(f):
            defunc_number += defunc(f).zfill(2)
            break

print('The color is:'+ defunc_number)