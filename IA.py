import tkinter as tk

def onClick(window,homeframe):
    homeframe.grid_forget()
    names = ["Distortion", "Overdrive", "Fuzz"]
#    for i in range(6):
#    button.append(
#        tk.Button(
#            homeframe,
#            text= names[i],
    #         width=30,
    #        height=15,
#            bg="white",
#            fg="blue",
#            command=lambda: onClick(window,homeframe)
#    ))
#    button[i].grid(row = int(i/3), column = int(i)%3, sticky=tk.NSEW)

window = tk.Tk()
window_height = 800
window_width = 480
window.geometry('800x480')#Pixels
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight = 1)
homeframe = tk.Frame(window, bg="black", width = window_width, height = window_height)
homeframe.columnconfigure(0, weight=1)
homeframe.columnconfigure(1, weight=1)
homeframe.columnconfigure(2, weight=1)
homeframe.rowconfigure(0, weight = 1)
homeframe.rowconfigure(1, weight = 1)
names = ["+", "+", "+", "+", "+", "+"]
#command = [AddEffect, AddEffect, AddEffect, AddEffect, AddEffect, AddEffect]
button = []
for i in range(6):
    button.append(
        tk.Button(
            homeframe,
            text= names[i],
    #         width=30,
    #        height=15,
            bg="white",
            fg="blue",
            command=lambda: onClick(window,homeframe)
    ))
    button[i].grid(row = int(i/3), column = int(i)%3, sticky=tk.NSEW)
   # button[i].pack()
homeframe.grid(row=0, column=0, sticky=tk.NSEW)
window.mainloop()
