import pyttsx3


def speak(text: str):
    engine = pyttsx3.init()

    for voice in engine.getProperty("voices"):
        if "spanish" in voice.name.lower() or "es" in voice.id.lower():
            engine.setProperty("voice", voice.id)
            break

    engine.setProperty("rate", 160)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()
