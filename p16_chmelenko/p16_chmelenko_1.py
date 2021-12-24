n = 16
def copy_tuple(boolean):
    def wrapper(func):
        def wrap(*args):
            l = func(*args)
            if boolean:
                l_changed = []
                for i in l:
                    l_changed.append([(i[j], i[j + 1], i[j + 2], i[j + 3]) for j in range(0, len(i), 4)])
                return l_changed
            return l
        return wrap
    return wrapper

@copy_tuple(True)
def copybook(number, a):
    lst = []
    b = int(a / 2)
    for q in range(0, number, a):
        lst_copybook = []
        lst.append([])
        lst_copybook.append((q + a - i, q + i + 1, q + i + 2, q + a - (i + 1))
        for i in range(0, b , 2))
        for i in lst_copybook:
            for w in i:
                lst[-1].extend(w)
    return lst

while 1:
    que = input('Enter pages (it must be a multiple of 16 and not more than 1280): ')
    if que.isdigit() and int(que) <= 1280 and int(que) % n == 0:
        que = int(que)
        break
    print('False que, try again!')
print('Copybooks queber = {}'.format(que//n))
print('-' * 15)
for i in copybook(que, n):
    for j in i:
        print(j)
print('-' * 15)