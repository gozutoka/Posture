"""
SpineGuard - Nasıl Çalışır Detaylı Açıklama Sayfası
"""

from flask import Blueprint, render_template_string

bp = Blueprint('nasil_calisir', __name__)

NASIL_CALISIR_HTML = '''<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>SpineGuard Nasıl Çalışır? | Teknik Detaylar ve Sensör Teknolojisi</title>
<meta name="description" content="SpineGuard'ın giyilebilir sensör teknolojisi nasıl çalışır? 6 eksenli IMU sensörleri, Kinesiology Tape yapıştırma sistemi ve gerçek zamanlı geri bildirim.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;line-height:1.6;color:#1e293b;overflow-x:hidden;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;background:#fafbfc}
.nav{background:rgba(255,255,255,0.98);padding:20px 0;position:sticky;top:0;z-index:1000;box-shadow:0 1px 3px rgba(0,0,0,0.04);border-bottom:1px solid #e2e8f0}
.nav .container{display:flex;justify-content:space-between;align-items:center}
.nav-brand{color:#0f4c81;font-size:1.6em;font-weight:900;text-decoration:none;letter-spacing:-0.5px}
.nav-links{display:flex;gap:35px;align-items:center}
.nav-links a{color:#475569;text-decoration:none;font-weight:500;transition:color 0.3s;font-size:0.95em}
.nav-links a:hover{color:#0f4c81}
.nav-demo{background:linear-gradient(135deg,#0f4c81,#14b8a6);color:white!important;padding:10px 20px;border-radius:8px;font-weight:700}
.container{max-width:1200px;margin:0 auto;padding:0 20px}
.hero{background:linear-gradient(135deg,#0f4c81 0%,#14b8a6 100%);color:white;padding:100px 20px 80px;text-align:center}
.hero h1{font-size:3.2em;margin-bottom:20px;font-weight:900;letter-spacing:-1px;line-height:1.1}
.hero p{font-size:1.3em;opacity:0.95;max-width:800px;margin:0 auto}
.section{padding:80px 20px;background:white}
.section-title{color:#0f172a;font-size:2.5em;margin-bottom:30px;text-align:center;font-weight:900;letter-spacing:-0.5px}
.section-subtitle{text-align:center;font-size:1.2em;color:#475569;max-width:700px;margin:0 auto 60px auto}
.step-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(350px,1fr));gap:40px;margin:60px 0}
.step-card{background:white;border-radius:20px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.08);border:1px solid #e2e8f0;transition:transform 0.3s,box-shadow 0.3s}
.step-card:hover{transform:translateY(-5px);box-shadow:0 8px 30px rgba(0,0,0,0.12)}
.step-number{background:linear-gradient(135deg,#0f4c81,#14b8a6);color:white;padding:20px;text-align:center;font-size:2em;font-weight:900}
.step-content{padding:35px}
.step-content h3{color:#0f172a;font-size:1.6em;margin-bottom:20px;font-weight:800}
.step-content p{color:#475569;line-height:1.8;margin-bottom:15px}
.step-content ul{margin:20px 0;padding-left:20px}
.step-content li{color:#475569;margin:12px 0;line-height:1.7}
.tech-box{background:linear-gradient(135deg,rgba(15,76,129,0.05),rgba(20,184,166,0.05));padding:50px 40px;border-radius:20px;margin:40px 0;border:1px solid #e2e8f0}
.tech-grid{display:grid;grid-template-columns:1fr 1fr;gap:50px;align-items:center}
.feature-list{list-style:none;padding:0}
.feature-list li{background:white;padding:20px;margin:15px 0;border-radius:12px;border-left:4px solid #14b8a6;box-shadow:0 2px 8px rgba(0,0,0,0.05)}
.feature-list li strong{color:#0f172a;font-weight:800;display:block;margin-bottom:8px;font-size:1.1em}
.highlight-banner{background:linear-gradient(135deg,#0f4c81,#14b8a6);color:white;padding:50px 40px;border-radius:20px;text-align:center;margin:60px 0}
.highlight-banner h3{font-size:2em;margin-bottom:20px;font-weight:900}
.highlight-banner p{font-size:1.2em;opacity:0.95;line-height:1.8}
.cta-section{background:#f8fafc;padding:80px 20px;text-align:center}
.cta-button{display:inline-block;background:linear-gradient(135deg,#0f4c81,#14b8a6);color:white;padding:18px 40px;border-radius:12px;text-decoration:none;font-weight:700;font-size:1.1em;transition:all 0.3s;box-shadow:0 4px 15px rgba(15,76,129,0.3)}
.cta-button:hover{transform:translateY(-2px);box-shadow:0 6px 20px rgba(15,76,129,0.4)}
@media(max-width:768px){.hero h1{font-size:2em}.tech-grid{grid-template-columns:1fr}.step-grid{grid-template-columns:1fr}}
</style>
</head>
<body>

<nav class="nav">
<div class="container">
<a href="/" class="nav-brand">SpineGuard</a>
<div class="nav-links">
<a href="/">Ana Sayfa</a>
<a href="/egitim">Bilgi Bankası</a>
<a href="/nasil-calisir">Nasıl Çalışır?</a>
<a href="/demo" class="nav-demo">🎥 Demo</a>
<a href="/developer" style="background:linear-gradient(135deg,#e67e22,#d35400);color:white!important;padding:10px 20px;border-radius:8px;font-weight:700">👨‍💻 Developer</a>
</div>
</div>
</nav>

<div class="hero">
<div class="container">
<h1>SpineGuard Nasıl Çalışır?</h1>
<p>Giyilebilir sensör teknolojisi ile 7/24 gerçek zamanlı duruş takibi - Adım adım tam sistem açıklaması</p>
</div>
</div>

<div class="section">
<div class="container">
<h2 class="section-title">Sistem Genel Bakış</h2>
<p class="section-subtitle">SpineGuard, vücudunuza yerleştirilen hafif sensörler, akıllı telefon uygulaması ve isteğe bağlı giyilebilir cihazlardan oluşan eksiksiz bir duruş takip sistemidir.</p>

<div class="tech-box">
<div class="tech-grid">
<div style="text-align:center">
<img src="/static/images/sensor-positions.jpg" alt="Sensör Pozisyonları" style="width:100%;max-width:400px;border-radius:15px;box-shadow:0 8px 30px rgba(0,0,0,0.15)">
<p style="margin-top:20px;color:#475569;font-size:1.05em"><strong>İki kritik nokta:</strong> L4 (Bel) ve T8-T10 (Sırt)</p>
</div>
<div>
<h3 style="color:#0f4c81;font-size:1.8em;margin-bottom:25px;font-weight:900">Sensör Yerleşimi</h3>
<ul class="feature-list">
<li>
<strong>📍 Sensör 1: L4 (4. Bel Omuru)</strong>
Bel eğriliği (lordoz) ve pelvik tilt ölçümü. En fazla yük taşıyan bölge.
</li>
<li>
<strong>📍 Sensör 2: T8-T10 (8-10. Göğüs Omuru)</strong>
Göğüs kamburluğu (kifoz) ve sırt eğimi ölçümü. Oturma pozisyonu kontrolü.
</li>
</ul>
<p style="background:rgba(20,184,166,0.1);padding:20px;border-radius:10px;margin-top:20px;color:#0f172a;line-height:1.7">
<strong>⚡ Neden bu noktalar?</strong> Bu iki sensör, tüm omurganın hareketini ve duruşunu %95 doğrulukla hesaplamamıza yeter. Daha fazla sensör daha fazla veri ama çok daha az konfor demektir.
</p>
</div>
</div>
</div>

<h2 class="section-title" style="margin-top:100px">Adım Adım Nasıl Çalışır?</h2>

<div class="step-grid">
<div class="step-card">
<div class="step-number">1</div>
<div class="step-content">
<h3>🔧 Giyilebilir Sensörler</h3>
<p><strong>6 Eksenli IMU (Inertial Measurement Unit) Teknolojisi</strong></p>
<ul>
<li><strong>3 Eksen İvmeölçer (Accelerometer):</strong> X, Y, Z eksenlerinde hareket ve eğim algılar</li>
<li><strong>3 Eksen Jiroskop (Gyroscope):</strong> Dönme hızı ve açısal hızı ölçer</li>
<li><strong>Örnekleme Hızı:</strong> Saniyede 100 ölçüm (100 Hz) - Gerçek zamanlı hassasiyet</li>
<li><strong>Hassasiyet:</strong> ±0.5° açı, ±0.02g ivme - Milimetre seviyesinde takip</li>
</ul>
<p style="margin-top:20px"><strong>🔋 Pil ve Güç:</strong></p>
<ul>
<li>30 gün kesintisiz kullanım</li>
<li>Şarj etmeye gerek yok - Kullan-at sensörler</li>
<li>Ultra düşük güçlü BLE (Bluetooth Low Energy) haberleşme</li>
<li>CR2032 pil ile tamamen güvenilir</li>
</ul>
</div>
</div>

<div class="step-card">
<div class="step-number">2</div>
<div class="step-content">
<h3>🩹 Kinesiology Tape Yapıştırma Sistemi</h3>
<p><strong>Hareket özgürlüğünüzü kısıtlamayan profesyonel çözüm</strong></p>
<ul>
<li><strong>Vücutla Esneyen:</strong> %140'a kadar elastik kumaş, her hareketle birlikte uzar</li>
<li><strong>Nefes Alır:</strong> Su geçirmez ama ter geçiren yapı - Terleme sorunu yok</li>
<li><strong>Uzun Ömürlü:</strong> 3-7 gün boyunca çıkarmadan kullanabilirsiniz</li>
<li><strong>Kolay Değişim:</strong> Tape eskidiğinde veya sensör bittiğinde kolayca yenilenebilir</li>
<li><strong>Cilde Zarar Vermez:</strong> Hypoallergenic (alerjik olmayan) yapıştırıcı</li>
</ul>
<p style="background:#fff3cd;padding:15px;border-radius:8px;margin-top:20px;font-size:0.95em">
<strong>💡 İpucu:</strong> Kinesiology tape, fizik tedavide kullanılan tıbbi bir üründür. Sporcular yıllardır bu tape'leri maç sırasında bile kullanır - hareket kısıtlaması yoktur.
</p>
</div>
</div>

<div class="step-card">
<div class="step-number">3</div>
<div class="step-content">
<h3>📱 Akıllı Telefon Bağlantısı</h3>
<p><strong>Bluetooth Low Energy (BLE) ile anlık veri aktarımı</strong></p>
<ul>
<li><strong>Düşük Enerji Tüketimi:</strong> Telefonunuzun pilini hemen hemen hiç tüketmez</li>
<li><strong>10 Metre Menzil:</strong> Telefonunuz cebinizde, çantanızda veya masanızda olabilir</li>
<li><strong>Gerçek Zamanlı:</strong> <10ms gecikme ile anında veri aktarımı</li>
<li><strong>Güvenli Bağlantı:</strong> AES-128 şifreleme ile verileriniz korunur</li>
</ul>
<p style="margin-top:20px"><strong>📲 Mobil Uygulama Özellikleri:</strong></p>
<ul>
<li>Canlı duruş görüntüleme - 3D avatar ile görselleştirme</li>
<li>Anlık uyarılar ve titreşim bildirimleri</li>
<li>Günlük/haftalık/aylık raporlar ve grafikler</li>
<li>Hedef belirleme ve ilerleme takibi</li>
</ul>
</div>
</div>

<div class="step-card">
<div class="step-number">4</div>
<div class="step-content">
<h3>⌚ Giyilebilir Cihazlarla Entegrasyon (Opsiyonel)</h3>
<p><strong>Apple Watch, Fitbit, Garmin ve diğer wearable'lar ile uyumlu</strong></p>
<ul>
<li><strong>Haptik (Titreşim) Geri Bildirim:</strong> Kötü duruş tespit edildiğinde saatiniz titrer</li>
<li><strong>Pozisyon Değiştirme Hatırlatmaları:</strong> 30 dakikada bir nazikçe uyarır</li>
<li><strong>Hızlı Bakış:</strong> Duruş skorunuzu watch face'de görebilirsiniz</li>
<li><strong>Sessiz Mod:</strong> Toplantı, uyku veya spor sırasında bildirimleri kapatabilirsiniz</li>
</ul>
<p style="background:#d1ecf1;padding:15px;border-radius:8px;margin-top:20px;font-size:0.95em">
<strong>✅ Avantaj:</strong> Telefonunuza bakmadan, kolunuzdaki hafif titreşimle anında uyarılırsınız. Bu, özellikle toplantılarda ve yoğun iş saatlerinde çok kullanışlıdır.
</p>
</div>
</div>
</div>

<div class="highlight-banner">
<h3>🎯 Gerçek Zamanlı Geri Bildirim Döngüsü</h3>
<p>Sensörler → Bluetooth → Telefon/Saat → Analiz → Uyarı → Düzeltme → Tekrar Ölçüm</p>
<p style="margin-top:20px;font-size:1em;opacity:0.9">Bu döngü saniyede 100 kez tekrarlanır. Kötü duruş tespit edildiğinde 1 saniyeden kısa sürede uyarılırsınız. Bu sayede vücudunuz henüz ağrı oluşmadan duruşunuzu düzeltme şansı bulur.</p>
</div>

<h2 class="section-title" style="margin-top:100px">Teknik Özellikler</h2>

<div class="tech-box">
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:30px">
<div style="background:white;padding:30px;border-radius:15px;box-shadow:0 2px 10px rgba(0,0,0,0.05)">
<div style="font-size:2.5em;margin-bottom:15px">⚙️</div>
<h4 style="color:#0f172a;font-size:1.3em;margin-bottom:15px;font-weight:800">Sensör Donanımı</h4>
<ul style="list-style:none;padding:0">
<li style="padding:8px 0;color:#475569">✓ 6-axis IMU (MPU-6050)</li>
<li style="padding:8px 0;color:#475569">✓ 16-bit ADC çözünürlük</li>
<li style="padding:8px 0;color:#475569">✓ ±2g/±250°/s hassasiyet</li>
<li style="padding:8px 0;color:#475569">✓ IP67 su/toz geçirmezlik</li>
</ul>
</div>

<div style="background:white;padding:30px;border-radius:15px;box-shadow:0 2px 10px rgba(0,0,0,0.05)">
<div style="font-size:2.5em;margin-bottom:15px">📡</div>
<h4 style="color:#0f172a;font-size:1.3em;margin-bottom:15px;font-weight:800">Haberleşme</h4>
<ul style="list-style:none;padding:0">
<li style="padding:8px 0;color:#475569">✓ Bluetooth 5.0 Low Energy</li>
<li style="padding:8px 0;color:#475569">✓ 10m menzil (açık alanda)</li>
<li style="padding:8px 0;color:#475569">✓ <10ms gecikme süresi</li>
<li style="padding:8px 0;color:#475569">✓ AES-128 şifreleme</li>
</ul>
</div>

<div style="background:white;padding:30px;border-radius:15px;box-shadow:0 2px 10px rgba(0,0,0,0.05)">
<div style="font-size:2.5em;margin-bottom:15px">🔋</div>
<h4 style="color:#0f172a;font-size:1.3em;margin-bottom:15px;font-weight:800">Güç ve Pil</h4>
<ul style="list-style:none;padding:0">
<li style="padding:8px 0;color:#475569">✓ CR2032 coin cell pil</li>
<li style="padding:8px 0;color:#475569">✓ 30 gün kullanım süresi</li>
<li style="padding:8px 0;color:#475569">✓ Şarj etmeye gerek yok</li>
<li style="padding:8px 0;color:#475569">✓ 50μA uyku modu akımı</li>
</ul>
</div>

<div style="background:white;padding:30px;border-radius:15px;box-shadow:0 2px 10px rgba(0,0,0,0.05)">
<div style="font-size:2.5em;margin-bottom:15px">📏</div>
<h4 style="color:#0f172a;font-size:1.3em;margin-bottom:15px;font-weight:800">Boyut ve Ağırlık</h4>
<ul style="list-style:none;padding:0">
<li style="padding:8px 0;color:#475569">✓ 30mm x 20mm x 5mm</li>
<li style="padding:8px 0;color:#475569">✓ Sadece 15 gram</li>
<li style="padding:8px 0;color:#475569">✓ Kıyafet altında görünmez</li>
<li style="padding:8px 0;color:#475569">✓ Esnek, hafif plastik kasa</li>
</ul>
</div>
</div>
</div>

</div>
</div>

<div class="cta-section">
<div class="container">
<h2 style="color:#0f172a;font-size:2.5em;margin-bottom:20px;font-weight:900">SpineGuard'ı Denemeye Hazır mısınız?</h2>
<p style="color:#475569;font-size:1.2em;margin-bottom:40px;max-width:600px;margin-left:auto;margin-right:auto">Canlı demo ile sistemi test edin veya daha fazla bilgi için bilgi bankasını inceleyin.</p>
<div style="display:flex;gap:20px;justify-content:center;flex-wrap:wrap">
<a href="/demo" class="cta-button">🎥 Canlı Demo İzle</a>
<a href="/egitim" class="cta-button" style="background:white;color:#0f4c81;border:2px solid #0f4c81">📚 Bilgi Bankası</a>
<a href="/developer" class="cta-button" style="background:linear-gradient(135deg,#e67e22,#d35400);color:white">👨‍💻 Developer Bilgileri</a>
</div>
</div>
</div>

<div style="background:#0f172a;color:white;padding:40px 20px;text-align:center">
<div class="container">
<p>&copy; 2026 SpineGuard. Tüm hakları saklıdır. | Sırt sağlığınız için bilimsel çözüm.</p>
</div>
</div>

</body>
</html>'''

@bp.route('/nasil-calisir')
def nasil_calisir():
    return render_template_string(NASIL_CALISIR_HTML)
