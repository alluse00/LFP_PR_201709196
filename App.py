from Analizador import Analizador
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
                Analizar.Leer()
                Analizar.AnalizarData()
            elif op == '2':
                pass
            elif op == '3':
                pass
            elif op == '4':
                pass
            elif op == '5':
                print('Finalizado')
                break
            else:
                print('Escoger una opción valida')

b = App()
