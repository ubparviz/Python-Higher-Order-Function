# Narxlarni $ belgisiz olish
# Quyidagi narxlar ro’yxatidan $ belgisiz faqat raqamlarni ajrating (lambda bilan).


prices = ["$120", "$340", "$50", "$90"]

results = list(map(lambda price: price.replace("$", ""), prices))

print(results)