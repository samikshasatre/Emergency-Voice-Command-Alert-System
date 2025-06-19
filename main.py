from utils.email_alert import send_email
from utils.gps_location import get_location
import cv2
import speech_recognition as sr

def capture_image():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    img_path = "alert_snapshot.jpg"
    if ret:
        cv2.imwrite(img_path, frame)
    cam.release()
    return img_path

def listen_for_trigger():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening for trigger words...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio).lower()
            print(f"Detected: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return ""

if __name__ == "__main__":
    TRIGGER_WORDS = ["help", "emergency", "code red", "need help"]
    while True:
        command = listen_for_trigger()
        if any(word in command for word in TRIGGER_WORDS):
            print("🚨 Emergency Trigger Detected!")
            image_path = capture_image()
            location = get_location()
            send_email(image_path, location)
            break
