from pynput import keyboard

def on_release(key):
	print(key)

listener = keyboard.Listener(on_release=on_release)
listener.start()

while True:
	i = 0