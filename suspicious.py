import psutil

BLACKLISTED = ['keylogger', 'netcat', 'wireshark', 'nmap', 'meterpreter']

def detect_suspicious_processes():
    suspicious = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            name = proc.info['name'].lower()
            if any(bad in name for bad in BLACKLISTED):
                suspicious.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return suspicious