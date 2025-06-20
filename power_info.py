import psutil

def battery_status():
    battery = psutil.sensors_battery()
    if battery:
        return f"Battery: {battery.percent}% | {'Charging' if battery.power_plugged else 'Discharging'}"
    return "Battery status not available"
