import psutil

def get_disks():
    disks = []
    for part in psutil.disk_partitions():
        usage = psutil.disk_usage(part.mountpoint)
        disks.append({
            'device': part.device,
            'mount': part.mountpoint,
            'usage': f"{usage.percent}%"
        })
    return disks