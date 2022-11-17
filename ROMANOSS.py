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
    'M':1000,'MM':2000,'MMM':3000,
}



def enteroARomano(N):
    
    N = str(N)
    lista = []
    if len(N) < 4:
        N = "{:0>4s}".format(N)   

    for digito in N:
            lista.append(digito)

    for i in range(len(lista)):
        lista[i] = lista[i]+"0"*((len(lista)-1)-i)
    
    return lista

print(enteroARomano(336))






