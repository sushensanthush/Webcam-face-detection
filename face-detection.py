import cv2
import sys

def main():
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)

    if face_cascade.empty():
        print(f"Error: Could not load cascade classifier from {cascade_path}")
        sys.exit(1)

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video capture device.")
        sys.exit(1)

    window_name = 'Face Detection System'
    
    cv2.namedWindow(window_name)

    print("Press 'q' or click the window Close (X) button to exit.")

    while True:
        if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
            print("Window closed by user.")
            break

        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to grab frame.")
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray_frame,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow(window_name, frame)

      
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("'q' key pressed. Exiting...")
            break


    cap.release()
    cv2.destroyAllWindows()
    print("Video stream closed cleanly.")

if __name__ == "__main__":
    main()