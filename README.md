# 🚌 Smart Student Boarding Monitoring System

> Real-time system for monitoring student boarding using face recognition, live camera, and a web dashboard.

---

## 🎯 Project Objective

This system allows **automatic and real-time monitoring of student boarding and alighting** using a camera (e.g. ESP32-CAM or USB webcam) and facial recognition. It features a **live web dashboard** for:

- ✅ Student check-in tracking
- ✅ Time logging
- ✅ Attendance summary chart
- ✅ Entry/exit history
- ✅ Real-time map of school bus

---

## ⚙️ Technologies Used

| Component             | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| 👁️ Facial Recognition  | Uses `face_recognition` and OpenCV to identify students from saved images. |
| 📷 Camera Feed         | Captures video stream (supports IP cameras or local USB webcams).           |
| 🌐 Flask Web Server    | Serves a local dashboard accessible via LAN.                                |
| 📊 Chart.js            | Displays attendance summary in a pie chart.                                 |
| 🗺️ Leaflet.js + OSM    | Shows current location of the school bus (static for demo).                 |
| 🧾 Attendance History  | Logs all student check-in events with timestamps.                           |

---

## 🧩 System Workflow

```mermaid
graph LR
A[Camera Captures Image] --> B[Run Face Recognition]
B --> C{Face Matched?}
C -- Yes --> D[Log Time + Name]
D --> E[Update Attendance List]
E --> F[Display on Web Dashboard]
````

---

## 📂 Project Structure

```
smart-attendance/
├── app.py                # Main Flask server (Python)
├── templates/
│   └── index.html        # Dashboard UI (camera, chart, map, list)
├── image_folder/         # Face images of students
├── requirements.txt      # Python dependencies
└── README.md             # You’re here
```

---

## 🔧 Setup Instructions

### ✅ Requirements

* Python 3.9+
* Linux (tested on Arch Linux), Windows, or macOS
* IP camera or webcam
* Dependencies in `requirements.txt`

### ✅ Installation

```bash
# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # Or 'venv\Scripts\activate' on Windows

# Install Python packages
pip install -r requirements.txt
```

> ⚠️ On Arch Linux, use system packages if needed:

```bash
sudo pacman -S python-opencv dlib cmake
```

---

## 🚀 Run the System

### 🧠 Start Flask Web Server

```bash
python app.py
```

It will start at:

```
http://0.0.0.0:5000
```

---

## 📱 Access from Your Phone (Same Wi-Fi)

1. Get your local IP:

```bash
ip a
```

Find something like `192.168.x.x`

2. On your phone, open browser and go to:

```
http://<your-ip>:5000
```

**Example:**

```
http://192.168.1.10:5000
```

> ✅ Make sure your phone is on the same Wi-Fi network.

---

## 🌐 Web Dashboard Features

* 🎥 Live camera feed from your bus or device
* 📊 Doughnut chart of attendance status
* 📋 Live student check-in list
* 🕒 History of entries with time
* 🗺️ School bus map (currently fixed to Hanoi University of Science and Technology)

---

## 📤 Data Logged

| Field       | Description                |
| ----------- | -------------------------- |
| `name`      | Student’s name             |
| `time`      | Check-in time (HH\:MM\:SS) |
| `history[]` | Full list of entry events  |

---

## 📸 Screenshot Placeholder

> Replace this with real UI screenshot when available

![UI Example](https://i.pinimg.com/736x/ef/9d/49/ef9d4976e27a723afb52bb39f471fb7b.jpg)

---

## 🛠 Future Improvements

* ✅ Add GPS integration for real-time bus tracking
* ✅ Separate views for parents and school admins
* ✅ Add email/SMS alerts for late/no-shows
* ✅ Integrate with RFID/NFC check-in

---

## 📄 License

This project is open-sourced under the [MIT License](./LICENSE).

---

## 🤝 Contributions

Contributions are welcome!

* Fork this repository
* Submit pull requests
* Report issues or suggest features

