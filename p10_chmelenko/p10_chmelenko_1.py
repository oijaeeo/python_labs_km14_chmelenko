def function(first_list):
    global salary_list
    global i
    salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
    for i, ii in enumerate(salary_list):
        print (salary_list[i], end=' ')
    print (' ')
    return ''
def funct(second_list):
    global salary_list_total
    salary_list_total = list(map(lambda a:round(a*1.3,2), salary_list))
    for i, ii in enumerate(salary_list_total):
        print (salary_list_total[i], end=' ')
    print (' ')
    return ''
def func(third_list):
    global salary_list_procent
    salary_list_procent = list(map(lambda a,b:round(a-b,2), salary_list_total, salary_list))
    for i, ii in enumerate(salary_list_procent):
        print (salary_list_procent[i], end=' ')
    return ''

print('Salary table:')              
print(function(list), funct(list), func(list)) 
