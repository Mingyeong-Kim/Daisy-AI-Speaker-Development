
# this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 130) 

# obtain audio from the microphone
r = sr.Recognizer()

with sr.Microphone(device_index=1, chunk_size=1024, sample_rate=48000) as source:
    print("Please wait. Calibrating microphone...")
    # listen for 5 seconds and create the ambient noise energy level   
    r.adjust_for_ambient_noise(source, duration=1) 
    r.energy_threshold = 45000   
    r.dynamic_energy_threshold = True    
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    '''
    sentence = r.recognize_sphinx(audio)
    print(sentence)
    '''
    word_list = []
    word_list = r.recognize_sphinx(audio).split(' ')
    
    if 'the' in word_list:
        print("removing 'the'")
        word_list.remove('the') 

    print(word_list)
    engine.say(r.recognize_sphinx(audio))
    engine.runAndWait()
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))