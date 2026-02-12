marks = [35, 78, 42, 90, 25, 60, 55]
def get_passed_students(marks):
    return list(filter(lambda x: x>=40,marks))
grace_marks=list(map(lambda x:x+5,marks))
def calculate_average(marks):
    return sum(marks)/len(marks)
print("Passed Students:",get_passed_students(marks))
print("Grace marks:",(grace_marks))
print("Average Marks:",calculate_average(marks))






















salaries = [25000, 40000, 52000, 61000, 30000, 80000]
def increase_salary(salaries):
    return list(map(lambda x: int(x * 1.10), salaries))
def high_salary_employees(salaries):
    return list(filter(lambda x: x > 50000, salaries))

def total_payout(salaries):
    return sum(salaries)

updated_salaries = increase_salary(salaries)
high_salary = high_salary_employees(updated_salaries)
total = total_payout(updated_salaries)


print("Updated Salaries:", updated_salaries)
print("High Salary Employees:", high_salary)
print("Total Salary Payout:", total)
