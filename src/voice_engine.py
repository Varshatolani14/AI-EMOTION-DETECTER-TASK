import pyttsx3

def speak(text, mood="neutral"):
    engine = pyttsx3.init()

    if mood == "happy":
        engine.setProperty("rate", 180)
    elif mood == "sad":
        engine.setProperty("rate", 120)
    else:
        engine.setProperty("rate", 150)

    engine.say(text)
    engine.runAndWait()
