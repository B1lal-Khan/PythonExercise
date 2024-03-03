import tkinter as tk

def color_change(color):
    main['bg'] = color

main = tk.Tk()
main.title("Colour changer")

for color in ["red", "blue"]:
    button = tk.Button(main_window, text=color,capitalise(), command=lambda c=color:
    button.pack(pady=10)
    
main_window.mainloop()