# 11. Juft sonlarning kvadratlari
# Faqat juft sonlarni tanlab, ularning kvadratlarini filter() + map() bilan hisoblang.

nums = list(range(1, 21))

juftlarning_kvadrati = list(map(lambda x: x ** 2, filter(lambda num: num % 2 == 0, nums)))

print(juftlarning_kvadrati)
               
