#Author:SercanCelenk
from datetime import datetime

simdi=datetime.now() #datetime.today()
print(simdi.year)
print(simdi.month)
print(simdi.day)
print(simdi.hour)
print(simdi.minute)
print(simdi.second)

print(datetime.ctime(simdi))
