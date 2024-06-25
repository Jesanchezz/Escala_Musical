from funciones.solicitar_nota import solicitar_nota
from funciones.acomodar_escala import acomodar_escala
from EscalaNatural import EscalaNatural
from EscalaPentatonica import EscalaPentatonica
from EscalaBlues import EscalaBlues

nota1 = EscalaNatural()
nota2 = EscalaPentatonica()
nota3 = EscalaBlues()

text = '''Ingresa 1 para obtener la escala natural 
Ingresa 2 para obtener la escala pentatonica 
Ingresa 3 para obtener la escala de blues
Ingresa 4 para obtener todas las escalas
Ingresa 0 para salir
->  '''


def menu():
    num = 1
    while num > 0:
        num= int(input(text))
        if num == 1:
            print("\tEscala Natural")
            info = solicitar_nota()
            escala_acomodada = acomodar_escala(info[0],info[1])
            print (f"Escala mayor de {info[1]}: {nota1.crear_escala_mayor(escala_acomodada)}")
            print (f"Escala menor de {info[1]}:{nota1.crear_escala_menor(escala_acomodada)}")

        elif num == 2:
            print("\tEscala Pentatonica")
            info = solicitar_nota()
            escala_acomodada = acomodar_escala(info[0],info[1])
            escala_mayor = nota1.crear_escala_mayor(escala_acomodada)
            escala_menor = nota1.crear_escala_menor(escala_acomodada)
            print(f"Escala pentatonica mayor de {info[1]}: {nota2.crear_escala_mayor(escala_mayor)}")
            print(f"Escala pentatonica menor de {info[1]}: {nota2.crear_escala_menor(escala_menor)}")
            
        elif num == 3:
            print("\tEscala de Blues")
            info = solicitar_nota()
            escala_acomodada = acomodar_escala(info[0],info[1])
            escala_mayor = nota1.crear_escala_mayor(escala_acomodada)
            escala_menor = nota1.crear_escala_menor(escala_acomodada)
            pentatonica_mayor = nota2.crear_escala_mayor(escala_mayor)
            pentatonica_menor = nota2.crear_escala_menor(escala_menor)
            print(f"Escala de Blues mayor de {info[1]}: {nota3.crear_escala_mayor(pentatonica_mayor)}")
            print(f"Escala de Blues menor de {info[1]}: {nota3.crear_escala_menor(pentatonica_menor)}")

        elif num == 4:
            info = solicitar_nota()
            escala_acomodada = acomodar_escala(info[0],info[1])

            print("\tTodas las escalas \n")

            escala_mayor = nota1.crear_escala_mayor(escala_acomodada)
            escala_menor = nota1.crear_escala_menor(escala_acomodada)

            print("\tEscala Natural: ")
            print (f"Escala mayor de {info[1]}: {escala_mayor}")
            print (f"Escala menor de {info[1]}:{escala_menor}")

            pentatonica_mayor = nota2.crear_escala_mayor(escala_mayor)
            pentatonica_menor = nota2.crear_escala_menor(escala_menor)

            print("\tEscala Pentatonica: ")
            print(f"Escala pentatonica mayor de {info[1]}: {pentatonica_mayor}")
            print(f"Escala pentatonica menor de {info[1]}: {pentatonica_menor}")

            print("\tEscala de Blues: ")
            print(f"Escala de Blues mayor de {info[1]}: {nota3.crear_escala_mayor(pentatonica_mayor)}")
            print(f"Escala de Blues menor de {info[1]}: {nota3.crear_escala_menor(pentatonica_menor)}")


        elif num > 3:
            print("Numero equivocado, ingresa uno de 1-4")
        
        else:
            print("\tSaliendo del programa")
