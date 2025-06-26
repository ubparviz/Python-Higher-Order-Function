# 15. Tanlovlar ro'yxatidan eng ko'p ovoz olganini topish
# Har bir tanlovda necha ovoz borligini bilgan holda eng ko'p ovoz olgan variantni aniqlang.

# max(..., key=lambda x: x["votes"])

votes = [
  {"option": "A", "votes": 123},
  {"option": "B", "votes": 145},
  {"option": "C", "votes": 97}
]

most_voted_user = max(map(lambda x: x["votes"], votes))

print(most_voted_user)

# most_voted_user = max(votes, key=lambda x: x["votes"])

# print("Eng ko'p ovoz olgan variant:", most_voted_user)
# print("Ovozlar soni:", most_voted_user["votes"])