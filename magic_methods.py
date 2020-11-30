class items():

    # New es mas usado a nivel de clase, subclases
    def __new__(cls):
        pass

    # Init es mas usado a nivel de Instancia
    def __init__(self):
        pass

    # Metodo antes que se llama el Garbage collector
    # Cuando se elimina, o modifica el valor permite ejecutar otra accion justo antes de desechar la memoria
    def __del__(self):
        pass

    # Comparacion ==
    def __eq__(self, other):
        pass

    # Comparacion !=
    def __ne__(self, other):
        pass

    # Comparacion <
    def __lt__(self, other):
        pass

    # Comparacion >
    def __gt__(self, other):
        pass

    """
    Funciones matematicas
    
    __add__(self, other)
    __sub__(self, other)
    __mul__(self, other)
    __floordiv__(self, other)
    __truediv__(self, other)
    __mod__(self, other)
    __pow__(self, other)
    __and__(self, other)
    __or__(self, other)
    __xor__(self, other)
    """

    """
     Funciones de conversion

     __int__(self)
    __long__(self)
    __float__(self)
    __complex__(self)
    __oct__(self)
    __hex__(self
     """

    """
    Funciones de representacion
    
    __str__(self)   # representacion del objeto
    __repr__(self)  # obtener una representacion del objeto como programador y maquina
    __dir__(self)   # ver los atributos de un objeto en particular
    """