import tkinter as tk
from playsound3 import playsound

root = tk.Tk()
root.wm_geometry("500x500")
root.configure(bg="black")

frame = tk.Frame(root)
frame.configure(bg="black")
frame.pack()

def song(filename):
    playsound(f"UnderSongs/{filename}.mp3")

lbl = tk.Label(frame, text="", bg="black")
lbl.pack(pady=5)

papsbutton = tk.Button(frame, text="Nyeh Heh Heh!", font=("Papyrus", 24), command=lambda:song("Nyeh Heh Heh!"))
papsbutton.pack(pady=10)

sansbutton = tk.Button(frame, text="sans.", font=("Comic Sans MS", 24), command=lambda:song("sans."))
sansbutton.pack(pady=15)

root.mainloop()