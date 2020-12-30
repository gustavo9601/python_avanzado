"""
Wreapper de clases o funciones, para agregar algun comportamiento
"""

def eggs(function):
    print("Decorator called")
    return function

@eggs
def smap_decorated():
    """
    This is spam funcion
    """
    print("smap function executed")
    return 'sucess decorated'