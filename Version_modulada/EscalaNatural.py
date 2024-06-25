from EscalaMusical import EscalaMusical

class EscalaNatural (EscalaMusical):
    def crear_escala_mayor(self, escala_acomodada):
        nueva_escala_mayor = []

        for i in range(len(escala_acomodada)):
            if (i%2==0 and i<=4):
                nueva_escala_mayor.append(escala_acomodada[i])
            elif (i%2!=0 and i>4):
                nueva_escala_mayor.append(escala_acomodada[i])

        #print("Escala mayor de ", key, ":", nueva_escala_mayor)
        return nueva_escala_mayor


    def crear_escala_menor(self, escala_acomodada):
        nueva_escala_menor =[]

        for i in range(len(escala_acomodada)):
            if i==0 or i==2:
                nueva_escala_menor.append(escala_acomodada[i])
            elif i%2!=0 and i>=3 and i<8:
                nueva_escala_menor.append(escala_acomodada[i])
            elif i%2==0 and i>=8:
                nueva_escala_menor.append(escala_acomodada[i])

        #print("Escala menor de: ", key, ":",  nueva_escala_menor)
        return nueva_escala_menor
