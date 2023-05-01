# Solution 1
def average(salary):
    salary.remove(min(salary))
    salary.remove(max(salary))
    result = sum(salary) / len(salary)
    return result

# Solution 2
def average(salary):
    salary.sort()
    total = 0

    for item in salary[1:-1]:
        total += item

    return total / len(salary[1:-1])

# Solution 3
def average(salary):
    first_num = salary[0]
    second_num = salary[0]

    for item in salary:
        if item > first_num:
            first_num = item
        if item < second_num:
            second_num = item

    salary.remove(first_num)
    salary.remove(second_num)

    return sum(salary) / len(salary)
