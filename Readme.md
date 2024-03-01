# Mood Detection System using Face Recognition

This Python program detects the mood of a user based on their facial expression using face recognition techniques.

## Setup and Dependencies

1. Make sure you have Python installed on your system.
2. Install the required libraries by running the following command:
    ```
    pip install numpy opencv-python face-recognition
    ```

## Usage

1. Run the `mood_detection.py` script.
2. The program will access your computer's camera to detect your facial expression.
3. Based on the detected mood, the system will either unlock or lock itself.
4. Press the 'q' key to exit the program.

## Methodology

- The program uses the `face_recognition` library to locate and encode faces in the video feed.
- It simulates mood detection by assuming a smile or cry expression based on a simple threshold.
- The detected mood is then used to determine whether to unlock or lock the system.

## Enhancements

- You can enhance the mood detection by integrating a more sophisticated machine learning model for better accuracy.
- Explore using deep learning models for facial emotion recognition to improve the system's performance.

## Author

This program was developed by Aditya Kumar. You can reach out to me at ceo@sameerswain.com for any questions or feedback.

Happy mood detection! 😊🤖