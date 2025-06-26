# 2. Har bir sonni kvadratga oshiring. map()

def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5]

result = map(square, numbers)

print(list(result))