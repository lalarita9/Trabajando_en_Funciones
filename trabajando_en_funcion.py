"""
Crear una función que sume dos números, otra que reste dos números, otra que multiplique dos
números, y otra que divida dos números. Adicionalmente, crear una función que acepte dos números 
como parámetros y regrese el resultado en forma de tupla de su suma, resta, multiplicación y división.
Los resultados se deben almacenar en un diccionario, cuyas claves serán: Suma, Resta, Multiplicación y
División, y los valores de cada clave serán los resultados obtenidos con la función creada anteriormente.  
"""
#Se crea función para sumar dos números
def sumar():
    suma= a + b
    return suma
#Se crea función para restar dos números
def restar():
    resta= a - b
    return resta
#Se crea función para multiplicar dos números
def multiplicar():
    multi= a * b
    return multi
#Se crea función para dividir dos números
def dividir():
    division= a / b
    return division
#Se crea función para devolver 4 operaciones matemáticas en forma de tupla
def tupla():
    resultado = [a + b], (a - b), a * b, {a / b}
    return resultado
#Se crea función para almacenar las 4 operaciones matemáticas en un diccionario
def diccionario():
    suma = {'Suma': '{} + {} = {}'.format(a, b, sumar())}
    resta = {'Resta': '{} - {} = {}'.format(a, b, restar())}
    multi=  {'Multiplicar': '{} * {} = {}'.format(a, b, multiplicar())}
    division = {'División': '{} / {} = {}'.format(a, b, dividir())}
    
   #return suma, resta, multi, division
    print("Diccionario:")
    print("\t",suma)
    print("\t",resta)
    print("\t",multi)
    print("\t",division)

#Se crea las variables conteniendo los números a usar en las operaciones
a= (7)
b= (8)
#Se llama a la función print para mostrar resultados en pantalla
print("Tupla:",tupla())
diccionario()


