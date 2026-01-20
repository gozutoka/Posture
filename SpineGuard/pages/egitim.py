"""
SpineGuard - Eğitim Sayfası
"""

from flask import Blueprint, render_template_string

bp = Blueprint('egitim', __name__)

EGITIM_HTML = '''<!DOCTYPE html>
<html lang="tr"><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>SpineGuard - Bilgi Bankası | Omurga Anatomisi ve Duruş Bilimi</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;line-height:1.8;color:#1e293b;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;background:#fafbfc}
.nav{background:rgba(255,255,255,0.98);padding:20px 0;position:sticky;top:0;z-index:1000;box-shadow:0 1px 3px rgba(0,0,0,0.04);border-bottom:1px solid #e2e8f0}
.nav .container{display:flex;justify-content:space-between;align-items:center}
.nav-brand{color:#0f4c81;font-size:1.6em;font-weight:900;text-decoration:none;letter-spacing:-0.5px}
.nav-links{display:flex;gap:35px;align-items:center}
.nav-links a{color:#475569;text-decoration:none;font-weight:500;transition:color 0.3s;font-size:0.95em}
.nav-links a:hover{color:#0f4c81}
.container{max-width:1000px;margin:0 auto;padding:0 20px}
.hero-mini{background:linear-gradient(135deg,#0f4c81 0%,#14b8a6 100%);color:white;padding:80px 20px;text-align:center}
.hero-mini h1{font-size:2.8em;margin-bottom:15px;font-weight:900;letter-spacing:-1px}
.hero-mini p{font-size:1.3em;opacity:0.95;font-weight:400}
.content{padding:60px 20px;background:white}
.section{margin-bottom:60px}
.section h2{color:#0f172a;font-size:2em;margin-bottom:20px;padding-bottom:10px;border-bottom:3px solid #14b8a6;font-weight:900;letter-spacing:-0.5px}
.section h3{color:#0f4c81;font-size:1.5em;margin:30px 0 15px 0;font-weight:800}
.spine-parts{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:20px;margin:30px 0}
.spine-part{background:white;padding:25px;border-radius:10px;box-shadow:0 1px 3px rgba(0,0,0,0.08);border:1px solid #e2e8f0;border-left:4px solid #14b8a6}
.spine-part h4{color:#0f172a;margin-bottom:10px;font-size:1.2em;font-weight:800}
.measurement-section{background:linear-gradient(135deg,rgba(15,76,129,0.05),rgba(20,184,166,0.05));padding:40px;border-radius:15px;margin:30px 0}
.measurement-points{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:25px;margin:30px 0}
.measurement-point{background:white;padding:30px;border-radius:10px;box-shadow:0 1px 3px rgba(0,0,0,0.08);border:1px solid #e2e8f0;transition:transform 0.3s}
.measurement-point:hover{transform:translateY(-5px);box-shadow:0 8px 30px rgba(0,0,0,0.12)}
.measurement-point .number{background:#0f4c81;color:white;width:50px;height:50px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.5em;font-weight:900;margin-bottom:15px}
.measurement-point h4{color:#0f172a;margin-bottom:10px;font-size:1.3em;font-weight:800}
.measurement-point p{color:#475569;font-weight:400}
.highlight-box{background:#fff3cd;border-left:5px solid #ffc107;padding:20px;border-radius:8px;margin:20px 0}
.info-box{background:#d1ecf1;border-left:5px solid #14b8a6;padding:20px;border-radius:8px;margin:20px 0}
.cta-box{background:linear-gradient(135deg,#0f4c81,#14b8a6);color:white;padding:40px;border-radius:15px;text-align:center;margin:40px 0}
.cta-box h3{font-size:1.8em;margin-bottom:15px;font-weight:900}
.cta-box p{font-weight:400}
.cta-box .btn{display:inline-block;background:white;color:#0f4c81;padding:15px 35px;border-radius:10px;text-decoration:none;font-weight:700;margin:10px;transition:all 0.3s;box-shadow:0 2px 8px rgba(0,0,0,0.15)}
.cta-box .btn:hover{transform:translateY(-2px);box-shadow:0 4px 12px rgba(0,0,0,0.2)}
ul{margin:15px 0 15px 30px}
li{margin:8px 0;color:#475569}
.tabs{display:flex;justify-content:center;gap:0;margin:40px 0 0 0;border-bottom:3px solid #e2e8f0}
.tab-btn{background:none;border:none;padding:18px 35px;font-size:1.1em;font-weight:700;color:#64748b;cursor:pointer;transition:all 0.3s;border-bottom:3px solid transparent;margin-bottom:-3px;position:relative}
.tab-btn:hover{color:#0f4c81;background:rgba(15,76,129,0.05)}
.tab-btn.active{color:#0f4c81;border-bottom-color:#14b8a6;background:rgba(15,76,129,0.08)}
.tab-content{display:none;animation:fadeIn 0.4s}
.tab-content.active{display:block}
@keyframes fadeIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
@media(max-width:768px){.hero-mini h1{font-size:2em}.nav-links{gap:15px;font-size:0.9em}.tabs{flex-wrap:wrap;gap:5px}.tab-btn{padding:12px 20px;font-size:0.95em}}
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
<a href="/demo">🎥 Demo</a>
<a href="/developer" style="background:linear-gradient(135deg,#e67e22,#d35400);color:white!important;padding:10px 20px;border-radius:8px;font-weight:700">👨‍💻 Developer</a>
</div>
</div>
</nav>
<div class="hero-mini">
<div class="container">
<h1>🧠 Omurga ve Duruş Bilimi</h1>
<p>Sırtınızı tanıyın, sağlığınızı koruyun</p>
</div>
</div>
<div class="content">
<div class="container">
<div class="tabs">
<button class="tab-btn active" onclick="switchTab(event, 'anatomi')">📚 Bel ve Sırt Anatomisi</button>
<button class="tab-btn" onclick="switchTab(event, 'problemler')">⚠️ Yaygın Sırt Problemleri</button>
<button class="tab-btn" onclick="switchTab(event, 'cozum')">🎯 Duruş Farkındalığı</button>
</div>

<div id="anatomi" class="tab-content active">
<div class="section">
<h2>🦴 Bel ve Sırt Anatomisi</h2>
<p>Sağlıklı bir duruş için öncelikle omurganın ve destek kas sisteminin nasıl çalıştığını anlamak gerekir. Bu bölümde bel bölgesi ve sırt kaslarının yapısını detaylı olarak inceleyeceğiz.</p>

<h3>📚 İskelet Sistemi: Omurganın Temelleri</h3>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:30px;margin:30px 0;align-items:start">
<div>
<img src="/static/images/full-skeleton.png" alt="İnsan İskeleti" style="width:100%;border-radius:10px;box-shadow:0 5px 20px rgba(0,0,0,0.15)">
<p style="text-align:center;margin-top:10px;font-size:0.9em;color:#666"><em>Tam iskelet yapısı - Omurganın vücuttaki konumu</em></p>
</div>
<div>
<img src="/static/images/SpineAnatomy1.png" alt="Omurga Anatomisi" style="width:100%;border-radius:10px;box-shadow:0 5px 20px rgba(0,0,0,0.15)">
<p style="text-align:center;margin-top:10px;font-size:0.9em;color:#666"><em>Omurga detaylı anatomisi</em></p>
</div>
</div>

<p>Omurga, 33 omur kemikten oluşan esnek bir yapıdır. Her omur, üst üste gelerek hem esneklik hem de dayanıklılık sağlar. Özellikle <strong>bel (lumbar) bölgesi</strong> vücudun en fazla yük taşıyan kısmıdır.</p>

<div class="spine-parts">
<div class="spine-part">
<h4>🔵 Servikal (Boyun) - C1-C7</h4>
<p><strong>7 omur</strong></p>
<p>Başın hareketlerini sağlar. İçe doğru eğrilik (lordoz). En hareketli omurga bölgesidir.</p>
</div>
<div class="spine-part">
<h4>🟢 Torasik (Göğüs) - T1-T12</h4>
<p><strong>12 omur</strong></p>
<p>Kaburgalara tutunur. Dışa doğru eğrilik (kifoz). Göğüs kafesini korur ve stabilize eder.</p>
</div>
<div class="spine-part">
<h4>🟡 Lumbar (Bel) - L1-L5</h4>
<p><strong>5 omur - EN YÜKÜ TAŞIYAN BÖLGE</strong></p>
<p>İçe doğru eğrilik (lordoz). Vücudun ağırlığının %60'ını taşır. Duruş bozukluklarında en çok etkilenen bölge.</p>
</div>
<div class="spine-part">
<h4>🔴 Sakral & Koksiks - S1-S5</h4>
<p><strong>9 omur (kaynaşmış)</strong></p>
<p>Pelvis ile bağlantı. Dışa doğru eğrilik. Oturma ve yürüme sırasında temel destek.</p>
</div>
</div>

<div class="info-box">
<strong>💡 Önemli:</strong> Bel omurları (L1-L5) vücudun en büyük omurlarıdır çünkü en fazla yükü taşırlar. Kötü duruş nedeniyle bel disklerine binen yük <strong>normal durumun 3-4 katına</strong> kadar çıkabilir!
</div>

<h3>💪 Kas Sistemi: Sırtın Destek Yapısı</h3>
<div style="text-align:center;margin:30px 0">
<img src="/static/images/back-muscles.png" alt="Sırt Kasları" style="max-width:500px;width:100%;border-radius:10px;box-shadow:0 5px 20px rgba(0,0,0,0.15)">
<p style="text-align:center;margin-top:10px;font-size:0.9em;color:#666"><em>Sırt kas anatomisi - Katmanlar halinde</em></p>
</div>

<p>Sırt kasları üç ana katmanda çalışır:</p>

<div class="spine-parts" style="margin-top:20px">
<div class="spine-part" style="border-left-color:#e74c3c">
<h4>Yüzeysel Katman (Trapezius, Latissimus Dorsi)</h4>
<p><strong>Görev:</strong> Büyük hareketler - Kol kaldırma, çekme, omuz hareketleri</p>
<p>Masa başı çalışmada en çok yorulan ve gerilen kaslar. Kamburluğun ana sebebi.</p>
</div>
<div class="spine-part" style="border-left-color:#3498db">
<h4>Orta Katman (Rhomboidler, Serratus)</h4>
<p><strong>Görev:</strong> Omuz kemiklerini stabilize etme</p>
<p>Duruş kontrolünde kritik rol. Zayıflığı omuzların öne kaymasına neden olur.</p>
</div>
<div class="spine-part" style="border-left-color:#2ecc71">
<h4>Derin Katman (Erector Spinae, Multifidus)</h4>
<p><strong>Görev:</strong> Omurgayı dik tutma ve dengeleme</p>
<p>Bel bölgesindeki kaslar. Sürekli aktif kalmalıdır, zayıflığı bel ağrılarına yol açar.</p>
</div>
</div>

<div class="highlight-box">
<strong>⚡ Kritik Bilgi:</strong> Oturma pozisyonunda bel kasları (Erector Spinae) <strong>%40 daha az aktif</strong> hale gelir. Bu yüzden masa başında çalışanlar bel kaslarını kaybeder ve sırt ağrıları başlar!
</div>

<h3>🔄 Temel Hareketler ve Kas-İskelet Etkileşimi</h3>
<p>Günlük hareketler sırasında bel ve sırt kaslarınız nasıl çalışır? Aşağıdaki görselde farklı pozisyonlarda kasların aktivasyonunu görebilirsiniz:</p>

<div style="text-align:center;margin:30px 0">
<img src="/static/images/back-muscles-in-position.png" alt="Hareketlerde Sırt Kasları" style="max-width:100%;border-radius:15px;box-shadow:0 8px 30px rgba(0,0,0,0.2)">
<p style="margin-top:15px;font-size:1.1em;color:#667eea"><strong>Farklı pozisyonlarda sırt ve bel kaslarının aktivasyonu</strong></p>
<p style="font-size:0.95em;color:#666;max-width:800px;margin:10px auto">Bu görselde farklı vücut pozisyonlarında hangi kas gruplarının aktif olduğunu ve nasıl çalıştığını görebilirsiniz. Renk yoğunluğu kas aktivasyonunu gösterir.</p>
</div>

<div style="background:linear-gradient(135deg,rgba(102,126,234,0.05),rgba(118,75,162,0.05));padding:40px;border-radius:15px;margin:30px 0">
<h4 style="color:#667eea;font-size:1.4em;margin-bottom:25px;text-align:center">Pozisyon Analizi</h4>

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:25px">
<div style="background:white;padding:25px;border-radius:10px;box-shadow:0 3px 15px rgba(0,0,0,0.1);border-top:4px solid #e74c3c">
<div style="display:flex;align-items:center;gap:15px;margin-bottom:15px">
<div style="background:#e74c3c;color:white;width:45px;height:45px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.4em;font-weight:bold;flex-shrink:0">1</div>
<h4 style="color:#e74c3c;margin:0;font-size:1.2em">Oturma Pozisyonu</h4>
</div>
<p style="margin:10px 0"><strong>Bel:</strong> Bel eğriliği düzleşir veya tersine döner</p>
<p style="margin:10px 0"><strong>Çalışan Kaslar:</strong> Kalça ön kasları aşırı çalışır, bacak arka kasları sıkışır</p>
<p style="margin:10px 0"><strong>Uyuyan Kaslar:</strong> Bel dikleştirici kaslar, kalça ve karın kasları devre dışı (%40 azalma)</p>
<p style="background:#fff3cd;padding:12px;border-radius:6px;margin-top:15px;font-size:0.95em"><strong>⚠️ Risk:</strong> Bel disklerine <strong>%150 ekstra yük</strong>. Kas dengesizliği ve bel ağrısı başlar.</p>
</div>

<div style="background:white;padding:25px;border-radius:10px;box-shadow:0 3px 15px rgba(0,0,0,0.1);border-top:4px solid #2ecc71">
<div style="display:flex;align-items:center;gap:15px;margin-bottom:15px">
<div style="background:#2ecc71;color:white;width:45px;height:45px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.4em;font-weight:bold;flex-shrink:0">2</div>
<h4 style="color:#2ecc71;margin:0;font-size:1.2em">Ayakta Durma (Dik)</h4>
</div>
<p style="margin:10px 0"><strong>Bel:</strong> Tüm doğal eğrilikler korunur, omurga ideal dizilimde</p>
<p style="margin:10px 0"><strong>Çalışan Kaslar:</strong> Bel dikleştirici kaslar, derin sırt kasları ve karın kasları dengeli çalışır</p>
<p style="margin:10px 0"><strong>Denge:</strong> Kalça ve baldır kasları vücudu dengede tutar</p>
<p style="background:#d1ecf1;padding:12px;border-radius:6px;margin-top:15px;font-size:0.95em"><strong>✅ İdeal:</strong> Yük dengeli dağılır. Tüm kaslar optimal çalışır. En sağlıklı pozisyon.</p>
</div>

<div style="background:white;padding:25px;border-radius:10px;box-shadow:0 3px 15px rgba(0,0,0,0.1);border-top:4px solid #f39c12">
<div style="display:flex;align-items:center;gap:15px;margin-bottom:15px">
<div style="background:#f39c12;color:white;width:45px;height:45px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.4em;font-weight:bold;flex-shrink:0">3</div>
<h4 style="color:#f39c12;margin:0;font-size:1.2em">Öne Eğilme</h4>
</div>
<p style="margin:10px 0"><strong>Bel:</strong> Tüm omurlar öne doğru bükülerek diskler ön tarafta sıkışır</p>
<p style="margin:10px 0"><strong>Çalışan Kaslar:</strong> Bel dikleştirici kaslar uzayarak kontrolü sağlar, bacak arka kasları gergin</p>
<p style="margin:10px 0"><strong>Tehlike Noktası:</strong> L4-L5 (4. ve 5. bel omurları arası disk) maksimum yük altında</p>
<p style="background:#fff3cd;padding:12px;border-radius:6px;margin-top:15px;font-size:0.95em"><strong>🚨 Kritik:</strong> Kötü teknikle disk kayması riski. <strong>Her zaman dizlerden eğilmeli!</strong></p>
</div>

<div style="background:white;padding:25px;border-radius:10px;box-shadow:0 3px 15px rgba(0,0,0,0.1);border-top:4px solid #9b59b6">
<div style="display:flex;align-items:center;gap:15px;margin-bottom:15px">
<div style="background:#9b59b6;color:white;width:45px;height:45px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.4em;font-weight:bold;flex-shrink:0">4</div>
<h4 style="color:#9b59b6;margin:0;font-size:1.2em">Kambur Oturma</h4>
</div>
<p style="margin:10px 0"><strong>Bel ve Sırt:</strong> Bel düzleşir, göğüs bölgesi aşırı kamburlaşır, boyun öne kayar</p>
<p style="margin:10px 0"><strong>Çalışan Kaslar:</strong> Boyun ve omuz kasları aşırı gergin, göğüs kasları kısalır</p>
<p style="margin:10px 0"><strong>Uyuyan Kaslar:</strong> Tüm sırt ve bel kasları pasif, omuz arkası kasları zayıflar</p>
<p style="background:#ffe6f0;padding:12px;border-radius:6px;margin-top:15px;font-size:0.95em"><strong>🛑 Tehlike:</strong> En kötü pozisyon! Bel disklerine <strong>%185 yük</strong> + kronik boyun ve omuz ağrısı + solunumda %30 azalma.</p>
</div>
</div>
</div>

<div class="info-box" style="margin-top:30px">
<strong>🔬 Bilimsel Gerçek:</strong> Bel disklerine binen yük pozisyona göre değişir:
<ul style="margin-top:10px">
<li>Sırt üstü yatarken: <strong>25 kg</strong> - Diskler minimum yük altında</li>
<li>Ayakta dik dururken: <strong>100 kg</strong> - Temel yük (referans)</li>
<li>Dik otururken: <strong>140 kg</strong> - %40 artış</li>
<li>Öne eğik kötü oturuşta: <strong>185 kg</strong> - %85 artış!</li>
<li>20 kg ağırlık kaldırırken (kötü teknik): <strong>340 kg</strong> - %240 artış!!</li>
</ul>
<p style="margin-top:15px"><em>Kaynak: Nachemson, A. (1981). "Disc pressure measurements". Spine Journal</em></p>
</div>
</div>
</div>
</div>

<div id="problemler" class="tab-content">
<div class="section">
<h2>⚠️ Sırt Ağrısı: Neden ve Nasıl Oluşur?</h2>
<p style="font-size:1.1em;margin-bottom:30px">Sırt ağrısı, modern toplumun en yaygın sağlık problemlerinden biridir. Ancak ağrıyı anlamak için önce <strong>ağrı hissinin nasıl oluştuğunu</strong> bilmemiz gerekir.</p>

<div style="background:#fff3cd;border-left:5px solid #ffc107;padding:20px;border-radius:8px;margin:25px 0">
<p style="margin:0;font-size:0.95em"><strong>⚠️ Önemli Not:</strong> Bu sayfa <strong>mekanik (postural) sırt ağrıları</strong> hakkındadır - yani kötü duruş, uygunsuz oturma/yatma ve hatalı hareketlerden kaynaklanan ağrılar. İleri seviye tıbbi sorunlar (disk hernisi, spondilolizis, omurga kırıkları, tumor, enfeksiyon gibi) bu kapsamda değildir. Uzun süreli veya şiddetli ağrılarda mutlaka bir sağlık profesyoneline danışın.</p>
</div>

<h3>🧠 Ağrı Mekanizması: Vücudunuz Nasıl Alarm Veriyor?</h3>
<div style="background:linear-gradient(135deg,rgba(231,76,60,0.1),rgba(192,57,43,0.1));padding:35px;border-radius:15px;margin:30px 0">
<div style="display:grid;grid-template-columns:1fr 2fr;gap:30px;align-items:start">
<div style="text-align:center">
<img src="/static/images/disk-pain.png" alt="Disk Ağrısı Mekanizması" style="width:100%;max-width:250px;border-radius:10px;box-shadow:0 5px 20px rgba(0,0,0,0.15)">
<p style="font-size:0.9em;color:#666;margin-top:10px"><em>Disk basısı ve sinir sıkışması</em></p>
</div>
<div>
<h4 style="color:#e74c3c;margin-bottom:20px;font-size:1.3em">Sırt Ağrısının 4 Ana Mekanizması:</h4>

<div style="background:white;padding:25px;border-radius:10px;margin-bottom:20px;border-left:4px solid #e74c3c">
<h5 style="color:#e74c3c;margin-bottom:15px;font-size:1.2em">1️⃣ Disk Basıncı ve Şişmesi (Disk Bulging)</h5>
<p style="margin-bottom:15px;line-height:1.7"><strong>Ne olur?</strong> Omurlar arasındaki diskler jel benzeri bir çekirdek (nucleus pulposus) ve bunu saran lifli bir halka (annulus fibrosus) içerir. Aşırı veya asimetrik yük altında çekirdek bir tarafa kayar ve disk dışa doğru şişer.</p>
<p style="margin-bottom:15px;line-height:1.7"><strong>Neden ağrır?</strong> Disk dokusu içindeki ve çevresindeki basınç reseptörleri (nosiseptörler) aktive olur. Şişen disk, disk çevresindeki ligamentlere (posterior longitudinal ligament) ve dura mater (omuriliği saran zar) dokusuna baskı yapar. Bu baskı beyne "hasar riski" sinyali olarak iletilir.</p>
<p style="margin-bottom:15px;line-height:1.7"><strong>Hangi durumlarda olur?</strong></p>
<ul style="margin-left:20px;line-height:1.8">
<li>Uzun süreli öne eğik oturma (disk önden sıkışır, arkadan şişer)</li>
<li>Ağırlık kaldırırken belten eğilme (L4-L5 diski öne kayar)</li>
<li>Sürekli tek tarafa dönük çalışma (asimetrik disk basıncı)</li>
</ul>
<p style="background:#ffe6e6;padding:12px;border-radius:6px;margin-top:15px;font-size:0.95em"><strong>🚨 Risk:</strong> Kronik disk basıncı, zamanla disk yırtığına (annular tear) ve disk hernisine ilerleyebilir.</p>
</div>

<div style="background:white;padding:25px;border-radius:10px;margin-bottom:20px;border-left:4px solid #e67e22">
<h5 style="color:#e67e22;margin-bottom:15px;font-size:1.2em">2️⃣ Sinir Sıkışması (Radikülopati / Nerve Compression)</h5>
<p style="margin-bottom:15px;line-height:1.7"><strong>Ne olur?</strong> Omuriliğinden çıkan sinir kökleri (spinal nerve roots), şişen disk veya yanlış hizalanmış omur tarafından mekanik olarak sıkıştırılır. Bu sıkışma sinir iletimini bozar.</p>
<p style="margin-bottom:15px;line-height:1.7"><strong>Neden ağrır?</strong> Sinir lifleri mekanik basınca maruz kalınca iki şey olur:<br>
1️⃣ <strong>Ektopatik ateşleme:</strong> Sinir "elektrik kesintisi" gibi anormal ve düzensiz elektrik sinyalleri üretir.<br>
2️⃣ <strong>Nöroinflamasyon:</strong> Sıkışan sinir çevresinde lokal inflamasyon oluşur, bu da ağrı sinyallerini artırır.</p>
<p style="margin-bottom:15px;line-height:1.7"><strong>Karakteristik belirtiler:</strong></p>
<ul style="margin-left:20px;line-height:1.8">
<li>"Işınlayan ağrı" (radicular pain) - Boyundan kola veya belden bacağa yayılan ağrı</li>
<li>Karıncalanma, uyuşma, güç kaybı</li>
<li>Belirli bir sinir yolunu takip eden ağrı (dermatom paterni)</li>
</ul>
<p style="margin-bottom:15px;line-height:1.7"><strong>Hangi durumlarda olur?</strong></p>
<ul style="margin-left:20px;line-height:1.8">
<li>Boyun öne kayması (C5-C6-C7 sinir kökleri sıkışır → kol ağrısı)</li>
<li>Bel kayması veya disk hernisi (L5-S1 sıkışması → siyatik ağrısı)</li>
<li>Yan eğilme ve rotasyonda asimetrik yük (foraminal stenoz - sinir çıkış deliği daralır)</li>
</ul>
<p style="background:#fff3e0;padding:12px;border-radius:6px;margin-top:15px;font-size:0.95em"><strong>🚨 Risk:</strong> Uzun süreli sinir sıkışması kalıcı sinir hasarına ve kas zayıflığına yol açabilir.</p>
</div>

<div style="background:white;padding:25px;border-radius:10px;margin-bottom:20px;border-left:4px solid #f39c12">
<h5 style="color:#f39c12;margin-bottom:15px;font-size:1.2em">3️⃣ Kas Spazmı ve İskemi (Muscle Spasm & Ischemia)</h5>
<p style="margin-bottom:15px;line-height:1.7"><strong>Ne olur?</strong> Kötü duruş nedeniyle bazı kaslar sürekli kasılı kalır (protective muscle guarding). Kasılı kas kan akışını kısıtlar, bu da <strong>iskemi</strong> (yetersiz oksijenlenme) yaratır. İskemik kas hücrelerinde laktik asit ve diğer metabolik atıklar birikir.</p>
<p style="margin-bottom:15px;line-height:1.7"><strong>Neden ağrır?</strong> Laktik asit, bradikinin, substans P ve prostaglandin gibi algojenik (ağrı üreten) maddeler kas dokusundaki nosiseptörleri uyarır. Bu "yanma hissi" ve "tutulma hissi" yaratır.</p>
<p style="margin-bottom:15px;line-height:1.7"><strong>Spazm-ağrı döngüsü:</strong> Ağrı → daha fazla kas koruma spazmı → daha fazla iskemi → daha fazla ağrı. Bu kısır döngü kronik hale gelir.</p>
<p style="margin-bottom:15px;line-height:1.7"><strong>Hangi kaslar etkilenir?</strong></p>
<ul style="margin-left:20px;line-height:1.8">
<li><strong>Boyun:</strong> Trapezius, levator scapulae, sternocleidomastoid (bilgisayar başı duruşu)</li>
<li><strong>Üst sırt:</strong> Rhomboidler, middle trapezius (kamburluk)</li>
<li><strong>Bel:</strong> Erector spinae, quadratus lumborum, psoas (uzun süreli oturma)</li>
<li><strong>Kalça:</strong> Hip flexors (iliopsoas), piriformis (oturma sırasında kısalır)</li>
</ul>
<p style="margin-bottom:15px;line-height:1.7"><strong>Hangi durumlarda olur?</strong></p>
<ul style="margin-left:20px;line-height:1.8">
<li>8+ saat oturma (bel kasları %40 zayıflar, kalça fleksörleri kısalır)</li>
<li>Sürekli aynı pozisyonda kalma (statik yük)</li>
<li>Tek tarafa yük (çantayı hep aynı omuzda taşıma)</li>
</ul>
<p style="background:#fff9c4;padding:12px;border-radius:6px;margin-top:15px;font-size:0.95em"><strong>💡 İyi haber:</strong> Kas kaynaklı ağrılar, düzenli pozisyon değişikliği ve germe egzersizleri ile hızlıca düzeltilebilir.</p>
</div>

<div style="background:white;padding:25px;border-radius:10px;border-left:4px solid #9b59b6">
<h5 style="color:#9b59b6;margin-bottom:15px;font-size:1.2em">4️⃣ İnflamasyon ve Sensitizasyon (Tissue Inflammation)</h5>
<p style="margin-bottom:15px;line-height:1.7"><strong>Ne olur?</strong> Kronik mekanik stres ve mikro travmalar, doku hasarına ve bağışıklık sisteminin devreye girmesine neden olur. Bağışıklık sistemi hasar bölgesine inflamatuar kimyasallar gönderir.</p>
<p style="margin-bottom:15px;line-height:1.7"><strong>Neden ağrır?</strong> İnflamatuar sitokinler (IL-1, IL-6, TNF-α) ağrı reseptörlerini aşırı duyarlı hale getirir (peripheral sensitization). Ayrıca prostaglandinler ve histamin gibi maddeler vazodilatasyon (damar genişlemesi) yaparak şişlik ve hassasiyet yaratır.</p>
<p style="margin-bottom:15px;line-height:1.7"><strong>Kronik inflamasyon:</strong> Tekrarlayan mikro travmalar iyileşme şansı vermez, bu da düşük seviyeli ama sürekli inflamasyona yol açar. Zamanla <strong>santral sensitizasyon</strong> gelişir - beyin ağrı sinyallerini abartarak algılar.</p>
<p style="margin-bottom:15px;line-height:1.7"><strong>Hangi yapılar iltihaplanır?</strong></p>
<ul style="margin-left:20px;line-height:1.8">
<li><strong>Facet eklemler:</strong> Omur arası küçük eklemler - sürtünme ve aşınma (facet joint syndrome)</li>
<li><strong>Ligamentler:</strong> Omurları bağlayan lifli bantlar - aşırı gerilme ve mikro yırtıklar</li>
<li><strong>Tendonlar:</strong> Kas-kemik bağlantıları - tekrarlayan yük altında tendinitis</li>
<li><strong>Bursalar:</strong> Eklem çevresindeki sıvı keseler - baskı ve sürtünme ile bursitis</li>
</ul>
<p style="margin-bottom:15px;line-height:1.7"><strong>Hangi durumlarda olur?</strong></p>
<ul style="margin-left:20px;line-height:1.8">
<li>Aşırı kamburluk (facet eklemler sürekli sürtünür)</li>
<li>Tekrarlayan hatalı hareketler (kaldır-bırak işleri)</li>
<li>Kronik duruş bozukluğu (yıllarca süren kötü duruş)</li>
</ul>
<p style="background:#ffe6f0;padding:12px;border-radius:6px;margin-top:15px;font-size:0.95em"><strong>🚨 Risk:</strong> Kronik inflamasyon, eklem dejenerasyonuna (osteoartrit) ve kalıcı doku değişikliklerine yol açabilir.</p>
</div>
</div>
</div>

<div class="info-box" style="margin-top:20px">
<strong>🔬 Bilimsel Gerçek:</strong> Ağrı, vücudun bir <strong>"koruma mekanizması"</strong>dır. Beyin, hasar potansiyeli algıladığında hareketi durdurmak için ağrı sinyali üretir. Ancak kronik kötü duruşta bu alarm sistemi sürekli aktif kalır ve kronik ağrıya dönüşür. İyi haber: Mekanik (postural) ağrıların %80'i erken farkındalık ve düzeltme ile tam olarak iyileşir.
</div>
</div>

<h3 style="margin-top:50px">🚨 3 Ana Duruş Bozukluğu ve Etkileri</h3>
<p style="font-size:1.05em;margin-bottom:30px">Modern yaşam tarzı, omurganın doğal eğriliklerini bozar. İşte en yaygın 3 problem:</p>

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:30px;margin:40px 0">
<div>
<img src="/static/images/correct-vs-textneck.png" alt="Doğru vs Text Neck" style="width:100%;border-radius:10px;box-shadow:0 5px 20px rgba(0,0,0,0.15)">
<div style="background:white;padding:25px;border-radius:10px;box-shadow:0 3px 15px rgba(0,0,0,0.1);margin-top:-30px;position:relative">
<h4 style="color:#e74c3c;margin-bottom:15px;font-size:1.3em">1. Text Neck (Boyun Kayması)</h4>
<p style="margin-bottom:10px"><strong>Ne olur?</strong> Baş öne kayar, boyun eğriliği düzleşir veya tersine döner</p>
<p style="margin-bottom:10px"><strong>Ağrı mekanizması:</strong></p>
<ul style="margin-left:20px;line-height:1.8">
<li>C5-C6-C7 omurlarına <strong>aşırı yük</strong> (15° = +12 kg)</li>
<li>Boyun kaslarında <strong>sürekli gerilim</strong> → kas spazmı</li>
<li>Servikal diskler <strong>ön taraftan sıkışır</strong> → disk basıncı</li>
<li>Trapezius ve levator scapulae kasları <strong>laktik asit birikimi</strong></li>
</ul>
<div style="background:#ffe6e6;padding:15px;border-radius:8px;margin-top:15px">
<strong>⚠️ Sonuç:</strong> Kronik boyun ağrısı, baş ağrısı, omuz tutulması, sinir sıkışması (C6-C7).
</div>
</div>
</div>

<div>
<img src="/static/images/correct-vs-kyphosis.png" alt="Doğru vs Kamburluk" style="width:100%;border-radius:10px;box-shadow:0 5px 20px rgba(0,0,0,0.15)">
<div style="background:white;padding:25px;border-radius:10px;box-shadow:0 3px 15px rgba(0,0,0,0.1);margin-top:-30px;position:relative">
<h4 style="color:#e67e22;margin-bottom:15px;font-size:1.3em">2. Kyphosis (Kamburluk)</h4>
<p style="margin-bottom:10px"><strong>Ne olur?</strong> Göğüs bölgesi aşırı kamburlaşır, omuzlar öne düşer</p>
<p style="margin-bottom:10px"><strong>Ağrı mekanizması:</strong></p>
<ul style="margin-left:20px;line-height:1.8">
<li>T1-T12 torasik omurları <strong>anormal açıda</strong> yük taşır</li>
<li>Rhomboid ve middle trapezius kasları <strong>aşırı uzar</strong> → zayıflar</li>
<li>Göğüs kasları (pectoralis) <strong>kısalır ve sıkışır</strong></li>
<li>Faset eklemler (omur arası eklemler) <strong>birbiririne sürtünür</strong> → inflamasyon</li>
</ul>
<div style="background:#fff3e0;padding:15px;border-radius:8px;margin-top:15px">
<strong>⚠️ Sonuç:</strong> Üst sırt ağrısı, göğüs sıkışması, solunum kapasitesi %30 azalma, omur artriti riski.
</div>
</div>
</div>

<div>
<img src="/static/images/correct-vs-pelvic.png" alt="Doğru vs Bel Eğriliği" style="width:100%;border-radius:10px;box-shadow:0 5px 20px rgba(0,0,0,0.15)">
<div style="background:white;padding:25px;border-radius:10px;box-shadow:0 3px 15px rgba(0,0,0,0.1);margin-top:-30px;position:relative">
<h4 style="color:#f39c12;margin-bottom:15px;font-size:1.3em">3. Lordosis (Aşırı Bel Eğriliği)</h4>
<p style="margin-bottom:10px"><strong>Ne olur?</strong> Bel içe doğru aşırı eğrilir, pelvis öne tilt olur</p>
<p style="margin-bottom:10px"><strong>Ağrı mekanizması:</strong></p>
<ul style="margin-left:20px;line-height:1.8">
<li>L4-L5 omurları <strong>aşırı lordoz</strong> → disk arka taraftan sıkışır</li>
<li>Erector spinae kasları <strong>sürekli kasılı</strong> → kronik spazm</li>
<li>Karın kasları <strong>zayıf ve pasif</strong> → destek kaybı</li>
<li>Facet eklemler <strong>birbirine çok yakın</strong> → sürtünme ve ağrı</li>
</ul>
<div style="background:#fff9c4;padding:15px;border-radius:8px;margin-top:15px">
<strong>⚠️ Sonuç:</strong> Alt bel ağrısı, kalça ağrısı, disk hernisi riski, pelvik instabilite.
</div>
</div>
</div>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:25px;margin:40px 0">
<div style="background:linear-gradient(135deg,#ff6b6b,#ee5a6f);color:white;padding:30px;border-radius:15px;box-shadow:0 5px 20px rgba(0,0,0,0.15)">
<h4 style="font-size:1.3em;margin-bottom:15px">📱 Text Neck Sendromu</h4>
<p style="margin-bottom:15px">Başınız her 15° öne eğildiğinde boyun kaslarına <strong>+12 kg</strong> yük eklenir.</p>
<p style="background:rgba(255,255,255,0.2);padding:15px;border-radius:8px;font-size:0.95em">Günde ortalama 4 saat telefon kullanan bir kişi, boynuna <strong>yılda 700-1400 saat ekstra yük</strong> bindiriyor!</p>
</div>
<div style="background:linear-gradient(135deg,#f093fb,#f5576c);color:white;padding:30px;border-radius:15px;box-shadow:0 5px 20px rgba(0,0,0,0.15)">
<h4 style="font-size:1.3em;margin-bottom:15px">💺 Ofis Sendromu</h4>
<p style="margin-bottom:15px">8 saat oturma = Bel kaslarında <strong>%40 güç kaybı</strong> + Kalça fleksörlerinde kısalma</p>
<p style="background:rgba(255,255,255,0.2);padding:15px;border-radius:8px;font-size:0.95em">30 yaşındaki bir ofis çalışanı, 50 yaşındaki aktif bir kişiden daha zayıf sırt kaslarına sahip olabilir.</p>
</div>
<div style="background:linear-gradient(135deg,#667eea,#764ba2);color:white;padding:30px;border-radius:15px;box-shadow:0 5px 20px rgba(0,0,0,0.15)">
<h4 style="font-size:1.3em;margin-bottom:15px">🏥 Sağlık Maliyeti</h4>
<p style="margin-bottom:15px">Kötü duruş nedeniyle oluşan problemler yılda <strong>milyarlarca TL</strong> sağlık harcamasına yol açıyor.</p>
<p style="background:rgba(255,255,255,0.2);padding:15px;border-radius:8px;font-size:0.95em">İş gücü kaybı + tedavi maliyeti + ameliyat riskleri = Önlenebilir bir sağlık krizi!</p>
</div>
</div>

<div class="highlight-box">
<strong>⚡ İstatistik:</strong> Ofis çalışanlarının %73'ü en az bir duruş bozukluğu yaşıyor. Bunların <strong>%65'i erken farkındalık ile önlenebilir!</strong>
</div>

<h3 style="margin-top:60px">🏠 Günlük Hayatta Sırt Ağrısına Yol Açan 4 Ana Durum</h3>
<p style="font-size:1.05em;margin-bottom:30px">Sırt ağrılarının çoğu günlük aktivitelerdeki yanlış pozisyonlardan kaynaklanır. İşte en sık yapılan 4 hata ve ağrı mekanizmaları:</p>

<div style="background:linear-gradient(135deg,rgba(52,152,219,0.1),rgba(41,128,185,0.1));padding:40px;border-radius:15px;margin:30px 0;border-left:5px solid #3498db">
<h4 style="color:#3498db;font-size:1.5em;margin-bottom:25px">💺 1. Uygunsuz Oturma</h4>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:30px">
<div>
<h5 style="color:#2c3e50;margin-bottom:15px">❌ Yanlış Oturuş Pozisyonları:</h5>
<ul style="line-height:2">
<li><strong>Öne eğik oturma:</strong> Bel düzleşir, disk arkadan şişer</li>
<li><strong>Sırtı desteksiz oturma:</strong> Bel kasları sürekli aktif, yorulur</li>
<li><strong>Bacak bacak üstüne atma:</strong> Pelvis asimetrik döner, bir taraf yüklenmiş olur</li>
<li><strong>Çok yumuşak/derin koltuk:</strong> Bel lordozu kaybolur, pelvis posterior tilt yapar</li>
<li><strong>Monitör çok alçak/yüksek:</strong> Boyun sürekli eğik veya uzatılmış</li>
</ul>
</div>
<div>
<h5 style="color:#e74c3c;margin-bottom:15px">🔥 Oluşan Ağrı Mekanizması:</h5>
<div style="background:white;padding:20px;border-radius:10px;margin-bottom:15px">
<p style="margin:0"><strong>Disk basıncı:</strong> L4-L5 diskine %150-185 ekstra yük biner. 8 saat kötü oturuş = disk dokusu sürekli deforme olur.</p>
</div>
<div style="background:white;padding:20px;border-radius:10px;margin-bottom:15px">
<p style="margin:0"><strong>Kas yorgunluğu:</strong> Bel dikleştirici kaslar (erector spinae) ve boyun kasları (trapezius) sürekli kasılı kalır → laktik asit birikimi → yanma hissi.</p>
</div>
<div style="background:white;padding:20px;border-radius:10px">
<p style="margin:0"><strong>Kas dengesizliği:</strong> Kalça fleksörleri kısalır, bel kasları zayıflar, karın kasları devre dışı kalır → kronik stabilite kaybı.</p>
</div>
</div>
</div>
<p style="margin-top:20px;background:rgba(52,152,219,0.15);padding:15px;border-radius:8px"><strong>💡 Önlem:</strong> Her 30 dakikada ayağa kalkın, bel desteği kullanın, monitörü göz hizasına ayarlayın. İdeal oturuş: Ayaklar yerde, dizler 90°, bel destekli, omuzlar gevşek.</p>
</div>

<div style="background:linear-gradient(135deg,rgba(155,89,182,0.1),rgba(142,68,173,0.1));padding:40px;border-radius:15px;margin:30px 0;border-left:5px solid #9b59b6">
<h4 style="color:#9b59b6;font-size:1.5em;margin-bottom:25px">🛏️ 2. Uygunsuz Yatma</h4>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:30px">
<div>
<h5 style="color:#2c3e50;margin-bottom:15px">❌ Yanlış Yatış Pozisyonları:</h5>
<ul style="line-height:2">
<li><strong>Yüzüstü yatma:</strong> Boyun 90° döner, servikal omurlar burkulur</li>
<li><strong>Çok yüksek/çok düz yastık:</strong> Boyun eğriliği bozulur</li>
<li><strong>Çok yumuşak yatak:</strong> Omurga "U" şeklinde çöker, destek kaybeder</li>
<li><strong>Çok sert yatak:</strong> Omuz ve kalça baskı noktaları oluşur</li>
<li><strong>Yan yatarken bacak desteksiz:</strong> Üstteki bacak pelvis çeker, bel yan eğilir</li>
</ul>
</div>
<div>
<h5 style="color:#e74c3c;margin-bottom:15px">🔥 Oluşan Ağrı Mekanizması:</h5>
<div style="background:white;padding:20px;border-radius:10px;margin-bottom:15px">
<p style="margin:0"><strong>Statik yükleme:</strong> Aynı pozisyon 7-8 saat sürer. Disk ve eklemler tek yönlü baskı altında → doku sıvı kaybı ve sabah sertliği.</p>
</div>
<div style="background:white;padding:20px;border-radius:10px;margin-bottom:15px">
<p style="margin:0"><strong>Sinir sıkışması:</strong> Yanlış boyun pozisyonu C5-C6 sinir köklerine baskı yapar → sabah kolda uyuşma. Yan yatarken omuz basısı brakial pleksus sinir sıkışmasına yol açar.</p>
</div>
<div style="background:white;padding:20px;border-radius:10px">
<p style="margin:0"><strong>Facet joint irritasyonu:</strong> Boyun ve bel bölgesi facet eklemler anormal açıda kalır → mikro travma → sabah tutulma ve ağrı.</p>
</div>
</div>
</div>
<p style="margin-top:20px;background:rgba(155,89,182,0.15);padding:15px;border-radius:8px"><strong>💡 Önlem:</strong> En ideal: sırtüstü (boyun destekli) veya yan yatış (bacaklar arası yastıkla). Yastık boyun eğriliğini koruyacak yükseklikte olmalı. Orta sertlikte yatak tercih edin.</p>
</div>

<div style="background:linear-gradient(135deg,rgba(241,196,15,0.1),rgba(243,156,18,0.1));padding:40px;border-radius:15px;margin:30px 0;border-left:5px solid #f39c12">
<h4 style="color:#f39c12;font-size:1.5em;margin-bottom:25px">🚶 3. Uygunsuz Duruş (Ayakta Durma)</h4>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:30px">
<div>
<h5 style="color:#2c3e50;margin-bottom:15px">❌ Yanlış Ayakta Duruş Pozisyonları:</h5>
<ul style="line-height:2">
<li><strong>Swayback duruş:</strong> Pelvis öne itilir, bel aşırı lordoz, göğüs kamburlaşır</li>
<li><strong>Tek ayak üzerinde durma:</strong> Pelvis yan tilt yapar, omurga "S" eğrisi oluşturur</li>
<li><strong>Ağırlık topuklarda:</strong> Bel düzleşir, dizler kilitlenmiş, pelvis posterior tilt</li>
<li><strong>Baş öne:</strong> Forward head posture, boyun kasları aşırı yüklenir</li>
<li><strong>Asimetrik omuz:</strong> Çanta tek omuzda → trapezius aşırı gergin, omurga yan eğilir</li>
</ul>
</div>
<div>
<h5 style="color:#e74c3c;margin-bottom:15px">🔥 Oluşan Ağrı Mekanizması:</h5>
<div style="background:white;padding:20px;border-radius:10px;margin-bottom:15px">
<p style="margin:0"><strong>Postural kas yorgunluğu:</strong> Anti-gravity kaslar (erector spinae, quadratus lumborum) sürekli çalışır ancak optimal hizada değil → verimsiz kas çalışması → erken yorulma ve spazm.</p>
</div>
<div style="background:white;padding:20px;border-radius:10px;margin-bottom:15px">
<p style="margin:0"><strong>Asimetrik yükleme:</strong> Tek ayak veya tek omuz yükleme, bir taraf kasları aşırı çalışır → kas dengesizliği → trigger point (tetik nokta) oluşumu.</p>
</div>
<div style="background:white;padding:20px;border-radius:10px">
<p style="margin:0"><strong>Eklem stres:</strong> Swayback duruşta L5-S1 facet eklemler sürekli sıkışır → facet joint syndrome.</p>
</div>
</div>
</div>
<p style="margin-top:20px;background:rgba(241,196,15,0.15);padding:15px;border-radius:8px"><strong>💡 Önlem:</strong> İdeal duruş: Kulak-omuz-kalça-ayak bilekleri aynı hizada. Ağırlık ayakta dengeli dağıtılmalı. Her 20 dakikada pozisyon değiştirin. Çantayı sık sık omuz değiştirerek taşıyın.</p>
</div>

<div style="background:linear-gradient(135deg,rgba(231,76,60,0.1),rgba(192,57,43,0.1));padding:40px;border-radius:15px;margin:30px 0;border-left:5px solid #e74c3c">
<h4 style="color:#e74c3c;font-size:1.5em;margin-bottom:25px">🏋️ 4. Uygunsuz Ağırlık Kaldırma</h4>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:30px">
<div>
<h5 style="color:#2c3e50;margin-bottom:15px">❌ Yanlış Kaldırma Teknikleri:</h5>
<ul style="line-height:2">
<li><strong>Belten eğilerek kaldırma:</strong> L4-L5 diski maksimum öne kayma riski</li>
<li><strong>Dönerek kaldırma:</strong> Rotasyon + fleksiyon kombinasyonu = disk yırtığı riski</li>
<li><strong>Ağırlık vücuttan uzak:</strong> Moment kolu uzar, bel omurlarına kat kat yük eklenir</li>
<li><strong>Ani hızlı kaldırma:</strong> Kaslar hazır değil → bel koruma spazmı</li>
<li><strong>Baş aşağı eğik:</strong> Boyun ve bel aynı anda fleksiyon → çift risk</li>
</ul>
</div>
<div>
<h5 style="color:#e74c3c;margin-bottom:15px">🔥 Oluşan Ağrı Mekanizması:</h5>
<div style="background:white;padding:20px;border-radius:10px;margin-bottom:15px">
<p style="margin:0"><strong>Aşırı disk basıncı:</strong> Yanlış teknikle 10 kg yük kaldırmak, L4-L5 diskine <strong>200-340 kg yük</strong> bindirir! Disk annulus fibrosus (dış halka) lifleri yırtılabilir → disk hernisi başlangıcı.</p>
</div>
<div style="background:white;padding:20px;border-radius:10px;margin-bottom:15px">
<p style="margin:0"><strong>Rotasyonel stres:</strong> Dönerek kaldırmak, disk liflerine burulma stresi ekler. Disk lifleri burulmaya karşı en zayıftır → annular tear (disk yırtığı) riski 3-4 kat artar.</p>
</div>
<div style="background:white;padding:20px;border-radius:10px;margin-bottom:15px">
<p style="margin:0"><strong>Ligament zorlanması:</strong> Hızlı kaldırma veya ani hareket, posterior longitudinal ligament ve interspinous ligamentleri aşırı gerer → mikro yırtıklar ve inflamasyon.</p>
</div>
<div style="background:white;padding:20px;border-radius:10px">
<p style="margin:0"><strong>Akut kas yaralanması:</strong> Hazır olmayan kas aniden yüklenince myofibril (kas lifi) yırtılmaları oluşur → akut bel burkulması (lumbar strain).</p>
</div>
</div>
</div>
<p style="margin-top:20px;background:rgba(231,76,60,0.15);padding:15px;border-radius:8px"><strong>💡 Önlem:</strong> <strong>DİZLERDEN EĞİLİN, BELİ DİK TUTUN!</strong> Ağırlık vücuda yakın olmalı. Karın kaslarını sıkın (core aktivasyonu). Dönerken adım atın, beli döndürmeyin. Çok ağır yük varsa yardım isteyin veya parçalara bölün.</p>
</div>

<div style="background:linear-gradient(135deg,#667eea,#764ba2);color:white;padding:35px;border-radius:15px;margin:40px 0">
<h4 style="font-size:1.4em;margin-bottom:20px;text-align:center">⚡ Kritik Uyarı: Birikimli Mikro Travma Sendromu</h4>
<p style="line-height:1.8;font-size:1.05em;text-align:center;max-width:900px;margin:0 auto">Bu 4 yanlış pozisyon tek başına hemen ağrı yaratmayabilir. Ancak <strong>günde 8-12 saat, haftada 5-7 gün, aylarca-yıllarca tekrarlandığında</strong> omurganıza binlerce kez mikro travma birikir. Sonuç: 30'lu yaşlarda başlayan kronik sırt ağrıları, 40'lı yaşlarda disk problemleri, 50'li yaşlarda ameliyat ihtiyacı. <strong>Fakat erken farkındalık ile %80'i önlenebilir!</strong></p>
</div>

<div class="cta-box" style="margin-top:50px">
<h3>Duruşunuzu Kontrol Edin!</h3>
<p>Bu problemlerden kaçını yaşıyorsunuz? SpineGuard ile gerçek zamanlı duruş analizi yapın ve erken farkındalık kazanın.</p>
<a href="/demo" class="btn">🎥 Ücretsiz Analiz Başlat</a>
</div>
</div>
</div>

<div id="cozum" class="tab-content">
<div class="section">
<h2>🎯 Duruş Farkındalığı: Problemleri Önlemenin Anahtarı</h2>
<p style="font-size:1.1em;margin-bottom:30px">Duruş problemlerinin <strong>%65'i erken farkındalık ile önlenebilir</strong>. Ancak çoğu insan kötü duruşunun farkında değildir - ta ki ağrı başlayana kadar.</p>

<h3>🏢 Gündelik Hayatta Duruş Farkındalığının Önemi</h3>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:25px;margin:30px 0">
<div style="background:linear-gradient(135deg,rgba(102,126,234,0.1),rgba(118,75,162,0.1));padding:30px;border-radius:15px;border-left:4px solid #667eea">
<h4 style="color:#667eea;font-size:1.3em;margin-bottom:15px">💼 İş Yerinde</h4>
<p style="margin-bottom:15px">8 saatlik masa başı çalışma sırasında <strong>ortalama 200+ kez</strong> kötü duruşa geçiş yapılır.</p>
<p style="background:white;padding:15px;border-radius:8px;font-size:0.95em"><strong>🔬 Bilimsel gerçek:</strong> Her 30 dakikada bir duruş değişikliği yapan çalışanlar, %40 daha az sırt ağrısı yaşarlar (Cornell University, 2019).</p>
</div>
<div style="background:linear-gradient(135deg,rgba(231,76,60,0.1),rgba(192,57,43,0.1));padding:30px;border-radius:15px;border-left:4px solid #e74c3c">
<h4 style="color:#e74c3c;font-size:1.3em;margin-bottom:15px">🏋️ Spor ve Yük Taşıma</h4>
<p style="margin-bottom:15px">Yanlış teknikle 10 kg yük kaldırmak, <strong>bel disklerine 200 kg yük</strong> bindirir.</p>
<p style="background:white;padding:15px;border-radius:8px;font-size:0.95em"><strong>🔬 Bilimsel gerçek:</strong> Gerçek zamanlı duruş geri bildirimi, spor yaralanmalarını %58 azaltır (Sports Medicine Journal, 2020).</p>
</div>
<div style="background:linear-gradient(135deg,rgba(155,89,182,0.1),rgba(142,68,173,0.1));padding:30px;border-radius:15px;border-left:4px solid #9b59b6">
<h4 style="color:#9b59b6;font-size:1.3em;margin-bottom:15px">🛏️ Yatarken</h4>
<p style="margin-bottom:15px">Yanlış yatış pozisyonu, <strong>7-8 saat boyunca</strong> boyun ve bel omurlarına anormal yük uygular.</p>
<p style="background:white;padding:15px;border-radius:8px;font-size:0.95em"><strong>🔬 Bilimsel gerçek:</strong> Düzenli pozisyon değişikliği, sabah sırt ağrısını %52 azaltır (Sleep Research Society, 2021).</p>
</div>
</div>

<div class="info-box" style="margin:30px 0">
<h4 style="color:#17a2b8;margin-bottom:15px;font-size:1.2em">📊 Kritik Bulgular</h4>
<p style="margin-bottom:10px">Stanford Medicine tarafından 5 yıllık araştırma:</p>
<ul style="margin-top:10px">
<li><strong>Gerçek zamanlı farkındalık:</strong> Kronik sırt ağrısını %63 azaltır</li>
<li><strong>30 dakikalık pozisyon hatırlatıcıları:</strong> Disk basıncını %45 düşürür</li>
<li><strong>Aktif duruş düzeltme:</strong> İlk 3 ayda kas gücünü %38 artırır</li>
<li><strong>Erken müdahale:</strong> Ameliyat ihtiyacını %71 azaltır</li>
</ul>
<p style="margin-top:15px;font-style:italic;font-size:0.95em">Sonuç: Duruş farkındalığı, tedaviden 10 kat daha etkili ve ekonomiktir.</p>
</div>

<h3 style="margin-top:50px">📡 SpineGuard: IMU Sensör Tabanlı Gerçek Zamanlı Duruş İzleme</h3>
<p style="font-size:1.05em;margin-bottom:30px">SpineGuard, vücudunuza yerleştirilen <strong>IMU (Inertial Measurement Unit) sensörleri</strong> ile milimetre hassasiyetinde duruş takibi yapar. 3 farklı seviyede çözüm sunuyoruz:</p>

<div style="background:linear-gradient(135deg,#667eea,#764ba2);color:white;padding:40px;border-radius:20px;margin:40px 0">
<h3 style="font-size:2em;margin-bottom:20px;text-align:center">🥉 Seviye 1: BASIC</h3>
<p style="font-size:1.1em;text-align:center;margin-bottom:30px">2 IMU Sensör - Bel ve Sırt İzleme</p>

<div style="display:grid;grid-template-columns:1fr 1.5fr;gap:30px;align-items:start;margin-top:30px">
<div style="text-align:center">
<img src="/static/images/sensor-positions.jpg" alt="Basic Sensör Pozisyonları" style="width:100%;max-width:300px;border-radius:10px;box-shadow:0 5px 20px rgba(0,0,0,0.3)">
<p style="margin-top:15px;font-size:0.95em">2 sensör ile temel duruş izleme</p>
</div>
<div>
<h4 style="margin-bottom:20px;font-size:1.3em">Sensör Yerleşimi:</h4>
<div style="background:rgba(255,255,255,0.15);padding:20px;border-radius:10px;margin-bottom:15px">
<h5 style="margin-bottom:10px">📍 Sensör 1: L4 (4. Bel Omuru)</h5>
<p style="margin:0;font-size:0.95em">Bel bölgesi - Lumbar eğriliği ve pelvik tilt ölçümü</p>
</div>
<div style="background:rgba(255,255,255,0.15);padding:20px;border-radius:10px">
<h5 style="margin-bottom:10px">📍 Sensör 2: T8-T10 Arası (8-10. Göğüs Omuru)</h5>
<p style="margin:0;font-size:0.95em">Üst sırt - Göğüs kamburluğu ve sırt eğimi ölçümü</p>
</div>
</div>
</div>

<div style="background:rgba(255,255,255,0.1);padding:30px;border-radius:15px;margin-top:30px">
<h4 style="margin-bottom:20px;font-size:1.3em">Bu 2 Sensör Neler Algılayabilir?</h4>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">
<div>
<h5 style="color:#ffd700;margin-bottom:15px">✅ Algılayabileceği Hareketler:</h5>
<ul style="line-height:2">
<li><strong>Oturma duruşu:</strong> L4 sensörü bel düzleşmesini, T8-T10 sensörü kamburlaşmayı algılar</li>
<li><strong>Ayakta durma:</strong> Her iki sensörün açısı referans değerlerle karşılaştırılır</li>
<li><strong>Öne eğilme:</strong> L4'te 40°+, T8-T10'da 25°+ fleksiyon tespit edilir</li>
<li><strong>Yan eğilme:</strong> Lateral tilt (yan eğim) her iki sensörde ölçülür</li>
<li><strong>Rotasyon:</strong> Sağa-sola dönme hareketleri gyroscope ile algılanır</li>
</ul>
</div>
<div>
<h5 style="color:#ffd700;margin-bottom:15px">📊 Teknik Detaylar:</h5>
<ul style="line-height:2">
<li><strong>Örnekleme hızı:</strong> 100 Hz (saniyede 100 ölçüm)</li>
<li><strong>Hassasiyet:</strong> ±0.5° açı, ±0.02g ivme</li>
<li><strong>Kapsama:</strong> ±180° rotasyon, ±90° fleksiyon/ekstansiyon</li>
<li><strong>Gecikme:</strong> <10ms (gerçek zamanlı)</li>
</ul>
</div>
</div>
</div>
</div>

<div style="margin-top:40px">
<h4 style="color:#667eea;font-size:1.4em;margin-bottom:25px">Örnek Hareket Senaryoları:</h4>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:25px">
<div style="background:white;padding:25px;border-radius:10px;border-top:4px solid #3498db">
<img src="/static/images/sitting-position-per-sensor.jpg" alt="Oturma Pozisyonu Sensör" style="width:100%;border-radius:8px;margin-bottom:15px">
<h5 style="color:#3498db;margin-bottom:10px">💺 Oturma Pozisyonu</h5>
<p style="font-size:0.95em;line-height:1.7"><strong>L4 sensörü:</strong> Bel eğriliği 15° → 5° düşüyor (lordoz kaybı)<br>
<strong>T8-T10 sensörü:</strong> Sırt eğimi 10° → 35° artıyor (kamburlaşma)<br>
<strong>Sonuç:</strong> "Kötü oturuş tespit edildi" uyarısı</p>
</div>

<div style="background:white;padding:25px;border-radius:10px;border-top:4px solid #e67e22">
<img src="/static/images/forward-head-posture-per-sensor.png" alt="Forward Head Sensör" style="width:100%;border-radius:8px;margin-bottom:15px">
<h5 style="color:#e67e22;margin-bottom:10px">📱 Öne Eğik Duruş</h5>
<p style="font-size:0.95em;line-height:1.7"><strong>T8-T10 sensörü:</strong> 40°+ öne eğim (kompansasyon hareketi)<br>
<strong>L4 sensörü:</strong> Bel lordozu artıyor (dengeleme)<br>
<strong>Sonuç:</strong> "Text neck algılandı - başınızı dik tutun"</p>
</div>

<div style="background:white;padding:25px;border-radius:10px;border-top:4px solid #27ae60">
<img src="/static/images/movements-per-sensor.webp" alt="Hareketler Sensör" style="width:100%;border-radius:8px;margin-bottom:15px">
<h5 style="color:#27ae60;margin-bottom:10px">🏋️ Yük Kaldırma</h5>
<p style="font-size:0.95em;line-height:1.7"><strong>L4 sensörü:</strong> 60°+ fleksiyon (tehlikeli eğim)<br>
<strong>T8-T10 sensörü:</strong> Ani ivmelenme (yük algılandı)<br>
<strong>Sonuç:</strong> "Tehlikeli! Dizlerden eğilin" sesli uyarı</p>
</div>
</div>
</div>

<div class="highlight-box" style="margin-top:30px">
<strong>✅ Basic Seviye Yeterli mi?</strong> Gündelik hayatta en yaygın 3 problemi (kamburluk, bel lordozu, yan eğilme) %95 doğrulukla tespit eder. Masa başı çalışanlar ve hafif aktivite yapanlar için ideal.
</div>

<div style="background:linear-gradient(135deg,#e67e22,#d35400);color:white;padding:40px;border-radius:20px;margin:60px 0 40px 0">
<h3 style="font-size:2em;margin-bottom:20px;text-align:center">🥈 Seviye 2: PRO</h3>
<p style="font-size:1.1em;text-align:center;margin-bottom:30px">3 IMU Sensör - Boyun ve Baş Hareketleri Eklendi</p>

<div style="display:grid;grid-template-columns:1fr 1.5fr;gap:30px;align-items:start;margin-top:30px">
<div style="text-align:center">
<img src="/static/images/sensor-positions-pro.jpg" alt="Pro Sensör Pozisyonları" style="width:100%;max-width:300px;border-radius:10px;box-shadow:0 5px 20px rgba(0,0,0,0.3)">
<p style="margin-top:15px;font-size:0.95em">3 sensör ile tam boyun ve baş kontrolü</p>
</div>
<div>
<h4 style="margin-bottom:20px;font-size:1.3em">Ek Sensör:</h4>
<div style="background:rgba(255,255,255,0.15);padding:20px;border-radius:10px;margin-bottom:15px">
<h5 style="margin-bottom:10px">📍 Sensör 3: C5 (5. Boyun Omuru)</h5>
<p style="margin:0;font-size:0.95em">Boyun bölgesi - Servikal eğrilik ve baş pozisyonu ölçümü</p>
</div>
<p style="background:rgba(255,255,255,0.1);padding:15px;border-radius:8px;margin-top:20px">
<strong>Neden C5?</strong> Boyun hareketlerinin merkezi noktası. C5 sensörü ile baş pozisyonunu milimetre hassasiyetinde hesaplayabiliriz.</p>
</div>
</div>

<div style="background:rgba(255,255,255,0.1);padding:30px;border-radius:15px;margin-top:30px">
<h4 style="margin-bottom:20px;font-size:1.3em">3. Sensörle Eklenen Yetenekler:</h4>
<ul style="line-height:2.2;font-size:1.05em">
<li><strong>Forward Head Posture hassas tespiti:</strong> C5-T8 açısı 160° altına düştüğünde anında uyarı</li>
<li><strong>Baş eğim açısı:</strong> Telefon kullanımı sırasında baş 15°, 30°, 45° eğimlerini ayrı ayrı algılar</li>
<li><strong>Boyun rotasyonu:</strong> Sağa-sola dönme hareketlerinde asimetri tespiti (tek tarafa bakmaktan kaynaklanan problemler)</li>
<li><strong>Cervical lordoz kaybı:</strong> Boyun eğriliğinin düzleşmesi veya tersine dönmesi anında tespit edilir</li>
<li><strong>Whiplash riski:</strong> Ani boyun hareketlerinde (araç çarpması simülasyonu) alarm</li>
</ul>
</div>
</div>

<div class="info-box" style="margin-top:30px">
<strong>🎯 Pro Seviye Kimler İçin?</strong> Yoğun bilgisayar/telefon kullanıcıları, gamers, boyun ağrısı yaşayanlar, uzun süreli araç kullananlar için önerilir. Text neck ve forward head posture'ı %99 doğrulukla tespit eder.
</div>

<div style="background:linear-gradient(135deg,#8e44ad,#6c3483);color:white;padding:40px;border-radius:20px;margin:60px 0 40px 0">
<h3 style="font-size:2em;margin-bottom:20px;text-align:center">🥇 Seviye 3: ULTRA</h3>
<p style="font-size:1.1em;text-align:center;margin-bottom:30px">5 IMU + 1 EMG Sensör - Profesyonel Tam Vücut İzleme</p>

<div style="background:rgba(255,255,255,0.15);padding:30px;border-radius:15px">
<h4 style="margin-bottom:20px;font-size:1.3em">Ek Donanım:</h4>
<ul style="line-height:2.2;font-size:1.05em">
<li><strong>2x Kol IMU Sensörleri:</strong> Her iki kola yerleştirilir, omuz-kol hareketlerini izler</li>
<li><strong>1x Sırt EMG Sensörü:</strong> T6-T8 bölgesine yerleştirilir, erector spinae kas aktivitesini ölçer</li>
</ul>
<p style="margin-top:20px;background:rgba(255,255,255,0.1);padding:20px;border-radius:10px">
<strong>Ultra seviye:</strong> Sporcu performans analizi, fizik tedavi takibi, rehabilitasyon süreçleri ve profesyonel duruş eğitimi için tasarlanmıştır. Kas aktivitesi + hareket verisi birleşimiyle en kapsamlı analizi sunar.</p>
</div>
</div>

<div class="cta-box">
<h3>Hangi Seviye Sizin İçin Uygun?</h3>
<p>İhtiyacınıza göre Basic, Pro veya Ultra seviyeyi seçin ve duruş farkındalığınızı artırın</p>
<a href="/demo" class="btn">🎥 Demo'yu İnceleyin</a>
</div>
<div class="measurement-section">
<div class="measurement-points">
<div class="measurement-point">
<div class="number">1</div>
<h4>Kulak-Omuz Hizası</h4>
<p><strong>Neden önemli:</strong> Başın konumunu belirler. İdeal durumda kulak omuz hizasında olmalıdır.</p>
<p><strong>Ölçüm:</strong> Kulak, omuz ve kalça arasındaki açı. 160° altı forward head posture göstergesidir.</p>
<p><strong>Etki:</strong> Her 10° sapma boyun kaslarına +5 kg ekstra yük ekler.</p>
</div>
<div class="measurement-point">
<div class="number">2</div>
<h4>Omuz-Kalça Hizası</h4>
<p><strong>Neden önemli:</strong> Göğüs ve üst sırt duruşunu gösterir. Sırt kamburluğunun ana göstergesidir.</p>
<p><strong>Ölçüm:</strong> Omuz orta noktası ile kalça arasındaki düşey hat açısı. 160° altı kifoz (kamburluk) işaretidir.</p>
<p><strong>Etki:</strong> Akciğer kapasitesini ve omurga esnekliğini doğrudan etkiler.</p>
</div>
<div class="measurement-point">
<div class="number">3</div>
<h4>Omuz Seviye Farkı</h4>
<p><strong>Neden önemli:</strong> Sol-sağ omuz dengesizliği skolyoz (omurga yan eğriliği) ve kas dengesizliğinin erken belirtisidir.</p>
<p><strong>Ölçüm:</strong> İki omuz arasındaki dikey mesafe farkı. 30 piksel üstü (yaklaşık 2 cm) anlamlıdır.</p>
<p><strong>Etki:</strong> Tedavi edilmezse kalıcı omurga eğriliklerine yol açabilir.</p>
</div>
</div>
<div class="info-box" style="margin-top:30px">
<strong>🔬 Bilimsel Temel:</strong> Bu üç nokta, <em>Journal of Physical Therapy Science</em> ve <em>European Spine Journal</em>'da yayınlanan çalışmalarda duruş değerlendirmesi için altın standart olarak belirlenmiştir. Fizik tedavi uzmanları bu noktaları manuel ölçümlerinde kullanır.
</div>
</div>
</div>
<div class="section">
<h2>🔄 Gerçek Zamanlı Takibin Önemi</h2>
<p>Geleneksel duruş değerlendirmeleri yalnızca klinik ortamda, statik pozisyonda yapılır. Ancak:</p>
<ul>
<li><strong>Dinamik duruş önemlidir:</strong> Günlük hayatta duruşunuz sürekli değişir</li>
<li><strong>Farkındalık kritiktir:</strong> Çoğu insan duruş bozukluğunun farkında değildir</li>
<li><strong>Erken müdahale şarttır:</strong> Problemler kronikleşmeden önce düzeltilmelidir</li>
</ul>
<p>SpineGuard, bu üç kritik noktayı <strong>her saniye 30 kez</strong> ölçerek size gerçek zamanlı geri bildirim sağlar. Böylece kötü duruş alışkanlıklarınızı fark eder ve düzeltme fırsatı bulursunuz.</p>
</div>
<div class="cta-box">
<h3>Duruşunuzu Şimdi Test Edin!</h3>
<p>Yapay zeka destekli sistemimiz ile gerçek zamanlı duruş analizi yapın</p>
<a href="/demo" class="btn">🎥 Demo'yu Başlat</a>
</div>
</div>

<div class="tabs" style="margin-top:60px;border-top:3px solid #e0e0e0;border-bottom:none">
<button class="tab-btn active" onclick="switchTab(event, 'anatomi')">📚 Bel ve Sırt Anatomisi</button>
<button class="tab-btn" onclick="switchTab(event, 'problemler')">⚠️ Yaygın Sırt Problemleri</button>
<button class="tab-btn" onclick="switchTab(event, 'cozum')">🎯 Duruş Farkındalığı</button>
</div>
</div>

<script>
function switchTab(event, tabId) {
  // Sayfa başına scroll
  window.scrollTo({ top: 0, behavior: 'smooth' });
  // Tüm tab içeriklerini gizle
  const contents = document.querySelectorAll('.tab-content');
  contents.forEach(content => content.classList.remove('active'));

  // Tüm tab butonlarından active class'ını kaldır
  const buttons = document.querySelectorAll('.tab-btn');
  buttons.forEach(btn => btn.classList.remove('active'));

  // Seçilen tab'ı göster
  document.getElementById(tabId).classList.add('active');

  // Seçilen tab'a karşılık gelen tüm butonları active yap (hem üstteki hem alttaki)
  buttons.forEach(btn => {
    if (btn.onclick.toString().includes(tabId)) {
      btn.classList.add('active');
    }
  });
}
</script>
</body></html>'''

@bp.route('/egitim')
def egitim():
    return render_template_string(EGITIM_HTML)