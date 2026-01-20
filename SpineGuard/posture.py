"""
SpineGuard - Complete Web Application
Landing page + Real-time Posture Detection
"""

import cv2
import numpy as np
from datetime import datetime
from flask import Flask, Response, render_template_string, request
import os

os.environ['OPENCV_LOG_LEVEL'] = 'FATAL'

try:
    from ultralytics import YOLO
except ImportError:
    print("Ultralytics kütüphanesi bulunamadı!")
    print("Lütfen şunu çalıştırın: pip install ultralytics flask opencv-python")
    exit()

class PostureAnalyzer:
    def __init__(self):
        print("YOLOv8 Pose modeli yükleniyor...")
        self.model = YOLO('yolov8n-pose.pt')
        self.NECK_ANGLE_THRESHOLD = 160
        self.BACK_ANGLE_THRESHOLD = 160
        self.SHOULDER_DIFF_THRESHOLD = 30
        self.bad_posture_frames = 0
        self.ALERT_THRESHOLD = 30
        self.NOSE = 0
        self.LEFT_EAR = 3
        self.RIGHT_EAR = 4
        self.LEFT_SHOULDER = 5
        self.RIGHT_SHOULDER = 6
        self.LEFT_ELBOW = 7
        self.RIGHT_ELBOW = 8
        self.LEFT_WRIST = 9
        self.RIGHT_WRIST = 10
        self.LEFT_HIP = 11
        self.RIGHT_HIP = 12
        self.SKELETON = [
            (self.LEFT_SHOULDER, self.RIGHT_SHOULDER),
            (self.LEFT_SHOULDER, self.LEFT_ELBOW),
            (self.RIGHT_SHOULDER, self.RIGHT_ELBOW),
            (self.LEFT_ELBOW, self.LEFT_WRIST),
            (self.RIGHT_ELBOW, self.RIGHT_WRIST),
            (self.LEFT_SHOULDER, self.LEFT_HIP),
            (self.RIGHT_SHOULDER, self.RIGHT_HIP),
            (self.LEFT_HIP, self.RIGHT_HIP),
        ]
        print("Model hazır!")
    
    def calculate_angle(self, p1, p2, p3):
        if p1 is None or p2 is None or p3 is None:
            return None
        a = np.array([p1[0], p1[1]])
        b = np.array([p2[0], p2[1]])
        c = np.array([p3[0], p3[1]])
        ba = a - b
        bc = c - b
        norm_ba = np.linalg.norm(ba)
        norm_bc = np.linalg.norm(bc)
        if norm_ba < 1e-6 or norm_bc < 1e-6:
            return None
        cosine_angle = np.dot(ba, bc) / (norm_ba * norm_bc)
        angle = np.arccos(np.clip(cosine_angle, -1.0, 1.0))
        return np.degrees(angle)
    
    def get_keypoint(self, keypoints, index, confidence_threshold=0.5):
        if len(keypoints) > index:
            x, y, conf = keypoints[index]
            if conf > confidence_threshold:
                return (int(x), int(y))
        return None
    
    def analyze_posture(self, keypoints):
        issues = []
        metrics = {'neck_angle': 0, 'back_angle': 0, 'shoulder_diff': 0}
        if keypoints is None or len(keypoints) < 13:
            return issues, metrics
        left_ear = self.get_keypoint(keypoints, self.LEFT_EAR)
        right_ear = self.get_keypoint(keypoints, self.RIGHT_EAR)
        left_shoulder = self.get_keypoint(keypoints, self.LEFT_SHOULDER)
        right_shoulder = self.get_keypoint(keypoints, self.RIGHT_SHOULDER)
        left_hip = self.get_keypoint(keypoints, self.LEFT_HIP)
        right_hip = self.get_keypoint(keypoints, self.RIGHT_HIP)
        shoulder_mid = None
        if left_shoulder and right_shoulder:
            shoulder_mid = ((left_shoulder[0] + right_shoulder[0]) // 2,
                          (left_shoulder[1] + right_shoulder[1]) // 2)
        hip_mid = None
        if left_hip and right_hip:
            hip_mid = ((left_hip[0] + right_hip[0]) // 2,
                      (left_hip[1] + right_hip[1]) // 2)
        ear_mid = None
        if left_ear and right_ear:
            ear_mid = ((left_ear[0] + right_ear[0]) // 2,
                      (left_ear[1] + right_ear[1]) // 2)
        if ear_mid and shoulder_mid and hip_mid:
            neck_angle = self.calculate_angle(ear_mid, shoulder_mid, hip_mid)
            if neck_angle:
                metrics['neck_angle'] = neck_angle
                if neck_angle < self.NECK_ANGLE_THRESHOLD:
                    issues.append(f"Boyun one egik! ({neck_angle:.1f})")
        if shoulder_mid and hip_mid:
            vertical_point = (hip_mid[0], hip_mid[1] + 200)
            back_angle = self.calculate_angle(shoulder_mid, hip_mid, vertical_point)
            if back_angle:
                metrics['back_angle'] = back_angle
                if back_angle < self.BACK_ANGLE_THRESHOLD:
                    issues.append(f"Sirt kamburlasmis! ({back_angle:.1f})")
        if left_shoulder and right_shoulder:
            shoulder_diff = abs(left_shoulder[1] - right_shoulder[1])
            metrics['shoulder_diff'] = shoulder_diff
            if shoulder_diff > self.SHOULDER_DIFF_THRESHOLD:
                side = "sol" if left_shoulder[1] < right_shoulder[1] else "sag"
                issues.append(f"Omuzlar dengesiz! ({side} yuksek)")
        return issues, metrics
    
    def draw_skeleton(self, frame, keypoints):
        for connection in self.SKELETON:
            pt1 = self.get_keypoint(keypoints, connection[0])
            pt2 = self.get_keypoint(keypoints, connection[1])
            if pt1 and pt2:
                cv2.line(frame, pt1, pt2, (0, 255, 255), 3)
        for i in range(len(keypoints)):
            pt = self.get_keypoint(keypoints, i)
            if pt:
                cv2.circle(frame, pt, 6, (0, 0, 255), -1)
                cv2.circle(frame, pt, 8, (255, 255, 255), 2)
        return frame
    
    def draw_feedback(self, image, issues, metrics):
        overlay = image.copy()
        panel_height = min(220, 70 + len(issues) * 30)
        cv2.rectangle(overlay, (10, 10), (550, panel_height), (0, 0, 0), -1)
        image = cv2.addWeighted(overlay, 0.7, image, 0.3, 0)
        cv2.putText(image, "SpineGuard - Durus Analizi", (20, 40),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        if issues:
            color = (0, 0, 255)
            y_offset = 75
            for issue in issues[:4]:
                cv2.putText(image, issue, (20, y_offset),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
                y_offset += 30
        else:
            cv2.putText(image, "Durus Mukemmel!", (20, 75),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        metrics_y = panel_height - 30
        metric_text = []
        if metrics['neck_angle'] > 0:
            metric_text.append(f"Boyun: {metrics['neck_angle']:.1f}")
        if metrics['back_angle'] > 0:
            metric_text.append(f"Sirt: {metrics['back_angle']:.1f}")
        if metric_text:
            cv2.putText(image, " | ".join(metric_text), (20, metrics_y),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        return image
    
    def generate_frames(self, camera_index=0):
        cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                results = self.model(frame, verbose=False)
                if results and len(results) > 0:
                    result = results[0]
                    if result.keypoints is not None and len(result.keypoints) > 0:
                        keypoints = result.keypoints.data[0].cpu().numpy()
                        frame = self.draw_skeleton(frame, keypoints)
                        issues, metrics = self.analyze_posture(keypoints)
                        if issues:
                            self.bad_posture_frames += 1
                            if self.bad_posture_frames >= self.ALERT_THRESHOLD:
                                print(f"\nUYARI: {datetime.now().strftime('%H:%M:%S')}")
                                for issue in issues:
                                    print(f"  {issue}")
                                self.bad_posture_frames = 0
                        else:
                            self.bad_posture_frames = max(0, self.bad_posture_frames - 1)
                        frame = self.draw_feedback(frame, issues, metrics)
                ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
                frame = buffer.tobytes()
                yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        finally:
            cap.release()

app = Flask(__name__)
analyzer = None

def get_available_cameras():
    available = []
    for i in range(10):
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        if cap.isOpened():
            available.append(i)
            cap.release()
    return available

EGITIM_PAGE = '''<!DOCTYPE html>
<html lang="tr"><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>SpineGuard - Eğitim</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;line-height:1.8;color:#333}
.nav{background:rgba(102,126,234,0.95);padding:15px 0;position:sticky;top:0;z-index:100;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
.nav .container{display:flex;justify-content:space-between;align-items:center}
.nav-brand{color:white;font-size:1.5em;font-weight:bold;text-decoration:none}
.nav-links{display:flex;gap:30px}
.nav-links a{color:white;text-decoration:none;font-weight:500;transition:opacity 0.3s}
.nav-links a:hover{opacity:0.8}
.container{max-width:1000px;margin:0 auto;padding:0 20px}
.hero-mini{background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:white;padding:60px 20px;text-align:center}
.hero-mini h1{font-size:2.5em;margin-bottom:15px}
.content{padding:60px 20px;background:white}
.section{margin-bottom:60px}
.section h2{color:#667eea;font-size:2em;margin-bottom:20px;padding-bottom:10px;border-bottom:3px solid #667eea}
.section h3{color:#764ba2;font-size:1.5em;margin:30px 0 15px 0}
.spine-diagram{background:#f8f9fa;padding:40px;border-radius:15px;margin:30px 0;text-align:center}
.spine-parts{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:20px;margin:30px 0}
.spine-part{background:white;padding:25px;border-radius:10px;box-shadow:0 3px 15px rgba(0,0,0,0.08);border-left:4px solid #667eea}
.spine-part h4{color:#667eea;margin-bottom:10px;font-size:1.2em}
.measurement-section{background:linear-gradient(135deg,rgba(102,126,234,0.1),rgba(118,75,162,0.1));padding:40px;border-radius:15px;margin:30px 0}
.measurement-points{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:25px;margin:30px 0}
.measurement-point{background:white;padding:30px;border-radius:10px;box-shadow:0 5px 20px rgba(0,0,0,0.1);transition:transform 0.3s}
.measurement-point:hover{transform:translateY(-5px)}
.measurement-point .number{background:linear-gradient(135deg,#667eea,#764ba2);color:white;width:50px;height:50px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.5em;font-weight:bold;margin-bottom:15px}
.measurement-point h4{color:#667eea;margin-bottom:10px;font-size:1.3em}
.highlight-box{background:#fff3cd;border-left:5px solid #ffc107;padding:20px;border-radius:5px;margin:20px 0}
.info-box{background:#d1ecf1;border-left:5px solid#17a2b8;padding:20px;border-radius:5px;margin:20px 0}
.cta-box{background:linear-gradient(135deg,#667eea,#764ba2);color:white;padding:40px;border-radius:15px;text-align:center;margin:40px 0}
.cta-box h3{font-size:1.8em;margin-bottom:15px}
.cta-box .btn{display:inline-block;background:white;color:#667eea;padding:15px 35px;border-radius:50px;text-decoration:none;font-weight:bold;margin:10px;transition:transform 0.3s}
.cta-box .btn:hover{transform:translateY(-3px)}
ul{margin:15px 0 15px 30px}
li{margin:8px 0}
@media(max-width:768px){.hero-mini h1{font-size:1.8em}.nav-links{gap:15px;font-size:0.9em}}
</style>
</head>
<body>
<nav class="nav">
<div class="container">
<a href="/" class="nav-brand">SpineGuard</a>
<div class="nav-links">
<a href="/">Ana Sayfa</a>
<a href="/egitim">Eğitim</a>
<a href="/demo">Demo</a>
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
<div class="section">
<h2>🦴 Omurganın Yapısı</h2>
<p>Omurga, insan vücudunun merkezi destek sistemidir. 33 omur kemikten oluşur ve vücudun ağırlığını taşırken aynı zamanda omurilik sinir sistemini korur. Sağlıklı bir omurga, belirli doğal eğriliklere sahiptir:</p>
<div class="spine-parts">
<div class="spine-part">
<h4>🔵 Servikal (Boyun)</h4>
<p><strong>7 omur</strong></p>
<p>Başı taşır ve geniş hareket açısı sağlar. İçe doğru eğri (lordoz)</p>
</div>
<div class="spine-part">
<h4>🟢 Torasik (Göğüs)</h4>
<p><strong>12 omur</strong></p>
<p>Kaburgalara bağlanır ve göğüs kafesini oluşturur. Dışa doğru eğri (kifoz)</p>
</div>
<div class="spine-part">
<h4>🟡 Lumbar (Bel)</h4>
<p><strong>5 omur</strong></p>
<p>Vücudun ağırlığının çoğunu taşır. İçe doğru eğri (lordoz)</p>
</div>
<div class="spine-part">
<h4>🔴 Sakral & Koksiks</h4>
<p><strong>9 omur (kaynaşmış)</strong></p>
<p>Pelvis ile bağlantı noktası. Dışa doğru eğri</p>
</div>
</div>
<div class="info-box">
<strong>💡 Önemli:</strong> Bu doğal eğriler vücudun ağırlığını dengeli dağıtır ve şokları emer. Duruş bozuklukları bu eğrilerin aşırı artması veya azalmasıyla ortaya çıkar.
</div>
</div>

<div class="section">
<h2>⚠️ Yaygın Duruş Problemleri</h2>
<h3>1. Forward Head Posture (Öne Eğik Baş Duruşu)</h3>
<p>Modern yaşamın en yaygın duruş bozukluğu. Telefon veya bilgisayar kullanımı sırasında başın öne kayması:</p>
<ul>
<li>Her 2.5 cm öne kayma, boyun üzerindeki yükü <strong>4-5 kg artırır</strong></li>
<li>Kronik boyun ve omuz ağrısına yol açar</li>
<li>Baş ağrısı ve sinir sıkışmasına neden olabilir</li>
</ul>

<h3>2. Kyphosis (Kamburluk)</h3>
<p>Göğüs bölgesindeki doğal eğriliğin aşırı artması:</p>
<ul>
<li>Uzun süre oturarak çalışmadan kaynaklanır</li>
<li>Solunum kapasitesini %30'a kadar azaltabilir</li>
<li>Omurga esnekliğini düşürür</li>
</ul>

<h3>3. Lordosis (Aşırı Bel Eğriliği)</h3>
<p>Bel bölgesindeki içe doğru eğriliğin artması:</p>
<ul>
<li>Zayıf karın kasları ve oturma pozisyonundan kaynaklanır</li>
<li>Alt sırtta kronik ağrıya yol açar</li>
<li>Bel disklerine aşırı yük bindirir</li>
</ul>

<div class="highlight-box">
<strong>⚡ İstatistik:</strong> Ofis çalışanlarının %73'ü en az bir duruş bozukluğu yaşıyor. Bunların %65'i önlenebilir durumlardır.
</div>
</div>

<div class="section">
<h2>🎯 SpineGuard'ın 3 Nokta Ölçüm Sistemi</h2>
<p>Duruş analizi için bilimsel olarak kanıtlanmış en kritik üç nokta:</p>

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
</div>
</body></html>'''

LANDING_PAGE = '''<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>SpineGuard - Sırt Sağlığınızın Dijital Asistanı</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;line-height:1.6;color:#333}
.nav{background:rgba(102,126,234,0.95);padding:15px 0;position:sticky;top:0;z-index:100;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
.nav .container{display:flex;justify-content:space-between;align-items:center}
.nav-brand{color:white;font-size:1.5em;font-weight:bold;text-decoration:none}
.nav-links{display:flex;gap:30px}
.nav-links a{color:white;text-decoration:none;font-weight:500;transition:opacity 0.3s}
.nav-links a:hover{opacity:0.8}
.hero{background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:white;padding:80px 20px;text-align:center;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:url('data:image/svg+xml,<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="2" fill="white" opacity="0.1"/></svg>');animation:float 20s linear infinite}
@keyframes float{from{transform:translateY(0)}to{transform:translateY(-100px)}}
@keyframes fadeInUp{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:translateY(0)}}
.container{max-width:1200px;margin:0 auto;padding:0 20px;position:relative;z-index:1}
h1{font-size:3em;margin-bottom:20px;animation:fadeInUp .8s ease}
.subtitle{font-size:1.3em;margin-bottom:30px;opacity:.95;animation:fadeInUp 1s ease}
.stat{font-size:2.5em;font-weight:bold;margin:30px 0;animation:fadeInUp 1.2s ease}
.cta-button{display:inline-block;background:white;color:#667eea;padding:18px 40px;border-radius:50px;text-decoration:none;font-weight:bold;font-size:1.1em;margin:10px;transition:transform .3s,box-shadow .3s;animation:fadeInUp 1.4s ease}
.cta-button:hover{transform:translateY(-3px);box-shadow:0 10px 30px rgba(0,0,0,.2)}
.cta-button.demo{background:#ff6b6b;color:white}
.problems{padding:80px 20px;background:#f8f9fa}
.problem-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:30px;margin-top:50px}
.problem-card{background:white;padding:40px;border-radius:15px;box-shadow:0 5px 20px rgba(0,0,0,.08);transition:transform .3s}
.problem-card:hover{transform:translateY(-10px)}
.problem-icon{font-size:3em;margin-bottom:20px}
.problem-card h3{color:#667eea;margin-bottom:15px;font-size:1.5em}
.solutions{padding:80px 20px;background:white}
.solution-item{display:flex;align-items:center;margin:50px 0;gap:50px}
.solution-item:nth-child(even){flex-direction:row-reverse}
.solution-content{flex:1}
.solution-visual{flex:1;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);height:300px;border-radius:20px;display:flex;align-items:center;justify-content:center;color:white;font-size:4em}
.solution-item h3{color:#667eea;font-size:2em;margin-bottom:20px}
.features{padding:80px 20px;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:white;text-align:center}
.feature-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:40px;margin-top:50px}
.feature-item{padding:30px}
.feature-item h4{font-size:1.3em;margin:20px 0}
.cta-section{padding:100px 20px;text-align:center;background:#f8f9fa}
.cta-section h2{font-size:2.5em;margin-bottom:30px;color:#333}
.section-title{text-align:center;font-size:2.5em;margin-bottom:20px;color:#333}
.section-subtitle{text-align:center;font-size:1.2em;color:#666;margin-bottom:50px}
@media(max-width:768px){h1{font-size:2em}.solution-item{flex-direction:column!important}.stat{font-size:2em}.nav-links{gap:15px;font-size:0.9em}}
</style>
</head>
<body>
<nav class="nav">
<div class="container">
<a href="/" class="nav-brand">SpineGuard</a>
<div class="nav-links">
<a href="/">Ana Sayfa</a>
<a href="/egitim">Eğitim</a>
<a href="/demo">Demo</a>
</div>
</div>
</nav>
<div class="hero">
<div class="container">
<h1>Sırt Sağlığınızı Koruyun</h1>
<p class="subtitle">Giyilebilir teknoloji ile duruş bozukluklarını gerçek zamanlı takip edin, sağlıklı bir yaşam sürün</p>
<div class="stat">%80</div>
<p>İnsanların %80'i hayatında en az bir kere bel veya sırt ağrısı yaşar</p>
<br><br>
<a href="/demo" class="cta-button demo">🎥 Demo'yu Deneyin</a>
<a href="#" class="cta-button">Erken Erişim İçin Kayıt Olun</a>
</div>
</div>
<div class="problems">
<div class="container">
<h2 class="section-title">Sorunlar Önlenebilir</h2>
<p class="section-subtitle">Sırt ağrılarının çoğu, bilgi eksikliği ve farkındalık yetersizliğinden kaynaklanır</p>
<div class="problem-grid">
<div class="problem-card">
<div class="problem-icon">🤷</div>
<h3>Bilgi Eksikliği</h3>
<p>İnsanlar sırt ve bel bölgelerini tanımaz, neyin iyi neyin kötü olduğunu bilmez. Bu sorunları yaşadıklarında bile tam olarak nedenini anlayamazlar.</p>
</div>
<div class="problem-card">
<div class="problem-icon">👁️</div>
<h3>Farkındasızlık</h3>
<p>Çalışırken, dinlenirken veya TV izlerken duruş bozukluklarıyla gündelik hayatınızı geçirirsiniz. Zamanınızın büyük çoğunluğunu geçirdiğiniz anlarda bunu fark etmezsiniz.</p>
</div>
<div class="problem-card">
<div class="problem-icon">🧘</div>
<h3>Yanlış Egzersizler</h3>
<p>Esneme hareketleri yapmanız gerektiğini bilirsiniz ama nasıl yapacağınızı, doğru yapıp yapmadığınızı bilemezsiniz.</p>
</div>
</div>
</div>
</div>
<div class="solutions">
<div class="container">
<h2 class="section-title">Çözümümüz</h2>
<p class="section-subtitle">Giyilebilir teknoloji ve akıllı takip sistemi ile sırt sağlığınızı koruyun</p>
<div class="solution-item">
<div class="solution-content">
<h3>📚 Eğitim Platformu</h3>
<p>Sırt ve bel sağlığı hakkında kapsamlı bilgi edinin. Neyin iyi, neyin kötü olduğunu öğrenin. Sırt bölgenizi tanıyın ve nasıl bakım yapacağınızı keşfedin.</p>
<a href="/egitim" style="color:#667eea;font-weight:bold;text-decoration:none">→ Daha Fazla Bilgi</a>
</div>
<div class="solution-visual">📖</div>
</div>
<div class="solution-item">
<div class="solution-content">
<h3>⚡ Gerçek Zamanlı Duruş Takibi</h3>
<p>Giyilebilir cihazımız ile duruş bozuklukları anında tespit edilir. Canlı uyarılar alarak doğru duruş pozisyonunu korursunuz. Tüm verileriniz sürekli kayıt altında tutulur.</p>
</div>
<div class="solution-visual">📍</div>
</div>
<div class="solution-item">
<div class="solution-content">
<h3>🎯 Kişiselleştirilmiş Egzersiz Önerileri</h3>
<p>Size özel esneme hareketleri önerilir. Canlı hareket takibi ile egzersizleri doğru yaptığınızdan emin olursunuz. İlerlemeniz kaydedilir ve analiz edilir.</p>
</div>
<div class="solution-visual">💪</div>
</div>
<div class="solution-item">
<div class="solution-content">
<h3>👨‍⚕️ Doktor İşbirliği</h3>
<p>Kayıtlı verileriniz sayesinde doktorlar basit hareket bozukluğu ihtimalini kolayca eler. Altta yatan sorunlara hızla ulaşılması mümkün hale gelir.</p>
</div>
<div class="solution-visual">🏥</div>
</div>
</div>
</div>
<div class="features">
<div class="container">
<h2>Platform Özellikleri</h2>
<div class="feature-grid">
<div class="feature-item">
<div style="font-size:3em">⌚</div>
<h4>Giyilebilir Teknoloji</h4>
<p>Günlük hayatınıza kolayca entegre olan medikal olmayan akıllı cihaz</p>
</div>
<div class="feature-item">
<div style="font-size:3em">📊</div>
<h4>Detaylı Analiz</h4>
<p>Duruş alışkanlıklarınızı ve ilerlemenizi görselleştirin</p>
</div>
<div class="feature-item">
<div style="font-size:3em">🔔</div>
<h4>Akıllı Uyarılar</h4>
<p>Duruş bozukluğu olduğunda anında bildirim alın</p>
</div>
<div class="feature-item">
<div style="font-size:3em">📱</div>
<h4>Mobil Uygulama</h4>
<p>Her yerden verilerinize erişin ve egzersizlerinizi takip edin</p>
</div>
</div>
</div>
</div>
<div class="cta-section">
<div class="container">
<h2>Sırt Sağlığınızı Korumaya Bugün Başlayın</h2>
<p style="font-size:1.2em;color:#666;margin-bottom:40px">Erken erişim listesine katılın ve özel fırsatlardan yararlanın</p>
<a href="/demo" class="cta-button demo">🎥 Demo'yu Deneyin</a>
<a href="#" class="cta-button">Erken Erişim İçin Kayıt Olun</a>
</div>
</div>
</body>
</html>'''

DEMO_PAGE = '''<!DOCTYPE html>
<html><head><title>SpineGuard Demo</title>
<style>
body{margin:0;padding:20px;font-family:-apple-system,sans-serif;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);min-height:100vh;display:flex;flex-direction:column;align-items:center}
.back-button{position:absolute;top:20px;left:20px;background:rgba(255,255,255,.2);color:white;padding:10px 20px;border-radius:25px;text-decoration:none;font-weight:500}
.back-button:hover{background:rgba(255,255,255,.3)}
h1{color:white;margin-bottom:10px;margin-top:60px}
.subtitle{color:rgba(255,255,255,.9);margin-bottom:30px}
.camera-selector{background:rgba(255,255,255,.2);padding:15px 25px;border-radius:50px;margin-bottom:20px;display:flex;align-items:center;gap:15px}
.camera-selector label{color:white;font-weight:500}
.camera-selector select{padding:8px 15px;border-radius:20px;border:none;font-size:14px;cursor:pointer;background:white}
.camera-selector button{padding:8px 20px;border-radius:20px;border:none;background:white;color:#667eea;font-weight:bold;cursor:pointer}
.video-container{background:white;padding:20px;border-radius:20px;box-shadow:0 20px 60px rgba(0,0,0,.3);max-width:1280px;position:relative}
.loading{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);color:#667eea;font-size:1.2em;font-weight:bold}
img{max-width:100%;border-radius:10px;display:block;min-height:480px}
.info{color:white;margin-top:20px;text-align:center}
</style></head>
<body>
<a href="/" class="back-button">← Ana Sayfa</a>
<h1>🧍 SpineGuard - Canlı Demo</h1>
<p class="subtitle">Gerçek zamanlı duruş analizi</p>
<div class="camera-selector">
<label>📹 Kamera:</label>
<select id="cameraSelect">
{% for cam in cameras %}
<option value="{{cam}}" {%if cam==current_camera%}selected{%endif%}>Kamera {{cam}}</option>
{% endfor %}
</select>
<button onclick="changeCamera()">Değiştir</button>
<button onclick="startStream()" id="startBtn">▶ Başlat</button>
</div>
<div class="video-container">
<div class="loading" id="loading">Başlatmak için ▶ Başlat butonuna tıklayın</div>
<img id="videoStream" style="display:none">
</div>
<div class="info">
<p>Kameranın önünde durun ve duruşunuzu analiz edin</p>
</div>
<script>
let streamStarted=false;
function startStream(){
if(!streamStarted){
const select=document.getElementById('cameraSelect');
const camera=select.value;
const videoStream=document.getElementById('videoStream');
const loading=document.getElementById('loading');
const startBtn=document.getElementById('startBtn');
loading.textContent='Kamera başlatılıyor...';
videoStream.src='/video_feed?camera='+camera+'&t='+Date.now();
videoStream.style.display='block';
videoStream.onload=function(){loading.style.display='none';};
startBtn.textContent='⏸ Durdur';
startBtn.style.background='#ff6b6b';
startBtn.style.color='white';
streamStarted=true;
}else{
const videoStream=document.getElementById('videoStream');
const loading=document.getElementById('loading');
const startBtn=document.getElementById('startBtn');
videoStream.src='';
videoStream.style.display='none';
loading.style.display='block';
loading.textContent='Başlatmak için ▶ Başlat butonuna tıklayın';
startBtn.textContent='▶ Başlat';
startBtn.style.background='white';
startBtn.style.color='#667eea';
streamStarted=false;
}
}
function changeCamera(){
const select=document.getElementById('cameraSelect');
const newCamera=select.value;
const videoStream=document.getElementById('videoStream');
const loading=document.getElementById('loading');
videoStream.src='';
if(streamStarted){
loading.style.display='block';
loading.textContent='Kamera değiştiriliyor...';
videoStream.style.display='none';
setTimeout(function(){
videoStream.src='/video_feed?camera='+newCamera+'&t='+Date.now();
videoStream.style.display='block';
setTimeout(function(){loading.style.display='none';},500);
},300);
}
}
</script>
</body></html>'''

@app.route('/')
def index():
    return render_template_string(LANDING_PAGE)

@app.route('/egitim')
def egitim():
    return render_template_string(EGITIM_PAGE)

@app.route('/demo')
def demo():
    cameras = get_available_cameras()
    return render_template_string(DEMO_PAGE, cameras=cameras, current_camera=0)

@app.route('/video_feed')
def video_feed():
    camera = int(request.args.get('camera', 0))
    return Response(analyzer.generate_frames(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    print("="*60)
    print("SpineGuard - Web Application")
    print("="*60)
    print("\nKurulum: pip install ultralytics flask opencv-python")
    print("="*60)
    analyzer = PostureAnalyzer()
    cameras = get_available_cameras()
    print(f"\nKameralar: {cameras}")
    print("\n"+"="*60)
    print("Ana Sayfa: http://localhost:5000")
    print("Demo: http://localhost:5000/demo")
    print("Durdurmak: Ctrl+C")
    print("="*60+"\n")
    app.run(debug=False, threaded=True, port=5000)