# Keylogger with Screenshot Capture for Discord

This Python script captures keystrokes and periodically takes screenshots, sending the data to Discord channels using webhooks. It utilizes the `pynput`, `requests`, and `PIL` (Pillow) libraries for keystroke capture, HTTP requests, and screenshot capture, respectively.

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.x installed
- `pynput` library installed (`pip install pynput`)
- `requests` library installed (`pip install requests`)
- `PIL` (Pillow) library installed (`pip install pillow`)
- A Discord account
- Discord webhook URLs for keylogs and screenshots (Replace `'WEBHOOK_URL'` and `'WEBHOOK_URL_SCREENS'` in the code with your actual Discord webhook URLs)

## Usage

1. Clone the repository or copy the code into a Python script file (e.g., `Keylogger.py`).
2. Open the script file in a text editor and replace `'WEBHOOK_URL'` and `'WEBHOOK_URL_SCREENS'` with your actual Discord webhook URLs.
3. Save the changes.
4. Open a terminal or command prompt and navigate to the directory where the script is located.
5. Run the script using the command `python Keylogger.py`.
6. The script will start capturing keystrokes and sending them to the specified Discord channel via the webhook every 10 seconds. Screenshots will be captured and sent every 60 seconds.

## Features

- Dynamic buffer size adjustment based on typing speed.
- Capture and send screenshots at regular intervals.
- Discord webhook integration for easy monitoring.

## Important Note

Be cautious when using keyloggers, as they can potentially violate privacy and legal regulations. Ensure you have proper authorization and adhere to ethical guidelines when using or sharing code like this.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
