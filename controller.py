import pyautogui
import threading
import time
from config import SCROLL_AMOUNT, MOVE_DISTANCE
from utils import typewriter, banner, flicker_line, launch_sequence

class MouseController:
    def __init__(self):
        self.running = False
        self.thread = None

    def start(self, delay):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.run, args=(delay,), daemon=True)
            self.thread.start()

    def run(self, delay):
        launch_sequence()  # Matrix-style cinematic intro
        banner("MOUSE AUTOMATION ACTIVE", color="cyan")
        while self.running:
            flicker_line("-> Scrolling Up", final_color="green")
            pyautogui.scroll(SCROLL_AMOUNT)
            time.sleep(1)

            flicker_line("-> Scrolling Down", final_color="yellow")
            pyautogui.scroll(-SCROLL_AMOUNT)
            time.sleep(1)

            flicker_line("-> Moving Right", final_color="blue")
            pyautogui.moveRel(MOVE_DISTANCE, 0, duration=0.3)
            time.sleep(1)

            flicker_line("-> Moving Left", final_color="magenta")
            pyautogui.moveRel(-MOVE_DISTANCE, 0, duration=0.3)
            time.sleep(1)

            typewriter(f"Waiting {delay}s before next cycle...\n", color="gray")
            time.sleep(delay)

    def stop(self):
        self.running = False
        banner("MOUSE AUTOMATION STOPPED", color="red")
        flicker_line("Shutdown sequence complete.", final_color="red")
