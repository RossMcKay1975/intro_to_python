beatles = [
    {"name": "John Lennon", "birth_year": 1940, "death_year": 1980, "instrument": "piano"},
    {"name": "Paul McCartney", "birth_year": 1942, "death_year": None, "instrument": "bass"},
    {"name": "George Harrison", "birth_year": 1943, "death_year": 2001, "instrument": "guitar"},
    {"name": "Ringo Starr", "birth_year": 1940, "death_year": None, "instrument": "drums"}
]

# Use the `beatles` list above to answer the following questions:

# 1. John Lennon also plays guitar. Access the `instrument` key in his dictionary and change its value:
# element = beatles[0]
# element["instrument"] = "guitar"
# print(element)

# 2. Write a function which takes in the list of band members as a parameter,
#    and returns a list of all the Beatles' names:
# Expected result: ['John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Starr']

# def band_members(members):
#     list = []
#     for member in members:
#         list.append(member["name"])
#     return list
#
# print(band_members(beatles))


# 3. Write a function which takes in the list of band members as a parameter,
#    and returns a list of the members who are still alive
#    (i.e. they have no value for `death_year`)
#    Return the full dictionary for each member
# Expected result: [
#    {'name': 'Paul McCartney', 'birth_year': 1942, 'death_year': None, 'instrument': 'bass'},
#    {'name': 'Ringo Starr', 'birth_year': 1940, 'death_year': None, 'instrument': 'drums'}
# ]
def living_members(members):
    living = []
    for living_member in members:
        if living_member["death_year"] == None:
            living.append(living_member)
    return living

print(living_members(beatles))




# 4. Combine the above two functions to return the names of all the members who are alive:

def living_members(members):
    living = []
    for living_member in members:
        if living_member["death_year"] == None:
            living.append(living_member["name"])
    return living

print(living_members(beatles))

# Expected result: ['Paul McCartney', 'Ringo Starr']
