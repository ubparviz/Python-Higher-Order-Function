# 9. Eng uzoq ismni toping
# max() va lambda yordamida eng uzun ismni toping:

names = ["Ali", "Valijon", "Samir", "Diyorbek"]

longer_name = max(names, key=lambda name: len(name))

print(longer_name)