"""En este mini-proyecto la idea es covertir la camara de un dispositivo en 
    una camara de vigilancia, para llevar a cabo el proceso lo inicial es 
    instalar opencv para python
"""
#ya instalado opencv lo importamos para poder usar la libreria
import cv2
"""tenemos una url que para poder obtenerla lo inicial es descargar
    la app llamada ip webcam, al iniciar el server, nos brinda una 
    direccion ip, que sera la que usaremos en este caso.
"""
url ="https://192.168.1.3:8080/video" 
"""Definimos el atributo que llevara la clase captura de video mediante
    la libreria de opencv y en su constructor ira la url de acceso al dispositivo
"""
videocap = cv2.VideoCapture(url)
"""Se define el ciclo while donde van las opciones de la ejecucion, por tanto
    lo inicial es que este abierto
"""
while(
    videocap.isOpened()):
    """en este punto lo que se declara en el atributo camera
    es la lectura de la secuencia de imagenes del atributo videocap
    declarada antes y se le asigna la medida de la ventana que
    presenta la imagen"""
    camera, frame = videocap.read()
    try:
        cv2.imshow('Video',
                    cv2.resize(frame, (1200,800)))
        """en este caso se le asigna un tiempo de un milisegundo por imagen en la secuencia"""
        key = cv2.waitKey(1)
        """se declara un if en donde se ponen las opciones 
        en el primer caso es que con "q" se corte la ejecicion
        y en caso de que ocurra un error se envie el mensaje fin de conexion"""
        if key == ord('q'):
            break
    except cv2.error:
        print("end conection")
        break
    """por ultimo se hace una destruccion de todas las ventanas en ejecucion"""
cv2.destroyAllWindows()