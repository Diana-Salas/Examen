#DICTIONARIES    ex39.py

# crear un mapeo de estado a su abreviatura
states = {
  'Oregon': 'OR',
  'Florida': 'FL',
  'California': 'CA',
  'New York': 'NY',
  'Michigan': 'MI'
}

# crear un conjunto básico de estados y algunas ciudades de ellos
cities = { 
   'CA': 'San Francisco',
   'MI': 'Detroit',
   'FL': 'Jacksonville'
}

# agregamos mas ciudades
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# imprimir algunas ciudades
print ('- ' * 10)
print ("NY State has: ", cities['NY'])
print ("OR State has: ", cities['OR'])

# imprimir algunos estados con abreviacion
print ('- ' * 10)
print ("Michigan's abbreviation is: ", states['Michigan'])
print ("Florida's abbreviation is: ", states['Florida'])

# imprimir el estado y luego las ciudades
print ('- ' * 10)
print ("Michigan has: ", cities[states['Michigan']])
print ("Florida has: ", cities[states['Florida']])

# imprimir cada abreviatura del estado
print ('- ' * 10)
for state, abbrev in states.items():
	print ("%s is abbreviated %s" % (state, abbrev))

# imprimir todas las ciudades del estado
print ('- ' * 10)
for abbrev, city in cities.items():
	print ("%s has the city %s" % (abbrev, city))

# ahora hace las dos cosas al mismo tiempo
print ('- ' * 10)
for state, abbrev in states.items():
	print ("%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))

print ('- ' * 10)
# obtener de manera segura una abreviatura por estado que podría no estar allí
state = states.get('Texas', None)

if not state:
	print ("Sorry, no Texas.")

# obtener una ciudad con un valor predeterminado
city = cities.get('TX', 'Does Not Exist')
print ("The city for the state 'TX' is: %s" % city)
