import speech_to_text as stt
import text_to_speech as tts
import execCommand as assistant_exec

assistant_stt = stt.speech_to_text()
assistant_tts = tts.text_to_speech()

assistant_tts.say('Hello, I am Corvo.')

while True:
    assistant_tts.say('How may I help you?')

    while not assistant_stt.text:
        assistant_stt.listen_to_microphone()
        assistant_stt.convert_to_text()

    to_say = assistant_exec.execute(assistant_stt.text)
    assistant_tts.say(to_say)

    if 'exit' or 'that would be all' in assistant_stt.text:
        break