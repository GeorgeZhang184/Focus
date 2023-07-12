import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class FocusTimer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Focus Timer")
        
        self.timer_frame = ttk.Frame(self.window, padding="20 20 20 20")
        self.timer_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        
        self.welcome_label = ttk.Label(self.timer_frame, text="Welcome to the Focus Timer!")
        self.welcome_label.grid(column=0, row=0, columnspan=2, pady=20)
        
        self.start_button = ttk.Button(self.timer_frame, text="Start", command=self.start_timer)
        self.start_button.grid(column=0, row=1, pady=10)
        
        self.time_label = ttk.Label(self.timer_frame, text="Focus Time (minutes):")
        self.time_label.grid(column=0, row=2, pady=10)
        
        self.time_spinbox = ttk.Spinbox(self.timer_frame, from_=1, to=60)
        self.time_spinbox.grid(column=1, row=2, pady=10)
        
        self.next_button = ttk.Button(self.timer_frame, text="Next", command=self.set_timer)
        
        self.timer_label = ttk.Label(self.timer_frame, text="")
        
        self.stop_button = ttk.Button(self.timer_frame, text="Stop", command=self.stop_timer)
        
        self.congrats_label = ttk.Label(self.timer_frame, text="Congratulations! Timer finished.")
        
        self.timer = None
        self.time_left = 0
    
    def start_timer(self):
        self.start_button.grid_forget()
        self.time_label.grid_forget()
        self.time_spinbox.grid_forget()
        self.next_button.grid(column=0, row=3, pady=10)
        
        self.timer_label.grid(column=0, row=4, columnspan=2, pady=10)
        self.stop_button.grid(column=0, row=5, pady=10)
        
        self.congrats_label.grid_forget()
        
    def set_timer(self):
        focus_time = int(self.time_spinbox.get())
        self.time_left = focus_time * 60
        
        self.next_button.grid_forget()
        self.timer_label["text"] = f"Time Left: {focus_time}:00"
        
        self.timer = self.window.after(1000, self.update_timer)
    
    def update_timer(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.timer_label["text"] = f"Time Left: {minutes}:{seconds:02}"
        
        if self.time_left > 0:
            self.time_left -= 1
            self.timer = self.window.after(1000, self.update_timer)
        else:
            self.finish_timer()
    
    def finish_timer(self):
        self.timer_label.grid_forget()
        self.stop_button.grid_forget()
        self.congrats_label.grid(column=0, row=4, columnspan=2, pady=20)
        
        messagebox.showinfo("Congratulations!", "Timer finished.")
    
    def stop_timer(self):
        self.window.after_cancel(self.timer)
        self.start_button.grid(column=0, row=1, pady=10)
        self.time_label.grid(column=0, row=2, pady=10)
        self.time_spinbox.grid(column=1, row=2, pady=10)
        self.next_button.grid_forget()
        self.timer_label.grid_forget()
        self.stop_button.grid_forget()
        
        self.congrats_label.grid_forget()
    
    def run(self):
        self.window.mainloop()

focus_timer = FocusTimer()
focus_timer.run()
