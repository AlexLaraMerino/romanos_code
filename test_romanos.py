from main import entero_a_romano, romano_a_entero, RomanNumberError
import pytest

def test_entero_a_romano():
    assert entero_a_romano(336) == "CCCXXXVI"

def test_entero_a_romano():
    assert entero_a_romano(2022) == "MMXXII"

def test_romano_a_entero(): 
    assert romano_a_entero("MDCCXIII") == 1713

def test_romano_a_entero(): 
    assert romano_a_entero("I") == 1

def test_romano_a_entero_restar_izquierda():
    assert romano_a_entero("IV") == 4

def test_romano_a_entero_no_repetir_mas_de_tres():
    with pytest.raises( RomanNumberError) as exceptionInfo:
        romano_a_entero("LIIII")
    assert str(exceptionInfo.value) == "No se puede repetir el valor más de tres veces"