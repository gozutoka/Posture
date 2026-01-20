"""
SpineGuard - Developer Sayfası (Geçici - Canlıya çıkmadan önce silinecek)
Geliştirici ve test amaçlı teknik bilgiler
"""

from flask import Blueprint, render_template_string

bp = Blueprint('developer', __name__)

DEVELOPER_HTML = '''<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>SpineGuard - Developer | Geliştirici Bilgileri</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;line-height:1.6;color:#fff;overflow-x:hidden;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;background:linear-gradient(135deg,#2c3e50,#34495e);min-height:100vh}
.nav{background:rgba(255,255,255,0.98);padding:20px 0;position:sticky;top:0;z-index:1000;box-shadow:0 1px 3px rgba(0,0,0,0.04);border-bottom:1px solid #e2e8f0}
.nav .container{display:flex;justify-content:space-between;align-items:center}
.nav-brand{color:#0f4c81;font-size:1.6em;font-weight:900;text-decoration:none;letter-spacing:-0.5px}
.nav-links{display:flex;gap:35px;align-items:center}
.nav-links a{color:#475569;text-decoration:none;font-weight:500;transition:color 0.3s;font-size:0.95em}
.nav-links a:hover{color:#0f4c81}
.container{max-width:1200px;margin:0 auto;padding:0 20px}
.hero{padding:80px 20px;text-align:center}
.hero h1{font-size:3.5em;margin-bottom:20px;font-weight:900;letter-spacing:-1px;line-height:1.1}
.hero p{font-size:1.3em;opacity:0.95;max-width:800px;margin:0 auto 30px auto}
.warning-badge{display:inline-block;background:rgba(241,196,15,0.2);border:2px solid #f1c40f;color:#f1c40f;padding:12px 30px;border-radius:25px;font-weight:700;font-size:1.1em;margin-top:20px}
.section{padding:60px 20px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(350px,1fr));gap:30px;margin:40px 0}
.card{background:rgba(255,255,255,0.1);padding:35px;border-radius:15px;transition:transform 0.3s,box-shadow 0.3s}
.card:hover{transform:translateY(-5px);box-shadow:0 8px 30px rgba(0,0,0,0.3)}
.card h3{font-size:1.5em;margin-bottom:20px;font-weight:800}
.card.blue{border-left:5px solid #3498db}
.card.blue h3{color:#3498db}
.card.purple{border-left:5px solid #9b59b6}
.card.purple h3{color:#9b59b6}
.card.orange{border-left:5px solid #e67e22}
.card.orange h3{color:#e67e22}
.card.red{border-left:5px solid #e74c3c}
.card.red h3{color:#e74c3c}
.card.green{border-left:5px solid #1abc9c}
.card.green h3{color:#1abc9c}
.card.yellow{border-left:5px solid #f39c12}
.card.yellow h3{color:#f39c12}
.code-block{background:rgba(0,0,0,0.3);padding:20px;border-radius:10px;font-family:monospace;font-size:0.9em;margin:10px 0;line-height:1.8}
.code-block p{margin:8px 0}
.code-block strong{font-weight:700}
.info-list{list-style:none;padding:0;line-height:2}
.info-list li{padding:5px 0}
.info-list code{background:rgba(0,0,0,0.3);padding:2px 6px;border-radius:3px;font-family:monospace;font-size:0.9em}
.footer-warning{background:rgba(241,196,15,0.15);border:2px dashed rgba(241,196,15,0.5);padding:30px;border-radius:15px;margin-top:50px;text-align:center}
.back-button{display:inline-block;background:rgba(255,255,255,0.1);color:white;padding:15px 35px;border-radius:10px;text-decoration:none;font-weight:700;margin-top:20px;transition:all 0.3s;border:2px solid rgba(255,255,255,0.3)}
.back-button:hover{background:rgba(255,255,255,0.2);transform:translateY(-2px)}
@media(max-width:768px){.hero h1{font-size:2.2em}.nav-links{gap:15px;font-size:0.9em}.grid{grid-template-columns:1fr}}
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

<div class="hero">
<div class="container">
<h1>👨‍💻 Developer Bilgileri</h1>
<p>Geliştirici ve test amaçlı teknik bilgiler</p>
<div class="warning-badge">⚠️ TEMPORARY - Development Only</div>
</div>
</div>

<div class="section">
<div class="container">

<h2 style="font-size:2.5em;margin-bottom:40px;text-align:center;font-weight:900">🏗️ Sistem Mimarisi</h2>

<div style="background:rgba(255,255,255,0.08);padding:50px;border-radius:20px;margin-bottom:60px;border:2px solid rgba(255,255,255,0.2)">
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:35px">

<div style="background:linear-gradient(135deg,rgba(52,152,219,0.2),rgba(41,128,185,0.2));padding:30px;border-radius:15px;border-left:5px solid #3498db;text-align:center">
<div style="font-size:3em;margin-bottom:15px">📟</div>
<h3 style="color:#3498db;font-size:1.4em;margin-bottom:20px;font-weight:800">Sensörler</h3>
<ul style="list-style:none;padding:0;text-align:left;line-height:2">
<li>🔷 <strong>BLE/MCU Modül</strong><br><span style="font-size:0.9em;opacity:0.8">Nordic nRF52832</span></li>
<li>⚙️ <strong>6-Eksen IMU</strong><br><span style="font-size:0.9em;opacity:0.8">MPU-6050 (Accel+Gyro)</span></li>
<li>🔋 <strong>Pil</strong><br><span style="font-size:0.9em;opacity:0.8">3V CR1216 (4 ay ömür)</span></li>
<li>📡 <strong>Anten</strong><br><span style="font-size:0.9em;opacity:0.8">PCB anten 2.4GHz</span></li>
</ul>
</div>

<div style="display:flex;align-items:center;justify-content:center">
<div style="font-size:4em;color:rgba(255,255,255,0.5)">→</div>
</div>

<div style="background:linear-gradient(135deg,rgba(155,89,182,0.2),rgba(142,68,173,0.2));padding:30px;border-radius:15px;border-left:5px solid #9b59b6;text-align:center">
<div style="font-size:3em;margin-bottom:15px">📱</div>
<h3 style="color:#9b59b6;font-size:1.4em;margin-bottom:20px;font-weight:800">BLE Bağlantısı</h3>
<ul style="list-style:none;padding:0;text-align:left;line-height:2">
<li>🔗 <strong>Protokol:</strong> BLE 5.0</li>
<li>📊 <strong>Veri Hızı:</strong> 100 Hz</li>
<li>📏 <strong>Menzil:</strong> ~10 metre</li>
<li>⚡ <strong>Güç:</strong> Düşük enerji</li>
</ul>
</div>

<div style="display:flex;align-items:center;justify-content:center">
<div style="font-size:4em;color:rgba(255,255,255,0.5)">→</div>
</div>

<div style="background:linear-gradient(135deg,rgba(46,204,113,0.2),rgba(39,174,96,0.2));padding:30px;border-radius:15px;border-left:5px solid #2ecc71;text-align:center">
<div style="font-size:3em;margin-bottom:15px">📲</div>
<h3 style="color:#2ecc71;font-size:1.4em;margin-bottom:20px;font-weight:800">Telefon App</h3>
<ul style="list-style:none;padding:0;text-align:left;line-height:2">
<li>💾 <strong>History Kaydı</strong><br><span style="font-size:0.9em;opacity:0.8">30 günlük veri</span></li>
<li>🧮 <strong>Data Processor</strong><br><span style="font-size:0.9em;opacity:0.8">Doğru/yanlış hareket</span></li>
<li>🔔 <strong>Geri Bildirim</strong><br><span style="font-size:0.9em;opacity:0.8">Titreşim+Sesli uyarı</span></li>
<li>⌚ <strong>Akıllı Saat</strong><br><span style="font-size:0.9em;opacity:0.8">Notification sync</span></li>
</ul>
</div>

</div>
</div>



<div class="card yellow">
<h3>📦 Critical BOM (Bill of Materials)</h3>
<ul class="info-list">
<li><strong>MCU/BLE:</strong> <code>Nordic nRF52805-CAAA-R: 2.3 Euro (muadil bul)</code></li>
<li><strong>6-Eksen IMU:</strong> <code>Bosch BMI271: 3 Euro (muadil bul)</code></li>
<li><strong>Crystal:</strong> <code>32MHz Kyocera CX2016DB32000D0FLJCC</code></li>
<li><strong>Pil:</strong> <code>CR1216: 0.5 Euro</code></li>
<li><strong>PCB:</strong> <code>Custom 2-layer FR4 (25mm x 15mm)</code></li>
<li><strong>Tape:</strong> <code>Kinesiology Tape (20cm): 0.2 Euro</code></li>
</ul>
<li><strong>Tape:</strong> <code>Estimated Critical BOM Cost: 6 Euro (dusebilir) + PCB + Dizgi</code></li>
</ul>
<h4 style="margin-top:25px;color:#f39c12">💻 Software Repositories:</h4>
<ul class="info-list">
<li><strong>Sensor Firmware:</strong> <a href="" 
style="color:#3498db;text-decoration:none">TBD</a></li>
<li><strong>Website:</strong> <a href= "https://github.com/gozutoka/Posture"
style="color:#3498db;text-decoration:none">github.com/gozutoka/Posture</a></li>
<li><strong>Mobile Application:</strong> <a href=""
style="color:#3498db;text-decoration:none">TBD</a></li>
</ul>
</div>


⚠️ <strong>Uyarı:</strong> Bu development versiyonudur.</p>
</div>
</div>
</div>

<div class="footer-warning">
<p style="font-size:1.2em;margin-bottom:15px">💡 <strong>Not:</strong> Bu sayfa sadece iç test ve geliştirme amaçlıdır.</p>
<p style="font-size:1em;opacity:0.9">Site canlıya çıkmadan önce bu Developer sayfası ve tüm referansları tamamen kaldırılacaktır.</p>
<p style="font-size:0.95em;margin-top:20px;opacity:0.8"><strong>Silme:</strong> pages/developer.py dosyasını silin ve app.py'den import'u kaldırın.</p>
<a href="/nasil-calisir" class="back-button">← Nasıl Çalışır? Sayfasına Dön</a>
</div>

</div>
</div>

<div style="background:#0f172a;color:white;padding:40px 20px;text-align:center">
<div class="container">
<p>&copy; 2026 SpineGuard. Tüm hakları saklıdır. | Developer Mode - Internal Use Only</p>
</div>
</div>

</body>
</html>'''

@bp.route('/developer')
def developer():
    return render_template_string(DEVELOPER_HTML)
