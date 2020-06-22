# word_list=['where', 'place','that','people' 'use','the', 'most']
# word_list=['what','is','the','average','time','of','bicycles','for','members']
word_list=['what','average','age',"female",'users']

sqlquery = []

for loop in word_list:
    if loop == 'what' or loop =='which' or loop =='where' or loop == "where's":
        sqlquery.append("select ")

    elif loop == 'bicycles':
        sqlquery.append("from divvy_2015 ")

    elif loop == ('place' or 'station'):
        sqlquery.append("from_station_name ")
        sqlquery.append("from divvy_2015 group by from_station_name ")

    elif loop == 'age':
        sqlquery.append("(birthyear) ")

    elif loop == "female":
        sqlquery.append("from divvy_2015 where gender='Female' ")

    elif loop == 'average':
        sqlquery.append('avg')
         
    elif loop == 'time':
        sqlquery.append('(tripduration) ')

    elif loop == 'each':
        sqlquery.append('from divvy_2015 ')
        sqlquery.append('group by ')

    elif loop == 'for':
        sqlquery.append('where ')

    elif loop == 'members' or loop == 'member':
        sqlquery.append("usertype='Subscriber' ")
       
    elif loop == 'most' or (loop == 'almost'):
        sqlquery.append("order by count(*) desc ")
        sqlquery.append("limit 1 ")
        # sqlquery.insert(1,"count(*), ")

    
strsqlquery= ''.join(sqlquery) + ';'
print(strsqlquery)