customer = {
    'name': 'John Smith',
    'age': 30,
    'is_verified': True
}
print(customer['name'])
print(customer.get('name'))
print(customer.get('birthday'))
print(customer.get('birthdate', "Jan 1 1980"))
# Case-sensitive

customer["name"] = "John Doe"
print(customer)
customer["birthdate"] = "Jan 1 1980"
print(customer)