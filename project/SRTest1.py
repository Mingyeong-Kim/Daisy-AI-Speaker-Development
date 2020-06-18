
# this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
engine.setProperty('rate', 130) 
# obtain audio from the microphone
r = sr.Recognizer()

with sr.Microphone(device_index=1, chunk_size=1024, sample_rate=48000) as source:
    print("Please wait. Calibrating microphone...")
    # listen for 5 seconds and create the ambient noise energy level   
    r.adjust_for_ambient_noise(source, duration=1) 
    r.energy_threshold = 1000
    r.dynamic_energy_threshold = True
    r.dynamic_energy_adjustment_damping = 0.15
    r.dynamic_energy_adjustment_ratio = 2.0
    r.pause_threshold = 0.8
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
    
    for words in r.recognize_sphinx(audio).split(' '):
        if (words == 'the') or (words =='is'):
            continue
        else:
            word_list.append(words)
    print(word_list)

    sqlquery = []

    for loop in word_list:
        if loop == 'what' or loop =='which' or loop =='where' or loop == "where's":
            sqlquery.append("SELECT ")

        elif loop == ('place' or 'station'):
            # sqlquery.append("FROM_STATION_NAME ")
            sqlquery.append("from divvy_2015 ")
            sqlquery.append("group by FROM_STATION_NAME ")

        elif loop == ('most'):
            sqlquery.append("order by count(*) desc ")
            sqlquery.insert(1,"count(*) ")

    
    strsqlquery= ''.join(sqlquery) + ';'
    print(strsqlquery)
    
    # engine.say(r.recognize_sphinx(audio))
    # engine.say(strsqlquery)

    engine.runAndWait()
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))