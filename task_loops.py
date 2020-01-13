# ages = [5, 15, 64, 27, 84,26]
#
# total = 0
# for age in ages :
#     total = total + age
#
# print(total)
#
# average = total/len(ages)
# print average

# words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
# letters = [word[0].lower()for word in words]
# print(letters)

pupils = ["Alison", "James", "Stephen", "Mandy", "Henry", "Jack"]
found = False
for name in pupils:
    if name == "Jack":
        found = True

    if found:
        print("Jacks here mofos!!")
    else:
        print("Wheres Jack!?")
