import random
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def play_guessing_game():
    console.print("\n[bold magenta]🎮 Welcome to the Number Guessing Game![/bold magenta]")
    console.print("[cyan]I am thinking of a number between 1 and 50. Can you guess it?[/cyan]\n")
    
    number = random.randint(1, 50)
    attempts = 0
    guess = 0
    
    while guess != number:
        guess = int(Prompt.ask("Enter your guess"))
        attempts += 1
        if guess < number:
            console.print("[yellow]Too low! Try again.[/yellow]")
        elif guess > number:
            console.print("[yellow]Too high! Try again.[/yellow]")
        else:
            console.print(f"[bold green]🎉 Correct! The number was {number}. You guessed it in {attempts} attempts.[/bold green]\n")
