### DICTIONARY ###
# Key π Value
# Laptop (key) π Apple (value)
# Mutable (change-able)


# print(person['name'])
# print(person['shirt'])
# print(person['laptop'])

def netWorth():
  return person['assets'] - person['debt']

def introducer():
  person = {
  'name': 'Qazi', 
  'shirt': 'Black', 
  'laptop': 'Apple',
  'phone_number': '224-123-3456',
  'assets': 100,
  'debt': 50,
  'favoriteFruits': ['π', 'π', 'π'],
  'netWorth': lambda: person['assets'] - person['debt']
}

  person['shirt'] = 'Orange'
  person['assets'] = 1000
  
  print(f"π Hi my name is {person['name']}, 
  \nπ I am wearing a {person['shirt']} shirt, 
  \nπ¨βπ» and the laptop I use to code is an {person['laptop']}, 
  \nπ°and my net worth is ${person['netWorth']()} USD, 
  \nπ₯My favorite fruits are {person['favoriteFruits']}")

  print(list(person.values()))
  print(person.keys())

introducer()