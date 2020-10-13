import pythainlp
import codecs
from pythainlp.tag import pos_tag 
from pythainlp.tokenize import word_tokenize
file = codecs.open('./data/fb2.txt','w+','utf-8')

sentence = [""]
words = word_tokenize(sentence, engine="newmm",keep_whitespace=False)

# print(pos_tag(words, engine="unigram", corpus="lst20"))