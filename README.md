# Car-Parking-Space-Detection
---

### Overview
This project presents a dynamic web-based solution for detecting and counting available and occupied parking spaces in real-time video streams. By leveraging cutting-edge deep learning techniques and computer vision tools, the application accurately classifies each parking spot as either free or occupied. Built with **Flask**, **OpenCV**, and **TensorFlow/Keras**, the system processes video feeds to display live results, including the current status of parking spaces.

---

## ✨ Key Features
- **Real-Time Detection**: Effortlessly track parking space availability in live video streams.
- **Parking Space Status**: Classifies predefined spaces as "occupied" or "available" using a pre-trained CNN model.
- **Live Video Stream Overlay**: Visualize real-time data with overlaid parking space information directly on the video feed.
- **REST API Integration**: Access current space availability via a simple API for external use.

---

## 🛠️ Technology Stack
- **Flask**: Lightweight web framework for serving the application.
- **OpenCV**: For handling and processing video streams in real-time.
- **TensorFlow/Keras**: Deep learning framework used for car detection through a trained Convolutional Neural Network (CNN).
- **NumPy**: High-performance numerical operations and array handling.
- **Pickle**: For saving and loading parking space configuration data.

---

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/Karthic-Elangovan/Car-Parking-Space-Detection.git
cd parking-space-detection
```

### 2. Install the Required Dependencies

The following packages are required to run the application:
- Flask
- OpenCV
- TensorFlow/Keras
- NumPy
- Pickle

```bash
pip install -r requirements.txt
```

### 3. Prepare Required Files
- **Model**: Place the trained CNN model (`model_final.h5`) in the root directory.
- **Parking Configuration**: Ensure the file `carposition.pkl` is available, containing the saved parking spot locations.
- **Video Feed**: Include a video file (e.g., `car_test.mp4`) for testing in the project directory.

### 4. Launch the Application
Start the Flask server:
```bash
python app.py
```


---


## ⚙️ How It Works
1. **Video Frame Processing**: The application reads the video stream frame by frame.
2. **Parking Spot Detection**: Each frame is analyzed to check predefined parking spaces using the CNN model, classifying each spot as either occupied or free.
3. **Overlay Information**: The status of each parking space is overlaid onto the video feed, providing a clear visual display of real-time availability.
4. **Space Count API**: The `/space_count` API endpoint returns a JSON response with the current number of free and occupied spaces.


---

## 🤝 Contribution Guidelines
We welcome contributions! Whether it's bug fixes, new features, or improvements, feel free to fork the repository, submit issues, or make pull requests.

---

Demo Video:https://drive.google.com/file/d/1rxdaPOtBfZCNgTlF8EEguFlOKueVk5j9/view?usp=sharing
