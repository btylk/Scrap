import pythainlp
import codecs
from pythainlp.tag import pos_tag 
from pythainlp.tokenize import word_tokenize
file = codecs.open('./data/data7.txt','r','utf-8')
i=0
# for line in file:
sentence = file.readline()
words = word_tokenize(sentence, engine="newmm",keep_whitespace=False)

print(pos_tag(words, engine="unigram", corpus="lst20"))
