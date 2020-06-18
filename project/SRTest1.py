
# this example requires PyAudio because it uses the Microphone class
import speech_recognition as sr
import pyttsx3
import sqlite3

engine = pyttsx3.init()
rate = engine.getProperty('rate')               
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
            sqlquery.append("select")

        elif loop == ('place' or 'station'):
            # sqlquery.append("FROM_STATION_NAME ")
            sqlquery.append("from divvy_2015 ")
            sqlquery.append("group by from_station_name ")

        elif loop == ('most'):
            sqlquery.append("order by count(*) desc ")
            sqlquery.insert(1,"count(*) ")

    
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
    print("Success")

    for row in cursor:
        print(row)
        print(row[0])
        engine.say(row[0])
        engine.runAndWait()
        print("\n")

    cursor.close()

    engine.runAndWait()
except sr.UnknownValueError:
    print("Sphinx could not understand audio")

except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")