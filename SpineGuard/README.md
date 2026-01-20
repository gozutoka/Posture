# SpineGuard - Gerçek Zamanlı Duruş Analiz Sistemi

SpineGuard, yapay zeka destekli duruş analizi yapan bir web uygulamasıdır. YOLOv8 pose detection kullanarak gerçek zamanlı duruş takibi yapar.

## 🚀 Özellikler

- **Gerçek zamanlı duruş analizi** - Kamera ile anlık duruş kontrolü
- **Yapay zeka destekli** - YOLOv8 pose detection modeli
- **Eğitici içerik** - Omurga anatomisi ve sırt sağlığı bilgileri
- **Modern arayüz** - Responsive ve kullanıcı dostu tasarım

## 📋 Gereksinimler

- Python 3.8+
- Webcam
- GPU (opsiyonel, performans için önerilir)

## 🔧 Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install flask ultralytics opencv-python numpy
```

2. Uygulamayı başlatın:
```bash
python app.py
```

3. Tarayıcınızda açın:
```
http://localhost:5000
```

## 📁 Proje Yapısı

```
SpineGuard/
├── app.py                  # Ana uygulama
├── posture_analyzer.py     # Duruş analiz motoru
├── pages/                  # Sayfa modülleri
│   ├── landing.py         # Ana sayfa
│   ├── egitim.py          # Bilgi bankası
│   ├── nasil_calisir.py   # Sistem açıklaması
│   ├── demo.py            # Canlı demo
│   └── developer.py       # Developer sayfası (geçici)
├── static/                 # Statik dosyalar (görseller)
└── yolov8n-pose.pt        # YOLOv8 model dosyası
```

## 🎯 Kullanım

### Ana Sayfa
- SpineGuard'ın özelliklerini keşfedin
- Duruş problemleri hakkında bilgi edinin

### Bilgi Bankası
- Omurga anatomisi
- Yaygın sırt problemleri
- Duruş farkındalığı

### Nasıl Çalışır?
- Sistem mimarisi
- Sensör teknolojisi
- Teknik detaylar

### Canlı Demo
- Kameranızı açın
- Gerçek zamanlı duruş analizi yapın
- Anlık geri bildirim alın

## 🔬 Teknoloji

- **Backend:** Flask (Python)
- **AI Model:** YOLOv8 Pose Detection
- **Computer Vision:** OpenCV
- **Frontend:** HTML/CSS (inline)

## 📊 Duruş Metrikleri

SpineGuard şu metrikleri ölçer:
- **Boyun açısı** - Forward head posture tespiti
- **Sırt açısı** - Kamburluk (kyphosis) tespiti
- **Omuz dengesi** - Asimetri kontrolü

## ⚠️ Geliştirme Notları

### Developer Sayfası (Geçici)
`/developer` endpoint'i geliştirme amaçlıdır. Production'a geçmeden önce:
1. `pages/developer.py` dosyasını silin
2. `app.py`'den import ve blueprint kaydını kaldırın
3. Diğer sayfalardaki developer linklerini kaldırın

### .gitignore
Aşağıdaki dosyalar repository'e dahil edilmemelidir:
- `__pycache__/`
- `.claude/`
- `ngrok.exe`, `cloudflared.exe` (büyük binary dosyalar)
- `*.log`

## 🌐 Web'de Yayınlama

Geliştirme ortamında test için Cloudflare Tunnel kullanılmıştır:
```bash
./cloudflared.exe tunnel --url http://localhost:5000
```

## 📝 Lisans

Bu proje eğitim ve test amaçlıdır.

## 👥 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit edin (`git commit -m 'Add amazing feature'`)
4. Push edin (`git push origin feature/amazing-feature`)
5. Pull Request açın

## 📧 İletişim

Sorularınız için issue açabilirsiniz.

---

**Not:** Bu uygulama tıbbi bir cihaz değildir. Sağlık sorunları için mutlaka bir sağlık profesyoneline danışın.
