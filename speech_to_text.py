import speech_recognition as sr


class speech_to_text():

    def save_in_file(self):
        print('\nCorvo: Saving to File...')

        audio_data = self.audio.get_wav_data()

        with open('recordings/recording.wav', 'w+b')  as record_file:
            record_file.write(audio_data)

        print('Corvo: Saved\n')


    def  listen_in_background(self):
        pass


    def listen_to_microphone(self, saveToFile=None):

        with sr.Microphone() as source:
            self.speech_rec.adjust_for_ambient_noise(source)
            self.speech_rec.pause_threshold = 0.5
            print('\nCorvo: Listening...')
            self.audio =  self.speech_rec.listen(source)

        print('Corvo: Done Listening\n')

        if saveToFile:
            self.audio_file = save_in_file(self.audio)

        return True


    def convert_to_text(self):

        try:
            self.text = self.speech_rec.recognize_google(self.audio)
            print('Corvo: Converting to Text...')
            print('Speaker: ' + self.text)
        except sr.UnknownValueError:
            print('Corvo: What\'s that? I did not recognize it.')


    def  __init__(self):

        self.speech_rec = sr.Recognizer()
        self.text = False