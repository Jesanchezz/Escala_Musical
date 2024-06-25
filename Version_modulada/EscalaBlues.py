from EscalaMusical import EscalaMusical
from escala import escala

class EscalaBlues(EscalaMusical):
    def crear_escala_mayor(self, pentatonica):
        #Nota bemolizada, entre el segundo y tercer grado
        nota_anterior = pentatonica[1]
        index = escala.index(nota_anterior)
        nota_blues = escala[index+1]
        pentatonica.insert(2, nota_blues)
        #print("Escala de blues mayor de", key, ":", pentatonica)
        return pentatonica


    def crear_escala_menor(self, pentatonica):
        #Nota bemolizada, entre el tercer y cuarto grado
        nota_anterior = pentatonica[2]
        index = escala.index(nota_anterior)
        nota_blues = escala[index+1]
        pentatonica.insert(3, nota_blues)
        #print("Escala de blues menor de", key, ":", pentatonica)
        return pentatonica