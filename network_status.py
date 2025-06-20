import psutil

def list_connections(limit=10):
    conns = []
    for c in psutil.net_connections(kind='inet'):
        if c.laddr and c.raddr:
            conns.append({
                'pid': c.pid,
                'status': c.status,
                'local': f"{c.laddr.ip}:{c.laddr.port}",
                'remote': f"{c.raddr.ip}:{c.raddr.port}"
            })
    return conns[:limit]