import clases

persona = clases.Persona()
persona.setNombre("Juan David")
persona.setApellidos("Rosas Diaz")
persona.setAltura("220cm")
persona.setEdad("78 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())