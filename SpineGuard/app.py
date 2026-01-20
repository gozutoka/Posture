"""
SpineGuard - Ana Uygulama
Tüm modülleri bir araya getirir
"""

from flask import Flask
import os

os.environ['OPENCV_LOG_LEVEL'] = 'FATAL'

# Modülleri import et
from pages import landing, egitim, demo, nasil_calisir, developer

# Flask uygulaması oluştur
app = Flask(__name__)

# Route'ları kaydet
app.register_blueprint(landing.bp)
app.register_blueprint(egitim.bp)
app.register_blueprint(demo.bp)
app.register_blueprint(nasil_calisir.bp)
app.register_blueprint(developer.bp)  # TEMPORARY - Remove before production

if __name__ == "__main__":
    print("=" * 60)
    print("SpineGuard - Web Application")
    print("=" * 60)
    print("\nKurulum: pip install ultralytics flask opencv-python")
    print("=" * 60)
    
    print("\n" + "=" * 60)
    print("Ana Sayfa: http://localhost:5000")
    print("Eğitim: http://localhost:5000/egitim")
    print("Nasıl Çalışır: http://localhost:5000/nasil-calisir")
    print("Demo: http://localhost:5000/demo")
    print("Durdurmak: Ctrl+C")
    print("=" * 60 + "\n")
    
    app.run(debug=False, threaded=True, host='0.0.0.0', port=5000)