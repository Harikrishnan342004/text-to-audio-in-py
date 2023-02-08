from gtts import gTTS    # --> pip install gtts   
# -->  gtts - " Google text to speech " python library ...


from playsound import playsound           # pip install playsound 
# --> playsound is one of the python laibrary ....

audio = 'speech.mp3'
language = 'en'

sp = gTTS(text = input("enter the sentence = ") , lang = language,slow = False)

sp.save(audio)
playsound(audio)