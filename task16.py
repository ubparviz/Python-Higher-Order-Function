# 16. lambda bilan ro'yxatni qisqartirish
# Berilgan ro’yxatdagi faqat string va uzunligi 5 dan katta bo‘lganlarni ajrating:


data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

result = list(filter(lambda x: isinstance(x, str) and len(x) > 5, data))

print(result)
