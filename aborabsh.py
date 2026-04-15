import sys
import whois
import nmap
import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# واجهة الأداة الاحترافية
def show_banner():
    banner = """
    [bold cyan]
    _    ____   ___  ____        _    ____  ____  _   _ 
   / \  | __ ) / _ \|  _ \      / \  | __ )/ ___|| | | |
  / _ \ |  _ \| | | | |_) |    / _ \ |  _ \\___ \| |_| |
 / ___ \| |_) | |_| |  _ <    / ___ \| |_) |___) |  _  |
/_/   \_\____/ \___/|_| \_\  /_/   \_\____/|____/|_| |_|
    [/bold cyan]
    [bold white]ABORABSHTOOL v1.0 | Professional OSINT & Scan[/bold white]
    [bold green]Developed by: ABORABSH[/bold green]
    [bold magenta]Instagram: @mindsdontshout[/bold magenta]
    """
    console.print(Panel(banner, title="[bold red]SYSTEM READY[/bold red]", border_style="blue"))

# وظيفة البحث عن الحسابات
def check_social(username):
    platforms = {
        "Instagram": f"https://www.instagram.com/{username}",
        "Twitter/X": f"https://twitter.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}"
    }
    
    table = Table(title=f"\n[bold yellow]Searching for: {username}[/bold yellow]", style="magenta")
    table.add_column("Platform", style="cyan")
    table.add_column("Status", style="bold green")
    
    console.print("[bold white][*] Checking Social Media Platforms...[/bold white]")
    
    for name, url in platforms.items():
        try:
            # إضافة headers عشان المنصات ما تحظر الطلب
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                table.add_row(name, "FOUND ✓")
            else:
                table.add_row(name, "[red]NOT FOUND[/red]")
        except Exception:
            table.add_row(name, "[red]ERROR[/red]")
    
    console.print(table)

# وظيفة فحص المواقع والـ Nmap
def check_website(domain):
    try:
        console.print(f"\n[bold yellow][*] Fetching Domain Info for: {domain}[/bold yellow]")
        w = whois.whois(domain)
        console.print(f"[green][+] Registrar:[/green] {w.registrar}")
        console.print(f"[green][+] Creation Date:[/green] {w.creation_date}")
    except Exception:
        console.print("[red][!] WHOIS Lookup Failed.[/red]")

    console.print(f"\n[bold yellow][*] Starting Nmap Port Scan (Please wait...)[/bold yellow]")
    nm = nmap.PortScanner()
    try:
        # فحص أهم المنافذ (80, 443, 21, 22, 3306)
        nm.scan(domain, '21,22,80,443,3306', '-sV')
        
        table = Table(style="blue")
        table.add_column("Port", style="cyan")
        table.add_column("State", style="bold green")
        table.add_column("Service", style="white")

        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                ports = nm[host][proto].keys()
                for port in ports:
                    state = nm[host][proto][port]['state']
                    service = nm[host][proto][port]['name']
                    table.add_row(str(port), state.upper(), service)
        
        console.print(table)
    except Exception as e:
        console.print(f"[red][!] Nmap Error: Make sure Nmap is installed on your Windows.[/red]")

def main():
    show_banner()
    if len(sys.argv) < 3:
        console.print("\n[bold yellow]Usage Commands:[/bold yellow]")
        console.print("[cyan]1. Search User:[/cyan]  python module2.py --user [name]")
        console.print("[cyan]2. Scan Site:[/cyan]  python module2.py --site [domain]")
        return

    mode = sys.argv[1]
    target = sys.argv[2]

    if mode == "--user":
        check_social(target)
    elif mode == "--site":
        check_website(target)

if __name__ == "__main__":
    main()
