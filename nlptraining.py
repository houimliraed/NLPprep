#importing needed libraries
import nltk
from nltk.stem import PorterStemmer
import regex

text = "whatever u wouln't say is next with a space after this," ""
print("******************* word tokenizer **********************")
# better word tokenizers example of use compared to regex
regex_text = regex.split("[\s\.\,]",text)
print(regex_text)

nltk_text = nltk.word_tokenize(text)
print(nltk_text)
#steeming 
print("****************** Stemming *****************************")
stemmer = PorterStemmer()
