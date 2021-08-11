import requests
r = requests.get('https://pyscripting.herokuapp.com/api/people')   
print(r)
print(r.headers)
print(r.text)
print(r.status_code)
result = r.json()
print(type(result) , result)
person = result['42']
print(type(person), person)

name = person ['name']
email = person['email']
phone = person['phone']
print(name, email, phone)
