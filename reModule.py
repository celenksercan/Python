import re

str0="Sercan Celenk IDENTITY"
str1="Ali ata bak."


result0=re.split(" ",str0)
result1=re.sub("\s","-",str1)

print(result0)
print(result1)