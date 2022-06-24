from unittest import result
from main import *

def test_count_char():
    input = ["blabla", "45218552", "Bonjour!!!"]
    expected = [6,8,10]
    result = [count_char(password) for password in input]
    assert expected == result

def test_check_invalid_special_char():
    """
        banned char: '@', '=', '+', ' '
    """
    input = ['Bonjour',"77788885", 'Bonjour@', 'blabla oui', 'blabla=',"bonjou+r"]
    expected = [True, True, False, False, False, False]
    result = [check_invalid_special_char(password) for password in input]
    assert expected == result

def test_check_if_maj():
    input = ["Bonjour", "bonjour","bonJour","bonjouR","BONjour","12313656"]
    expected = [True, False, True, True, True, False]
    result = [check_if_maj(password) for password in input]
    assert expected == result

def test_check_if_special_char():
    """
        banned char: '!', '#', ';'
    """
    input = ["Bonjour!", "bonjour#",";bonJour","#bonjouR","@BONjour","12313656", "bonjour"]
    expected = [True, True, True, True, False, False, False]
    result = [check_if_special_char(password) for password in input]
    assert expected == result

def test_check_if_password_valid():
    input = ["Bonjourrrrrr@", "bonjourrrr", "Bonjoureffr!",'bonjourffr!', 'Bonjo urrrr!','rrrrRrrrrrr!']
    expected = [False, False, True, False, False, True]
    result = [check_if_password_valid(password) for password in input]
    assert expected == result
