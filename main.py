'''
1-Crear una funcion que pase de entero > 0 y < 4000 a romano
2-Cualquier otra entrada debe dar error
'''

class RomanNumberError( Exception ):
    pass

dic_entero_a_romano={
    1:'I',2:'II',3:'III',
    4:'IV',5:'V',6:'VI',
    7:'VII',8:'VIII',9:'IX',
    10:'X',20:'XX',30:'XXX',
    40:'XL',50:'L',60:'LX',
    70:'LXX',80:'LXXX',90:'XC',
    100:'C',200:'CC',300:'CCC',
    400:'CD',500:'D',600:'DC',
    700:'DCC',800:'DCCC',900:'CM', 
    1000:'M',2000:'MM',3000:'MMM'
}



def entero_a_romano(num:int)->str:

    num = "{:0>4d}".format(num)
    lista = list(num) 
    longitud = len(lista)
    numero_romano=""

    for i in range(longitud):       
        longitud -=1
        lista[i] += "0"*longitud        
        numero_romano += dic_entero_a_romano.get( int(lista[i]),'')

    return numero_romano

entero_a_romano(336)

dic_romano_a_entero = {
 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000   
}

# MDCCXIII -> 1713
# ['M', 'D', 'C', 'C', 'X', 'I', 'I', 'I']
# 1000, 500, 100, 100, 10, 1, 1, 1
# CMXCVII -> 997


def romano_a_entero(rom:str) -> int:
    
    valor_entero=0
    caracter_anterior = ""
    cont_repes = 0
    for caracter in rom:

        if caracter == caracter_anterior:
            cont_repes +=1
        else: cont_repes = 1

        if cont_repes > 3:
            raise RomanNumberError("No se puede repetir el valor más de tres veces")

        if dic_romano_a_entero.get(caracter_anterior, 0) < dic_romano_a_entero.get(caracter):
                valor_entero -= dic_romano_a_entero.get(caracter_anterior, 0)*2

        caracter_anterior = caracter
        valor_entero += dic_romano_a_entero.get(caracter)
    
    return valor_entero



