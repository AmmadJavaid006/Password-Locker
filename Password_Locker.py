import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My GUI")

# Add widgets (e.g., button)
button = tk.Button(window, text="Dont click me")
button.pack()

# Run the main loop
window.mainloop()