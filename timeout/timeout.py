import os
import platform
import time

def execute_command(action, delay_seconds):
    current_os = platform.system().lower()

    print(f"\n[ALERT] {action.capitalize()} will be performed in {delay_seconds} seconds!")
    for remaining in range(delay_seconds, 0, -1):
        print(f"Executing in {remaining} second(s)... Press Ctrl+C to abort!", end="\r", flush=True)
        time.sleep(1)
    print("\nTime's up! Executing command...")

    if current_os == "windows":
        # /f forces running applications to close without warning
        if action == "restart":
            os.system("shutdown /r /t 0 /f")
        else:  # shutdown
            os.system("shutdown /s /t 0 /f")
    elif current_os in ["linux", "darwin"]:  # Linux & macOS
        if action == "restart":
            os.system("shutdown -r now")
        else:
            os.system("shutdown -h now")
    else:
        print("Operating system not recognized. Action aborted.")

def get_delay():
    while True:
        unit = input("Choose time unit: (m)inutes or (s)econds? ").strip().lower()
        if unit in ("m", "s"):
            break
        print("Invalid input. Please enter 'm' or 's'.")

    while True:
        try:
            value = float(input("Enter the number: ").strip())
            if value <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid number. Please enter a numeric value.")

    if unit == "m":
        return int(value * 60)  # convert minutes to seconds
    else:
        return int(value)

def check_secret_word():
    print("\n=== Welcome to the Python System Control ===")
    print("\nType 1 to restart or 2 to shutdown: ")
    print("\t 1: restart  ")
    print("\t 2: shutdown \n")

    user_input = input("Enter your option: ").strip().lower()

    if user_input == "restart" or 1:
        action = "restart"
    elif user_input == "shutdown" or 2:
        action = "shutdown"
    else:
        print("Incorrect word. Access denied. No action taken.")
        return

    print(f"\n[PROCESSING] Identifying operating system...")
    time.sleep(2)
    current_os = platform.system().lower()
    if current_os not in ["windows", "linux", "darwin"]:
        print("Operating system not recognized. Action aborted.")
        return

    print("\n!!! WARNING: System will be {} shortly !!!".format(action))
    delay = get_delay()
    execute_command(action, delay)

if __name__ == "__main__":
    try:
        check_secret_word()
    except KeyboardInterrupt:
        print("\n\n[SAFE] Action cancelled by user. Safe to continue working!")
