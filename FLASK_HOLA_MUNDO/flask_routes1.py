'''
============== BRAINTELS LABS ==========
ARTIFICIAL INTELLIGENCE,IMAGE PROCESSING & EMBEDDED SYSTEMS
'''
#importar herramientas necesarias
from flask import Flask
app = Flask(__name__)
'''
decorador route()
tiene como objetivo vincular la URL con una función 
'''
contenido="""=================== BrainTels Labs============
Hola mundo en Flask y python .
Artificial Intelligence , Image processing & embedded systems

"""
@app.route("/")#Vincular URL home con la función home()
def home():
    return contenido
if __name__=="__main__":
    #realizar el despligue en host="tu ip" o por defecto en 127.0.0.1
    app.run(debug=True,host="192.169.5.15")
