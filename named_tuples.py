from collections import namedtuple
import datetime

# Person = namedtuple("Person", "name age job_title")
#
# john = Person("John", 37, "instructor")
# jane = Person("Jane", 27, "instructor")
# print(john.name)
# print(john.age)
# print(john.job_title)

Employee = namedtuple("Employee", "name ni_number dob")

ross = Employee("Ross", "jb12345h", datetime.datetime(1975, 12, 18))
print(ross.name)
print(ross.ni_number)
print(ross.dob)
