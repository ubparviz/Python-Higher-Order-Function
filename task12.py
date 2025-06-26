# 12. Talabalarni baho bo‘yicha tartiblang
# Baholar bo‘yicha saralash (kichikdan katta):

students = [
  {"name": "Aziz", "grade": 89},
  {"name": "Kamola", "grade": 95},
  {"name": "Javlon", "grade": 76}
]

tartiblash = sorted(students, key = lambda grade: grade["grade"])

print(tartiblash)