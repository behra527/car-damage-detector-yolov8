# Car Damage Detector (YOLOv8 + Flask)

A web-based car damage detection system built with **YOLOv8** and **Flask**. The application allows users to upload a car image and automatically detects visible damage using a trained object detection model.

## Badges

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.0-lightgrey?logo=flask)](https://flask.palletsprojects.com/)
[![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLOv8-purple)](https://ultralytics.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

---

## Overview

The **Car Damage Detector** uses a YOLOv8 object detection model to identify different types of visible damage in car images.

The project combines:

* YOLOv8 for object detection
* Ultralytics for model training and inference
* Flask for the web application
* HTML/Jinja2 for the user interface
* Image upload and result visualization

Users can upload an image of a car, and the system processes the image using the trained `best.pt` model and displays the detected damage.

---

## Key Objectives

* Detect visible car damage automatically.
* Identify different damage categories.
* Provide confidence scores for detected objects.
* Build a simple web interface for image-based detection.
* Integrate a trained YOLOv8 model with Flask.
* Display detection results directly in the browser.

---

## Project Details

| Component    | Details                      |
| ------------ | ---------------------------- |
| Project Type | Object Detection             |
| Domain       | Automotive / Computer Vision |
| Model        | YOLOv8                       |
| Framework    | Ultralytics                  |
| Backend      | Flask                        |
| Frontend     | HTML / Jinja2                |
| Dataset      | Custom Car Damage Dataset    |
| Model File   | `best.pt`                    |
| License      | MIT                          |

---

## Model

The project uses **YOLOv8**, an object detection architecture provided through the Ultralytics framework.

The trained model is stored as:

```text
weights/best.pt
```

During inference, the model receives an uploaded image and predicts:

* Damage location
* Damage class
* Confidence score
* Bounding box coordinates

Example detection classes may include:

```python
[
    "scratch",
    "dent",
    "broken_light",
    "crack"
]
```

Replace the example classes above with the actual classes used in your trained dataset.

---

## System Architecture

```text
User
  |
  v
Upload Car Image
  |
  v
Flask Web Application
  |
  v
YOLOv8 Model
  |
  v
Object Detection
  |
  +----> Damage Class
  |
  +----> Confidence Score
  |
  +----> Bounding Box
  |
  v
Annotated Result Image
  |
  v
Display Result in Browser
```

---

## Technology Stack

### Programming Language

* Python

### Backend

* Flask 3.1.0

### Template Engine

* Jinja2 3.1.4

### Computer Vision

* Ultralytics YOLOv8
* OpenCV through the detection pipeline

### Model

* YOLOv8
* Custom-trained weights

---

## Project Structure

```text
car-damage-detector-yolov8/
│
├── app.py
│
├── static/
│   ├── uploads/
│   └── results/
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

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/car-damage-detector-yolov8.git
cd car-damage-detector-yolov8
```

Replace `your-username` with your GitHub username.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Requirements

The project uses the following main dependencies:

```text
Flask==3.1.0
Jinja2==3.1.4
ultralytics==8.3.32
```

You can install them using:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask application:

```bash
python app.py
```

The application will run locally.

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

## Usage

### Step 1: Open the Web Application

Launch the Flask server and open the application in your browser.

### Step 2: Upload an Image

Select an image containing a car.

### Step 3: Run Detection

The uploaded image is passed to the YOLOv8 model.

### Step 4: View Results

The system displays the detected damage with bounding boxes and confidence scores.

---

## Detection Workflow

```text
Input Image
     |
     v
Image Upload
     |
     v
Flask Application
     |
     v
YOLOv8 Inference
     |
     v
Damage Detection
     |
     v
Bounding Boxes + Confidence
     |
     v
Result Image
     |
     v
Browser Display
```

---

## Model Inference

The trained YOLOv8 model can be loaded using Ultralytics:

```python
from ultralytics import YOLO

model = YOLO("weights/best.pt")

results = model("image.jpg")
```

The model returns detection results that can be used to identify damage classes and their locations.

---

## Input

The system accepts car images through the web interface.

Example:

```text
car_image.jpg
```

The uploaded image is stored temporarily in:

```text
static/uploads/
```

---

## Output

The processed image containing detected damage is stored in:

```text
static/results/
```

The output can contain:

* Bounding boxes
* Damage labels
* Confidence scores

Example:

```text
Scratch     0.91
Dent        0.87
Crack       0.79
```

These values are examples only and depend on the actual model prediction.

---

## Main Components

### `app.py`

The main Flask application responsible for:

* Starting the web server
* Handling image uploads
* Loading the YOLOv8 model
* Running inference
* Saving detection results
* Returning results to the frontend

### `templates/index.html`

Provides the web interface for:

* Image selection
* Uploading images
* Displaying detection results

### `weights/best.pt`

Contains the trained YOLOv8 model weights.

### `static/uploads/`

Stores uploaded input images.

### `static/results/`

Stores processed images containing detection results.

---

## Future Improvements

Possible improvements include:

* Add more car damage categories.
* Improve the training dataset.
* Add data augmentation.
* Improve model accuracy and generalization.
* Add image quality validation.
* Add confidence threshold controls.
* Add batch image detection.
* Add video-based damage detection.
* Deploy the application using Docker.
* Deploy the model to a cloud server.
* Add an API endpoint for external applications.
* Add database support for storing detection history.

---

## Limitations

* Detection performance depends on the quality and diversity of the training dataset.
* The model may perform poorly on damage types that were not included during training.
* Poor lighting, blurry images, and unusual viewing angles can affect detection.
* Small or partially hidden damage may be difficult to detect.
* Model performance should be evaluated on an independent test set before production deployment.

---

## Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test the application.
5. Commit your changes.
6. Push the branch.
7. Create a Pull Request.

Example:

```bash
git checkout -b feature/new-feature
git add .
git commit -m "Add new feature"
git push origin feature/new-feature
```

---

## License

This project is licensed under the **MIT License**.

The MIT License allows users to use, modify, distribute, and reuse the project subject to the license terms.

---

## Author

**Muhammad Behram Hassan**

AI Engineer | Machine Learning | Computer Vision

Email: `muhammadbehramhassan@gmail.com`

---

## Project Status

**Status:** Completed

The current version provides a Flask-based interface for uploading car images and performing YOLOv8-based damage detection using trained model weights.
