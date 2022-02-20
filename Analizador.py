from tkinter import Tk
from tkinter.filedialog import askopenfilename

class Analizador():

    def __init__(self):
        self.text = ""
        self.id_data = 1
        self.id_inst = 1
        self.data = {}
        self.inst = {}

    def Leer(self, extension):
        content = ""
        y = ""
        Tk().withdraw()
        try:
            ruta = askopenfilename(title='Seleccionar archivo',
                                    filetypes=[("Archivos", f"*{extension}"),
                                        ("All Files", "*")])
            print(ruta)
            with open(ruta, encoding='utf-8') as infile:
                content = infile.read().strip()
            print(str(content))

        except:
            print('Error, no seleccionó un archivo')
            return

        content = content.lower()
        com = False
        for letra in content:
            if letra != '\"':
                if (letra != " " and letra != "\n" and letra != "\t") or com:
                    y += letra
            elif not com:
                y += letra
                com = True
            else:
                y += letra
                com = False
        print(y)
        self.text = y

    def AnalizarData(self):
        cadena = self.text
        name = False
        year = False
        par = 0
        datos = False

        name_n = ""
        year_n = ""
        data = ""
        data_list = []

        coriz = False
        cordr = False
        caso = 0
        error = False

        for letra in cadena:
            if name == False:
                if letra != ':':
                    name_n += letra
                else:
                    name = True
            elif year == False:
                if letra != "=":
                    year_n += letra
                else:
                    year = True
            elif letra == '(' and name == True and year == True:
                par += 1
            elif letra == ')' and name == True and year == True and par == True:
                par += 1
                print("Archivo leido correctamente")
                break
            elif datos == False:
                if letra == '[':
                    coriz = True
                elif letra == ']' and coriz == True:
                    cordr = True
                elif coriz == True and cordr == False:
                    if letra == "\"":
                        caso += 1
                    else:
                        data += letra
                elif letra == ";":
                    if coriz == True and cordr == True and caso == 2:
                        lista = data.split(',')
                        if len(lista) != 3:
                            error = True
                            print("Error, no se puede leer el archivo")
                            break
                        try:
                            lista[1] = float(lista[1])
                            lista[2] = float(lista[2])
                        except:
                            error = True
                            print("Error, no se puede leer el archivo")
                            break
                        data_list.append(lista)
                        print(lista)
                        data = ""
                        coriz = False
                        cordr = False
                        caso = 0
            else:
                error = True
                print("Error, no se puede leer el archivo")
                break

        if not error:
            try:
                year_n = int(year_n)
                if year_n != 0 and name_n != "" and data_list != [] and par == 2:
                    self.data[self.id_data] = {'year': year_n, 'mes': name_n, 'productos': data_list}
                    self.id_data += 1
                else:
                    print("Error, no se puede leer el archivo")
                print(self.data)
            except:
                print("Error, no se puede leer el archivo")

    def AnalizarInstrucciones(self):
        cadena = self.text
        inicio = cadena[0:2]
        a = len(cadena) - 3
        b = len(cadena)

        fin = cadena[a:b]
        caso = 0
        entry = False
        aux = {}

        if inicio == "<¿" and fin == '"?>':
            cadena = cadena[2:]
            cadena = cadena[:-2]
            cadena += "$"
            comando = ""
            nombre = ""

            for letra in cadena:
                if letra != ":" and caso == 0:
                    comando += letra
                elif letra == ":":
                    caso = 1
                elif letra == '"':
                    if entry:
                        entry = False
                    else:
                        entry = True
                elif entry == True:
                    nombre += letra
                elif (letra == "," and caso == 1) or letra == "$":
                    if comando == 'nombre':
                        aux[comando] = nombre
                    elif comando == 'grafica':
                        aux[comando] = nombre
                    elif comando == 'titulo':
                        aux[comando] = nombre
                    elif comando == 'titulox':
                        aux[comando] = nombre
                    elif comando == 'tituloy':
                        aux[comando] = nombre
                    else:
                        print("Error, no se reconoce el comando")
                        aux = {}
                        break
                    nombre = ""
                    comando = ""
                    caso = 0
                else:
                    print("Error, no se puede leer este archivo")
                    aux = {}
                    break
            if 'nombre' in aux and 'grafica' in aux:
                self.inst[self.id_inst] = aux
                self.id_inst += 1
                #print(self.inst)
            else:
                print("Error, faltan datos")
        else:
            print("Error, no se puede leer el archivo")

    def EjeX(self, id):
        ejex = []
        if id in self.data:
            for p in self.data[id]['productos']:
                ejex.append(p[0])
        return ejex
            
    def EjeY(self, id):
        ejey = []
        if id in self.data:
            for p in self.data[id]['productos']:
                ejey.append(p[2])
        return ejey

    def getData(self):
        for dato in self.data:
            print(str(dato)+".", self.data[dato]['mes'])
        res = input("Seleccionar una opción: ")
        return int(res)

    def getInst(self, id):
        for id in self.inst:
            return self.inst[id]
