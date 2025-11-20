class BaseModule:
    name = "Base Module"
    description = "Plantilla base para módulos extendidos"

    def run(self, target):
        raise NotImplementedError("Este módulo debe implementar run()")
