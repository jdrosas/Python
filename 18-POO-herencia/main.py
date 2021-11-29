import clases

persona = clases.Persona()
persona.setNombre("Juan David")
persona.setApellidos("Rosas Diaz")
persona.setAltura("220cm")
persona.setEdad("78 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())
print("-------------------------------------")

Informatico = clases.Informatico()
Informatico.setNombre("Juan")
Informatico.setApellidos("Rosas")

print(f"El informatico es: {Informatico.getNombre()} {Informatico.getApellidos()}")
print(Informatico.getLenguajes())
print(Informatico.caminar())
print(Informatico.experiencia)

print("-------------------------------------")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Juan D")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())