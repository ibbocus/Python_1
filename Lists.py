cities = ["Tokyo", "Paris", "Prague", "Luxembourg"]
print(cities)
cities[3] = "Amsterdam"
print(cities)
cities.append("London")
print(cities)


print(cities.pop(1))
print(cities)
cities = [["Tokyo", "Paris"], ["Prague", "Luxembourg"]]
del cities[1]
print(cities)
cities.insert(4, "London")
print(cities)

other_list = [1,2,3]
print((cities + other_list)[0])