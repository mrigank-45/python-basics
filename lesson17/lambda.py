from functools import reduce
# def squared(num): return num * num
squared = lambda num : num * num

print(squared(2))


# def add_two(num): return num + 2
add_two = lambda num : num + 2

print(add_two(12))


def sum_total(a, b): return a + b
# lambda a, b : a + b


print(sum_total(10, 8))

#######################


def funcBuilder(x):
    return lambda num: num + x


add_ten = funcBuilder(10)
add_twenty = funcBuilder(20)

print(add_ten(7))
print(add_twenty(7))

########################


numbers = [3, 7, 12, 18, 20, 21]

func1 = lambda num: num * num
squared_nums = map(func1, numbers)

print(list(squared_nums))

###############################

func2 = lambda num: num % 2 != 0
odd_nums = filter(func2, numbers)

print(list(odd_nums))

#############################


numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers, 10))


names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
