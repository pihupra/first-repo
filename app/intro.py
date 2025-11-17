from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def show_introduction():
    # Display introduction in a styled panel
    console.print(Panel("[bold cyan]Hello! I'm Pihu Prakash[/bold cyan]\n"
                        "[green]B.Tech CSE | Product Design & Technology[/green]\n"
                        "[yellow]Published Researcher, SIH Finalist, Patent Holder[/yellow]\n"
                        "[magenta]Python & IoT Enthusiast[/magenta]",
                        title="👋 About Me", expand=False))

    # Display skills in a table
    table = Table(title="Skills & Interests")
    table.add_column("Category", style="bold cyan")
    table.add_column("Details", style="bold green")
    
    table.add_row("Programming", "Python, JavaScript")
    table.add_row("Product Design", "IoT, CAD, Prototyping")
    table.add_row("Other", "Hackathons, Research, GitHub")
    
    console.print(table)
