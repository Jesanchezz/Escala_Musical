__author__ = 'Frodo'

class EscalaMusical:
    escala = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E','F','F#','G','G#']

    def solicitar_nota(self):
        key = input('Ingresa la nota que desea la escala: ')

        if key.islower():
            key = key.upper()

        elif key not in self.escala:
            print("No existe esa nota")

        index = self.escala.index(key)
        return index, key


    def acomodar_escala(self,index, key):
        if index == 0:
            print("Escala natural de ", key, ":", self.escala)
        else:
            tajada = self.escala[0:index]

            for nota in tajada:
                if nota in self.escala:
                    self.escala.remove(nota)
                for nota in tajada:
                    if nota not in self.escala:
                        self.escala.append(nota)
            print("Escala natural de ", key,": ", self.escala)

        return self.escala


    def crear_escala_mayor(self, escala_acomodada, key):
        nueva_escala_mayor = []

        for i in range(len(escala_acomodada)):
            if (i%2==0 and i<=4):
                nueva_escala_mayor.append(escala_acomodada[i])
            elif (i%2!=0 and i>4):
                nueva_escala_mayor.append(escala_acomodada[i])

        print("Escala mayor de ", key, ":", nueva_escala_mayor)
        return nueva_escala_mayor


    def crear_escala_menor(self, escala_acomodada, key):
        nueva_escala_menor =[]

        for i in range(len(escala_acomodada)):
            if i==0 or i==2:
                nueva_escala_menor.append(escala_acomodada[i])
            elif i%2!=0 and i>=3 and i<8:
                nueva_escala_menor.append(escala_acomodada[i])
            elif i%2==0 and i>=8:
                nueva_escala_menor.append(escala_acomodada[i])

        print("Escala menor de: ", key, ":",  nueva_escala_menor)
        return nueva_escala_menor


    def crear_pentatonica_mayor(self, escala_mayor, key):
        escala_mayor.pop(6)
        escala_mayor.pop(3)
        pentatonica_mayor = escala_mayor
        print("Pentatonica mayor de ", key, ":", pentatonica_mayor)
        return pentatonica_mayor


    def crear_pentatonica_menor(self, escala_menor, key):
        escala_menor.pop(5)
        escala_menor.pop(1)
        pentatonica_menor = escala_menor
        print("Pentatonica menor de ", key, ":", pentatonica_menor)
        return pentatonica_menor


    def crear_escala_blues_mayor(self, pentatonica, key):
        #Nota bemolizada, entre el segundo y tercer grado
        nota_anterior = pentatonica[1]
        index = self.escala.index(nota_anterior)
        nota_blues = self.escala[index+1]
        pentatonica.insert(2, nota_blues)
        print("Escala de blues mayor de", key, ":", pentatonica)


    def crear_escala_blues_menor(self, pentatonica, key):
        #Nota bemolizada, entre el tercer y cuarto grado
        nota_anterior = pentatonica[2]
        index = self.escala.index(nota_anterior)
        nota_blues = self.escala[index+1]
        pentatonica.insert(3, nota_blues)
        print("Escala de blues menor de", key, ":", pentatonica)


nota = EscalaMusical()

info_escala = nota.solicitar_nota()
index = info_escala[0]
nota_escala = info_escala[1]

escala_acomodada = nota.acomodar_escala(index,nota_escala)
escala_mayor = nota.crear_escala_mayor(escala_acomodada, nota_escala)
escala_menor = nota.crear_escala_menor(escala_acomodada, nota_escala)
pentatonica_mayor = nota.crear_pentatonica_mayor(escala_mayor, nota_escala)
pentatonica_menor = nota.crear_pentatonica_menor(escala_menor, nota_escala)
nota.crear_escala_blues_mayor(pentatonica_mayor, nota_escala)
nota.crear_escala_blues_menor(pentatonica_menor, nota_escala)