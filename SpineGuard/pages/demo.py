"""
SpineGuard - Demo Sayfası
Gerçek zamanlı duruş analizi
"""

from flask import Blueprint, render_template_string, Response, request
import cv2
from posture_analyzer import PostureAnalyzer

bp = Blueprint('demo', __name__)

# Analyzer instance
analyzer = None

def get_available_cameras():
    available = []
    for i in range(10):
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        if cap.isOpened():
            available.append(i)
            cap.release()
    return available

DEMO_HTML = '''<!DOCTYPE html>
<html><head><title>SpineGuard - Canlı Demo | Gerçek Zamanlı Duruş Analizi</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
body{margin:0;padding:20px;font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:linear-gradient(135deg,#0f4c81 0%,#14b8a6 100%);min-height:100vh;display:flex;flex-direction:column;align-items:center;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}
.nav{background:rgba(255,255,255,0.98);padding:20px 0;position:fixed;top:0;left:0;right:0;z-index:1000;box-shadow:0 1px 3px rgba(0,0,0,0.04);border-bottom:1px solid #e2e8f0}
.nav .container{max-width:1200px;margin:0 auto;padding:0 20px;display:flex;justify-content:space-between;align-items:center}
.nav-brand{color:#0f4c81;font-size:1.6em;font-weight:900;text-decoration:none;letter-spacing:-0.5px}
.nav-links{display:flex;gap:35px;align-items:center}
.nav-links a{color:#475569;text-decoration:none;font-weight:500;transition:color 0.3s;font-size:0.95em}
.nav-links a:hover{color:#0f4c81}
.content{margin-top:100px;width:100%}
h1{color:white;margin-bottom:10px;margin-top:20px;text-align:center;font-weight:900;letter-spacing:-1px;font-size:2.5em}
.subtitle{color:rgba(255,255,255,.95);margin-bottom:30px;text-align:center;font-size:1.2em;font-weight:400}
.camera-selector{background:rgba(255,255,255,.15);padding:18px 30px;border-radius:12px;margin-bottom:25px;display:flex;align-items:center;gap:15px;justify-content:center;backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.2)}
.camera-selector label{color:white;font-weight:600}
.camera-selector select{padding:10px 18px;border-radius:8px;border:none;font-size:14px;cursor:pointer;background:white;font-family:'Inter',sans-serif;font-weight:500}
.camera-selector button{padding:10px 24px;border-radius:8px;border:none;background:white;color:#0f4c81;font-weight:700;cursor:pointer;transition:all 0.3s;box-shadow:0 2px 8px rgba(0,0,0,0.15);font-family:'Inter',sans-serif}
.camera-selector button:hover{transform:translateY(-2px);box-shadow:0 4px 12px rgba(0,0,0,0.2)}
.video-container{background:white;padding:20px;border-radius:15px;box-shadow:0 8px 30px rgba(0,0,0,.3);max-width:1280px;position:relative;margin:0 auto;border:1px solid #e2e8f0}
.loading{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);color:#0f4c81;font-size:1.2em;font-weight:700}
img{max-width:100%;border-radius:10px;display:block;min-height:480px}
.info{color:white;margin-top:25px;text-align:center;font-weight:400;font-size:1.05em}
.info p{opacity:0.95;margin:8px 0}
@media(max-width:768px){h1{font-size:2em}.nav-links{gap:15px;font-size:0.9em}}
</style></head>
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
<div class="content">
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
<p>Uyarılar konsola yazdırılacak</p>
</div>
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

@bp.route('/demo')
def demo():
    global analyzer
    if analyzer is None:
        analyzer = PostureAnalyzer()
    cameras = get_available_cameras()
    return render_template_string(DEMO_HTML, cameras=cameras, current_camera=0)

@bp.route('/video_feed')
def video_feed():
    camera = int(request.args.get('camera', 0))
    return Response(analyzer.generate_frames(camera), mimetype='multipart/x-mixed-replace; boundary=frame')