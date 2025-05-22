import sys
import time
import random
import string
import os

COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "gray": "\033[90m",
    "reset": "\033[0m"
}

def typewriter(text, delay_range=(0.01, 0.03), color="green"):
    ansi = COLORS.get(color, COLORS["reset"])
    for char in text:
        sys.stdout.write(ansi + char + COLORS["reset"])
        sys.stdout.flush()
        time.sleep(random.uniform(*delay_range))
    print()

def banner(text, color="cyan"):
    ansi = COLORS.get(color, COLORS["reset"])
    border = "=" * 40
    centered_text = text.center(40)
    print(f"{ansi}{border}")
    print(centered_text)
    print(f"{border}{COLORS['reset']}")

def flicker_line(text, flicker_times=25, flicker_delay=0.02, final_color="yellow"):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+{}[]<>|\\/"
    for _ in range(flicker_times):
        junk = ''.join(random.choice(chars) for _ in range(len(text)))
        sys.stdout.write('\r' + COLORS["gray"] + junk + COLORS["reset"])
        sys.stdout.flush()
        time.sleep(flicker_delay)
    sys.stdout.write('\r' + COLORS.get(final_color, "") + text + COLORS["reset"] + '\n')
    sys.stdout.flush()

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def matrix_stream(lines=20, width=60, speed=0.01):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    for _ in range(lines):
        line = ''.join(random.choice(chars) for _ in range(width))
        print(COLORS["green"] + line + COLORS["reset"])
        time.sleep(speed)

def flicker_message(msg, flicker_times=20, delay=0.03, final_color="cyan"):
    for _ in range(flicker_times):
        junk = ''.join(random.choice(string.printable) for _ in range(len(msg)))
        sys.stdout.write('\r' + COLORS["green"] + junk + COLORS["reset"])
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\r' + COLORS.get(final_color, "") + msg + COLORS["reset"] + '\n')
    sys.stdout.flush()

def launch_sequence():
    clear_terminal()
    matrix_stream(lines=10, width=80, speed=0.01)
    flicker_message("Initializing mouse automation system...", final_color="cyan")
    time.sleep(0.5)
    flicker_message("Scanning input devices...", final_color="yellow")
    time.sleep(0.5)
    flicker_message("Establishing control channels...", final_color="magenta")
    time.sleep(0.5)
    matrix_stream(lines=5, width=70, speed=0.01)
    flicker_message("Status: ONLINE", final_color="green")
    typewriter("System ready for interaction.", color="green")
    print()
