# Smart Face Attendance System

The **Smart Face Attendance System** is a facial recognition-based solution for efficiently managing attendance records. This application uses machine learning algorithms to detect and recognize faces, ensuring accurate and automated attendance tracking.

---

## Features

- **Face Detection**: Uses pre-trained Haar Cascade classifiers for facial detection.
- **Face Recognition**: Implements FaceNet's `InceptionResnetV1` model for high-accuracy face recognition using embeddings.
- **Student Management**: Manages student data through a dedicated database.
- **Attendance Tracking**: Records attendance, including late entries, in CSV files.
- **Database Support**: Attendance and student data are stored in an SQLite database for reliability and easy access.
- **Text-to-Speech Feedback**: Provides auditory feedback using Windows SAPI.

---

## Directory Structure

```
smart face attendance system/
├── haarcascade_frontalface_default.xml   # Pre-trained face detection model
├── main.py                              # Main script for running the application
├── student_db.py                        # Script for managing student database
├── Attendance/
│   ├── Attendance_.csv                  # Records of attendance
│   └── late_attendance_record.csv       # Records of late entries
├── data/
│   └── attendance.db                    # SQLite database for attendance data
```

---

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone <https://github.com/ragultv/smart-face-attendance-system.git>
   cd smart-face-attendance-system
   ```

2. **Install Required Libraries**:
   Make sure you have Python 3.x installed. Install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Execute the main script to start the system:
   ```bash
   python main.py
   ```

---

## How It Works

1. **Face Detection**: The `haarcascade_frontalface_default.xml` file is used for detecting faces in real time.
2. **Face Recognition**: Face embeddings are generated using the FaceNet model (`InceptionResnetV1`), and matches are identified based on cosine similarity.
3. **Database Management**: The `attendance.db` file stores all attendance records securely.
4. **Attendance Records**: CSV files in the `Attendance/` folder maintain detailed logs of attendance and late entries.
5. **Text-to-Speech**: Provides auditory feedback for enhanced user experience.

---

## Dependencies

- OpenCV
- SQLite3
- Pandas
- NumPy
- PyTorch
- Facenet-PyTorch
- pywin32

---

## Contribution

Feel free to fork this repository and submit pull requests to improve the system.

---

