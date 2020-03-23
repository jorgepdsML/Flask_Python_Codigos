from flask import Response
from flask import Flask
from flask import render_template
import threading
import datetime
import time
import cv2
#variable outputFrame
outputFrame = None
#crear objeto lock para proteger los datos de acceso simultaneo
lock = threading.Lock()
#crear objeto flask
app = Flask(__name__)
#crear objeto para manipular la camara web
vs=cv2.VideoCapture(0)
#iniciar el codigo despues de 1 segundo
time.sleep(1)
print("=== INICIO ====")
#uso del decorador route para agregar url
@app.route("/")
def index():
    #regresar el archivo html
    return render_template("index.html")
frameCount=10
#crear hilo N°1
def thread1():
    #camara , lock y outputframe global
    global vs, outputFrame, lock
    total = 0
    #por cada frame
    while True:
        #leer imagen de la camara
        ret,frame = vs.read()
        #cambiar dimensiones
        frame=cv2.resize(frame,(700,500),interpolation=cv2.INTER_AREA)
        #información sobre la fecha
        timestamp = datetime.datetime.now()
        #colocar fecha en la imagen
        cv2.putText(frame, timestamp.strftime(
            "%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
        #context manager lock
        with lock:
            outputFrame = frame.copy()
def generate():
    global outputFrame, lock
    while True:
        # esperar hasta que el objeto lock este desbloqueado
        with lock:
            #outputFrame esta disponible ?
            if outputFrame is None:
                continue
            # CODIFICAR EL FRAME EN FORMATO jpg
            (flag, encodedImage) = cv2.imencode(".jpg", outputFrame)
            # DETERMINAR SI LA CODIFICACIÓN FUE CORRECTA
            if not flag:
                continue
        print("===EJECUTANDOSE ===")
        # yield the output frame in the byte format
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage) + b'\r\n')
@app.route("/video_cv")
def video_cv():
    print("FUNCIÓN VIDEO EJECUTADA")
    # type (mime type)
    return Response(generate(),mimetype="multipart/x-mixed-replace; boundary=frame")
if __name__ == '__main__':
    #======Crear hilo mediante la clase Thread
    #=====target=función a invocar============
    t = threading.Thread(target=thread1)
    #=====modo daemon=True
    t.daemon = True
    #=====iniciar la actividad de hilo===========
    t.start()
    #===iniciar el servidor de flask con ip ============
    app.run(host="192.168.0.4", debug=True,
            threaded=True, use_reloader=False)
vs.release()
print("==========FIN CODIGO======")
