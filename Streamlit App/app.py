# Gerekli kütüphaneleri içe aktarma
# Flask: web uygulaması oluşturmak için
# render_template: HTML dosyalarını göstermek için
# request: form verilerini almak için
# pickle: daha önce eğitilmiş modeli yüklemek için
from flask import Flask, render_template, request
import pickle

# Flask uygulamasını başlatma
app = Flask(__name__)

# Daha önce eğitilmiş maaş tahmin modelini yükleme
# 'maas.pkl' dosyasında saklanan modeli açıyoruz
model = pickle.load(open('maas.pkl', 'rb'))

# Ana sayfa route'u ('/')
# Kullanıcı ilk girdiğinde index.html sayfasını gösterir
@app.route('/')
def index():
    return render_template('index.html')

# Tahmin yapma route'u ('/predict')
# POST metodu ile formdan veri alınır ve model ile tahmin yapılır
@app.route('/predict', methods=["POST"])
def predict():
    # Formdan kullanıcı bilgilerini alma
    isim = request.form.get('isim')            # Kullanıcının adı
    tecrube = float(request.form.get('tecrube'))  # İş tecrübesi (yıl)
    yazili = float(request.form.get('yazili'))    # Yazılı sınav puanı
    mulakat = float(request.form.get('mulakat'))  # Mülakat puanı
    
    # Modelden maaş tahmini alma
    tahmin = model.predict([[tecrube, yazili, mulakat]])
    
    # Tahmini kullanıcıya okunabilir biçimde hazırlama
    tahmin_text = f"Sayın {isim}, tahmin edilen maaşınız: ${tahmin[0][0]:,.2f}"
    
    # Sonucu yeniden aynı sayfada gösterme
    return render_template('index.html', tahmin=tahmin_text, isim=isim)

# Uygulamayı çalıştırma
# debug=True => Kod değiştiğinde sunucu otomatik yenilenir
if __name__ == "__main__":
    app.run(debug=True)



# python app.py ile terminalde çalıştırabilirim.