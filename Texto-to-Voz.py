# importar el módulo requerido para convertir texto a voz
import win32com.client

# Llamar al método Dispatch del módulo
# Interactuar con Microsoft Speech SDK para hablar
# La entrada del texto es dada desde el teclado

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while 1:
    print("Introduzca el texto que desea convertir a voz:")
    s = input()
    speaker.Speak(s)