import pyttsx3 as tts

class text_to_speech():

    assistant = tts.init()

    def __init__(self):

        self.assistant.setProperty('rate', 175)

        voices = self.assistant.getProperty('voices')
        self.assistant.setProperty('voice', voices[1].id)

    def say(self, text):

        self.assistant.say(text)
        self.assistant.runAndWait()