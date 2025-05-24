from abc import ABC, abstractmethod

class RepositorioTareas(ABC):
    @abstractmethod
    def crear(self, tarea):
        pass

    @abstractmethod
    def listar(self):
        pass