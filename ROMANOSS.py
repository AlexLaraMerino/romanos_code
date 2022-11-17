'''
1-Crear una funcion que pase de entero > 0 y < 4000 a romano

2-Cualquier otra entrada debe dar error

Casos de prueba

a) 1994 -> MCMXCIV
b) 4000->RomanNumberError("el valor debe ser menor de 4000")
c)"unacadena" -> RomanNumberError("debe ser un entero")
d)0-> RomanNumberError("el valor debe ser mayor a cero")
e)-3 ->RomanNumberError("el valor debe ser mayor de cero")
f)4.5 -> RomanNumberError("Debe ser un entero")
'''

# Constantes 
ROMANOS = {

    "Unidades":{'I':1,'II':2,'III':3,
    'IV':4,'V':5,'VI':6,
    'VII':7,'VIII':8,'IX':9},

    "Decenas":{'X':10,'XX':20,'XXX':30,
    'XL':40,'L':50,'LX':60,
    'LXX':70,'LXXX':80,'XC':90},

    "Centenas":{'C':100,'CC':200,'CCC':300,
    'CD':400,'D':500,'DC':600,
    'DCC':700,'DCCC':800,'CM':900},

    "Millares":{'M':1000,'MM':2000,'MMM':3000}
}

ROMANOS_OFF = dict(sorted(ROMANOS.items(), key=lambda item:item[0], reverse = True))

unidades={
    'I':1,'II':2,'III':3,
    'IV':4,'V':5,'VI':6,
    'VII':7,'VIII':8,'IX':9
}
decenas={
    'X':10,'XX':20,'XXX':30,
    'XL':40,'L':50,'LX':60,
    'LXX':70,'LXXX':80,'XC':90
}
centenas={
    'C':100,'CC':200,'CCC':300,
    'CD':400,'D':500,'DC':600,
    'DCC':700,'DCCC':800,'CM':900
}
millares={
    'M':1000,'MM':2000,'MMM':3000
}

# Clases 
class RomanNumberError(Exception):

    def __init__(self, nombre="RomanNumberError", error="el valor debe ser mayor a cero" ):

        self.nombre = nombre
        self.error = error

# Funciones
# Esta función permite asegurar que el dato introducido por el usuario es un Int.
def comprobarInput():

    while True:
        try:
            data = int(input(f'Dime un número para convertir en romano '))

            if data <= 0:

                try: 
                    raise RomanNumberError
                except RomanNumberError as error:
                    print(error.nombre)
                    print(error.error)

            elif data >= 4000:
                try: 

                    raise RomanNumberError(nombre="RomanNumberError", error="el valor debe ser menor de 4000")
                except RomanNumberError as error:
                    print(error.nombre)
                    print(error.error)
            else:
                return data

        except ValueError:
            print('El dato debe de ser un número entero')

def enteroARomano(N):
    
    N = str(N)
    N = "{:0>4s}".format(N)
    lista = list(N)
    longitud = len(lista)

    for i in range(longitud):
        lista[i] = lista[i]+"0"*((len(lista)-1)-i)
    
    return lista

def transformarRomano(N, diccionario):

    lista = []
    for i in range(4): # Índice de la lista original
        for key,value in ROMANOS.items(): # Cada uno de los diccionarios en orden decreciente
            for _key,_value in value.items():
                if int(N[i]) == _value:
                    lista.append(_key)
    
    lista = "".join(lista)
    
    return lista

print(transformarRomano(enteroARomano(comprobarInput()),ROMANOS))








