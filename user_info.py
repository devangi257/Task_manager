import psutil

def get_users():
    return [f"{u.name} on {u.terminal} from {u.host}" for u in psutil.users()]