#LOOPS AND LISTS   ex32.py

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

 # este primer tipo de for-loop pasa por una lista
for number in the_count:
 print ("This is count %d" % number)

 # es lo mismo que arriba
 for fruit in fruits:
    print ("A fruit of type: %s" % fruit)

 # también podemos ver listas mixtas
 # tener en cuenta que tenemos que usar %r ya que no sabemos qué contiene
 for i in change:
  print ("I got %r" % i)

 # también podemos construir listas, primero comenzamos con una vacía
 elements = []

 # luego usamos la función de rango para hacer conteos de 0 a 5
 for i in range(0, 6):
   print ("Adding %d to the list." % i)
 # append es una función que enumera
 elements.append(i)

 # ahora podemos imprimirlos también
 for i in elements:
   print ("Element was: %d" % i)
