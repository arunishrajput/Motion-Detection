# Motion Detection with OpenCV and Telegram Notifications

This project detects motion using OpenCV in Python and sends notifications with photos to a Telegram chat.

## Features

- Motion detection using `OpenCV` and background subtraction.
- Integration with `Telegram Bot API` for notifications.
- Adjustable parameters for motion sensitivity and cooldown periods.

## Requirements

- Python 3.6 or higher
- Requests library (for sending HTTP requests)
- Telegram Bot API credentials (Bot Token and Chat ID)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/arunishrajput/motion-detection.git
   cd motion-detection
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   Or install the libraries manually:

   ```bash
   pip install opencv-python requests
   ```

3. **Setup Telegram Bot:**

   - Create a Telegram bot using [BotFather](https://t.me/BotFather) and note down the `Bot Token`.
   - Obtain your `Telegram Chat ID` using [userinfobot](https://t.me/userinfobot).

4. **Configuration:**

- Replace placeholders in the script (`TELEGRAM_CHAT_ID` and `TELEGRAM_BOT_TOKEN`) with your actual Telegram credentials.

## Usage

1. **Run the Script:**

   ```bash
   python main.py
   ```

2. **Motion Detection:**

   - Adjust `camera` variable (0 for default camera) or specify a video file path.

   - Customize `initial_delay_seconds`, `motion_cooldown_seconds`, and `threshold` as per your requirements.

3. **Exit:**

   - Press Esc key to exit the application.

## Functionality

- **Captures frames from the camera or video file.**
- **Defines a smaller square area in the frame for motion detection.**
- **Sends a Telegram notification with a photo when motion is detected.**
- **Uses background subtraction and contour detection for motion identification.**

## Troubleshooting

- Ensure Python environment and dependencies are correctly installed.
- Verify Telegram credentials and network connectivity for sending notifications.

## Contribution

- Feel free to fork this repository, create a feature branch, and submit a pull request. Contributions, issues, and feature requests are welcome!

## Acknowledgments

- [OpenCV](https://opencv.org/)
- [Telegram API Documentation](https://core.telegram.org/bots/api)
