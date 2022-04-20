import tkinter as tk
window_height = 800
window_width = 480

def onClick(window,homeframe):
    homeframe.grid_forget()
    createMenuFrame(window)
def onClicktwo(window,menuframe):
    menuframe.grid_forget()
    createDistortionFrame(window)
def createHomeFrame(window):
    homeframe = tk.Frame(window, bg="black", width = window_width, height = window_height)
    homeframe.columnconfigure(0, weight=1)
    homeframe.columnconfigure(1, weight=1)
    homeframe.columnconfigure(2, weight=1)
    homeframe.rowconfigure(0, weight = 1)
    homeframe.rowconfigure(1, weight = 1)
    names = ["AddEffect", "AddEffect", "AddEffect", "AddEffect", "AddEffect", "AddEffect"]
    
    for i in range(6):
        tk.Button(homeframe, text= names[i], bg="light blue", fg="black",
            command=lambda: onClick(window,homeframe)).grid(row = int(i/3), column = int(i)%3, sticky=tk.NSEW)
    homeframe.grid(row=0, column=0, sticky=tk.NSEW)
    return homeframe

def createMenuFrame(window):
    menuframe = tk.Frame(window, bg="black", width = window_width, height = window_height)
    menuframe.columnconfigure(0, weight=1)
    menuframe.rowconfigure(0, weight = 1)
    menuframe.rowconfigure(1, weight = 1)
    menuframe.rowconfigure(2, weight = 1)
    menuframe.rowconfigure(3, weight = 1)
    menuframe.rowconfigure(4, weight = 1)
    text = tk.Label(menuframe, text="Select Effect")
    text.grid(row = 0, column = 0, sticky=tk.NSEW)
    names = ["Distortion", "Fuzz", "Overdrive"]
    for i in range(3):
        tk.Button(menuframe, text= names[i], bg="light blue", fg="black",
            command=lambda: onClicktwo(window,menuframe)).grid(row = i+1, column = 0, sticky=tk.NSEW)
    menuframe.grid(row=0, column=0, sticky=tk.NSEW)
    return menuframe

def createDistortionFrame(window):
    distortionframe = tk.Frame(window, bg="black", width = window_width, height = window_height)
    distortionframe.columnconfigure(0, weight=1)
    distortionframe.rowconfigure(0, weight = 1)
    distortionframe.rowconfigure(1, weight = 1)
    distortionframe.rowconfigure(2, weight = 1)
    distortionframe.rowconfigure(3, weight = 1)
    distortionframe.rowconfigure(4, weight = 1)
    text = tk.Label(distortionframe, text="Distortion")
    text.grid(row = 0, column = 0, sticky=tk.NSEW)
    names = ["Level", "Tone", "Distortion"]
    slide1 = tk.Scale(window, from_= 0, to = 100, resolution = 2, orient = tk.HORIZONTAL)
    slide1.pack()
    slide2 = tk.Scale(window, from_= 0, to = 100, resolution = 2, orient = tk.HORIZONTAL)
    slide2.pack()
    slide3 = tk.Scale(window, from_= 0, to = 100, resolution = 2, orient = tk.HORIZONTAL)
    slide3.pack()
    #for i in range(3):
    #    tk.Button(distortionframe, text= names[i], bg="light blue", fg="black",
    #        command=lambda: onClicktwo(window,distortionframe)).grid(row = i+1, column = 0, sticky=tk.NSEW)
    distortionframe.grid(row=0, column=0, sticky=tk.NSEW)

    return distortionframe

window = tk.Tk()
window.geometry('800x480')#Pixels
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight = 1)
createHomeFrame(window)
window.mainloop()
