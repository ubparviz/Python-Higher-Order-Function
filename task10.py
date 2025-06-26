# 10. Matndan raqamlarni ajratish
# Berilgan matndan faqat sonlarni ajrating:

text = ["apple", "34", "banana", "100", "abc", "75"]

only_words = list(filter(lambda word: word.isalpha(), text))

print(only_words)