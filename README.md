# 🆘 Emergency Voice Command Alert System

This is a **Python-based Emergency Alert System** that continuously listens for specific voice commands like "help"` or a secret keyword. When triggered, the system captures an image using the connected camera, fetches the user's real-time GPS location, and sends an emergency alert via SMS or email to predefined contacts.

---

## ⚙️ How It Works

1. **Voice Command Detection**
   - Uses SpeechRecognition or similar libraries to detect specific keywords (like "help"`).
   - Can run in the background and trigger alerts automatically when the command is detected.

2. **Camera Capture**
   - Captures an image using the default webcam or external camera (via OpenCV).
   - The image is saved locally and optionally sent as an attachment.

3. **GPS Location Fetching**
   - Gets real-time latitude and longitude using geocoder, geopy, or a GPS module (for Raspberry Pi or similar).
   - Converts coordinates into a Google Maps link.

4. **Emergency Alert**
   - Sends an SMS using services like Twilio`, Fast2SMS, or built-in GSM module (for hardware-based setups).
   - Optionally sends an **email alert** with the location and captured image via smtplib`.

---

## 🧰 Technologies Used

- Python 3.x**
- SpeechRecognition`
- PyAudio`
- OpenCV`
- smtplib` (for email)
- geocoder` / `geopy`




