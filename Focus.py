import tkinter as tk
from tkinter import messagebox
import time

class FocusTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Focus Timer")
        self.root.geometry("285x150")

        self.focus_time = 0
        self.timer_running = False

        self.create_welcome_page()

    def create_welcome_page(self):
        self.label_welcome = tk.Label(self.root, text="Welcome to Focus Timer", font=("Arial", 12))
        self.label_welcome.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Start", command=self.show_timer_page)
        self.start_button.pack()

    def show_timer_page(self):
        self.start_button.pack_forget()
        self.create_timer_page()

    def create_timer_page(self):
        self.label_welcome.pack_forget()
        self.spin_box = tk.Spinbox(self.root, from_=1, to=240, width=10)
        self.spin_box.pack(pady=10)

        self.label_time_left = tk.Label(self.root, text="How long do you want to focus?(minutes)", font=("Arial", 12))
        self.label_time_left.pack(pady=20)

        self.next_button = tk.Button(self.root, text="Start!", command=self.start_timer)
        self.next_button.pack(pady=10)
        
    def start_timer(self):
        self.focus_time = int(self.spin_box.get())

        if self.focus_time > 0:
            self.focus_time *= 60  # Convert to seconds
            self.next_button.config(state=tk.DISABLED)
            self.spin_box.config(state=tk.DISABLED)
        
            self.timer_running = True
            self.update_timer()
        else:
            messagebox.showerror("Invalid Time", "Please set a valid focus time!")

    def stop_timer(self):
        self.timer_running = False
        self.label_time_left.config(text="Time Left: ")
        
        self.next_button.config(state=tk.NORMAL)
        self.spin_box.config(state=tk.NORMAL)

    def update_timer(self):
        self.spin_box.pack_forget()
        self.next_button.pack_forget()
        if self.focus_time >= 0 and self.timer_running:
            minutes = self.focus_time // 60
            seconds = self.focus_time % 60

            self.label_time_left.config(text=f"{minutes:02d}:{seconds:02d}",font=("Arial",57))
            
            if self.focus_time == 0:
                self.timer_running = False
                self.congrats_page()
            else:
                self.focus_time -= 1
                self.root.after(1000, self.update_timer)

    def congrats_page(self):
        messagebox.showinfo("Congrats!", "You've completed the focus time!")
        self.label_time_left.config(text="Time Left: ")
        self.next_button.config(state=tk.NORMAL)
        self.spin_box.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    timer = FocusTimer(root)
    root.mainloop()
  
