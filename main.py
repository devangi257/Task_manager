from process_manager import list_processes
from system_monitor import get_system_usage
from suspicious import detect_suspicious_processes
from network_status import list_connections
from uptime import get_uptime
from user_info import get_users
from disk_info import get_disks
from memory_top import top_memory_processes
from power_info import battery_status
from rich.console import Console
from rich.table import Table

console = Console()

def show_menu():
    console.print("\n[bold cyan]Cybersecurity Task Manager (Safe Version)[/bold cyan]")
    console.print("[1] Show Running Processes")
    console.print("[2] Show System Usage")
    console.print("[3] Scan for Suspicious Processes")
    console.print("[4] Show Network Connections")
    console.print("[5] Show System Uptime")
    console.print("[6] Show Logged-in Users")
    console.print("[7] Show Disk Usage")
    console.print("[8] Show Top Memory Processes")
    console.print("[9] Show Battery Status")
    console.print("[10] Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            table = Table(title="Running Processes")
            table.add_column("PID", style="cyan")
            table.add_column("Name", style="magenta")
            table.add_column("User", style="green")
            table.add_column("CPU %", justify="right")
            table.add_column("Memory %", justify="right")
            for p in list_processes():
                table.add_row(str(p['pid']), p['name'], str(p['username']), str(p['cpu_percent']), f"{p['memory_percent']:.2f}")
            console.print(table)

        elif choice == '2':
            usage = get_system_usage()
            for k, v in usage.items():
                console.print(f"[bold yellow]{k}:[/] {v}")

        elif choice == '3':
            suspicious = detect_suspicious_processes()
            if suspicious:
                console.print("[red]Suspicious Processes Detected:[/red]")
                for s in suspicious:
                    console.print(f"[red]- PID: {s['pid']}, Name: {s['name']}[/red]")
            else:
                console.print("[green]No suspicious processes found.[/green]")

        elif choice == '4':
            connections = list_connections()
            for conn in connections:
                console.print(f"PID: {conn['pid']} | {conn['local']} --> {conn['remote']} | Status: {conn['status']}")

        elif choice == '5':
            console.print(get_uptime())

        elif choice == '6':
            users = get_users()
            for u in users:
                console.print(f"[bold cyan]{u}[/bold cyan]")

        elif choice == '7':
            disks = get_disks()
            for d in disks:
                console.print(f"Device: {d['device']}, Mount: {d['mount']}, Usage: {d['usage']}")

        elif choice == '8':
            top_mem = top_memory_processes()
            for p in top_mem:
                console.print(f"PID: {p['pid']}, Name: {p['name']}, Memory: {p['memory_percent']:.2f}%")

        elif choice == '9':
            console.print(battery_status())

        elif choice == '10':
            console.print("[bold green]Exiting Task Manager...[/bold green]")
            break

        else:
            console.print("[red]Invalid option.[/red]")

if __name__ == '__main__':
    main()
