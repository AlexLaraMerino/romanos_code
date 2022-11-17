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

N = comprobarInput()

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

