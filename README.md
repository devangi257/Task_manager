# 🛡️ Task Manager using Python

Welcome to the **Task Manager**, a safe Python-based system info dashboard built by **Devangi Khatri**.

> 📌 This project gives real-time system monitoring, suspicious process detection, uptime tracking, and more — all within the terminal using the `rich` library.

---

## 🎯 Features

- ✅ Real-time Process Monitor (with CPU & Memory %)
- ✅ System Usage Stats (CPU, RAM, Disk)
- ✅ Suspicious Process Detection (based on keywords)
- ✅ Logged-in User Details
- ✅ Network Connection Tracker
- ✅ Uptime Monitoring
- ✅ Battery Status
- ✅ Stylish CLI using `rich`

---

## 🗂️ File Structure

```bash
Task_manager-master/
├── main.py                  # Dashboard & Menu Interface
├── process_manager.py       # Shows running processes
├── system_monitor.py        # CPU, RAM, Disk usage
├── suspicious.py            # Suspicious process scanner
├── network_status.py        # Active network connections
├── uptime.py                # System uptime
├── user_info.py             # Logged in users
├── disk_info.py             # Disk partitions & usage
├── memory_top.py            # Top memory consuming processes
├── power_info.py            # Battery level and status
├── requirements.txt         # Required packages
├── __pycache__/             # Python cache (excluded via .gitignore)

# 1. Clone this repo
git clone https://github.com/devangi257/Task_manager.git
cd Task_manager-master

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the tool
python main.py






