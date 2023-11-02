import speech_recognition as sr
import pyttsx3
import json
import tkinter as tk
import threading
import time

# Inicializa el reconocimiento de voz y el motor de texto a voz
recognizer = sr.Recognizer()
microphone = sr.Microphone()
engine = pyttsx3.init()

# Función para convertir texto a voz
def texto_a_audio(comando):
    palabra = pyttsx3.init()
    palabra.say(comando)
    palabra.runAndWait()

# Función para capturar audio desde el micrófono y analizar posibles errores
def capturar_voz(reconocer, microfono, tiempo_ruido=1.0):
    if not isinstance(reconocer, sr.Recognizer):
        raise TypeError("'reconocer' no es una instancia de 'Recognizer'")

    if not isinstance(microfono, sr.Microphone):
        raise TypeError("'microfono' no es una instancia de 'Microphone'")

    with microfono as fuente:
        reconocer.adjust_for_ambient_noise(fuente, duration=tiempo_ruido)
        audio = reconocer.listen(fuente)

    respuesta = {
        "suceso": True,
        "error": None,
        "mensaje": None,
    }
    try:
        respuesta["mensaje"] = reconocer.recognize_google(audio, language="es-PE")
    except sr.RequestError:
        respuesta["suceso"] = False
        respuesta["error"] = "API no disponible"
    except sr.UnknownValueError:
        respuesta["error"] = "Habla ininteligible"
    return respuesta

# Función para convertir a una cadena de texto en minúscula el audio enviado por micrófono
def enviar_voz():
    while True:
        palabra = capturar_voz(recognizer, microphone)
        if palabra["mensaje"]:
            break
        if not palabra["suceso"]:
            print("Algo no está bien. No puedo reconocer tu micrófono o no lo tienes enchufado.")
            texto_a_audio("Algo no está bien. No puedo reconocer tu micrófono o no lo tienes enchufado.")
            exit(1)
        print("No pude escucharte, ¿podrías repetirlo?\n")
        texto_a_audio("No pude escucharte, ¿podrías repetirlo?")
    return palabra["mensaje"].lower()

# Carga los datos desde un archivo JSON (por ejemplo, basedatos.json)
with open('basedatos.json', 'r') as archivo:
    datos = json.load(archivo)

# Crear la GUI
def create_gui():
    gui = tk.Tk()
    gui.title("Asistente de Voz")

    def start_listening():
        time.sleep(1)
        texto_a_audio(datos['bienvenida'])
        print("Di tu nombre: ")
        nombre = enviar_voz()
        print("Hola {}. Mucho gusto.".format(nombre))
        texto_a_audio("Hola {}. Mucho gusto.".format(nombre))
        print("{} Ahora voy a explicarte sobre las opciones que tiene este programa. Tienes 3 opciones para escoger.".format(nombre))
        texto_a_audio("{} Ahora voy a explicarte sobre las opciones que tiene este programa. Tienes 3 opciones para escoger.".format(nombre))
        print("\n 1) Aprendizaje\n 2) Tests\n 3) Juegos\n")
        texto_a_audio("Aprendizaje. Tests. Juegos.")
        print("La opción Aprendizaje es donde podrás aprender todo con respecto a la Estructura de un computador. La opción Tests es donde podrás poner en práctica lo que aprendiste mediante exámenes. Y por último, la tercer opción, es Juegos, donde también podrás demostrar lo que aprendiste jugando.")
        texto_a_audio("La opción Aprendizaje es donde podrás aprender todo con respecto a la Estructura de un computador. La opción Tests es donde podrás poner en práctica lo que aprendiste mediante exámenes. Y por último, la tercer opción, es Juegos, donde también podrás demostrar lo que aprendiste jugando.")
        print("¿Qué opción eliges?")
        texto_a_audio("¿Qué opción eliges?")
        time.sleep(0.5)
        texto_a_audio("¿Aprendizaje? ¿Tests? ¿Juegos?")

    tk.Label(gui, text="Bienvenido al Asistente de Voz", font=("Helvetica", 16)).pack()
    tk.Button(gui, text="Empezar a escuchar", command=start_listening, font=("Helvetica", 12)).pack()

    gui.mainloop()

# Ejecutar la GUI en un hilo separado
if __name__ == "__main__":
    threading.Thread(target=create_gui).start()





