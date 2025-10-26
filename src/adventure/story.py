from adventure.utils import read_events_from_file
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import random

# Initialize Rich console
console = Console()

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[italic red]You stand still, unsure what to do. The forest swallows you...[/italic red]"

def left_path(event):
    return f"[green]You walk left.[/green] [bold yellow]{event}[/bold yellow]"

def right_path(event):
    return f"[blue]You walk right.[/blue] [bold magenta]{event}[/bold magenta]"

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    # Opening scene with a panel box for effect
    intro_text = Text("You wake up in a dark forest.\nYou can go left or right.")
    intro_text.stylize("bold white")
    console.print(Panel(intro_text, border_style="bright_green"))

    while True:
        # Styled input prompt
        choice = console.input("[bold yellow]Which direction do you choose?[/bold yellow] (left/right/exit): ")
        choice = choice.strip().lower()

        if choice == 'exit':
            console.print("[bold red]You decide to leave the forest...[/bold red]")
            console.print("[italic green]Goodbye, traveler. The adventure awaits another day![/italic green]")
            break

        
        result = step(choice, events)
        console.print(Panel(result, border_style="cyan"))
