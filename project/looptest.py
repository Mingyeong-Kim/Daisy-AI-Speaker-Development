# word_list=['where', 'place','that','people' 'use','the', 'most']
# word_list=['what','is','the','average','time','of','bicycles','for','members']
word_list=['what','average','age',"female",'users']
# word_list=['how', 'many', 'customer','rent', 'bicycles']
# word_list=['how', 'many', 'subscriber','rent', 'bicycles']
# word_list=['how', 'many', 'females','rent', 'bicycles']

sqlquery = []
avg_list = []


def avg():
    for i in range(len(word_list)):
        if word_list[i]=='average':
            if word_list[i+1] == 'time':
                return('avg(tripduration) ')
            elif word_list[i+1] == 'age':
                return('avg(tripduration) ')

for loop in word_list:

    if loop == 'what' or loop =='which' or loop =='where' or loop == "where's" or loop == 'how':
        sqlquery.append("select ")

    elif loop == ('place' or 'station'):
        sqlquery.append("from_station_name ")
        sqlquery.append("from divvy_2015 group by from_station_name ")


    elif loop == 'average':
        sqlquery.append(avg()) 

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

