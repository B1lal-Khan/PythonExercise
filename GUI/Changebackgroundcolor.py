import tkinter as tk

def change_color(color):
    main_window['bg'] = color

# Create the main window
main_window = tk.Tk()
main_window.title("Color Changer")

# Create buttons and set their command to the change_color function
for color in ["red", "blue"]:
    button = tk.Button(main_window, text=color.capitalize(), command=lambda c=color: change_color(c))
    button.pack(pady=10)

# Run the Tkinter event loop
main_window.mainloop()