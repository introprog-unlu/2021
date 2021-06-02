#################################################
# hw0.py
#
# Nombre:
# DNI:
#################################################

#################################################
# Funciones que tenés que programar
#################################################

def hello_world():
# Modificar este código para que devuelva el string "Hello World!"
    
    return 1

#################################################
# Funciones de Test (no modificar)
#################################################

def test_hello():
    print('Testeando testHelloWorld()... ', end='')
    assert hello_world() == "Hello World!"
    print('Pasó!')

#################################################
# main
#################################################

def main():
    test_hello()   

if __name__ == '__main__':
    main()
