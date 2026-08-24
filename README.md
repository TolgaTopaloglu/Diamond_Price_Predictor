# 💎 Diamond Price Predictor

<img width="1285" height="685" alt="DiamondPriceWebPage" src="https://github.com/user-attachments/assets/5ba892b0-72ee-4ac0-8d62-f373f7183f8e" />

## 📌 Proje Hakkında

**Diamond Price Predictor**, pırlantaların kesim, renk, berraklık ve geometrik özelliklerini makine öğrenmesi kullanarak analiz eden ve tahmini piyasa değerini hesaplayan uçtan uca bir web uygulamasıdır.

Projenin temel amacı, kullanıcıdan alınan 4C (**Carat, Cut, Color, Clarity**) ve boyut (**X, Y, Z, Depth, Table**) bilgilerini değerlendirerek mümkün olduğunca doğru bir fiyat tahmini sunmaktır.

Geliştirilen model, test verileri üzerinde **%98.0 R² skoru** elde etmiştir.

Projede veri hazırlama, veri temizleme, Keşifçi Veri Analizi (EDA), veri ön işleme, model seçimi, hiperparametre optimizasyonu ve model değerlendirme süreçleri gerçekleştirilmiştir.

Eğitilen en başarılı model, **LightGBM Pipeline** olarak `diamond_regression.pkl` dosyasına kaydedilmiş ve **FastAPI** kullanılarak web uygulamasına entegre edilmiştir.

Frontend tarafında HTML, CSS ve JavaScript kullanılarak oluşturulan modern, lüks ve Dark Mode odaklı arayüz **Cursor AI desteğiyle** geliştirilmiştir. Backend ve makine öğrenmesi modelinin frontend'e entegrasyonu tarafımca gerçekleştirilmiştir.

---

## 🛠️ Kullanılan Teknolojiler

### ⚙️ Backend & API

- **FastAPI** — Makine öğrenmesi modelini web uygulamasına bağlamak için
- **Uvicorn** — FastAPI uygulamasını çalıştırmak için
- **Jinja2** — HTML template'lerini render etmek için
- **Python-Multipart** — Form verilerinin işlenmesi için

### 🧠 Veri Bilimi & Makine Öğrenmesi

- **Scikit-Learn** — `StandardScaler`, `OneHotEncoder`, `Pipeline` ve model değerlendirme
- **LightGBM** — Pırlanta fiyat tahmin modeli
- **Pandas** — Veri işleme ve analiz
- **NumPy** — Sayısal işlemler

### 🎨 Frontend

- **HTML**
- **CSS**
- **JavaScript**
- **Cursor AI** — Frontend geliştirme ve arayüz tasarımı

---

## 📊 Makine Öğrenmesi ve Model Performansı

Projede farklı regresyon algoritmaları test edilmiş ve modeller **R² (R-Squared)** metriği üzerinden karşılaştırılmıştır.

| Model | R² Skoru |
|---|---:|
| 🥇 **LightGBM (Tuning)** | **%98.0 (0.980)** |
| 🥈 **LightGBM (Base)** | **%98.0 (0.980)** |
| 🥉 **XGBoost** | **%97.8 (0.978)** |
| Random Forest | %97.3 (0.973) |
| KNN | %95.4 (0.954) |
| Gradient Boost | %95.1 (0.951) |
| Decision Tree | %95.0 (0.950) |
| Linear Regression | %91.8 (0.918) |
| Ada Boost | %84.4 (0.844) |
| SVM | %50.4 (0.504) |

<img width="1112" height="536" alt="DiamondPriceRegressionModel" src="https://github.com/user-attachments/assets/dd3f7722-8f5f-451d-b85b-48c7fc5f723c" />

Test sonuçlarına göre **LightGBM**, test edilen modeller arasında en başarılı sonucu vermiştir. Bu nedenle canlı tahmin sistemi için **Tuned LightGBM Pipeline** kullanılmıştır.

---

## 🔍 Özellik Önemi (Feature Importance)

Modelin pırlanta fiyatını tahmin ederken hangi özelliklerden daha fazla etkilendiğini görmek amacıyla *feature importance* analizi yapılmıştır.

Öne çıkan özellikler:

1. **Karat (`num_col__carat`)** — `2701`
2. **Derinlik Oranı (`num_col__depth`)** — `2579`
3. **Z Boyutu (`num_col__z`)** — `2539`
4. **Y Boyutu (`num_col__y`)** — `2443`
5. **X Boyutu (`num_col__x`)** — `2205`
6. **Tablo Oranı (`num_col__table`)** — `1319`
7. **Renk: J (`cat_col__color_J`)** — `650`
8. **Berraklık: SI2 (`cat_col__clarity_SI2`)** — `637`

<img width="312" height="812" alt="FeatureImpotanceDiamondPrice" src="https://github.com/user-attachments/assets/5e2a5733-3e21-4b59-bb14-7f527805341c" />

Analiz sonucunda pırlantanın **karat ağırlığı** ve fiziksel geometrisini belirleyen **depth, x, y ve z** gibi boyutsal özelliklerin model açısından en önemli değişkenler olduğu görülmüştür.

---

## 💻 Uygulama Özellikleri

- 💎 Pırlanta fiyat tahmini
- 📊 4C özelliklerinin kullanımı: Carat, Cut, Color, Clarity
- 📐 Geometrik özelliklerin kullanımı: X, Y, Z, Depth, Table
- ⚡ Anlık fiyat tahmini
- 🌐 FastAPI backend entegrasyonu
- 🤖 LightGBM tabanlı makine öğrenmesi modeli
- 🎨 Modern ve Dark Mode odaklı kullanıcı arayüzü

---

## 🖥️ Uygulama Akışı

~~~text
Kullanıcı
   ↓
Pırlanta 4C & Ölçüleri
   ↓
Frontend
   ↓
FastAPI
   ↓
main.py
   ↓
diamond_regression.pkl
   ↓
Preprocessing Pipeline
   ↓
LightGBM
   ↓
Fiyat Tahmini ($)
   ↓
Frontend
   ↓
Kullanıcı
~~~

---

## 📂 Proje Yapısı

~~~text
Diamond_Price_Predictor/
│
├── templates/
│   └── index.html
│       # Frontend HTML arayüzü
│
├── main.py
│   # FastAPI backend rotaları ve model entegrasyonu
│
├── diamond_regression.pkl
│   # Eğitilmiş LightGBM Pipeline modeli
│
├── requirements.txt
│   # Proje bağımlılıkları
│
└── README.md
    # Proje dokümantasyonu
~~~

---

## 🚀 Kurulum ve Çalıştırma

### Gereksinimler

- Python 3.9+
- Git
- pip

### 1. Repoyu Klonlayın

~~~bash
git clone https://github.com/USERNAME/Diamond_Price_Predictor.git
cd Diamond_Price_Predictor
~~~

> `USERNAME` kısmını kendi GitHub kullanıcı adınızla değiştirin.

### 2. Sanal Ortam Oluşturun

#### Windows

~~~bash
python -m venv venv
venv\Scripts\activate
~~~

#### macOS / Linux

~~~bash
python3 -m venv venv
source venv/bin/activate
~~~

### 3. Bağımlılıkları Yükleyin

Projede kullanılan tüm Python bağımlılıkları `requirements.txt` dosyasında bulunmaktadır.

~~~bash
pip install -r requirements.txt
~~~

### 4. Uygulamayı Başlatın

FastAPI uygulamasını Uvicorn ile başlatın:

~~~bash
uvicorn main:app --reload
~~~

### 5. Web Uygulamasını Açın

Uygulama başladıktan sonra tarayıcınızdan:

~~~text
http://127.0.0.1:8000
~~~

adresine giderek uygulamayı kullanabilirsiniz.

FastAPI'nin otomatik Swagger API dokümantasyonuna:

~~~text
http://127.0.0.1:8000/docs
~~~

adresinden ulaşabilirsiniz.

> **Not:** `diamond_regression.pkl` eğitilmiş **LightGBM Pipeline** modelini içerdiği için modeli yeniden eğitmenize gerek yoktur. `requirements.txt` içerisindeki bağımlılıkları kurduktan sonra uygulamayı doğrudan çalıştırabilirsiniz.

---


---

## 👨‍💻 Proje Amacı

Bu proje, bir makine öğrenmesi modelini yalnızca notebook içerisinde eğitmek yerine **uçtan uca çalışan bir makine öğrenmesi uygulamasına dönüştürmek** amacıyla geliştirilmiştir.

Proje içerisinde:

**Veri Analizi → Veri Ön İşleme → Modelleme → Hiperparametre Optimizasyonu → Model Değerlendirme → Model Kaydetme → FastAPI → Frontend → Live Inference**

sürecinin tamamı tek bir proje içerisinde bir araya getirilmiştir.

---
