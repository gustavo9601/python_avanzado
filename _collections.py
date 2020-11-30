import collections
import builtins

dic1 = {
    'name': 'Gus',
    'surname': 'Maquez'
}

dic2 = {
    'age': '24'
}

# .ChainMap(diccionarios**)
# une en una tupla todos los diccionarios pasados por parametro
merge_dicts = collections.ChainMap(dic1, dic2)
print("merge_dicts => ", merge_dicts)

# .get('llave')
# Obteniendo informacion de cualquiera de los diccionarios
print("merge_dicts.get('age') => ", merge_dicts.get('name'))

# Counter
# Permite obtener cuantas veces se encuentra en el objeto iterable
# Devuelve un diccionario con los indices como los valores del iterable, y el valor sera la cantidad de veces iteradas
food = ['tomato', 'banana', 'banana', 'pineapple', 'apple', 'orange', 'tomato', 'tomato']
print("collections.Counter(food) => ", collections.Counter(food))

# most_commons(cantidad_De_comunes)
# devuelve los valores que mas se repiten, de acuerdo al parametro enviado
counter_food = collections.Counter(food)
print("counter_food.most_common(2) => ", counter_food.most_common(2))

# .OrderedDict()
# ordena alfabeticamente los indices
print("collections.OrderedDict(sorted(counter_food.items())) => ",
      collections.OrderedDict(sorted(counter_food.items())))
