# Car Damage Detector (YOLOv8 + Flask)

[![Python](https://camo.githubusercontent.com/8ade7aa7794286744e80c85a211c7f0b6882c059eb17d0ac4a5e263cbfe44c6e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31302532422d626c75653f6c6f676f3d707974686f6e)](https://www.python.org/) [![Flask](https://camo.githubusercontent.com/dfb7a8b9ad83ae9f36193da7d6528998510962652a4db43c8e3e81d3765194c3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f466c61736b2d4261636b656e642d6c69676874677265793f6c6f676f3d666c61736b)](https://flask.palletsprojects.com/) [![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLOv8-blue?logo=ultralytics)](https://ultralytics.com/) [![YOLOv8][![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)(https://camo.githubusercontent.com/d6bc2b26794002c24d023acaab01b6dbb953c57ab9cb80ba5b8aa2f2bd5de99a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6f676f2d4d49542d626c7565)](LICENSE)

A computer vision application that uses a trained **YOLOv8 object detection model** to automatically identify and localize car damage in uploaded images.

The project provides a simple **Flask-based web interface** where users can upload a car image and view detected damage areas with bounding boxes.

---

## Project Overview

The Car Damage Detector is designed to detect different types of visible damage from car images.

The YOLOv8 model processes the uploaded image and identifies damage locations by generating bounding boxes and class labels.

### Key Objectives

* Detect visible car damage from images
* Localize damage using bounding boxes
* Classify detected damage types
* Provide predictions through a Flask web application
* Display detection results directly in the browser

---

## Demo

Upload an image of a car through the web interface. The trained YOLOv8 model processes the image and highlights detected damage areas using bounding boxes.

---

## Model Details

| Component     | Details                         |
| ------------- | ------------------------------- |
| Model         | YOLOv8                          |
| Framework     | Ultralytics                     |
| Task          | Object Detection                |
| Dataset       | Custom Car Damage Dataset       |
| Model Weights | `best.pt`                       |
| Input         | Car Images                      |
| Output        | Damage Classes + Bounding Boxes |

### Damage Classes

The model can be trained to detect different types of car damage, such as:

```text
scratch
dent
broken_light
crack
```

> Replace the classes above with the exact classes used in your trained model if they are different.

---

## System Architecture

```text
Car Image
    ↓
Image Upload
    ↓
Flask Web Application
    ↓
YOLOv8 Model
    ↓
Object Detection
    ↓
Damage Classification + Bounding Boxes
    ↓
Detection Result
    ↓
Display Result in Browser
```

---

## Tech Stack

| Component       | Version | Description                 |
| --------------- | ------- | --------------------------- |
| **Python**      | —       | Application development     |
| **Flask**       | 3.1.0   | Backend web framework       |
| **Jinja2**      | 3.1.4   | HTML template engine        |
| **Ultralytics** | 8.3.32  | YOLOv8 model and inference  |
| **YOLOv8**      | —       | Car damage object detection |

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/car-damage-detector-yolov8.git
cd car-damage-detector-yolov8
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Requirements

```text
Flask==3.1.0
Jinja2==3.1.4
ultralytics==8.3.32
```

---

## Usage

### 1. Run the Flask Application

```bash
python app.py
```

### 2. Open the Application

```text
http://127.0.0.1:5000/
```

### 3. Upload an Image

Upload a car image through the web interface.

The YOLOv8 model will:

1. Process the uploaded image.
2. Detect visible damage.
3. Draw bounding boxes around detected areas.
4. Assign damage class labels.
5. Save the detection result.
6. Display the processed image in the browser.

---

## Project Structure

```text
car-damage-detector-yolov8/
│
├── app.py
│
├── static/
│   ├── uploads/
│   │   └── uploaded images
│   │
│   └── results/
│       └── detection results
│
├── templates/
│   └── index.html
│
├── weights/
│   └── best.pt
│
├── requirements.txt
│
└── README.md
```

### Main Components

| File / Folder          | Purpose                                |
| ---------------------- | -------------------------------------- |
| `app.py`               | Flask application and prediction logic |
| `weights/best.pt`      | Trained YOLOv8 model weights           |
| `templates/index.html` | Web interface                          |
| `static/uploads/`      | Stores uploaded images                 |
| `static/results/`      | Stores processed detection images      |
| `requirements.txt`     | Python dependencies                    |
| `README.md`            | Project documentation                  |

---

## Detection Workflow

```text
1. User uploads car image
          ↓
2. Flask receives the image
          ↓
3. YOLOv8 loads the trained model
          ↓
4. Model performs object detection
          ↓
5. Damage areas are identified
          ↓
6. Bounding boxes are generated
          ↓
7. Result image is saved
          ↓
8. Result is displayed to the user
```

---

## Example Output

### Input

A car image containing visible damage.

### Output

The processed image contains:

* Bounding boxes around detected damage
* Damage class labels
* Detection confidence scores

Example:

```text
Detected Damage:
- Scratch
- Dent

Confidence:
Scratch: 0.91
Dent: 0.87
```

The example values above are only for illustration and should be replaced with actual model output when available.

---

## Model Inference

The trained YOLOv8 model is loaded from:

```text
weights/best.pt
```

The model performs object detection on the uploaded image and returns detected objects along with their bounding-box coordinates and confidence scores.

---

## Future Improvements

* Improve detection accuracy with a larger dataset
* Add more car damage categories
* Add confidence threshold controls
* Support multiple image uploads
* Add image history and result management
* Add REST API support
* Deploy the application using Docker
* Deploy the application to a cloud platform
* Optimize the model for faster inference
* Add real-time camera-based damage detection

---

## Limitations

* Detection performance depends on the quality and diversity of the training dataset.
* Very small or unclear damage may be difficult to detect.
* Poor lighting, image quality, or unusual viewing angles can affect predictions.
* The model should be evaluated on independent data before production use.
* Detection results should be treated as automated assistance rather than a definitive insurance or repair assessment.

---

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push the branch.
6. Open a Pull Request.

For major changes, open an issue first to discuss the proposed changes.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Author

**Muhammad Behram Hassan**

AI Engineer | Machine Learning | Computer Vision | Generative AI

Email: `muhammadbehramhassan@gmail.com`

---

## Support

If you find this project useful, consider giving the repository a star and sharing your feedback.
