import json

person_string='{"name":"Ali","languages":["python","C#"]}'

# JSON string to Dict

result=json.loads(person_string)
print(result["name"])
print(result)


# Dict to JSON string
