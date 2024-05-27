import cv2

# Take picture from webcam
def takePic():
    cap = cv2.VideoCapture(1)  # Open the webcam (use 0 if 1 does not work)
    if not cap.isOpened():
        print("Error: Could not open video device.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        
        # Display the frame
        cv2.imshow('Webcam', frame)

        # Wait for a key press
        key = cv2.waitKey(1)
        if key != -1:  # If a key is pressed
            # Save the frame as an image
            cv2.imwrite("pedro.png", frame)
            print("Image saved as 'pedro.png'")
            break

    # Release the webcam and close the display window
    cap.release()
    cv2.destroyAllWindows()

takePic()
