# PRODIGY_CS_04

Create a basic keylogger program that records and logs keystrokes. Focus on logging the keys pressed and saving them to a file. Note: Ethical considerations and permissions are crucial for projects involving keyloggers.

Please take a moment to review the included [keylogger.py] file.

This Python code is designed to create a simple keylogger, a program that records keystrokes made on a computer's keyboard. When the program is run, it listens for any keys pressed by the user. Each time a key is pressed, the program records the corresponding character into a text file named "keylog.txt". The code uses the pynput library to monitor keyboard events and defines a function called key_pressed to handle key press events. This function extracts the character pressed, if available, and writes it to the text file. The main part of the program sets up a listener to continuously monitor keyboard events, ensuring that all keystrokes are captured until the program is terminated. While this program can be a useful tool for learning and understanding keyboard input handling in Python, it's important to use it responsibly and ethically, as keyloggers can potentially invade privacy if misused.
