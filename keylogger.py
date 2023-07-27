import time
from pynput import keyboard, mouse

def on_key_press(key):
    try:
        global last_time
        current_time = time.time()
        delay = current_time - last_time if last_time else 0
        last_time = current_time

        key_str = str(key)
        key_name = key_str.replace("'", "")

        with open("keylog.txt", "a") as f:
            f.write(f"{key_name} {int(delay * 1000)} millis\n")

    except Exception as e:
        print(f"Error: {e}")

def on_click(x, y, button, pressed):
    try:
        global last_time
        if not pressed:
            return

        current_time = time.time()
        delay = current_time - last_time if last_time else 0
        last_time = current_time

        button_name = "Left Click" if button == mouse.Button.left else "Right Click"

        with open("keylog.txt", "a") as f:
            f.write(f"{button_name.replace(' ','_')} {int(delay * 1000)} millis\n")

    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

if __name__ == "__main__":
    last_time = None
    quit_keylogger = False

    print("Recording key presses and mouse clicks... Type 'quit' to stop.")
    with keyboard.Listener(on_press=on_key_press, on_release=on_release) as key_listener:
        with mouse.Listener(on_click=on_click) as mouse_listener:
            while not quit_keylogger:
                user_input = input()
                if user_input.lower() == "quit":
                    quit_keylogger = True

            print("Keylogger stopped.")
            key_listener.stop()
            mouse_listener.stop()
