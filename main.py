import streamlit as st 
#pip install textblob
from textblob import TextBlob 
#https://pypi.org/project/googletrans/3.1.0a0/
#pip install googletrans==3.1.0a0
from googletrans import Translator 


st.title("Hello Roney env")
st.subheader("Kita akan belajar textblob dan google trans")

#textblob
# ingat, textblob tidak baik jika digunakan untuk bahasa indonesia
st.write(" Real Time Sentiment Analyzer ")
inputKalimat = st.text_input("Masukkan Kalimat Bahasa Indonesia...")
#google translate
translator = Translator()
translation = translator.translate(inputKalimat, dest="en")
sentence = translation.text

score = TextBlob(sentence).sentiment.polarity
btn = st.button("Cek Sentimen Analisis")
if btn:
  if score==0:st.write("Neutral 😐")
  elif score<0:st.write("Negative 😫")
  elif score>0:st.write("Positive 😀")

st.write(sentence)