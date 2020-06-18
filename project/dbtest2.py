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

    sqlite_Q1 = "select count(*) from divvy_2015 group by from_station_name order by count(*) desc;"
    print("Success")
    print(cursor)
    for row in cursor:
        #engine.say("How many males are used Divvy bikes?")
        #engine.runAndWait()
        print(row[0])
        engine.say(row[0])
        engine.runAndWait()
        print("\n")

    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")