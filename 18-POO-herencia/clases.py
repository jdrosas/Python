# Herencia: es la posibilidad de compartir atributos y metodos
# entre clases. Y que difenrentes clases hereden de otras. 

class Persona:
    """
    nombre
    apellidos
    altura
    edad
    """

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos
    
    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos
        
    def setAltura(self, altura):
        self.altura = altura
        
    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dromir(self):
        return "Estoy durmiendo"