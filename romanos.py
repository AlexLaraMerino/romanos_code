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

# CLASES 

class RomanNumberError(Exception):

    def __init__(self, nombre="RomanNumberError", error="el valor debe ser mayor a cero" ):

        self.nombre = nombre
        self.error = error



#--------------------------------------------------------------------------------------------------

# FUNCIONES  
def comprobarNumeroInput():

    while True:
        try:
            data = int(input(f'Dime un número para convertir en romano '))
            return data
        except ValueError:
            print('El dato debe de ser un número entero')
    

def acotarNumero(N):

    # Posible mejora con while
    if N <= 0:
        try: 
            raise RomanNumberError
        except RomanNumberError as error:
            print(error.nombre)
            print(error.error)

    elif N >= 4000:
        try: 
            raise RomanNumberError(nombre="RomanNumberError", error="el valor debe ser menor de 4000")
        except RomanNumberError as error:
            print(error.nombre)
            print(error.error)
    else: pass

def correccionSegunReglas(lista):

    romanos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for i in range(len(lista)):

        try:
            y = lista[i]
            suma = romanos[lista[i]] + romanos[lista[i-1]] + romanos[lista[i-2]] + romanos[lista[i-3]] + romanos[lista[i-4]]
            while lista[i] == lista[i-1] and lista[i] == lista[i-2] and lista[i] == lista[i-3]:
                # Opción 9
                if suma == 90:
                    for key in romanos.keys():
                        if lista[i] == key:
                            if key == "C":
                                lista[i-4] = key
                                lista[i-3] = "M"
                                lista.pop(i-2)
                                lista.pop(i-1)
                                lista.pop(i-2)
                            elif key == "X":
                                lista[i-4] = key
                                lista[i-3] = "C"
                                lista.pop(i-2)
                                lista.pop(i-1)
                                lista.pop(i-2)
                            elif key == "I":
                                lista[i-4] = key
                                lista[i-3] = "X"
                                lista.pop(i-2)
                                lista.pop(i-1)
                                lista.pop(i-2)
                elif suma == 900:
                    for key in romanos.keys():
                        if lista[i] == key:
                            if key == "C":
                                lista[i-4] = key
                                lista[i-3] = "M"
                                lista.pop(i-2)
                                lista.pop(i-1)
                                lista.pop(i-2)
                            elif key == "X":
                                lista[i-4] = key
                                lista[i-3] = "C"
                                lista.pop(i-2)
                                lista.pop(i-1)
                                lista.pop(i-2)
                            elif key == "I":
                                lista[i-4] = key
                                lista[i-3] = "X"
                                lista.pop(i-2)
                                lista.pop(i-1)
                                lista.pop(i-2)
                elif suma == 9:
                    for key in romanos.keys():
                        if lista[i] == key:
                            if key == "C":
                                lista[i-4] = key
                                lista[i-3] = "M"
                                lista.pop(i-2)
                                lista.pop(i-1)
                                lista.pop(i-2)
                            elif key == "X":
                                lista[i-4] = key
                                lista[i-3] = "C"
                                lista.pop(i-2)
                                lista.pop(i-1)
                                lista.pop(i-2)
                            elif key == "I":
                                lista[i-4] = key
                                lista[i-3] = "X"
                                lista.pop(i-2)
                                lista.pop(i-1)
                                lista.pop(i-2)
                # Opción 4
                elif suma == 1400:
                    for key in romanos.keys():
                        if lista[i] == key:        
                            if key == "C":
                                lista[i-3] = key
                                lista[i-2] = "D"
                                lista.pop(i-1)
                                lista.pop(i-1)
                            elif key == "X":
                                lista[i-3] = key
                                lista[i-2] = "L"
                                lista.pop(i-1)
                                lista.pop(i-1)
                            elif key == "I":
                                lista[i-3] = key
                                lista[i-2] = "V"
                                lista.pop(i-1)
                                lista.pop(i-1)
                elif suma == 140:
                    for key in romanos.keys():
                        if lista[i] == key:        
                            if key == "C":
                                lista[i-3] = key
                                lista[i-2] = "D"
                                lista.pop(i-1)
                                lista.pop(i-1)
                            elif key == "X":
                                lista[i-3] = key
                                lista[i-2] = "L"
                                lista.pop(i-1)
                                lista.pop(i-1)
                            elif key == "I":
                                lista[i-3] = key
                                lista[i-2] = "V"
                                lista.pop(i-1)
                                lista.pop(i-1)
                elif suma == 104:
                    for key in romanos.keys():
                        if lista[i] == key:        
                            if key == "C":
                                lista[i-3] = key
                                lista[i-2] = "D"
                                lista.pop(i-1)
                                lista.pop(i-1)
                            elif key == "X":
                                lista[i-3] = key
                                lista[i-2] = "L"
                                lista.pop(i-1)
                                lista.pop(i-1)
                            elif key == "I":
                                lista[i-3] = key
                                lista[i-2] = "V"
                                lista.pop(i-1)
                                lista.pop(i-1)
                elif suma == 14:
                    for key in romanos.keys():
                        if lista[i] == key:        
                            if key == "C":
                                lista[i-3] = key
                                lista[i-2] = "D"
                                lista.pop(i-1)
                                lista.pop(i-1)
                            elif key == "X":
                                lista[i-3] = key
                                lista[i-2] = "L"
                                lista.pop(i-1)
                                lista.pop(i-1)
                            elif key == "I":
                                lista[i-3] = key
                                lista[i-2] = "V"
                                lista.pop(i-1)
                                lista.pop(i-1)

        except IndexError:
            pass

    return lista 
#--------------------------------------------------------------------------------------------------

# PROGRAMA

romanos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
romanosOff = dict(sorted(romanos.items(), key=lambda item:item[1], reverse = True))

N = comprobarNumeroInput()
acotarNumero(N)

numeroRomano = []
for key, value in romanosOff.items():

    while (N - value) >= 0:

        N -= value

        numeroRomano.append(key)
print(numeroRomano)

numeroRomanoBien = correccionSegunReglas(numeroRomano)
numeroFinal = "".join(numeroRomanoBien)
print(numeroFinal)
#--------------------------------------------------------------------------------------------------





# MMCCCXLV 2345
# MMDCCLXIII 2763
# MMCMXCIX 2999
# MMMCDLVIII 3458

'''
1. Crear entonno virtual: python3 -m venv "nombre"

Nosotros podemos tener varios proyectos, usar varias librerias 
de python, y de este modo se encapsula el proyecto. 
No quieres librerias que no necesitas en un proyecto.

2. Activar el entorno virtual: source /entorno_virtual/bin/activate
3. Desactivar el entorno virtual: deactivate

4. Instalar Pytest en el entorno virtual: pip3 install pytest

5. Hacer pruebas com pytest: pytest (en consola)
    tiene que tener el nombre test en el nombre del archivo.

Git
1. iniciar repositorio: git init
2. Crear archivo .gitignore para seleccionar que archivos
    de la carpeta no se van a guardar en git.
3. Crear una carpeta con con los requerimientos:
pip3 freeze > requeriments.txt
4. git status, para ver que cosas no están añadidas aún. 
5. git add . -> toma todos los archivos y los guarda
6. git commit -m"nombre" -> para guardar
7. git log -> para ver los commits

8. Subirlo a git ->  git remote add origin https://github.com/AlexLaraMerino/romanos
                     git branch -M main
                     git push -u origin main

'''