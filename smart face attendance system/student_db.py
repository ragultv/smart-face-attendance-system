import cv2
import sqlite3


# Initialize video capture and face detection
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Connect to SQLite database (create if not exists)
conn = sqlite3.connect('data/attendance.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS faces
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   face_data BLOB)''')

# Initialize variables
faces_data = []
i = 0
name = input("Enter Your Name: ")

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        crop_img = frame[y:y + h, x:x + w, :]
        resized_img = cv2.resize(crop_img, (50, 50))

        # Convert image to bytes for storage in SQLite
        resized_img_bytes = resized_img.tobytes()

        # Store every 10th detected face
        if len(faces_data) <= 100 and i % 10 == 0:
            faces_data.append((name, resized_img_bytes))

        i += 1
        cv2.putText(frame, f"Faces Collected: {len(faces_data)}", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255),
                    1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 1)

    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)

    # Exit loop if 'q' is pressed or 100 faces are collected
    if k == ord('q') or len(faces_data) == 100:
        break

# Insert faces_data into SQLite database
cursor.executemany('INSERT INTO faces (name, face_data) VALUES (?, ?)', faces_data)
conn.commit()

# Close video capture and SQLite connection
video.release()
cv2.destroyAllWindows()
conn.close()
