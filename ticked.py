#Emily Torres
class Ticked: #Modelo ticked
    #Variables = Atributos = propiedades
    #Constructor
    #Metodos
    #Declarando Atributos
    id:int = None
    nombre:str = None
    fecha:str = None
    prioridad:str = None
    #Constructor
    def __init__(self, id, nombre, fecha, prioridad):
        self.id = id
        self.nombre = nombre
        self.fecha = fecha
        self.prioridad = prioridad