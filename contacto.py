""" Clase contacto define los contactos con su información """

class Contacto:
    
    contador = 0

    def __init__(self, nombre = None, apellido = None,
                 telefono = None, email = None):
        Contacto.contador += 1
        self.id = Contacto.contador
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"""Contacto {self.id}:
    Nombre: {self.nombre}
    Apellidos: {self.apellido}
    Teléfono: {self.telefono}
    E-mail: {self.email}"""

    def escribir_contacto(self):
        return f"{self.id},{self.nombre},{self.apellido},{self.telefono},{self.email}"

if __name__ == "__main__":
    contacto = Contacto(nombre ='Enrique', apellido = 'Puertas',
                        telefono = '637023360', email = 'puertasman@gmail.com')
    print(contacto)
    contacto.escribir_contacto()