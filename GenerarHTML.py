from Analizador import *
import webbrowser
entradaData = Analizador()
def Reporte():

    contenido = ''
    htmFile = open( "Reporte"+ ".html", "w")

    htmFile.write("""<!DOCTYPE HTML PUBLIC"
    <html>
    <head>
        <title>REPORTE </title>
     <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>    
    </head>
    <body>
    <div class="container">
  <h3>Nombre : Allan Josue Rafael Morales </h3>
  <h3> Carne : 201709196</h3>    
  <table class="table">
    <thead>
      <tr>
       
        <th>PRODUCTO</th>
        <th>PRECIO</th>
        <th>CANTIDAD</th>
        <th>GANANCIA</th>
        
      </tr>
    </thead>
    """)
    
    htmFile.write(contenido)
    
    htmFile.write("""
      </table>
    </div>
        </body>
        </html>""")
    webbrowser.open("Reporte.html")
    htmFile.close
