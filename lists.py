# my_list = ["spam", "ham", "eggs"]
# my_numbers = [1,2,3,4,5]
#
# print(my_list[0]) # spam
# print(my_list[-1]) # eggs
# print(my_list[0:2])
# print(len(my_list)) # 3
# total = sum(my_numbers)
# print(total)

stops = ["croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket"]
stops.append("Waverly")

# print(stops)
# stops.extend("Queen Street")
# print(stops)
stops.insert(0, "Queen Street")
print(stops)

stops.index("croy")
stops.insert(3, "Polmont")
stops.remove("Haymarket")
print(stops)
