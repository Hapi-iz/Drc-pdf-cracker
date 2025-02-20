import subprocess
import sys
import os
import argparse
import pikepdf
from concurrent.futures import ThreadPoolExecutor, as_completed
import signal
from rich.console import Console
from rich.progress import Progress
from rich import print
import time
import pyfiglet


console = Console()

# Global variables
pdf_path = ""
stop_flag = False  
found_password = None  

def signal_handler(sig, frame):
    print("\n[bold red]Process interrupted. Exiting...[/bold red]")
    os._exit(0)

def attempt_password(password):
    global stop_flag, found_password

    if stop_flag:
        return None 

    try:
        with pikepdf.open(pdf_path, password=password):
            stop_flag = True
            found_password = password
            return password
    except pikepdf.PasswordError:
        return None
    except Exception as e:
        print(f"\n[bold red]Error:[/bold red] {str(e)}")
        return None

def crack_pdf(pdf, wordlist, max_workers=4):
    global pdf_path, stop_flag
    pdf_path = pdf
    stop_flag = False  

    def password_generator(file_path):
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                yield line.strip()

    passwords = password_generator(wordlist)
    total_attempts = sum(1 for _ in open(wordlist, encoding="latin-1", errors="ignore"))

    if total_attempts > 1000000:  
        print(f"[bold yellow]Warning: The wordlist is large ({total_attempts} passwords). This process may take some time.[/bold yellow]")
        print("[bold yellow]Progress animation may not update as expected.[/bold yellow]")

    print(f"Total attempts: {total_attempts}")  
    print(f"[bold cyan]Number of threads being used: {max_workers}[/bold cyan]")

    with Progress() as progress:
        task = progress.add_task("[cyan]🔄 Brute-forcing...[/cyan]", total=total_attempts)

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(attempt_password, pw): pw for pw in passwords}

            for future in as_completed(futures):
                progress.update(task, advance=1)
                result = future.result()
                
                if result:
                    stop_flag = True
                    print(f"\n[bold green]✅ Password found: {result}[/bold green]")
                    return

    if not stop_flag:
        print("\n[bold red]❌ No password found. Try a different wordlist.[/bold red]")

def ascii_intro():
    ascii_art = pyfiglet.figlet_format("PDF Cracker", font="slant")
    console.print(f"[bold green]{ascii_art}[/bold green]")
    console.print("\n[bold yellow]Starting brute-force attempt... 🔓[/bold yellow]")
    time.sleep(1)

def main():
    ascii_intro()

    parser = argparse.ArgumentParser(description="PDF Brute Force Cracker")
    parser.add_argument("-p", "--pdf", required=True, help="Path to the PDF file")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the wordlist")
    parser.add_argument("-mp", "--max-workers", type=int, default=4, help="Number of parallel threads")

    args = parser.parse_args()

    if not os.path.exists(args.pdf):
        print(f"[bold red]Error: PDF file {args.pdf} does not exist.[/bold red]")
        return
    if not os.path.exists(args.wordlist):
        print(f"[bold red]Error: Wordlist file {args.wordlist} does not exist.[/bold red]")
        return

    print(f"\n[bold green]🔐 Cracking PDF file: [yellow]{args.pdf}[/yellow] 🔓[/bold green]\n")
    crack_pdf(args.pdf, args.wordlist, max_workers=args.max_workers)

    if found_password:
        print("\n[bold green]Brute-forcing process completed successfully![/bold green]")
    else:
        print("\n[bold red]Brute-forcing process completed with no password found.[/bold red]")

    print("\n[bold yellow]Thank you for using the PDF Cracker! Goodbye![/bold yellow]")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()
