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

    print(numero_romano) 

entero_a_romano(336)