""" Clase para gestionar los contactos """
from contacto import Contacto
import os

class GestorContactos:

    CONTACTOS = 'contactos.txt'

    def __init__(self):
        """ Definimos los contactos de la clase y cargamos si hay en el archivo """
        self.lista_contactos = []
        # Miramos el archivo y si no existe se crea
        if os.path.isfile(self.CONTACTOS):
            self.lista_contactos = self.obtener_contactos()
        # Si no existe cargamos algunos
        else:
            self.lista_contactos = self.cargar_contactos_iniciales()
    
    def obtener_contactos(self):
        """ Del archivo cargamos los datos de los contactos como contactos """
        lista_contactos = []
        try: 
            with open(GestorContactos.CONTACTOS ,'r+' ,encoding='UTF-8') as archivo:
                for linea in archivo:
                    id_contacto, nombre, apellido, telefono, email = linea.strip().split(',')
                    contacto = Contacto(nombre = nombre, apellido = apellido,
                                        telefono = telefono, email = email)
                    lista_contactos.append(contacto)
        except Exception as e:
            print(f"Hubo un problema al abrir el archivo: {e}")
        return lista_contactos

    def cargar_contactos_iniciales(self):
        print("No hay archivo de contactos, hay que crearlo con algunos vacíos")
        contactos_iniciales = [Contacto('Manuel', 'Pérez', '123456789', 'a@a.es'),
                               Contacto('Antonia', 'Martínez', '323234234', 'b@a.es'),
                               Contacto('Josefina', 'Ruiz', '987654321', 'c@a.es')]
        self.lista_contactos.extend(contactos_iniciales)
        self.guardar_contacto(self.lista_contactos)
        return contactos_iniciales

    def guardar_contacto(self, lista):
        """ Guardamos los snacks en la lista """
        try:
            with open(GestorContactos.CONTACTOS, 'a', encoding = "utf-8") as archivo:
                for contacto in lista:
                    archivo.write(f"{contacto.escribir_contacto()}\n")
        except Exception as e:
            print(f"Error al guardar snacks en el archivo: {e}")

    def add_contacto(self, contacto):
        """" Añadir un contacto """
        self.lista_contactos.append(contacto)
        self.guardar_contacto([contacto])

    def mostrar_contactos(self):
        for contacto in self.lista_contactos:
            print (contacto)

    def get_contactos(self):
        """ Obtener los snacks """
        return self.lista_contactos
    
if __name__ == '__main__':
    contactos = GestorContactos()
    contactos.add_contacto(Contacto('Daniel','Sánchez','000999888','d@d.es'))
    contactos.mostrar_contactos()
