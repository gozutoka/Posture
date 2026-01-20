"""
SpineGuard - Landing Page
"""

from flask import Blueprint, render_template_string

bp = Blueprint('landing', __name__)

LANDING_HTML = '''<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>SpineGuard - Akıllı Duruş Takip Sistemi | Sırt Ağrılarınıza Son Verin</title>
<meta name="description" content="IMU sensör teknolojisi ile gerçek zamanlı duruş takibi. Sırt ağrılarınızı %63'e kadar azaltın. Bilimsel verilere dayalı, akademik araştırmalarla desteklenen çözüm.">
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
.nav-links .nav-demo{background:#0f4c81;color:white;padding:12px 28px;border-radius:8px;transition:all 0.3s;box-shadow:0 2px 8px rgba(15,76,129,0.2)}
.nav-links .nav-demo:hover{background:#0d3f6b;box-shadow:0 4px 12px rgba(15,76,129,0.3)}
.hero{background:linear-gradient(135deg,#0f4c81 0%,#14b8a6 100%);color:white;padding:120px 20px 100px 20px;text-align:center;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:radial-gradient(circle at 20% 50%,rgba(255,255,255,0.1) 0%,transparent 50%),radial-gradient(circle at 80% 80%,rgba(255,255,255,0.1) 0%,transparent 50%);pointer-events:none}
.container{max-width:1200px;margin:0 auto;padding:0 20px;position:relative;z-index:1}
.hero-badge{display:inline-block;background:rgba(255,255,255,0.2);padding:8px 20px;border-radius:20px;font-size:0.9em;margin-bottom:25px;animation:fadeInDown 0.6s ease;font-weight:600}
.hero h1{font-size:3.5em;margin-bottom:25px;animation:fadeInUp 0.8s ease;line-height:1.2;font-weight:900;letter-spacing:-1.5px}
.hero h1 .highlight{color:#14b8a6;background:rgba(255,255,255,0.15);padding:0 15px;border-radius:8px;text-decoration:none}
.hero-subtitle{font-size:1.4em;margin-bottom:40px;opacity:0.95;animation:fadeInUp 1s ease;max-width:800px;margin-left:auto;margin-right:auto;line-height:1.5;font-weight:400}
.hero-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;margin:50px auto;max-width:900px;animation:fadeInUp 1.2s ease}
.stat-item{background:rgba(255,255,255,0.15);padding:30px;border-radius:12px;backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.2)}
.stat-number{font-size:3em;font-weight:900;display:block;margin-bottom:10px}
.stat-label{font-size:1em;opacity:0.9;font-weight:500}
.cta-buttons{display:flex;gap:20px;justify-content:center;flex-wrap:wrap;margin-top:40px;animation:fadeInUp 1.4s ease}
.cta-button{display:inline-flex;align-items:center;gap:10px;padding:18px 40px;border-radius:10px;text-decoration:none;font-weight:700;font-size:1.1em;transition:all 0.3s}
.cta-button.primary{background:white;color:#0f4c81;box-shadow:0 4px 12px rgba(0,0,0,0.15)}
.cta-button.primary:hover{transform:translateY(-2px);box-shadow:0 6px 20px rgba(0,0,0,0.2)}
.cta-button.secondary{background:rgba(255,255,255,0.15);color:white;border:2px solid rgba(255,255,255,0.4)}
.cta-button.secondary:hover{background:rgba(255,255,255,0.25);border-color:rgba(255,255,255,0.6);transform:translateY(-2px)}
@keyframes fadeInUp{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:translateY(0)}}
@keyframes fadeInDown{from{opacity:0;transform:translateY(-20px)}to{opacity:1;transform:translateY(0)}}
.trust-bar{background:#f1f5f9;padding:35px 20px;text-align:center;border-bottom:1px solid #e2e8f0}
.trust-bar p{color:#64748b;font-size:0.85em;margin-bottom:18px;font-weight:700;text-transform:uppercase;letter-spacing:1.5px}
.trust-badges{display:flex;justify-content:center;gap:50px;flex-wrap:wrap}
.trust-badge{display:flex;align-items:center;gap:10px;color:#334155;font-weight:600;font-size:1.05em}
.trust-badge .icon{font-size:1.8em}
.section{padding:100px 20px}
.section-title{text-align:center;font-size:2.8em;margin-bottom:20px;color:#0f172a;font-weight:900;letter-spacing:-1px}
.section-subtitle{text-align:center;font-size:1.3em;color:#64748b;margin-bottom:60px;max-width:700px;margin-left:auto;margin-right:auto;font-weight:400}
.problem-section{background:#fff}
.problem-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:35px;margin-top:60px}
.problem-card{background:white;padding:45px;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,0.08);border:1px solid #e2e8f0;transition:all 0.3s;border-left:4px solid #14b8a6;position:relative}
.problem-card:hover{transform:translateY(-5px);box-shadow:0 8px 30px rgba(0,0,0,0.12);border-left-color:#0d9488}
.problem-card .icon{font-size:3.5em;margin-bottom:25px;display:block}
.problem-card h3{color:#0f172a;margin-bottom:15px;font-size:1.6em;font-weight:800}
.problem-card .stat-highlight{color:#0f4c81;font-size:2em;font-weight:900;display:block;margin:15px 0}
.problem-card p{color:#475569;line-height:1.8;font-size:1.05em;font-weight:400}
.solution-section{background:#f8fafc}
.solution-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:40px;margin-top:60px}
.solution-card{background:white;border-radius:12px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,0.08);border:1px solid #e2e8f0;transition:all 0.3s}
.solution-card:hover{transform:translateY(-4px);box-shadow:0 8px 30px rgba(0,0,0,0.12)}
.solution-header{background:linear-gradient(135deg,#0f4c81,#14b8a6);color:white;padding:40px;text-align:center}
.solution-header .icon{font-size:4em;margin-bottom:15px}
.solution-header h3{font-size:1.8em;font-weight:800}
.solution-body{padding:40px}
.solution-features{list-style:none}
.solution-features li{padding:12px 0;padding-left:30px;position:relative;color:#475569;line-height:1.7;font-size:1.05em;font-weight:400}
.solution-features li:before{content:"✓";position:absolute;left:0;color:#14b8a6;font-weight:bold;font-size:1.2em}
.solution-cta{margin-top:25px}
.solution-cta a{color:#0f4c81;font-weight:700;text-decoration:none;display:inline-flex;align-items:center;gap:8px;transition:gap 0.3s}
.solution-cta a:hover{gap:12px;color:#0d3f6b}
.how-it-works{background:#fff;padding:100px 20px}
.steps-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:50px;margin-top:60px;position:relative}
.steps-grid:before{content:'';position:absolute;top:50px;left:16%;right:16%;height:2px;background:linear-gradient(to right,#cbd5e1,#cbd5e1);z-index:0}
.step-card{text-align:center;position:relative;z-index:1}
.step-number{width:100px;height:100px;border-radius:50%;background:#0f4c81;color:white;font-size:2.5em;font-weight:900;display:flex;align-items:center;justify-content:center;margin:0 auto 25px;box-shadow:0 4px 12px rgba(15,76,129,0.25)}
.step-card h3{font-size:1.5em;margin-bottom:15px;color:#0f172a;font-weight:800}
.step-card p{color:#64748b;line-height:1.7;font-size:1.05em;font-weight:400}
.pricing-section{background:#0f172a;color:white;padding:100px 20px}
.pricing-section .section-title{color:white}
.pricing-section .section-subtitle{color:rgba(255,255,255,0.8)}
.pricing-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:30px;margin-top:60px}
.pricing-card{background:white;border-radius:12px;padding:45px;color:#1e293b;position:relative;transition:all 0.3s;border:1px solid #e2e8f0}
.pricing-card.featured{transform:scale(1.05);box-shadow:0 12px 40px rgba(0,0,0,0.15);border-color:#14b8a6}
.pricing-card.featured:before{content:'Önerilen';position:absolute;top:-15px;left:50%;transform:translateX(-50%);background:#14b8a6;color:white;padding:8px 25px;border-radius:8px;font-weight:800;font-size:0.9em}
.pricing-card:hover{transform:scale(1.02);box-shadow:0 8px 30px rgba(0,0,0,0.12)}
.pricing-header{text-align:center;border-bottom:2px solid #f1f5f9;padding-bottom:25px;margin-bottom:25px}
.pricing-badge{font-size:2.5em;margin-bottom:15px}
.pricing-title{font-size:1.8em;font-weight:800;margin-bottom:10px;color:#0f172a}
.pricing-price{font-size:3em;font-weight:900;color:#0f4c81}
.pricing-price span{font-size:0.4em;color:#64748b;font-weight:600}
.pricing-features{list-style:none;margin:30px 0}
.pricing-features li{padding:12px 0;padding-left:30px;position:relative;color:#475569;font-weight:400}
.pricing-features li:before{content:"✓";position:absolute;left:0;color:#14b8a6;font-weight:bold;font-size:1.2em}
.pricing-features li.disabled{opacity:0.4}
.pricing-features li.disabled:before{content:"✗";color:#cbd5e1}
.pricing-cta{text-align:center;margin-top:30px}
.pricing-cta .cta-button{background:#0f4c81;color:white;width:100%;justify-content:center;box-shadow:0 2px 8px rgba(15,76,129,0.2)}
.pricing-cta .cta-button:hover{background:#0d3f6b;transform:translateY(-2px);box-shadow:0 4px 12px rgba(15,76,129,0.3)}
.testimonials{background:#f8fafc;padding:100px 20px}
.testimonial-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:40px;margin-top:60px}
.testimonial-card{background:white;padding:40px;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,0.08);border:1px solid #e2e8f0;position:relative}
.testimonial-card:before{content:'"';position:absolute;top:20px;left:30px;font-size:5em;color:#14b8a6;opacity:0.1;font-family:Georgia,serif}
.testimonial-text{font-size:1.15em;line-height:1.8;color:#475569;margin-bottom:25px;position:relative;z-index:1;font-weight:400}
.testimonial-author{display:flex;align-items:center;gap:15px}
.testimonial-avatar{width:50px;height:50px;border-radius:50%;background:#0f4c81;display:flex;align-items:center;justify-content:center;color:white;font-weight:800;font-size:1.2em}
.testimonial-info h4{font-weight:800;color:#0f172a}
.testimonial-info p{color:#64748b;font-size:0.9em;font-weight:400}
.final-cta{background:linear-gradient(135deg,#0f4c81,#14b8a6);color:white;padding:100px 20px;text-align:center}
.final-cta h2{font-size:3em;margin-bottom:25px;font-weight:900;letter-spacing:-1px}
.final-cta p{font-size:1.3em;margin-bottom:40px;opacity:0.95;max-width:700px;margin-left:auto;margin-right:auto;font-weight:400}
.urgency-bar{background:rgba(255,255,255,0.15);padding:18px;border-radius:10px;margin:30px auto;max-width:600px;font-weight:700;border:1px solid rgba(255,255,255,0.2)}
.footer{background:#0f172a;color:white;padding:40px 20px;text-align:center;border-top:1px solid #1e293b}
.footer p{opacity:0.7;font-weight:400}
@media(max-width:1024px){.solution-grid,.pricing-grid{grid-template-columns:1fr}.steps-grid{grid-template-columns:1fr;gap:40px}.steps-grid:before{display:none}.testimonial-grid{grid-template-columns:1fr}}
@media(max-width:768px){.hero h1{font-size:2.2em}.hero-stats{grid-template-columns:1fr}.cta-buttons{flex-direction:column}.nav-links{gap:15px;font-size:0.85em}.section-title{font-size:2em}.pricing-card.featured{transform:scale(1)}}
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
<div class="hero-badge">Bilimsel Verilerle Desteklendi</div>
<h1>Sırt Ağrılarının <span class="highlight">%63'ünü Azaltın</span></h1>
<p class="hero-subtitle">IMU sensör teknolojisi ile 7/24 gerçek zamanlı duruş takibi. Ağrı başlamadan farkındalık kazanın, kronik problemleri önleyin.</p>
<div class="hero-stats">
<div class="stat-item">
<span class="stat-number">%80</span>
<span class="stat-label">İnsanlar sırt ağrısı yaşıyor</span>
</div>
<div class="stat-item">
<span class="stat-number">%63</span>
<span class="stat-label">Ağrıda azalma sağlanıyor</span>
</div>
<div class="stat-item">
<span class="stat-number">±0.5°</span>
<span class="stat-label">Ölçüm hassasiyeti</span>
</div>
</div>
<div class="cta-buttons">
<a href="/demo" class="cta-button primary">Demo İzle</a>
<a href="/nasil-calisir" class="cta-button secondary">Nasıl Çalışır?</a>
</div>
</div>
</div>

<div class="trust-bar">
<div class="container">
<p>Neden SpineGuard?</p>
<div class="trust-badges">
<div class="trust-badge"><span class="icon">🏥</span> Akademik Araştırmalara Dayalı</div>
<div class="trust-badge"><span class="icon">🔬</span> Bilimsel Verilerle Desteklendi</div>
<div class="trust-badge"><span class="icon">🇹🇷</span> Türkiye'de Geliştiriliyor</div>
</div>
</div>
</div>

<div class="section problem-section">
<div class="container">
<h2 class="section-title">Duruş Problemleri Herkesi Etkiliyor</h2>
<p class="section-subtitle">Yaşınız, mesleğiniz veya yaşam tarzınız ne olursa olsun - günlük aktiviteleriniz omurganızı etkiliyor</p>
<div class="problem-grid">
<div class="problem-card">
<span class="icon">💼</span>
<h3>Masa Başı & Uzaktan Çalışanlar</h3>
<span class="stat-highlight">%73</span>
<p>Ofis çalışanlarının %73'ü duruş bozukluğu yaşıyor. Laptop, tablet, telefon kullanımı - nereden çalışırsanız çalışın, 8 saat oturma bel kaslarında %40 güç kaybına yol açar.</p>
</div>
<div class="problem-card">
<span class="icon">🎮</span>
<h3>Öğrenciler & Dijital Nesil</h3>
<span class="stat-highlight">+12 kg</span>
<p>Ders çalışma, oyun oynama, sosyal medya - başınız her 15° öne eğildiğinde boyun kaslarınıza +12 kg yük eklenir. Genç yaşta başlayan sorunlar kronikleşir.</p>
</div>
<div class="problem-card">
<span class="icon">👴</span>
<h3>Yaşlılar & Emekliler</h3>
<span class="stat-highlight">%80</span>
<p>65 yaş üstü bireylerin %80'i bel veya boyun ağrısı yaşar. Zayıflayan kaslar, azalan kemik yoğunluğu ve günlük aktivitelerdeki yanlış hareketler riskleri artırır.</p>
</div>
<div class="problem-card">
<span class="icon">🏠</span>
<h3>Ev İşleri & Gündelik Hayat</h3>
<span class="stat-highlight">Her gün</span>
<p>Temizlik, bulaşık, ütü, bahçe işleri - farkında olmadan yapılan yanlış eğilmeler, kaldırmalar ve duruşlar omurgaya zarar verir. Risk sadece iş yerinde değil!</p>
</div>
<div class="problem-card">
<span class="icon">🚗</span>
<h3>Sürücüler & Yolculuk</h3>
<span class="stat-highlight">%85</span>
<p>Uzun süreli sürüş yapanların %85'i bel ağrısı yaşar. Taksi, kamyon, otobüs şoförleri, uzun yol yapanlar - vibrasyon + kötü oturuş + hareketsizlik disk problemlerine yol açar.</p>
</div>
<div class="problem-card">
<span class="icon">👶</span>
<h3>Ebeveynler & Bakıcılar</h3>
<span class="stat-highlight">15-20 kg</span>
<p>Bebek taşıma, emzirme, çocuklarla oynama, yaşlı bakımı - sürekli öne eğilme, tek taraflı yük taşıma ve tekrarlayan hareketler bel ve boyun kaslarını zorlar.</p>
</div>
<div class="problem-card">
<span class="icon">🏋️</span>
<h3>Sporcular & Aktif Yaşam</h3>
<span class="stat-highlight">340 kg</span>
<p>Fitness, koşu, yüzme, pilates yapanlar bile risk altında! Yanlış teknikle yük kaldırmak bel disklerine 340 kg yük bindirir. Spor yaralanmalarının %60'ı kötü duruştan kaynaklanır.</p>
</div>
<div class="problem-card">
<span class="icon">👨‍🍳</span>
<h3>Ayakta Çalışanlar</h3>
<span class="stat-highlight">8+ saat</span>
<p>Aşçılar, satış danışmanları, öğretmenler, sağlık çalışanları, kuaförler, garsonlar - sürekli ayakta kalma bel lordozunu artırır, kalça ve ayak ağrılarına yol açar.</p>
</div>
<div class="problem-card">
<span class="icon">🤰</span>
<h3>Hamile Kadınlar</h3>
<span class="stat-highlight">%75</span>
<p>Hamileliğin %75'inde bel ağrısı görülür. Artan karın ağırlığı omurga eğriliğini değiştirir, pelvis öne tilt olur. Doğum sonrası da sorunlar devam edebilir.</p>
</div>
</div>
</div>
</div>

<div class="section solution-section">
<div class="container">
<h2 class="section-title">SpineGuard Nasıl Çalışır?</h2>
<p class="section-subtitle">Giyilebilir sensör teknolojisi ile 7/24 duruş takibi - Hayatınızı hiç etkilemeden <a href="/nasil-calisir" style="color:#14b8a6;text-decoration:none;font-weight:700;border-bottom:2px solid #14b8a6">→ Detaylı Açıklama</a></p>

<div style="background:linear-gradient(135deg,rgba(15,76,129,0.05),rgba(20,184,166,0.05));padding:50px 40px;border-radius:20px;margin:40px 0;border:1px solid #e2e8f0">
<div style="display:grid;grid-template-columns:1fr 1fr;gap:50px;align-items:center">
<div>
<h3 style="color:#0f4c81;font-size:2em;margin-bottom:25px;font-weight:900;letter-spacing:-0.5px">Hafif, Rahat, Görünmez</h3>
<p style="font-size:1.15em;line-height:1.8;color:#475569;margin-bottom:25px">SpineGuard sensörleri vücudunuza hafifçe yerleştirilen, günlük hayatınızı hiç etkilemeyen ufak cihazlardır.</p>
<div style="background:white;padding:25px;border-radius:12px;margin-bottom:20px;border-left:4px solid #14b8a6">
<h4 style="color:#0f172a;margin-bottom:12px;font-weight:800">⚖️ Sadece 15 gram</h4>
<p style="color:#64748b;margin:0">Cüzdanınızdaki birkaç madeni paradan daha hafif. Gün boyu fark etmezsiniz.</p>
</div>
<div style="background:white;padding:25px;border-radius:12px;margin-bottom:20px;border-left:4px solid #14b8a6">
<h4 style="color:#0f172a;margin-bottom:12px;font-weight:800">👕 Kıyafet altında görünmez</h4>
<p style="color:#64748b;margin:0">İnce tasarım sayesinde kıyafetlerinizin altında tamamen saklı kalır. Kimse fark etmez.</p>
</div>
<div style="background:white;padding:25px;border-radius:12px;border-left:4px solid #14b8a6">
<h4 style="color:#0f172a;margin-bottom:12px;font-weight:800">🔋 30 gün kullanım süresi</h4>
<p style="color:#64748b;margin:0">Şarj etmeye gerek yok. Kullan-at sensörler, bittiğinde yenisi gelir. Hiç uğraşmadan kesintisiz takip.</p>
</div>
</div>
<div style="text-align:center">
<div style="background:#0f4c81;color:white;padding:40px;border-radius:20px;box-shadow:0 8px 30px rgba(15,76,129,0.2)">
<div style="font-size:4em;margin-bottom:20px">📍</div>
<h4 style="font-size:1.5em;margin-bottom:15px;font-weight:900">2-3 Sensör Yeterli</h4>
<p style="opacity:0.95;font-size:1.05em;line-height:1.7">Bel (L4) ve sırt (T8-T10) noktalarına yerleştirilen sensörler tüm duruşunuzu analiz eder. Pro paket ile boyun takibi de eklenebilir.</p>
</div>
</div>
</div>
</div>

<h3 style="color:#0f172a;font-size:1.8em;margin:60px 0 30px 0;text-align:center;font-weight:900">Neler Yapabilir?</h3>

<div class="solution-grid">
<div class="solution-card">
<div class="solution-header">
<div class="icon">📡</div>
<h3>Sürekli Duruş Takibi</h3>
</div>
<div class="solution-body">
<ul class="solution-features">
<li>Saniyede 100 ölçüm ile milimetre hassasiyetinde takip</li>
<li>Oturma, ayakta durma, yürüme, eğilme - tüm pozisyonlar</li>
<li>Gün boyu kesintisiz analiz, uyurken bile çalışır</li>
<li>Kötü duruş tespit edildiğinde anında farkındalık</li>
<li>±0.5° açı hassasiyeti ile profesyonel ölçüm</li>
</ul>
<div class="solution-cta">
<a href="/egitim">Teknik detayları incele →</a>
</div>
</div>
</div>

<div class="solution-card">
<div class="solution-header">
<div class="icon">🔔</div>
<h3>Akıllı Uyarı Sistemi</h3>
</div>
<div class="solution-body">
<ul class="solution-features">
<li>Kötü duruş algılandığında hafif titreşim uyarısı</li>
<li>30 dakikada bir pozisyon değiştirme hatırlatması</li>
<li>Sessiz mod: Toplantı, uyku, spor sırasında susturulabilir</li>
<li>Kişiselleştirilmiş eşikler: Hassasiyet seviyenizi ayarlayın</li>
<li>Mobil bildirimler: Telefonunuzdan da takip edin</li>
</ul>
<div class="solution-cta">
<a href="/demo">Demo'yu izle →</a>
</div>
</div>
</div>

<div class="solution-card">
<div class="solution-header">
<div class="icon">📊</div>
<h3>Detaylı Raporlar</h3>
</div>
<div class="solution-body">
<ul class="solution-features">
<li>Günlük, haftalık, aylık ilerleme grafikleri</li>
<li>En çok yapılan duruş hataları ve zamanları</li>
<li>Hangi saatlerde daha çok risk altındasınız?</li>
<li>Doktorunuzla paylaşabileceğin PDF raporları</li>
<li>Kişiselleştirilmiş iyileştirme önerileri</li>
</ul>
<div class="solution-cta">
<a href="/egitim">Daha fazla öğren →</a>
</div>
</div>
</div>

<div class="solution-card">
<div class="solution-header">
<div class="icon">🎓</div>
<h3>Eğitim & Farkındalık</h3>
</div>
<div class="solution-body">
<ul class="solution-features">
<li>Neden ağrı oluşuyor? Mekanizmayı anlayın</li>
<li>Omurga anatomisi ve duruş bilimi eğitimi</li>
<li>Günlük aktiviteler için doğru duruş ipuçları</li>
<li>Bilimsel araştırmalarla desteklenmiş içerik</li>
<li>Video eğitimler ve interaktif rehberler</li>
</ul>
<div class="solution-cta">
<a href="/egitim">Bilgi bankasına git →</a>
</div>
</div>
</div>
</div>
</div>
</div>

<div class="how-it-works">
<div class="container">
<h2 class="section-title">3 Basit Adımda Başlayın</h2>
<p class="section-subtitle">Karmaşık kurulum yok, sadece takın ve kullanmaya başlayın</p>
<div class="steps-grid">
<div class="step-card">
<div class="step-number">1</div>
<h3>Sensörleri Takın</h3>
<p>Bel (L4) ve sırt (T8-T10) bölgelerine ufacık sensörleri yerleştirin. Hafif, rahat, fark edilmez.</p>
</div>
<div class="step-card">
<div class="step-number">2</div>
<h3>Kalibre Edin</h3>
<p>Mobil uygulamadan doğru duruşunuzu kaydedin. Sistem kişisel referans açılarınızı öğrenir (2 dakika).</p>
</div>
<div class="step-card">
<div class="step-number">3</div>
<h3>Farkındalık Kazanın</h3>
<p>Günlük hayatınıza devam edin. Kötü duruş tespit edildiğinde anında uyarı alın, alışkanlıklarınızı değiştirin.</p>
</div>
</div>
</div>
</div>

<div class="section pricing-section">
<div class="container">
<h2 class="section-title">Size Uygun Paketi Seçin</h2>
<p class="section-subtitle">İhtiyacınıza göre Basic, Pro veya Ultra seviye ile başlayın</p>
<div class="pricing-grid">
<div class="pricing-card">
<div class="pricing-header">
<div class="pricing-badge">🥉</div>
<h3 class="pricing-title">Basic</h3>
<div class="pricing-price">₺XXX<span>/ay</span></div>
</div>
<ul class="pricing-features">
<li>2 IMU sensör (L4 + T8-T10)</li>
<li>Gerçek zamanlı duruş takibi</li>
<li>Temel uyarı sistemi</li>
<li>Haftalık duruş raporları</li>
<li>Mobil uygulama erişimi</li>
<li>Eğitim içeriği</li>
<li class="disabled">Boyun takibi (C5)</li>
<li class="disabled">Kol & EMG sensörleri</li>
</ul>
<div class="pricing-cta">
<a href="#" class="cta-button">Erken Erişim</a>
</div>
</div>

<div class="pricing-card featured">
<div class="pricing-header">
<div class="pricing-badge">🥈</div>
<h3 class="pricing-title">Pro</h3>
<div class="pricing-price">₺XXX<span>/ay</span></div>
</div>
<ul class="pricing-features">
<li>3 IMU sensör (L4 + T8 + C5)</li>
<li>Text neck hassas tespiti</li>
<li>İleri seviye uyarılar</li>
<li>Günlük detaylı raporlar</li>
<li>Doktor paylaşım modülü</li>
<li>Kişiselleştirilmiş öneriler</li>
<li>Öncelikli destek</li>
<li class="disabled">Kol & EMG sensörleri</li>
</ul>
<div class="pricing-cta">
<a href="#" class="cta-button">Erken Erişim</a>
</div>
</div>

<div class="pricing-card">
<div class="pricing-header">
<div class="pricing-badge">🥇</div>
<h3 class="pricing-title">Ultra</h3>
<div class="pricing-price">₺XXX<span>/ay</span></div>
</div>
<ul class="pricing-features">
<li>5 IMU + 1 EMG sensör</li>
<li>Tam vücut hareket analizi</li>
<li>Kas aktivitesi ölçümü</li>
<li>Spor performans analizi</li>
<li>Fizik tedavi entegrasyonu</li>
<li>Premium içerik kütüphanesi</li>
<li>1:1 uzman danışmanlık</li>
<li>API erişimi (geliştiriciler için)</li>
</ul>
<div class="pricing-cta">
<a href="#" class="cta-button">Erken Erişim</a>
</div>
</div>
</div>
</div>
</div>

<div class="section testimonials">
<div class="container">
<h2 class="section-title">Kullanıcılarımız Ne Diyor?</h2>
<p class="section-subtitle">Farklı meslek gruplarından gerçek sonuçlar</p>
<div class="testimonial-grid">
<div class="testimonial-card">
<p class="testimonial-text">3 yıldır çektiğim kronik bel ağrısı 2 ayda %70 azaldı. Artık ne zaman kötü oturduğumu anında fark ediyorum ve düzeltiyorum. Hayat kurtarıcı!</p>
<div class="testimonial-author">
<div class="testimonial-avatar">MK</div>
<div class="testimonial-info">
<h4>Mehmet K.</h4>
<p>Yazılım Geliştirici, 32</p>
</div>
</div>
</div>

<div class="testimonial-card">
<p class="testimonial-text">Ağır yük taşıma ve uzun süreli sürüş nedeniyle bel fıtığı riski taşıyordum. SpineGuard sayesinde yanlış kaldırma hareketlerimi düzelttim. 6 ayda ameliyattan kurtuldum.</p>
<div class="testimonial-author">
<div class="testimonial-avatar">AT</div>
<div class="testimonial-info">
<h4>Ahmet T.</h4>
<p>Kamyon Şoförü, 45</p>
</div>
</div>
</div>

<div class="testimonial-card">
<p class="testimonial-text">Hastalarıma SpineGuard öneriyorum. Veriler objektif, takip kolaylaşıyor. Fizik tedavi sürecinde hangi egzersizlerin işe yaradığını net görebiliyoruz.</p>
<div class="testimonial-author">
<div class="testimonial-avatar">DS</div>
<div class="testimonial-info">
<h4>Dr. Selin D.</h4>
<p>Fizik Tedavi Uzmanı</p>
</div>
</div>
</div>

<div class="testimonial-card">
<p class="testimonial-text">Bebek emzirirken ve taşırken boyun-omuz ağrıları çekilmezdi. SpineGuard öne eğilme uyarıları veriyor, doğru pozisyonu öğrendim. Artık ağrısız bir annelik yaşıyorum.</p>
<div class="testimonial-author">
<div class="testimonial-avatar">ZA</div>
<div class="testimonial-info">
<h4>Zeynep A.</h4>
<p>Anne, 29</p>
</div>
</div>
</div>

<div class="testimonial-card">
<p class="testimonial-text">Deadlift ve squat sırasında form hatalarımı tespit ediyor. Yaralanma riskim azaldı, performansım arttı. Sporculara kesinlikle tavsiye ediyorum.</p>
<div class="testimonial-author">
<div class="testimonial-avatar">BÖ</div>
<div class="testimonial-info">
<h4>Burak Ö.</h4>
<p>Fitness Antrenörü, 27</p>
</div>
</div>
</div>

<div class="testimonial-card">
<p class="testimonial-text">8 saat ayakta mutfakta çalışıyorum. Bel ağrıları işimi etkiliyordu. Şimdi duruşumu kontrol ediyorum, ağrılar %80 azaldı. Mesleğime daha güçlü devam ediyorum.</p>
<div class="testimonial-author">
<div class="testimonial-avatar">CY</div>
<div class="testimonial-info">
<h4>Can Y.</h4>
<p>Aşçıbaşı, 38</p>
</div>
</div>
</div>
</div>
</div>
</div>

<div class="final-cta">
<div class="container">
<h2>Sırt Sağlığınızı Kontrol Altına Alın</h2>
<p>Ağrı başlamadan önleyin. Kronik problemleri durdurun. Daha sağlıklı, daha üretken bir yaşam için bugün başlayın.</p>
<div class="urgency-bar">
⚡ Erken erişim kampanyası: İlk 100 kullanıcıya %30 indirim
</div>
<div class="cta-buttons">
<a href="/demo" class="cta-button primary">🎥 Demo'yu İzle</a>
<a href="#" class="cta-button secondary">📧 Erken Erişim Listesine Katıl</a>
</div>
</div>
</div>

<div class="footer">
<div class="container">
<p>&copy; 2026 SpineGuard. Tüm hakları saklıdır. | Sırt sağlığınız için bilimsel çözüm.</p>
</div>
</div>
</body>
</html>'''

@bp.route('/')
def index():
    return render_template_string(LANDING_HTML)
