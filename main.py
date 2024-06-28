import cv2
import requests
import time

TELEGRAM_CHAT_ID = 'YOUR_TELEGRAM_CHAT_ID' # Obtain your "Telegram Chat ID" using @userinfobot.
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN' # Create a Telegram bot using @BotFather and note down the "Bot Token"
message = 'Motion Detected!!'  # Message to be sent on Telegram
camera = 1  # Use 0 for the default camera, or specify a video fdile path
initial_delay_seconds = 1  # Set the initial delay in seconds
motion_cooldown_seconds = 1  # Set the cooldown period in seconds

# Function to send a message with a photo to the Telegram bot
def send_telegram_message_with_photo(message, photo):
    send_photo_url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto'
    files = {'photo': ('motion.jpg', photo, 'image/jpeg')}
    data = {'chat_id': TELEGRAM_CHAT_ID, 'caption': message}
    response = requests.post(send_photo_url, files=files, data=data)
    return response.json()

# Wait for the initial delay
print(f"Waiting for {initial_delay_seconds} seconds before starting motion detection...")
time.sleep(initial_delay_seconds)

# Create a VideoCapture object to capture video from a webcam or video file
cap = cv2.VideoCapture(camera)

# Get the dimensions of the captured frame
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the size of the smaller square area
square_size = 200  # You can adjust the size as needed

# Calculate the coordinates for the smaller square area at the center
x = int(frame_width / 2 - square_size / 2)
y = int(frame_height / 2 - square_size / 2)
small_square_area = (x, y, square_size, square_size)

# Initialize the background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

# Set the initial window size
cv2.namedWindow('Motion Detection', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Motion Detection', 800, 600)  # Adjust the size as needed

motion_last_detected_time = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Extract the smaller square area from the frame
    x, y, w, h = small_square_area
    roi = frame[y:y+h, x:x+w]

    # Draw a green outline around the smaller square area
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle

    # Apply background subtraction to the smaller square area
    fgmask = fgbg.apply(roi)

    # Threshold the foreground mask to identify motion
    threshold = 50  # Adjust the threshold value as needed
    _, thresh = cv2.threshold(fgmask, threshold, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = False

    for contour in contours:
        if cv2.contourArea(contour) > 100:  # Adjust the area threshold as needed
            motion_detected = True

            # Draw a green rectangle around the detected motion area in the entire frame
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle

            # Capture the entire frame with the green rectangle
            motion_photo = frame.copy()

            break

    if motion_detected and (time.time() - motion_last_detected_time > motion_cooldown_seconds):
        print("Motion detected in the smaller square area!")
        send_telegram_message_with_photo(message, cv2.imencode('.jpg', motion_photo)[1].tobytes())  # Send Telegram notification with motion photo
        motion_last_detected_time = time.time()  # Update last detected time

    cv2.imshow('Motion Detection', frame)

    if cv2.waitKey(30) & 0xFF == 27:  # Press 'Esc' key to exit
        break

cap.release()
cv2.destroyAllWindows()
