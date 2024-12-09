#importing needed libraries
import nltk
import regex

text = "whatever u wouln't say is next with a space after this," ""
# better word tokenizers example of use compared to regex
regex_text = regex.split("[\s\.\,]",text)
print(regex_text)
print("***********************************************")
nltk_text = nltk.word_tokenize(text)
print(nltk_text)
