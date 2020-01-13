import datetime


me = {
    "name" : "Ross",
    "dob" : datetime.datetime(1991, 3, 12),
    "students" : ["Suzanne", "Chris", "Davide"]}

print( me["dob"].strftime("%A %d %b %Y") )
print( dir(datetime.datetime))
