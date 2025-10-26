# 🚗 Car Damage Detector (YOLOv8 + Flask)

This project uses a **YOLOv8** model to automatically detect **car damage** in uploaded images.  
It’s a simple **Flask-based web application** that allows users to upload a car image and view detected damage areas in real time.

## 📸 Demo
Upload an image of a car, and the app will highlight the damaged parts using bounding boxes drawn by the trained YOLOv8 model.



## 🧠 Model Details
- **Model**: YOLOv8 (trained with [Ultralytics](https://github.com/ultralytics/ultralytics))
- **Task**: Object Detection  
- **Dataset**: Custom dataset of car damage images  
- **Classes**: `["scratch", "dent", "broken_light", "crack", ...]` *(example — replace with your actual classes)*



## 🧩 Tech Stack

| Component | Version | Description |
|------------|----------|-------------|
| **Flask** | 3.1.0 | Backend web framework |
| **Jinja2** | 3.1.4 | Template engine for Flask |
| **Ultralytics** | 8.3.32 | YOLOv8 model and inference |



## 🚀 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/car-damage-detector-yolov8.git
cd car-damage-detector-yolov8

2️⃣ Create and Activate Virtual Environment
bash

Copy code
python -m venv venv
source venv/bin/activate      # on macOS/Linux
venv\Scripts\activate         # on Windows


3️⃣ Install Dependencies
bash

Copy code
pip install -r requirements.txt
requirements.txt

ini
Copy code
Flask==3.1.0
Jinja2==3.1.4
ultralytics==8.3.32

🧰 Usage
1️⃣ Run the Flask App
bash

Copy code
python app.py

2️⃣ Open in Browser
cpp
Copy code
http://127.0.0.1:5000/
3️⃣ Upload an Image
Upload an image of a car, and the model will detect and mark damaged areas.

📂 Project Structure
php
Copy code
car-damage-detector-yolov8/
│
├── app.py
├── static/
│   ├── uploads/         # uploaded images
│   └── results/         # output images with detections
├── templates/
│   └── index.html       # Jinja2 HTML template
├── weights/
│   └── best.pt          # your trained YOLOv8 model
├── requirements.txt
└── README.md
🧪 Example Output
Input	Output


🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📜 License
This project is licensed under the MIT License  see the LICENSE file for details.

🧑‍💻 Author
Your Name
📧 muhammadbehramhassan@gmail.com
🌐 GitHub

⭐ If you find this project useful, please consider giving it a star!



