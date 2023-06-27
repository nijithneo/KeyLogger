# Keylogger Discord Webhook

This script captures keystrokes and sends them to a Discord channel using a webhook. It utilizes the `keyboard` and `requests` libraries to capture keystrokes and send HTTP requests to the Discord webhook URL.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed
- `keyboard` library installed (`pip install keyboard`)
- `requests` library installed (`pip install requests`)
- A Discord account
- A Discord webhook URL (Replace `'WEBHOOK_URL'` in the code with your actual Discord webhook URL)

## Usage

1. Clone the repository or copy the code into a Python script file (e.g., `keylogger.py`).
2. Open the script file in a text editor and replace `'WEBHOOK_URL'` with your actual Discord webhook URL.
3. Save the changes.
4. Open a terminal or command prompt and navigate to the directory where the script is located.
5. Run the script using the command `python keylogger.py`.
6. The script will start capturing keystrokes and sending them to the specified Discord channel via the webhook every 10 seconds.
7. To stop the script, press `Ctrl + C` in the terminal or command prompt.

## Important Note

Be cautious when using keyloggers, as they can potentially violate privacy and legal regulations. Make sure you have proper authorization and adhere to ethical guidelines when using or sharing code like this.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
