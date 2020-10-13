import sys
import codecs
file = codecs.open('fb2.txt','w+','utf-8')
for line in file:
    if not line.isspace():
        file.write()