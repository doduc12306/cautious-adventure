from flask import Flask, render_template, Response, jsonify
import cv2
import face_recognition
import numpy as np
import urllib.request
import os
from datetime import datetime

app = Flask(__name__)

# Dữ liệu nhận diện
path = r'/home/duc/Downloads/ATTENDANCE/image_folder'
url = 'http://172.20.10.3/cam-hi.jpg'

images = []
classNames = []

attendance_log = {}  # tên -> giờ gần nhất
attendance_history = []  # danh sách toàn bộ lịch sử

# Load ảnh và tên
myList = os.listdir(path)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodings(images)

# Ghi nhận điểm danh và lịch sử
def markAttendance(name):
    now = datetime.now().strftime('%H:%M:%S')
    attendance_log[name] = now
    attendance_history.append({'name': name, 'time': now})

# Luồng xử lý video
def gen_frames():
    while True:
        try:
            img_resp = urllib.request.urlopen(url)
            imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
            img = cv2.imdecode(imgnp, -1)

            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
                    markAttendance(name)

            ret, buffer = cv2.imencode('.jpg', img)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        except Exception as e:
            print("Video stream error:", e)

# Giao diện chính
@app.route('/')
def index():
    return render_template('index.html')

# Truyền video
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Trả vị trí xe (cố định)
@app.route('/location')
def location():
    return jsonify({'lat': 21.005144, 'lng': 105.843410})

# Trả học sinh đã điểm danh (gần nhất)
@app.route('/attendance')
def attendance():
    return jsonify(attendance_log)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
