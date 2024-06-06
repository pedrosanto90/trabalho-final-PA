import cv2
import numpy as np
import face_recognition
import os
from main import main_window
from src.database.users import verify_login

# Define path to images
path = 'images'
images = []
classNames = []

# Ensure the path exists
if not os.path.exists(path):
    raise FileNotFoundError(f"The directory '{path}' does not exist.")

# List images in the directory
myList = os.listdir(path)

print(myList)

# Load images and class names
for cl in myList:
    curImg = cv2.imread(os.path.join(path, cl))
    if curImg is None:
        print(f"Warning: Could not load image {cl}. Skipping.")
        continue
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

# Function to find encodings for all images
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img)
        if encodings:
            encodeList.append(encodings[0])
        else:
            print("Warning: No faces found in an image. Skipping.")
    return encodeList

def faceRec():
    # Get known encodings
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    # Start webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise RuntimeError("Error: Could not open webcam.")

    try:
        while True:
            success, img = cap.read()
            if not success:
                print("Warning: Failed to capture image. Retrying...")
                continue

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
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

                    # Show the name on the image for a brief period before calling main_window
                    cv2.imshow('Webcam', img)
                    cv2.waitKey(2500)  # Wait for 2.5 seconds
                    cap.release()
                    cv2.destroyAllWindows()
                    if verify_login(name) == "Operador":
                        main_window("Operador")
                    else:
                        main_window("Contabilidade")
                    return  # Exit the function after calling main_window

            cv2.imshow('Webcam', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    faceRec()
