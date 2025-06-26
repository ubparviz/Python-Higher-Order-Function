# 5. lambda bilan ko'paytirish
# Har bir elementni 5 ga ko'paytirish uchun map() va lambdadan foydalaning.


numbers = [2, 4, 6, 8]

result = list(map(lambda x: x * 5, numbers))

print(result)
