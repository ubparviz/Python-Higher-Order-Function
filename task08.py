# 8. Yoshi bo'yicha sortlash
# Quyidagi lug’atdagi odamlarni yosh bo’yicha o’sish tartibida saralang.

people = [
  {"name": "Ali", "age": 25},
  {"name": "Sami", "age": 19},
  {"name": "Lola", "age": 31}
]

sorted_by_age = sorted(people, key=lambda person: person["age"])

print(sorted_by_age)