import streamlit as st  
import pickle  

# Streamlit kütüphanesini arayüz (web uygulaması) oluşturmak için,  
# pickle kütüphanesini ise önceden eğitilmiş modeli yüklemek için içe aktarıyoruz

st.title('Tecrübe, Yazılı ve Mülakata Göre Maaş Tahmini :heavy_dollar_sign:')  

# Uygulama başlığı — kullanıcıya tahminin neyle ilgili olduğunu açıklar

model = pickle.load(open('maas.pkl', 'rb'))  

# Daha önce kaydedilen maaş tahmin modelini yüklüyoruz

tecrube = st.number_input('Tecrübe (Yıl)', 1, 10)  
yazili = st.number_input('Yazılı Sınav Puanı', 1, 10)  
mulakat = st.number_input('Mülakat Puanı', 1, 10)  

# Kullanıcıdan model için gerekli girişleri (tecrübe, yazılı sınav ve mülakat puanları) alıyoruz

if st.button('Tahmin Et'):  
    tahmin = model.predict([[tecrube, yazili, mulakat]])  
    tahmin = round(tahmin[0][0])  
    st.success(f'Yapay zekanın tahmin ettiği maaş: ${tahmin}')  

# Kullanıcı “Tahmin Et” butonuna bastığında model tahmini gerçekleştirir  
# Tahmin edilen maaş yuvarlanarak ekranda gösterilir  

# Not: Uygulamayı terminalden çalıştırmak için şu komutu kullanabiliriz:
# streamlit run app2.py
