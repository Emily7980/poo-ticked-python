#Emily Torres
from ticked import Ticked
class AdministrarTicked:
    tickeds = []
    siguiente_id = 1
    #tickeds.append([13424,'Falla Tecnica','05-03-26',1])
    #tickeds.append([45678,'Sobrecalentamiento','05-03-26',2])
    #print(tickeds)
    def agregar_ticked(self, nombre, fecha, prioridad):
        ticked = Ticked(self.siguiente_id,nombre,fecha,prioridad)
        self.tickeds.append(ticked)
        self.siguiente_id += 1
    def listar_tickeds(self):
        return self.tickeds