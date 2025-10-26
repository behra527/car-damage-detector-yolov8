from flask import Flask, render_template, request, url_for
import os
from ultralytics import YOLO

app = Flask(__name__)

# Load YOLOv8 model
model = YOLO('models/best.pt')

# Class names for your model (update if your model uses different names)
CLASS_NAMES = ['Bonnet', 'Bumper', 'Dickey', 'Door', 'Fender', 'Light', 'Windshield']

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files.get('image')
    if not file:
        return render_template('index.html', result="No file uploaded.")
    # Save the uploaded image to a temp location
    upload_path = os.path.join('static', 'uploaded.jpg')
    file.save(upload_path)
    # Run YOLOv8 prediction
    results = model(upload_path)
    # Save the result image with bounding boxes
    detected_path = os.path.join('static', 'detected.jpg')
    results[0].save(detected_path)
    # Get detected class IDs
    detected_classes = set()
    for box in results[0].boxes:
        class_id = int(box.cls.item())
        if 0 <= class_id < len(CLASS_NAMES):
            detected_classes.add(CLASS_NAMES[class_id])
    if detected_classes:
        result = "Detected parts: " + ", ".join(detected_classes)
    else:
        result = "No damage detected."
    return render_template('index.html', result=result, detected_image='detected.jpg', uploaded_image='uploaded.jpg')

if __name__ == '__main__':
    app.run(debug=True)