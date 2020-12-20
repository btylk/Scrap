import codecs
file = codecs.open('bully_word.txt','r','utf-8')
linestoken = file.readlines()
tokens_column_number = 3
resulttoken=[]
for x in linestoken:
    resulttoken.append(x.split()[tokens_column_number])
file.close()
print(resulttoken)