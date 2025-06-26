# 1. Berilgan ro'yxatdan musbat sonlarni filter() yordamida ajrating.

def positive(number):
    return number > 0

numbers = [4, -2, 0, 7, -9, 3, -1, 5]

result = filter(positive, numbers)

print(list(result))