from app.intro import show_introduction
from app.game import play_guessing_game
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def main():
    console.print("\n[bold underline cyan]Welcome to My Interactive Dashboard[/bold underline cyan]\n")
    
    # Show introduction
    show_introduction()
    
    # Ask if user wants to play a game
    play = Prompt.ask("\nDo you want to play a mini game?", choices=["yes", "no"], default="yes")
    
    if play.lower() == "yes":
        play_guessing_game()
    
    console.print("\n[bold magenta]Thank you for visiting my dashboard![/bold magenta]")

if __name__ == "__main__":
    main()
