from abc import ABC, abstractmethod

class BaseModule(ABC):
    """
    Clase base abstracta para todos los módulos del Recon Suite.
    Asegura una estructura obligatoria y estandarizada.
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.results = None

    @abstractmethod
    def run(self, target: str):
        """ Ejecuta el módulo contra un objetivo """
        pass

    def return_dict(self) -> dict:
        return {
            "module": self.name,
            "description": self.description,
            "results": self.results
        }
