import tkinter as tk
import time

def update_clock():
    """Update the clock label with the current time."""
    current_time = time.strftime("%H:%M:%S")  # 24-hour format
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)  # Schedule next update in 1 second

# Create main application window
root = tk.Tk()
root.title("Live Digital Clock")
root.geometry("300x100")
root.resizable(True, True)  # Allow resizing

# Create and style the clock label
clock_label = tk.Label(
    root,
    font=("Helvetica", 40, "bold"),
    background="black",
    foreground="cyan"
)
clock_label.pack(expand=True, fill="both")

# Start the clock
update_clock()

# Run the application
try:
    root.mainloop()
except KeyboardInterrupt:
    print("Clock stopped.")
