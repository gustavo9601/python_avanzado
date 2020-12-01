"""
Comprenhensions
"""

# List Comprenhensions
squares = [x ** 2 for x in range(10)]
print("squares => ", squares)

# para cada x se multiplicara por 2
# siempre y cuando el modulo sea diferente a 0 "impares"
uneven_squeres = [x ** 2 for x in range(10) if x % 2 != 0]
print("uneven_squeres => ", uneven_squeres)

# Set Comprenhensions
uneven_squeres_set = {x ** 2 for x in range(10) if x % 2 != 0}
print("uneven_squeres_set => ", uneven_squeres_set)

# Dict Comprenhensions
# cada iteracion de x la usa como llave
# cada potencia de x es el valor de la llave
# siempre y cuando el modulo sea diferente a 0 "impares"
dict1 = {x: x ** 2 for x in range(10) if x % 2 != 0}
print("dict1 => ", dict1)

# Tuples Comprenhensions
# Al ser tupla se comporta como generador, lo parseamos a una lista
tuple1 = list(x for x in range(5))
print("tuple1 => ", tuple1)