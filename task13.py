# 13. Top 3 eng uzun so‘z
# Matndagi eng uzun 3 ta so‘zni toping:

# Foydalaning: sorted(), lambda, split(), [:3]

sentence = "Functional programming in Python is very powerful and elegant"

sentence_list = sentence.split()

sorted_by_len = list(sorted(sentence_list, key = lambda word: len(word), reverse = True))

Three_longer_words = sorted_by_len[:3]

print(f"Eng uzun uchta so'z: {Three_longer_words}")



# Yoki Bir qator Python kod bilan ham chiqarsa bo'ladi

Three_longer_words = list(sorted(sentence.split(), key = lambda word: len(word), reverse = True))[:3]

print(f"Eng uzun uchta so'z: {Three_longer_words}")