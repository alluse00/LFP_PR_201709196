from Analizador import Analizador
from Graficador import Graficador
from GenerarHTML import Reporte

Analizar = Analizador()

class App:
    def __init__(self):
        self.app()

    def app(self):
        while True:
            op = input('''
        -------------------------------
        *********PRACTICA N.1*********
        1. Cargar Data
        2. Cargar Instrucciones
        3. Analizar
        4. Reportes
        5. Salir 
        -------------------------------
        Opción: ''')
            if op == '1':
                Analizar.Leer('.data')
                Analizar.AnalizarData()
            elif op == '2':
                Analizar.Leer('.lfp')
                Analizar.AnalizarInstrucciones()
            elif op == '3':              
                resp = int(Analizar.getData())
                inst = Analizar.getInst(resp)
                nombre = inst['nombre']
                grafica = inst['grafica']
                titulo = inst['titulo']
                titulox = inst['titulox']
                tituloy = inst['tituloy']
                ejex = Analizar.EjeX(resp)
                ejey = Analizar.EjeY(resp)
                graf = Graficador(nombre, grafica, titulo, titulox, tituloy, ejex, ejey)
                graf.Analizar()
            elif op == '4':
                Reporte()
            elif op == '5':
                print('Finalizado')
                break
            else:
                print('Escoger una opción valida')

b = App()
