import streamlit as st  
from textblob import TextBlob  

# Gerekli kütüphaneleri içe aktarıyoruz  
# Streamlit → web arayüzü oluşturmak için  
# TextBlob → metin analizi (özellikle duygu analizi) için kullanılır

st.title('Sentiment Analyzer 💬')  

# Uygulamanın başlığını oluşturuyoruz

text = st.text_area('Enter Text')  

# Kullanıcıdan duygu analizi yapılacak metni alıyoruz

if text:  
    polarity = TextBlob(text).sentiment.polarity  
    # Polarity (duygusal kutupluluk) değerini hesaplıyoruz  
    # Değer -1 ile 1 arasında olur: negatif, nötr veya pozitif duyguyu temsil eder

    if polarity > 0.10:  
        sentiment = 'Positive'  
    elif polarity < -0.10:  
        sentiment = 'Negative'  
    else:  
        sentiment = 'Neutral'  

    st.write('The sentiment is:', sentiment)  

# Kullanıcı metin girdiğinde analiz yapılır ve sonucu ekranda gösterilir

# Not: Uygulamayı terminalden çalıştırmak için şu komutu kullanabiliriz:
# streamlit run app3.py
