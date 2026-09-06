
import os
import platform
import time

def execute_command(action, delay_seconds):
    current_os = platform.system().lower()

    print(f"\n[ZINGATIA] Itachakata ndani ya sekunde {delay_seconds} ")
    for remaining in range(delay_seconds, 0, -1):
        print(f"Inachakata ndani ya sekunde {remaining}... Bonyeza Ctrl+C kusitisha! ", end="\r", flush=True)
        time.sleep(1)
    print("\nInachakata amri...\n")

    if current_os == "windows":   # Windows
        if action == "restart":
            os.system("shutdown /r /t 0 /f")
        else: 
            os.system("shutdown /s /t 0 /f")
    elif current_os in ["linux", "darwin"]:  # Linux & macOS
        if action == "restart":
            os.system("shutdown -r now")
        else:
            os.system("shutdown -h now")
    else:
        print("\nProgramu kuu haijajulikani. Amri imesitishwa.\n")

def get_delay():
    while True:
        unit = input("Chagua 'd' dakika au 's' sekunde ").strip().lower()
        if unit in ("d", "s"):
            break
        print("\nChaguo lako sio sawa. Tafadhali chagua 'd' au 's'.")

    while True:
        try:
            value = float(input("\nTafadhali ingiza namba: ").strip())
            if value <= 0:
                print("\nTafadhali ingiza namba chanya.")
                continue
            break
        except ValueError:
            print("\nTafadhali ingiza namba.")

    if unit == "d":
        return int(value * 60)  
    else:
        return int(value)

def check_secret_word():
    print("\n=== Karibu kwenye Python System Control === \n")
    print("Andika amri (au neno) moja hapo chini kuamuru Kompyuta yako: ")
    print("  1: anzisha ")
    print("  2: zima ")

    user_input = input("\nAndika amri hapa: ").strip().lower()

    if user_input == "anzisha" or 1:
        action = "restart"
    elif user_input == "zima" or 2:
        action = "shutdown"
    else:
        print("\nNeno uliloingiza ni batili. Hakuna amri iliyotekelezwa! .")
        return

    print(f"\n[ZINGATIA] Amri imekubaliwa! , Inagundua aina ya programu kuu...")
    time.sleep(3)
    current_os = platform.system().lower()
    if current_os not in ["windows", "linux", "darwin"]:
        print("\nProgramu kuu haijajulikani. Amri imesitishwa.")
        return

    print("\n!!! TAHADHARI: Kompyuta yako ita {} muda si mrefu !!!\n".format(action))
    delay = get_delay()
    execute_command(action, delay)

if __name__ == "__main__":
    try:
        check_secret_word()
    except KeyboardInterrupt:
        print("\n\n[SALAMA] Amri imesitishwa na mtumiaji. Uko salama kuendelea na kazi!")
