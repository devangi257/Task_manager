import psutil

def top_memory_processes(limit=5):
    procs = []
    for p in psutil.process_iter(['pid', 'name', 'memory_percent']):
        try:
            procs.append(p.info)
        except:
            continue
    return sorted(procs, key=lambda x: x['memory_percent'], reverse=True)[:limit]