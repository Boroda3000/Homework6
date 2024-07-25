my_dict = {"Camomile" : 50, "Iris" : 100, "Orchid" : 100, "Rose" : 150}
print(my_dict)
print(my_dict["Camomile"])
print(my_dict.get("Camellia"))
my_dict["Aster"] = 90
my_dict.update({"Tulip" : 70, "Edelweiss" : 110})
print(my_dict)
miss_prod = my_dict.pop("Iris")
print(miss_prod)
print(my_dict)

my_set = {1, 45, 13.6, "Rose", True, 45, "Rose", False, 1}
print(my_set)
my_set.add("Notebook")
my_set.add(1354)
print(my_set)
my_set.discard(0)
print(my_set)