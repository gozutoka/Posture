"""
SpineGuard - Duruş Analiz Motoru
YOLOv8 ile pose detection ve duruş analizi
"""

import cv2
import numpy as np
from datetime import datetime
from ultralytics import YOLO

class PostureAnalyzer:
    def __init__(self):
        print("YOLOv8 Pose modeli yükleniyor...")
        self.model = YOLO('yolov8n-pose.pt')
        self.NECK_ANGLE_THRESHOLD = 160
        self.BACK_ANGLE_THRESHOLD = 160
        self.SHOULDER_DIFF_THRESHOLD = 30
        self.bad_posture_frames = 0
        self.ALERT_THRESHOLD = 30
        
        # COCO Keypoints
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