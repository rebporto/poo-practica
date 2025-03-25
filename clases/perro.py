

#definiendo la clase (plantilla)
class PerroTeste: #todos los perros que queremos hacer va a salir de esa plantilla
    #metodo contrusctor (__init__)
    def __init__(self, nombre, edad):
        #self es la instancia de perro, lo que va a permitit tener el control de perro
        self.nombre=nombre # al atributo nombre de la instancia, le asignamos "nombre" que nos envian como argumento en el constructor
        self.edad=edad # al atributo edad de la instancia, le asignamos "edad" que nos envian como argumento en el constructor
    def ladra (self): #aqui vamos a poner un metodo, un comportamiento del perro, en ese caso
        return "!Guau!"
#--------------------------------- se termina la classe