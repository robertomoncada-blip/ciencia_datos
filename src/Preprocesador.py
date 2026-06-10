class Preprocesador:
    def __init__(self, dataset=None, ruta=None):
        self.dataset = dataset
        self.ruta = ruta

    def cargar_datos(self):
        import pandas as pd
        self.dataset = pd.read_csv(self.ruta)
        return self.dataset