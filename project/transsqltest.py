
sentence = "Where is the place where bicycles are used the most"
print(sentence)

word_list=[]

for words in sentence.split(' '):
    if words == 'the':
        continue
    else:
        word_list.append(words)
print(word_list)

'''
word_li = []
word_li = sentence.split(' ')
print(word_li)
print(len(word_li))

word_list=[]

for i in range(0,len(word_li)):    
    if word_li[i] != 'the':
        word_list.append(word_li[i])
print(word_list)
'''

sqlquery = ""

for loop in word_list:

    if loop[0] == 'where' or 'which' or 'what':
        sqlquery.append("SELECT ")

    if word_list[1] == 'place' or 'station'
        sqlquery.append("FROM_STATION_NAME")
        sqlquery.append("from divvy_2015")

