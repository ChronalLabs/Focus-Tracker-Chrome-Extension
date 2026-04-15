# FocusTracker

## Two‑Line Description

FocusTracker is a Chrome extension that monitors your browsing activity and categorizes websites into **productive** and **distractive** to measure your focus.
It calculates a **Focus Score** using your productivity time vs total time and visualizes your performance with clean analytics dashboards.

---

# FocusTracker — Stay Productive, Stay Focused

FocusTracker is a productivity‑focused Chrome extension that tracks your browsing behavior across websites, categorizes them into **productive** or **distractive**, and generates a **Focus Score** to help you improve your daily efficiency.

Whether you're studying, working, or trying to reduce distractions, FocusTracker provides **real‑time insights** into how you spend your time online.

---

# Features

* 📊 Track time spent across multiple websites
* 🧠 Categorize websites into **Productive**, **Distractive**, and **Neutral**
* ⏱️ Rechecks browsing activity every **2 seconds**
* 🪟 Detects websites even when opened but not actively used
* 🎯 Focus Score calculation
* 📈 Visual analytics dashboard using charts
* ⚡ Fast backend using FastAPI
* 🎨 Clean UI with Bootstrap & Chart.js
* 🔄 Real-time tracking and updates

---

# 🎯 Focus Score Categories

| Focus Score | Category             | Meaning                |
| ----------- | -------------------- | ---------------------- |
| 0 — 39      | Require Improvement  | High distraction level |
| 40 — 69     | Average Focus Person | Moderate productivity  |
| 70 — 100    | High Focus Power     | Highly productive      |

---

# Focus Score Logic

```
focus_score = (productivity_time / total_time) * 100
```

* **Productivity Time** → Time spent on productive websites
* **Total Time** → Total browsing time tracked

Example:

* Productive Time = 3 hours
* Total Time = 5 hours

Focus Score = **60%**

---

# Tech Stack

### Backend

* Python 3
* FastAPI
* Uvicorn
* Pydantic
* SQLAlchemy
* Python Multipart

### Frontend

* HTML
* CSS
* JavaScript
* Bootstrap
* Chart.js
* FontAwesome
* Google Fonts

### Platform

* Google Chrome Extension

---

# Project Structure

```
FocusTracker/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── routes.py
│
├── extension/
│   ├── manifest.json
│   ├── background.js
│   ├── popup.html
│   ├── popup.js
│   └── styles.css
│
├── templates/
│   └── dashboard.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── charts/
│
└── README.md
```

---

# 💻 System Requirements

### Minimum Requirements

* Python **3.14** (Recommended) or **3.8+**
* Google Chrome (Latest Version)
* Chrome Developer Mode Enabled
* Minimum **512 MB RAM**
* At least **50 MB Disk Space**
* Localhost Network Configuration (No WiFi Required)
* Routing Activation Enabled
* Chrome Extension **Manifest V3** Configuration

---

# Installation Guide

## 1. Clone the Repository

```
git clone https://github.com/your-username/FocusTracker.git
cd FocusTracker
```

---

## 2. Create Virtual Environment

```
python -m venv venv
```

Activate Virtual Environment

### Windows

```
./venv/Scripts/activate
```

### Mac/Linux

```
source venv/bin/activate
```

---

## 3. Install Dependencies

```
pip install fastapi uvicorn sqlalchemy pydantic python-multipart
```

---

# Run the Backend Server

```
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# Load Chrome Extension

1. Open Google Chrome
2. Go to

```
chrome://extensions/
```

3. Enable **Developer Mode**
4. Click **Load Unpacked**
5. Select the extension folder

---

# Dashboard Features

* Daily Focus Score
* Productive vs Distractive Chart
* Website‑wise breakdown
* Time tracking visualization

---

# Use Cases

* Students preparing for exams
* Developers tracking coding time
* Remote workers improving focus
* Anyone reducing social media distractions

---

# Future Improvements

* AI‑based website classification
* Weekly & Monthly reports
* Productivity goals
* Block distracting websites
* Pomodoro Timer Integration

---

# Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch
3. Commit your changes
4. Push to branch
5. Open a Pull Request

---

# Support

If you found this project helpful, please consider giving it a **star ⭐**

---

# Contact

For suggestions or feedback, feel free to open an issue.

---

# Final Note

FocusTracker helps you **understand where your time goes**, so you can take control of your productivity and stay focused every day.

Stay Focused. Stay Productive. 🚀
