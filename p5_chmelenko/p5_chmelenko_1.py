# Task 1

salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
procent = 0.3
print("Salary table:")
for i, ii in enumerate(salary_list):
    index = salary_list[i] * procent 
    total = salary_list[i] + index
    print(salary_list[i], round(total,2), round(index, 2))

