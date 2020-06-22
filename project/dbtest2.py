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
    print("\n")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)

    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    print("\n")

    sqlite_Q1 = "select count(*) from divvy_2015 group by from_station_name order by count(*) desc limit 1;"
    print("Success")
    cursor.execute(sqlite_Q1)
    '''
    row = cursor.fetchall()
    print(row[0])
    engine.say(row[0])
    engine.runAndWait()
    print("\n")
    '''
    for row in cursor:
        print(row)
        print("\n")

    engine.say('The answer is {0}'.format(row))
    engine.runAndWait()

    
    cursor.close()
    
    '''
    for row in cursor:
        print(row[0])
        engine.say(row[0])
        engine.runAndWait()
        print("\n")
    '''
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")