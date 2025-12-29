import streamlit as st  
import cv2  
import numpy as np  
from PIL import Image  

# Gerekli kütüphaneleri içe aktarıyoruz  
# Streamlit → web arayüzü oluşturmak için  
# OpenCV (cv2) → görüntü işleme işlemleri için  
# NumPy → dizi (array) işlemleri için  
# PIL → yüklenen görselleri okumak ve dönüştürmek için kullanılır

st.title('Image to Sketch')  

# Uygulama başlığını oluşturuyoruz

file = st.file_uploader('Upload a Portrait Image', type=['jpg', 'png', 'jpeg'])  

# Kullanıcıdan bir portre görseli yüklemesini istiyoruz

if file:  
    img = Image.open(file).convert('RGB')  
    # Yüklenen görseli RGB formatına dönüştürüyoruz

    img2 = np.array(img)  
    # Görseli NumPy dizisine çeviriyoruz (OpenCV ile işlemek için)

    img_bw = cv2.cvtColor(img2, cv2.COLOR_RGB2BGR)  
    gray = cv2.cvtColor(img_bw, cv2.COLOR_RGB2GRAY)  
    # Görseli gri tonlamaya dönüştürüyoruz

    inverted = 255 - gray  
    # Görselin negatifini alıyoruz

    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)  
    # Görseli Gaussian Blur filtresiyle yumuşatıyoruz

    def dodge(front, back):  
        return cv2.divide(front, 255 - back, scale=255)  
    # dodge() fonksiyonu, orijinal ve bulanık görüntüleri birleştirerek çizim (sketch) efekti oluşturur

    sketch = dodge(gray, blurred)  
    # Gri tonlamalı ve bulanık görselleri kullanarak çizim efekti üretiyoruz

    st.subheader('Original vs Sketch')  
    col1, col2 = st.columns(2)  
    # Görselleri yan yana göstermek için iki sütun oluşturuyoruz

    with col1:  
        st.image(img, caption='Original', use_container_width=True)  
        # Orijinal görseli gösteriyoruz

    with col2:  
        st.image(sketch, caption='Sketch', use_container_width=True)  
        # Çizim (sketch) halini gösteriyoruz

# Not: Bu uygulamayı çalıştırmak için terminalde şu komutu kullanabilirsiniz:
# streamlit run app5.py
