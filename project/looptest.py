word_list=['Where', 'is', 'place', 'where', 'bicycles', 'are', 'used', 'most']

sqlquery = []

for loop in word_list:
    if loop == 'What' or loop =='Which' or loop =='Where':
        sqlquery.append("SELECT ")

    elif loop == ('place' or 'station'):
        sqlquery.append("FROM_STATION_NAME ")
        sqlquery.append("from divvy_2015 ")
    
    elif loop == ('where'):
        sqlquery.append("group by FROM_STATION_NAME ")

    elif loop == ('most'):
        sqlquery.append("order by count(*) desc")
        sqlquery.insert(1,"count(*)")
        print('"costomer"')
         

print(''.join(sqlquery) + ';')