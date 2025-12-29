# Tek satırda web sayfası oluşturmak için Streamlit'i import ediyoruz
import streamlit as st
import pandas as pd
import plotly.express as px

# Sayfanın başlığını belirliyoruz
st.title(':balloon: MLOps Streamlit App :kite:')

# CSV dosyasını okuyoruz
df = pd.read_csv('prog_languages_data.csv')

# DataFrame’i ekranda gösteriyoruz
st.write(df)

# 1️⃣ Plotly Express ile Pasta Grafiği (Pie Chart)
fig = px.pie(df, values='Sum')
st.plotly_chart(fig)

# 2️⃣ Çubuk Grafik (Bar Chart)
fig2 = px.bar(df, x='lang', y='Sum')
st.plotly_chart(fig2)

# Kullanıcıdan bilgi almak için çeşitli Streamlit bileşenleri:
st.radio('Medeni Durumu', ('Evli', 'Bekar', 'Dul', 'Nişanlı'))
# Radio button — sadece bir seçenek seçilebilir

st.selectbox('Bildiğiniz Programlama Dilleri', ['C++', 'Python', 'Java', 'ASP', 'C', 'Q#'])
# Açılır kutu (dropdown)

st.multiselect('Bildiğiniz Programlama Dilleri', ['C++', 'Python', 'Java', 'ASP', 'C', 'Q#'])
# Birden fazla dil seçmeye izin verir

# Ekranda balon animasyonu gösterir 🎈
st.balloons()

# Görsel ekleme
st.image('image_02.jpg')

# Bölücü çizgi
st.divider()

# Video oynatma (lokal video)
st.video('secret_of_success.mp4')

st.divider()

# YouTube videosu oynatma (link ile)
st.video('https://www.youtube.com/watch?v=IEl2-ZyhXeo')

st.divider()

# Kamera kullanımı (fotoğraf çekme özelliği)
st.camera_input('Kamera :star:')

st.divider()

# Metin girişi (kullanıcıdan ad alır)
st.text_input('Adınızı Giriniz:')

# Tarih ve saat seçimi
st.date_input('Tarih seç :star:')
st.time_input('Saat seç :star:')

# Yaş seçimi için slider
st.slider('Yaş', 1, 100)

# Çok satırlı metin kutusu
st.text_area('Mesajınızı girin :star:')

# Dosya yükleme bileşeni
st.file_uploader('Dosya Yükle')

# Statik mesaj gösterimleri
st.write('Merhaba')
st.success('Başarılı')
st.error('Hatalı')
st.warning('Yok yok olmaz böyle')

# Uygulamayı terminalden çalıştırmak için:
# streamlit run app1.py
