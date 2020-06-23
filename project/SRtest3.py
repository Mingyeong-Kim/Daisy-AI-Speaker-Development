
# this example requires PyAudio because it uses the Microphone class
import speech_recognition as sr
import pyttsx3
import sqlite3

engine = pyttsx3.init()
rate = engine.getProperty('rate')               
engine.setProperty('rate', 130) 

engine.say("Hi, I'm Daisy")
engine.runAndWait()
print("Hi, I'm Daisy")

# obtain audio from the microphone
r = sr.Recognizer()

with sr.Microphone(device_index=1, chunk_size=1024, sample_rate=48000) as source:
    print("Please wait. Calibrating microphone...")
    # listen for 5 seconds and create the ambient noise energy level   
    r.adjust_for_ambient_noise(source, duration=1) 
    r.energy_threshold = 1000
    r.dynamic_energy_threshold = True
    r.dynamic_energy_adjustment_damping = 0.15
    r.dynamic_energy_adjustment_ratio = 1.5
    r.pause_threshold = 0.8

    engine.say("Say something!")
    engine.runAndWait()
    print("Say something!")

    audio = r.listen(source)

# recognize speech using Sphinx

try:
    
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    
    word_list = []
    
    for words in r.recognize_sphinx(audio).split(' '):
        if (words == 'the') or (words =='is') or (words == 'a') or (words == 'of'):
            continue
        else:
            word_list.append(words)
    print(word_list)

    def avg():
        for i in range(len(word_list)):
            if word_list[i]=='average':
                if word_list[i+1] == 'time':
                    return('avg(tripduration) ')
                elif word_list[i+1] == 'age':
                    return('avg(tripduration) ')
    

    sqlquery = []

    for loop in word_list:

        if loop == 'what' or loop =='which' or loop =='where' or loop == "where's" or loop == 'how':
            sqlquery.append("select ")

        elif loop == ('place' or 'station'):
            sqlquery.append("from_station_name ")
            sqlquery.append("from divvy_2015 group by from_station_name ")

        elif loop == 'age':
            sqlquery.append("(birthyear) ")

        elif loop == 'average':
            sqlquery.append(avg())
            
        elif loop == 'time':
            sqlquery.append('(tripduration) ')

        elif loop == 'each':
            sqlquery.append('from divvy_2015 ')
            sqlquery.append('group by ')

        elif loop == 'members' or loop == 'member':
            sqlquery.append("from divvy_2015 where usertype='Subscriber' ")
        
        elif loop == 'most' or (loop == 'almost'):
            sqlquery.append("order by count(*) desc ")
            sqlquery.append("limit 1 ")
            # sqlquery.insert(1,"count(*), ")
        
        elif loop == ('many'):
            sqlquery.append("count(*) ")

        elif loop == ('customer'):
            sqlquery.append('from divvy_2015 where usertype="Customer" ')
                
        elif loop == ('subscriber'):
            sqlquery.append('from divvy_2015 where usertype="Subscriber" ')
                
        elif loop == 'female' or (loop == 'females'):
            sqlquery.append('from divvy_2015 where gender="Female"')


    
    strsqlquery= ''.join(sqlquery) + ';'
    print(strsqlquery)

    # engine.say(r.recognize_sphinx(audio))
    # engine.say(strsqlquery)

    sqliteConnection = sqlite3.connect("C:\\Users\\USER\\divvy.db")
    cursor =sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)

    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)

    # sqlite_Q1 = "select count(*) from divvy_2015 where gender='Male';"
    cursor.execute(strsqlquery)
    '''
    row = cursor.fetchall()
    print(row[0])
    engine.say(row[0])
    engine.runAndWait()
    print("\n")
    '''
    
    # cursor.fetchall()
    for row in cursor:
        print(row)
        engine.say('The answer is {0}'.format(row))
        engine.runAndWait()
        print("\n")
    
    cursor.close()

except sr.UnknownValueError:
    print("Sphinx could not understand audio")
    engine.say("Sphinx could not understand audio.Could you tell me question again?")
    engine.runAndWait()

except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
    engine.say("I can't understand your question. Could you tell me question again?")
    engine.runAndWait()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
    engine.say("I can't understand your question. Could you tell me question again?")
    engine.runAndWait()

finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")