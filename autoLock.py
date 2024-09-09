import os
import time
import threading
from pynput import mouse, keyboard

print("Auto Lock Application Running...");
def alert_and_lock():
    # Display alert message
    print("System will lock in 5 seconds due to inactivity.")
    for i in range(5, 0, -1):
        print(f"Locking in {i}...")
        time.sleep(1)
    
    # Lock the system
    if os.name == 'nt':  # Windows
        os.system('rundll32.exe user32.dll,LockWorkStation')
    elif os.name == 'posix':  # macOS
        os.system(r'/System/Library/CoreServices/Menu\ Extras/User.menu/Contents/Resources/CGSession -suspend')
    else:
        print("Auto lock is not supported on this OS.")

def reset_inactivity_timer():
    global last_activity_time
    last_activity_time = time.time()

def check_inactivity():
    global last_activity_time  # Declare this variable as global
    while True:
        current_time = time.time()
        if current_time - last_activity_time > 10:  # 10 seconds inactivity
            alert_and_lock()
            last_activity_time = current_time  # Reset timer after locking
        time.sleep(1)

if __name__ == "__main__":
    last_activity_time = time.time()
    
    # Start the inactivity check in a separate thread
    inactivity_thread = threading.Thread(target=check_inactivity)
    inactivity_thread.daemon = True
    inactivity_thread.start()
    
    # Start listening to mouse and keyboard events
    mouse_listener = mouse.Listener(on_move=lambda x, y: reset_inactivity_timer())
    keyboard_listener = keyboard.Listener(on_press=lambda key: reset_inactivity_timer())

    mouse_listener.start()
    keyboard_listener.start()
    
    try:
        # Keep the main thread running while listeners are active
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program terminated.")
