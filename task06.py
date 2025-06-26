# 6. Email domenlarini ajratish
# Quyidagi email ro’yxatidan faqat gmail.com domeniga tegishlilarni ajrating.


emails = ["ali@gmail.com", "vali@yahoo.com", "samir@gmail.com", "bek@outlook.com"]

result = list(filter(lambda email: email.endswith("@gmail.com"), emails))

print(result)
