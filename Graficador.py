import matplotlib.pyplot as grafic

class Graficador():

    def __init__(self, nombre, grafica, titulo = "", titulox = "", tituloy= "", ejex = [], ejey = []):
        self.nombre = nombre
        self.grafica = grafica
        self.titulo = titulo
        self.titulox = titulox
        self.ejex = ejex
        self.tituloy = tituloy
        self.ejey = ejey

    def Analizar(self):
        grafic.bar(self.ejex, self.ejey)
        grafic.xlabel(self.titulox)
        grafic.ylabel(self.tituloy)
        grafic.title(self.titulo)
        grafic.show()