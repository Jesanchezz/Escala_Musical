from escala import escala


def solicitar_nota():
    key = input('Ingresa la nota que desea la escala: ')

    if key.islower():
        key = key.upper()

    elif key not in escala:
        print("No existe esa nota")

    index = escala.index(key)
    return index, key