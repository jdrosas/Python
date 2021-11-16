# Programación orientada a objetos (POO o OOP)

# Definir una clase (nolde para crear mas objetos de ese tipo
# (coche) cib caracacteristicas similares) 

class Coche:

    # Atributos o propiedades (variables)
    # Caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Metodos, son acciones que hace el objeto (coche) (funciones)
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    
# fin definicio clase

# Crear objeto / Instaciar la clase
coche = Coche()

print("----------------COCHE 1--------------------")

coche.setColor("Amarillo")
coche.setModelo("Murcielago")

print(coche.marca, coche.getModelo(), coche.getColor())
print("Velocidad actual: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Velocidad nueva: ", coche.getVelocidad())

print("----------------COCHE 2--------------------")
# Crear mas objetos

coche2 = Coche()
coche2.setColor("Verde")
coche2.setModelo("Gallardo")

print(coche2.marca, coche2.getModelo(), coche2.getColor())

print(type(coche2))