# word_list=['what','is','the','average','time','of','bicycles','for','members']
word_list=['what','average','age',"female",'users']

sqlquery = []
avg_list = []

def avg():
    for i in range(len(word_list)):
        if word_list[i]=='average':
            print(i)
            print(word_list[i+1])
            if word_list[i+1] == 'time':
                return('avg(tripduration) ')
            elif word_list[i+1] == 'age':
                return('avg(birthyear) ')

avg()
avg_list.append(avg())
print(avg_list)