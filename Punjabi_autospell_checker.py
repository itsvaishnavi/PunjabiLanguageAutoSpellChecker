import re
import string
import pandas as pd
from inltk.inltk import get_similar_sentences
from inltk.inltk import setup
setup('pa')

df = pd.read_csv (r'pan_words.csv')
Wordslist=df['word'].tolist()

original_text="""ਨੂੰ ਅੰਗਰਜ਼ੀ ਉੱਤਤੇ ਨਿਭਰਰਤਾ ਤੋਂ ਪੂਰਨ ਰੂਪ ਵਿੱਚ ਮਕਤੀ ਮਿਲ ਜਵੇਗੀ। ਯੂਨੀਕੋਡ ਪ੍ਰਣਾਲੀ ਦੀਮਦਦ ਨਾਲ ਕਿਸੇਵੀ ਭਾਸ਼ਾ ਵਿੱਚ ਕੰਪਿਊਟਰ ਪ੍ਰੋਗਰਾਮ ਬਣਾਏ ਜਾ ਸਰਦੇ ਹਨ।

ਇਸ ਨਵੀਂ ਤਕਨੀਕ ਦੇ ਵਿਕਸਿਤ ਹੋਣ ਨਾਲ ਹੁਣ ਕੋ ਈ ਵਿਅਕਤੀਇਕ ਕੰਪਿਊਟਰ ਤੋਂ ਦੂਮਰੇ ਕੰਪਿਊਟਰ ਵਿੱਚ ਗੁਰਮੁਖੀ ਅਕੜਿਆਂ ਦਾ ਸਥਾਨੰਤਰਨ ਬਿਨਾਂ ਕਿਸੇ ਨੁਕਸਾਨ ਦੇ ਅਤੇ ਫੌਂਟ ਦੀ ਚਿੰਤਾ ਕੀਤੇ ਬਿਨਾਂ ਕਰ ਸਕਦਾ ਹੈ।

ਯੂਨੀਕੋਡ ਫੌਂਟ ਵਿਚ ਤਿਆ ਰ ਕੀਤਾ ਡਾਟਾ ਬੇਸ ਵਰਣਾ ਬਹੁਤ ਆਸ਼ਾਨ ਹੈ। ਵਰਤਮਾਨਸਮੇਂ ਵਿੱਚ ਮੋਬਾਇਲ ਫ਼ੋਨਂ , ਪਅਲੇਰ, ਫ਼ੋਨ-ਬਾਕਸ ਮੈਸੇਜ ਬੋਰਡ ਆਦਿ ਪੂਰੀ ਤਰ੍ਹਾਂ ਯੂਨੀਕੋਡ ਅਨੁਕੂਲ ਹੋ ਰਹੇ ਹਨ।

ਯੂ ਨੀਕੋਡ ਅਨੁਕੂਲ ਕਿਸੇ ਵੀ ਕੰਪਿਊਟਰ ਵਿੱਚ"""
modified_text=original_text
text=original_text

print("Given text is==>\n",original_text)

text = re.sub('\[.*?\]', '', text)
text = re.sub('।', '', text)
text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
text = re.sub('\w*\d\w*', '', text)

from inltk.inltk import tokenize
textwords=tokenize(text, "pa")
temp=[]
for i in textwords:
    j=i.replace('▁','')
    temp.append(j)
textwords=temp


errors_list=[]
for word in textwords:
    if word not in Wordslist:
        if word not in errors_list:
            errors_list.append(word)
print("Error==>\n",errors_list)     

print(get_similar_sentences('ਰਜ਼', 1, 'pa'))
suggest_word=[]
for error in errors_list:
    suggest_word.append(get_similar_sentences(error, 1, 'pa'))
    #print("error==",error)
    #s_word=get_similar_sentences(error, 1, 'pa')
    #print(s_word)


print("Suggested words for error words==>\n",suggest_word)

for i in range(0,len(suggest_word)):
    modified_text.replace(suggest_word[i][0],suggest_word[i][1])  

print("Corrected Text==>\n",modified_text)