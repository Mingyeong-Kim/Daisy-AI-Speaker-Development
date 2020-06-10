
sentence = "Where is the place where bicycles are used the most"
print(sentence)

word_list=[]

for words in sentence.split(' '):
    if words == ('the' or 'is'):
        continue

    else:
        word_list.append(words)
print(word_list)

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
        sqlquery.insert(1,"count(*) ")
         
strsqlquery= ''.join(sqlquery) + ';'
print(strsqlquery)




'''
sqlquery = []

if word_list[0] == ("Where" or "Which" or "How"):
    sqlquery.append("SELECT ")
	        
if word_list[2] == ('place' or 'station'):
    sqlquery.append("FROM_STATION_NAME ")
    sqlquery.append("from divvy_2015 ")


print(sqlquery)
print(''.join(sqlquery))
word_li = []
word_li = sentence.split(' ')
print(word_li)
print(len(word_li))

word_list=[]

for i in range(0,len(word_li)):    
    if word_li[i] != 'the':
        word_list.append(word_li[i])
print(word_list)

for loop in word_list:
    print(loop)
    if loop == "where":
        sqlquery.append("SELECT ")
    else:
        continue
print(sqlquery)
'''    

'''
    if loop[0] == 'where' or 'which' or 'what':
        sqlquery.append("SELECT ")
    
    
    if word_list[1] == 'place' or 'station':
        sqlquery.append("FROM_STATION_NAME")
        sqlquery.append("from divvy_2015")

print(''.join(sqlquery))
'''

