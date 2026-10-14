import cv2
import time
import winsound  # Import winsound

# Absolute paths to the Haar cascade files
face_cascade_path = r"C:\Users\yakes\Downloads\FINAL YEAR PRO\FINAL YEAR PRO\haarcascade_frontalface_default.xml"
eye_cascade_path = r"C:\Users\yakes\Downloads\FINAL YEAR PRO\FINAL YEAR PRO\haarcascade_eye.xml"

# Load the Haar cascade files
face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

# Verify if the cascades loaded correctly
if face_cascade.empty():
    print("Error loading face cascade file. Check the path.")
    exit()
if eye_cascade.empty():
    print("Error loading eye cascade file. Check the path.")
    exit()

# Initialize the webcam (0 for default webcam)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open webcam")
    exit()

# Parameters for drowsiness detection
consecutive_frames_threshold = 3  # Number of consecutive frames eyes must be closed
distraction_threshold = 2  # seconds head turns away
eye_closed_counter = 0
head_turn_start_time = None
alarm_triggered = False  # To prevent multiple alarms

def trigger_alarm():
    global alarm_triggered
    if not alarm_triggered:
        alarm_triggered = True
        print("ALARM! Wake up or stop distractions!")
        # Play beep sound: frequency=2500Hz, duration=1000ms
        winsound.Beep(2500, 1000)

def detect_eyes_and_face(frame):
    global eye_closed_counter, head_turn_start_time, alarm_triggered
    
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect face
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    # Loop over all detected faces
    for (x, y, w, h) in faces:
        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Region of interest for eyes within the face rectangle
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        
        # Detect eyes within the face
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5)
        num_eyes_detected = len(eyes)
        
        # Draw rectangles around detected eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        
        # Display the number of detected eyes for debugging
        cv2.putText(frame, f"Eyes Detected: {num_eyes_detected}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        if num_eyes_detected < 2:
            eye_closed_counter += 1
            cv2.putText(frame, f"Eyes Closed Frames: {eye_closed_counter}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            if eye_closed_counter >= consecutive_frames_threshold:
                cv2.putText(frame, "Drowsiness Detected!", (100, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                trigger_alarm()
        else:
            eye_closed_counter = 0  # Reset counter if eyes are detected
            alarm_triggered = False  # Reset alarm trigger when eyes are open
    
        # Head position (basic distraction detection by tracking face position)
        frame_width = frame.shape[1]
        if x < 50 or x + w > frame_width - 50:
            if head_turn_start_time is None:
                head_turn_start_time = time.time()
                print("Head turned detected, starting timer.")
            else:
                elapsed_time = time.time() - head_turn_start_time
                print(f"Head turned for {elapsed_time:.2f} seconds.")
                if elapsed_time >= distraction_threshold:
                    cv2.putText(frame, "Distraction Detected!", (100, 150),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    trigger_alarm()
        else:
            if head_turn_start_time is not None:
                print("Head returned to normal, resetting timer.")
            head_turn_start_time = None
    
    return frame

# Main loop
try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to grab frame")
            break
        
        # Detect eyes and face
        frame = detect_eyes_and_face(frame)
        
        # Display the resulting frame
        cv2.imshow('Driver Alertness Detection', frame)
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting program.")
            break
finally:
    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()




