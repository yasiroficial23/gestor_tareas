class CrearTareaUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def ejecutar(self, tarea):
        return self.repositorio.crear(tarea)


class ListarTareasUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def ejecutar(self):
        return self.repositorio.listar()