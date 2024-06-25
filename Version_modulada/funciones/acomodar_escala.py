from escala import escala


def acomodar_escala(index, key):
    if index == 0:
        print("Escala acomodada de ", key, ":", escala)
    else:
        tajada = escala[0:index]

        for nota in tajada:
            if nota in escala:
                escala.remove(nota)
            for nota in tajada:
                if nota not in escala:
                    escala.append(nota)
        print("Escala acomodada de ", key,": ", escala)

    return escala
