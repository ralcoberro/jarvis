import openai
import speech_recognition as sr
import pyttsx3

# Configura tu API Key
openai.api_key = "YOUR-API-KEY"

# Configura el motor de síntesis de voz
engine = pyttsx3.init()

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

def obtener_respuesta(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

def escuchar_audio():
    # Usa el micrófono para escuchar
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            # Reconocer el audio utilizando Google Speech Recognition
            texto = r.recognize_google(audio, language='es-ES')
            if texto.lower() == "jarvis":
                print("Pregunta...")
                try:
                    audio = r.listen(source)
                    texto = r.recognize_google(audio, language='es-ES')
                    return texto
                except sr.UnknownValueError:
                    print("No se entendió la consulta")
                    return ""
        except sr.UnknownValueError:
            print("No se entendió el audio.")
            return ""
    #except sr.RequestError as e:
    #    print(f"Error al conectarse al servicio de reconocimiento de voz: {e}")
     #   return ""

def main():
    while True:
        print("Deci Jarvis para empezar a grabar tu pregunta")
        pregunta = escuchar_audio()
        if pregunta:
            respuesta = obtener_respuesta(pregunta)
            print(f"Respuesta: {respuesta}")
            hablar(respuesta)

if __name__ == "__main__":
    main()
