"""
Clean code
Mantenibilidad
Reducir deuda tecnica (problemas que tiene con resultado de un compromiso y una mala desicion que se tomo)
Trabajo agil y efectivo

Ejemplos
# No seguir ningun patron de diseño claro
# no adherirse a ningun estadar de codigo
# tener codigo altamente acoplado
# falta de documentacion


PEP8 Estandar

# Ancho de linea 78 caracteres max
pip install flake8
pip install pylint
pip install mypy
pip install black


PEP20 Zen de python
# ejecutar en el Ipython
import this

# si no es claro de donde viene un paquete o importacion, es mejor siempre definir su origine
# definir siempre el namespace u origen para entender de donde se importa
# Usar alias en las importaciones segun se requiera
origen.funcion()

# plano es mejor que anidado
# si la funcion tiene muchos for, dentro de otros y asi suceviamente, es mejor separar en pequeñas porciones en funciones e ir llamandose

# Dejar espacios entre lineas y no todo en una sola linea de codigo

# Que se pueda reducir todo el codigo en una sola linea de codigo, no significa que sea mucho mas facil de mantener
# Vale la pena hacerlos con funciones cortas

# tratar de refactorizar en el momento

# Los errores deben controlarce, y en funcion del error retornar que tipo de exepcion o error se levanto

# Hay que tratar de no generar codigo ambiguo, al no saber que parametros o que valores espera
# definir el nombre expliciito como parametros, poner el retorno de la funcion

# Tratar de brindar una sola manera de hacer las cosas
# ya que si se deja de multiples formas, se dejara el soporte a multiles formas

# Si no se puede corregir algun bug o un refactorign necesario, se puede dejar un warning o alerta, para no olvidarlo y despues revisarlo

# Si la implementacion es dificl de explicar, es una mala idea, en caso conrario si es facil en el codigo sera facil

# Usar dosctring para documentar clases, o funcionesm modulos -> cual es el proposito y depronto el que hace y como se utiliza
ejemplo open()

"""
