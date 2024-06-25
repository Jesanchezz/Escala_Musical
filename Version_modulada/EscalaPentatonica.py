from EscalaMusical import EscalaMusical

class EscalaPentatonica(EscalaMusical):
    def crear_escala_mayor(self, escala_mayor):
        escala_mayor.pop(6)
        escala_mayor.pop(3)
        pentatonica_mayor = escala_mayor
        #print("Pentatonica mayor de ", key, ":", pentatonica_mayor)
        return pentatonica_mayor


    def crear_escala_menor(self, escala_menor):
        escala_menor.pop(5)
        escala_menor.pop(1)
        pentatonica_menor = escala_menor
        #print("Pentatonica menor de ", key, ":", pentatonica_menor)
        return pentatonica_menor
