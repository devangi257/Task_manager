import psutil
import datetime

def get_uptime():
    boot = datetime.datetime.fromtimestamp(psutil.boot_time())
    now = datetime.datetime.now()
    uptime = now - boot
    return f"Boot Time: {boot.strftime('%Y-%m-%d %H:%M:%S')}\nUptime: {str(uptime).split('.')[0]}"