import psutil

def get_system_usage():
    return {
        'CPU Usage': f"{psutil.cpu_percent(interval=1)}%",
        'Memory Usage': f"{psutil.virtual_memory().percent}%",
        'Disk Usage': f"{psutil.disk_usage('/').percent}%",
        'Network Sent': f"{psutil.net_io_counters().bytes_sent // (1024*1024)} MB",
        'Network Received': f"{psutil.net_io_counters().bytes_recv // (1024*1024)} MB"
    }
