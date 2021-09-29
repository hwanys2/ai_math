import speech_recognition as sr

r =  sr.Recognizer()

def voicetotext():
    with sr.Microphone() as source:

        print('Speak Anything : ')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='ko-KR')
            print('You said : {}'.format(text))
        except:
            text = 'error'
            print('Sorry could not recognize your voice')
    return text

