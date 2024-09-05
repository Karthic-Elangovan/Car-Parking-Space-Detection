import sys
import cv2
import pickle
import numpy as np
from tensorflow.keras.models import  load_model

sys.stdout.reconfigure(encoding='utf-8')

model = load_model("model_final.h5")

class_dictionary = {0: 'no car', 1:'car'}

video = cv2.VideoCapture("car_test.mp4")

with open('carposition.pkl', 'rb') as f:
    positionList = pickle.load(f)

width = 130
height = 65

def checkingCarParking(img):
    imgCrops = []
    spaceCounter = 0
    for pos in positionList:
        x, y = pos
        cropped_img = img[y:y+height, x:x+width]
        imgResized = cv2.resize(cropped_img, (48,48))
        imgNormalized = imgResized/255.0
        imgCrops.append(imgNormalized)
    imgCrops = np.array(imgCrops)
    predictions = model.predict(imgCrops)

    for i, pos in enumerate(positionList):
        x, y = pos
        intId = np.argmax(predictions[i])
        label = class_dictionary[intId]
        if label == 'no car':
            color = (0,255,0)
            thickness = 5
            spaceCounter +=1
            textColor = (0,0,0)
        else:
            color = (0,0,255)
            thickness = 2
            textColor = (255,255,255)

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cv2.putText(img, label,(x, y+height-3), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    cv2.putText(img, f'Space Count: {spaceCounter}', (100, 50), (cv2.FONT_HERSHEY_SIMPLEX), 1, textColor, 2)

while True:
    if video.get(cv2.CAP_PROP_POS_FRAMES) == video.get(cv2.CAP_PROP_FRAME_COUNT):
        video.set(cv2.CAP_PROP_FRAMES, 0)
    ret, image = video.read()
    image = cv2.resize(image, (1280, 720))
    if not ret:
        break
    checkingCarParking(image)
    cv2.imshow("Image", image)
    if cv2.waitKey(10) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
