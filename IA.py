import tkinter as tk

window = tk.Tk()

window.geometry('200x50')#Pixels
names = ["Distortion", "Fuxx", "Overdrive", "Four", "Five", "Six"]
#command = [distortion, fuzz, overdrive, four, five, six]
button = []
for i in range(6):
    button.append(
        tk. Button(
            window,
            text= names[i],
            width=25,
            height=5,
            bg="blue",
            fg="yellow",
    ))
    button[i].grid(row = int(i/3), column = int(i)%3)
   # button[i].pack()

window.mainloop()
