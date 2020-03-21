#importar herramientas necesarias
from flask import Flask
from flask import render_template
from flask import request
app=Flask(__name__)
#usar decorador route para agregar ruta URL
@app.route('/',methods=["GET"])
def index():
    #método get
    if request.method=="GET":
        #leer lo que se ha enviado
        nombre=request.args.get("fname","No existe1")
        apellido=request.args.get("lname","No existe 2")
        #=======Mostrar datos ingresados en el formulario===
        print("====Los datos recibidos fueron====")
        print("===nombre: ",nombre,"===apellido:",apellido)
        #======================================================
    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)
    print("======FIN CODIGO======")