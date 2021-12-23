from exp_root.exponentation import exp2, exp3
from exp_root.root import root2, root3
from factorial.factorial import factorial
from logarithm.logarithm import log, lg, ln


def main():
    chose = input('Choose function (Exponentiation(exp);  Root(r); Logarithmic(log); Factorial(f)):')
    if chose == 'exp':
        while True:
            n = input('Input exponentiation:')
            try:
                n = int(n)
                print('exp2:' + str(exp2(n)))
                print('exp3:' + str(exp3(n)))
                break
            except Exception:
                print('Uncorrect data!')
            else:
                raise Exception
                break
    elif chose == 'r':
        while True:

            try:
                r = int(input('Input number:'))
                if r < 0:
                    raise Exception
                print('root2:' + str(root2(r)))
                print('root3:' + str(root3(r)))
                break
            except Exception as j:
                print(j)
            else:
                break
    elif chose == 'log':
        while True:
            n1 = input('Please, input which type of logarithm: (log (1); ln (2); lg (3)):')
            try:
                if n1 == '1':
                    a = int(input('Input a:'))
                    b = int(input('Input b:'))
                if a < 0 and b < 0:
                    raise Exception
                if a == 1 and b == 1:
                    raise Exception
                elif print('Log is:' + str(log(b, a))):
                    break
            except Exception as null:
                print(null)
            try:
                if n1 == '2':
                    a = int(input('Input a:'))
                if a < 0:
                    raise Exception
                elif print('Ln is:' + str(ln(a))):
                    break
            except Exception as t:
                print(t)
                try:
                    if n1 == '3':
                        a = int(input('Input a:'))
                    if a < 0:
                        raise Exception
                    elif print('Lg is:' + str(lg(a))):
                        break
                except Exception as l:
                    print(l)
    elif chose == 'f':
        while True:
            f = input('Input factorial:')
            try:
                f = int(f)
                if f < 0:
                    raise Exception
                print('Factorial: ' + str(factorial(f)))
                break
            except Exception as m:
                print(m)

if __name__ == '__main__':
    main()