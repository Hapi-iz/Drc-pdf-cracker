import argparse
import pikepdf
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import sys
import signal
from rich.console import Console
from rich.progress import track
from rich import print
import time

# Initialize the console for rich output
console = Console()

# Global variables
pdf_path = ""
verbose = False
stop_flag = False  # Used to stop the brute force when password is found

# Function to handle Ctrl+C for stopping the process
def signal_handler(sig, frame):
    print("\n[bold red]Process interrupted. Exiting...[/bold red]")
    os._exit(0)  # Immediately kill the process

# Function to attempt password opening the PDF
def attempt_password(password):
    global stop_flag  # Ensure we modify stop_flag correctly

    if stop_flag:
        return None  # If already found, skip further attempts

    try:
        time.sleep(0.1)  # Simulating delay for realistic output
        
        with pikepdf.open(pdf_path, password=password):
            stop_flag = True  # Stop brute force when password is found
            print(f"\n[bold green]✅ [underline]Password found![/underline] [green]{password}[/green] 🔥")
            return password
    except pikepdf.PasswordError:
        if verbose:
            print(f"[yellow]Password incorrect: {password}[/yellow]")
        return None
    except Exception as e:
        print(f"[bold red]Error:[/bold red] {str(e)}")
        return None

# Function to crack the PDF with a wordlist
def crack_pdf(pdf, wordlist, max_workers=4):
    global pdf_path, stop_flag
    pdf_path = pdf
    stop_flag = False  # Reset stop flag

    # Read the wordlist
    with open(wordlist, 'r') as file:
        passwords = (line.strip() for line in file)

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(attempt_password, pw): pw for pw in passwords}

            for future in track(futures, description="🔄 [cyan]Brute-forcing...[/cyan] "):
                result = future.result()
                if result:
                    stop_flag = True  # Stop further attempts
                    return result  # Exit function once found
                if stop_flag:
                    break

    print("\n[bold red]No password found. Please try a different wordlist.[/bold red]")
    return None

# Main function to parse arguments and execute the process
def main():
    global verbose

    # Argument parsing
    parser = argparse.ArgumentParser(description="DRC PDF Brute Force Cracker")
    parser.add_argument("-p", "--pdf", help="Path to the PDF file", required=True)
    parser.add_argument("-w", "--wordlist", help="Path to the wordlist", required=True)
    parser.add_argument("-v", "--verbose", help="Enable verbose output", action="store_true")
    parser.add_argument("-mp", "--max-workers", help="Maximum number of workers", type=int, default=4)

    args = parser.parse_args()
    verbose = args.verbose

    # Validate file paths
    if not os.path.exists(args.pdf):
        print(f"[bold red]Error: PDF file {args.pdf} does not exist.[/bold red]")
        return
    if not os.path.exists(args.wordlist):
        print(f"[bold red]Error: Wordlist file {args.wordlist} does not exist.[/bold red]")
        return

    # Start cracking
    print(f"\n🔍 Cracking PDF: [yellow]{args.pdf}[/yellow]")
    crack_pdf(args.pdf, args.wordlist, max_workers=args.max_workers)

# Entry point
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C
    main()
