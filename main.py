import tkinter as tk
from tkinter import messagebox
from controller import MouseController

class MouseAutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Automation Tool")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        self.controller = MouseController()

        tk.Label(root, text="Delay (seconds):").pack(pady=10)
        self.delay_var = tk.StringVar(value="60")
        tk.Entry(root, textvariable=self.delay_var, width=10).pack()

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop, state=tk.DISABLED)
        self.stop_button.pack()

        self.status_label = tk.Label(root, text="Status: Idle", fg="blue")
        self.status_label.pack(pady=20)

    def start(self):
        try:
            delay = int(self.delay_var.get())
            self.controller.start(delay)
            self.status_label.config(text="Status: Running", fg="green")
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def stop(self):
        self.controller.stop()
        self.status_label.config(text="Status: Stopped", fg="red")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = MouseAutomationApp(root)
    root.mainloop()
