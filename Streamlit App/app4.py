import streamlit as st  
from gtts import gTTS  

# Gerekli kütüphaneleri içe aktarıyoruz  
# Streamlit → web arayüzü oluşturmak için  
# gTTS (Google Text-to-Speech) → yazıyı sese dönüştürmek için kullanılır

st.title('Text to Speech 🎶')  

# Uygulamanın başlığını belirliyoruz

text = st.text_area('Enter Text')  

# Kullanıcıdan sese dönüştürülecek metni alıyoruz

if text:  
    tts = gTTS(text, lang='tr')  
    # Girilen metni Türkçe dilinde sese dönüştürüyoruz

    tts.save('ses.mp3')  
    # Oluşturulan sesi 'ses.mp3' adlı dosyaya kaydediyoruz

    ses = open('ses.mp3', 'rb')  
    st.audio(ses.read())  
    # Ses dosyasını okuyup uygulama içinde çalıyoruz

# Not: Uygulamayı çalıştırmak için terminalde şu komutu kullanabilirsiniz:
# streamlit run app4.py
