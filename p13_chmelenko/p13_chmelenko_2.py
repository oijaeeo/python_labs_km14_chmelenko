contains = {}
m = []
f = []
txt = []
content = []

def fem(dt):
    dictionary = {}
    for line in dt:
        lst = dt.split()
        for F in lst:
            if F in dictionary: 
                female = line.split(',')[0] 
                female = line.split(',')[2]
            else: 
                dictionary[F] = 1
            return dictionary
def mal(dt):
    dictionary = {}
    for line in dt:
        lst = dt.split()
        for M in lst:
            if M in dictionary: 
                male = line.split(',')[0]
                male = line.split(',')[2]
            else: 
                dictionary[M] = 1
            return dictionary
     
print('Result:')
print('-' * 15)

for v in range(1880, 2020):
    file = open('yob' + str(v) + '.txt')
    d = file.read()
    print(mal(d))

for v in range(1880, 2020):
    file = open('yob' + str(v) + '.txt')
    d = file.read()
    print(fem(d))  
     
print('-' * 15)
