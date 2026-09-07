# Python System Control Script

A lightweight Python script that allows you to **restart** or **shut down** your computer by typing a secret word, with a **customizable delay** before the action is executed.

---

## Features

- 🔐 **Command activation** – type `restart` or `1' to restart or `shutdown` or `2` to shut down.
- ⏱️ **Configurable delay** – choose between **minutes** (`d`) or **seconds** (`s`) and enter any positive number.
- 🖥️ **Cross‑platform** – works on **Windows**, **Linux**, and **macOS**.
- ⚡ **Force‑close applications** on Windows (uses `/f` flag to suppress “shutdown anyway” dialogs).
- 🛑 **Cancellable** – press `Ctrl+C` during the countdown to abort safely.

---

## Prerequisites

- Python 3.x installed on your system.
- **Administrative/root privileges** to execute system restart/shutdown commands.

---

## Installation

Simply save the script as, for example, `timeout.py` (or any name you prefer).  
No additional dependencies are required – it uses only the Python standard library (`os`, `platform`, `time`).

---

## Usage

1. Open a terminal (Command Prompt / PowerShell on Windows, or a shell on Linux/macOS) **with administrator privileges**:
   - **Windows**: right‑click the terminal icon and select **“Run as administrator”**.
   - **Linux/macOS**: use `sudo` when running the script (e.g., `sudo python3 timeout.py`).

2. Run the script:

   ```bash
   python timeout.py
