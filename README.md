# 💎 DiamondMLOps: Uçtan Uca Pırlanta Fiyat Tahmin ve Analiz Motoru

<img width="850" alt="DiamondMLOps Uygulama Ekranı" src="DiamondPriceWebPage.png" />

## 📌 Proje Hakkında

**DiamondMLOps**, pırlantaların kesim, renk, berraklık ve geometri özelliklerini makine öğrenmesi kullanarak analiz eden ve tahmini piyasa değerini hesaplayan uçtan uca bir web uygulamasıdır.

Projenin temel amacı, kullanıcıdan alınan 4C (Carat, Cut, Color, Clarity) ve boyut (X, Y, Z, Depth, Table) bilgilerini değerlendirerek mümkün olduğunca doğru bir fiyat tahmini sunmaktır. Geliştirdiğim model, test verileri üzerinde **%98.0 R² skoru** elde etmiştir.

Projeyi geliştirirken özellikle **veri bilimi, makine öğrenmesi ve backend** tarafına odaklandım. Veri setinin hazırlanması, temizlenmesi, Keşifçi Veri Analizi (EDA), veri ön işleme (`StandardScaler`, `One-Hot Encoding`), model seçimi, hiperparametre optimizasyonu (Grid/Randomized Search) ve test süreçlerini sıfırdan geliştirdim. Eğitilen en başarılı modeli **FastAPI** kullanarak bir API haline getirip frontend ile entegre ettim.

**Frontend tarafında ise HTML, CSS ve JavaScript kullanılarak oluşturulan modern, lüks ve Dark Mode odaklı arayüz tasarımı tamamen Cursor AI tarafından geliştirilmiştir.** Backend ve makine öğrenmesi tarafının bu arayüze entegrasyonu ise bizzat tarafımca kurgulanmıştır.

Bu projede temel hedefim sadece başarılı bir makine öğrenmesi modeli oluşturmak değil; veri hazırlama aşamasından modellemeye, API geliştirmeden kullanıcı arayüzüne kadar tüm süreci bir bütün olarak ele alıp, modeli **gerçek hayatta kullanılabilecek interaktif bir web uygulamasına** dönüştürmekti.

---

## 🛠️ Mimari ve Kullanılan Teknolojiler

### ⚙️ Backend & API

- **FastAPI:** Modeli frontend'e bağlamak ve yüksek performanslı API altyapısını oluşturmak için kullanıldı.
- **Uvicorn:** FastAPI uygulamasını asenkron olarak çalıştırmak için kullanıldı.
- **Jinja2:** Dinamik HTML template'lerinin render edilmesi için kullanıldı.
- **Python-Multipart:** Form verilerinin backend tarafında işlenmesi için kullanıldı.

### 🧠 Veri Bilimi & Makine Öğrenmesi

- **Scikit-Learn:** Veri ön işleme (`StandardScaler`, `OneHotEncoder`), `Pipeline` kurgusu ve model değerlendirme süreçlerinde kullanıldı.
- **LightGBM:** Projenin ana tahmin modeli (Tuned LGBMRegressor) olarak kullanıldı.
- **Pandas & NumPy:** Veri temizleme, düzenleme ve manipülasyon süreçlerinde kullanıldı.

### 🎨 Frontend

- **Cursor AI:** Modern arayüz tasarımı ve frontend (HTML/CSS/JS) kodlamalarının tamamında kullanıldı.

---

## 📊 Makine Öğrenmesi ve Model Performansı

Projede veri setine en uygun modeli bulabilmek için farklı makine öğrenmesi algoritmaları test edildi ve sonuçlar **R² (R-Squared)** metriği üzerinden karşılaştırıldı. 

### 🏆 Model Karşılaştırması

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

<img width="900" alt="Model Performans Karşılaştırması" src="DiamondPriceRegressionModel.png" />

Test sonuçlarına ve hiperparametre optimizasyonuna (Grid/Randomized Search) göre **LightGBM**, diğer modeller arasında en başarılı sonucu verdi. Bu nedenle sistemin canlı (live inference) tahmin modeli olarak `LightGBM Tuning` tercih edildi.

---

## 🔍 Özellik Önemi (Feature Importance)

Modelin pırlanta fiyatını tahmin ederken hangi özelliklerden daha fazla etkilendiğini görmek için *feature importance* analizi yapıldı.

Öne çıkan özellikler ve model üzerindeki ağırlıkları:

1. **Karat (`num_col__carat`)** — `2701`
2. **Derinlik Oranı (`num_col__depth`)** — `2579`
3. **Z Boyutu (Derinlik mm) (`num_col__z`)** — `2539`
4. **Y Boyutu (Genişlik mm) (`num_col__y`)** — `2443`
5. **X Boyutu (Uzunluk mm) (`num_col__x`)** — `2205`
6. **Tablo Oranı (`num_col__table`)** — `1319`
7. **Renk: J (`cat_col__color_J`)** — `650`
8. **Berraklık: SI2 (`cat_col__clarity_SI2`)** — `637`

<img width="350" alt="Feature Importance" src="FeatureImpotanceDiamondPrice.png" />

Analiz sonucunda, pırlantanın **karat ağırlığı** ve fiziksel geometrisini belirleyen **boyutsal ölçülerin (depth, x, y, z)** fiyat üzerinde en belirleyici etmenler olduğu kanıtlanmıştır.

---

## 💻 Uygulama Özellikleri

- **Etkileşimli Arayüz:** Carat, Cut, Color, Clarity gibi kalite standartları ile Table, Depth, X, Y, Z gibi fiziksel ölçüler kolayca girilebilir.
- **Anlık Fiyat Tahmini (Live Inference):** Form gönderildiğinde pırlanta bilgileri backend'e gönderilir, `Pipeline` üzerinden işlenir ve tahmini fiyat saniyeler içinde kullanıcıya gösterilir.
- **Karanlık Tema (Dark Mode):** Pırlanta ışıltısını öne çıkaran, lüks ve şık bir stüdyo/atelier tasarımı kurgulanmıştır.

---

## 🖥️ Uygulama Akışı

Kullanıcı pırlanta bilgilerini girdikten sonra veriler **FastAPI** backend'ine iletilir. Backend tarafında eğitim sırasında kurulan (StandardScaler + OneHotEncoder) `Pipeline` çalışır ve veriler **LightGBM** modeline aktarılır. Modelin ürettiği sonuç formatlanarak arayüze yansıtılır.

```text
Kullanıcı
   ↓
Pırlanta 4C & Ölçüleri
   ↓
Frontend
   ↓
FastAPI (Endpoint: /predict)
   ↓
Data Preprocessing (Pipeline)
   ↓
LightGBM Model
   ↓
Fiyat Tahmini ($)
   ↓
Frontend
   ↓
Kullanıcı
