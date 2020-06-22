'''
author: Mingyeong Kim
'''

import sqlite3
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')   
engine.setProperty('rate', 130) 

try:
    sqliteConnection = sqlite3.connect("C:\\Users\\USER\\divvy.db")
    cursor =sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)

    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)

    engine.say("How many males are used Divvy bikes?")
    engine.runAndWait()
    sqlite_Q1 = "select count(*) from divvy_2015 where gender='Male';"
    rows = cursor.execute(sqlite_Q1)
    print(rows[0])
    engine.say('The answer is',rows)
    engine.runAndWait()
    print("Success")
    '''
    for row in cursor:
        engine.say("How many males are used Divvy bikes?")
        engine.runAndWait()
        print(row)
        speech_row = row
        print(speech_row)
        engine.say(speech_row)
        print("\n")
    '''
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")