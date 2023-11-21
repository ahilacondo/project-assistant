import speech_recognition as sr
import pyttsx3
import time
import sys
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json

# Función para convertir cadenas de texto a audio y reproducirlas
def texto_a_audio(comando):
    palabra = pyttsx3.init()
    palabra.say(comando)
    palabra.runAndWait()

# Función para capturar voz desde el micrófono y analizar posibles errores
def capturar_voz(reconocer, microfono, tiempo_ruido=3.0):
    if not isinstance(reconocer, sr.Recognizer):
        raise TypeError("'reconocer' no es de la instacia 'Recognizer'")

    if not isinstance(microfono, sr.Microphone):
        raise TypeError("'reconocer' no es de la instacia 'Recognizer'")
    
    with microfono as fuente:
        reconocer.adjust_for_ambient_noise(fuente, duration = tiempo_ruido)
        print("iniciando reconcimiento")
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
        respuesta["error"] = "Habla inteligible"
    print("termino reconocimiento")
    return respuesta

# Función para convertir a una cadena de texto en minúscula el audio enviado por el micrófono
def enviar_voz():
    while (1):
        palabra = capturar_voz(recognizer, microphone)
        if palabra["mensaje"]:
            break
        if not palabra["suceso"]:
            print("Algo no está bien. No puedo reconocer tu micrófono o no lo tienes enchufado. <", nombre["error"],">")
            texto_a_audio("Algo no está bien. No puedo reconocer tu micrófono o no lo tienes enchufado.")
            exit(1)
        print("No pude escucharte, ¿podrias repetirlo?\n")
        texto_a_audio("No pude escucharte, ¿podrias repetirlo?")
    return palabra["mensaje"].lower()

# Función para manejar la continuación del programa
def manejar_continuacion():
    print("¿Quieres seguir aprendiendo?")
    texto_a_audio("¿Quieres seguir aprendiendo?")
    time.sleep(0.5)
    print("Responde con:\n1) Está bien\n2) No gracias")

    respuesta = enviar_voz()
    print("Tu respuesta " + respuesta)

    if respuesta == "está bien":
        # ELEGIMOS CON QUÉ OPCIÓN SEGUIR
        print("Elige la opción que desees aprender: ")
        texto_a_audio("Elige la opción que desees aprender: ")
        print("\n1) Aprendizaje\n2) Test\n3) Juegos\n")
    elif respuesta == "no gracias":
        print("Oh. es una lástima. En ese caso nos veremos en otra ocasión.")
        texto_a_audio("Oh. es una lástima. En ese caso nos veremos en otra ocasión.")
        time.sleep(0.5)
        print("Espero que hayas aprendido mucho sobre este tema. Hasta luego.")
        texto_a_audio("Espero que hayas aprendido mucho sobre este tema. Hasta luego.")
        exit(0)
    else:
        print(nombre + " creo que no has respondido con alguna de las instrucciones indicadas anteriormente")
        texto_a_audio(nombre + " creo que no has respondido con alguna de las instrucciones indicadas anteriormente")
        print("Responde con:\n1) Está bien\n2) No gracias")

# Función principal del programa
def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        texto_a_audio(datos['bienvenida'])
        print("Di tu nombre: ")
        nombre = enviar_voz()
        print("Hola {}. Mucho gusto.".format(nombre))
        texto_a_audio("Hola {}. Mucho gusto.".format(nombre))

        while True:
            print("{} ¿Quieres seguir aprendiendo?".format(nombre))
            texto_a_audio("{} ¿Quieres seguir aprendiendo?".format(nombre))
            time.sleep(0.5)
            print("Responde con:\n1) Está bien\n2) No gracias")
            respuesta = enviar_voz()
            print("Tu respuesta " + respuesta)

            if respuesta == "está bien":
                print("Elige la opción que desees aprender: ")
                texto_a_audio("Elige la opción que desees aprender: ")
                print("\n1) Aprendizaje\n2) Test\n3) Juegos\n")
                texto_a_audio("Aprendizaje. Tests. Juegos.")
                print("La opción Aprendizaje es donde podrás aprender todo con respecto a la Estructura de un computador. La opción Tests es donde podrás poner en práctica lo que aprendiste mediante exámenes. Y por último, la tercer opción, es Juegos, donde también podrás demostrar lo que aprendiste jugando.")
                texto_a_audio("La opción Aprendizaje es donde podrás aprender todo con respecto a la Estructura de un computador. La opción Tests es donde podrás poner en práctica lo que aprendiste mediante exámenes. Y por último, la tercer opción, es Juegos, donde también podrás demostrar lo que aprendiste jugando.")
                print("¿Qué opción eliges?")
                texto_a_audio("¿Qué opción eliges?")
                time.sleep(0.5)
                texto_a_audio("¿Aprendizaje? ¿Tests? ¿Juegos?")

                while True:
                    respuesta = enviar_voz()
                    print("Tu respuesta " + respuesta)

                    if respuesta == "aprendizaje":
                        print("Elegiste la opcion APRENDIZAJE.")
                        texto_a_audio("Elegiste la opcion APRENDIZAJE.")
                        # ... (Tu código para la opción de aprendizaje)

                    elif respuesta == "test":
                        print("Elegiste la opción TEST.")
                        texto_a_audio("Elegiste la opción TEST.")
                        # ... (Tu código para la opción de test)

                    elif respuesta == "juegos":
                        print("Elegiste la opción JUEGOS.")
                        texto_a_audio("Elegiste la opción JUEGOS.")
                        # ... (Tu código para la opción de juegos)

                    else:
                        print(nombre + " creo que no has respondido con alguna de las instrucciones indicadas anteriormente")
                        texto_a_audio(nombre + " creo que no has respondido con alguna de las instrucciones indicadas anteriormente")
                        print("Responde con:\n1) Aprendizaje\n2) Test\n3) Juegos\n")

            elif respuesta == "no gracias":
                print("Oh. es una lástima. En ese caso nos veremos en otra ocasión.")
                texto_a_audio("Oh. es una lástima. En ese caso nos veremos en otra ocasión.")
                time.sleep(0.5)
                print("Espero que hayas aprendido mucho sobre este tema. Hasta luego.")
                texto_a_audio("Espero que hayas aprendido mucho sobre este tema. Hasta luego.")
                exit(0)

            else:
                print(nombre + " creo que no has respondido con alguna de las instrucciones indicadas anteriormente")
                texto_a_audio(nombre + " creo que no has respondido con alguna de las instrucciones indicadas anteriormente")
                print("Responde con:\n1) Está bien\n2) No gracias")

if __name__ == "__main__":
    main()
