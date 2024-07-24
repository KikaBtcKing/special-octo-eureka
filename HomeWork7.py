my_dict = {"Bro": 1979, "Katty": 1998, "Seva": 1987, "Baga": 1983}
print(my_dict)
print(my_dict["Baga"])
my_dict["Kika"] = 1988
print(my_dict ["Kika"])
my_dict .update({"Sveta": 1999, "Maxim": 2000})
print(my_dict)
del my_dict ["Baga"]
print(my_dict.get("Baga"))
print(my_dict)

my_set = {11,22,11,35,True,"true",909}
print(my_set)
my_set .add("Chicken")
print(my_set)
my_set .add(1000)
print(my_set)
my_set .remove("true")
print(my_set)