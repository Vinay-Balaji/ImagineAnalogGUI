import tkinter as tk
from turtle import home
import tkinter.font as font
window_height = 800
window_width = 480
homeNames = ["distortion", "+", "+", "+", "+", "+"]
#plusFont = None
def sliderCommand(var, label): 
    label['text'] = var
def onClickGeneric(window, frameToForget, createFrame):
    frameToForget.grid_forget()
    createFrame(window)
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
    colors = ["red", "orange", "yellow", "green", "light blue", "purple"]
    
    for i in range(6):
        temp = tk.Frame(homeframe, bg=colors[i])
        temp.columnconfigure(0, weight=1)
        temp.columnconfigure(1, weight=5)
        temp.columnconfigure(2, weight=1)
        temp.rowconfigure(0,weight=1)
        temp.rowconfigure(1,weight=5)
        temp.rowconfigure(2,weight=1)
        temp.grid(row=int(i/3), column=int(i)%3, sticky=tk.NSEW, padx=25, pady=25)
        tk.Button(temp, text= homeNames[i], bg="black", fg="white", bd = 0,  font=plusFont if homeNames[i]=="+" else wordFont,
            command=lambda: onClick(window,homeframe)).grid(row = 1, column = 1, sticky=tk.NSEW)
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
    distortionframe.columnconfigure(0, weight=3)
    distortionframe.columnconfigure(1, weight=1)
    distortionframe.columnconfigure(2, weight=1)
    distortionframe.rowconfigure(0, weight = 1)
    distortionframe.rowconfigure(1, weight = 1)
    distortionframe.rowconfigure(2, weight = 1)
    distortionframe.rowconfigure(3, weight = 1)
    distortionframe.rowconfigure(4, weight = 1)
    text = tk.Label(distortionframe, text="Distortion", bg="black", fg="white", font=titleFont)
    text.grid(row = 0, column = 0, sticky=tk.NSEW)
    names = ["Level", "Tone", "Distortion"]
    colors = ["green", "yellow", "light blue"]
    sliderLabels = [tk.Label(distortionframe, text="0", bg="black", fg="white") for i in range(3)]
    slider = [tk.Scale(distortionframe,  from_= 0, to = 100, resolution = 1, orient = tk.HORIZONTAL, 
                        length = 500, width = 15, fg = colors[i], bg="black", label=n, bd=1, troughcolor=colors[i], 
                        font=sliderFont, showvalue=0) for i, n in enumerate(names)]
    for i, s in enumerate(slider): 
        s.grid(row=i+1, column=0, sticky=tk.EW)
        sliderLabels[i].grid(row=i+1, column=1, stick=tk.NSEW)
    tk.Button(distortionframe, text= "Add Effect", bg="black", fg="white",
            command=lambda: onClickGeneric(window,distortionframe, createHomeFrame)).grid(row = 2, column = 2, sticky=tk.EW)
    """
    slide1 = tk.Scale(distortionframe, from_= 0, to = 100, resolution = 1, orient = tk.HORIZONTAL, length = 500, width = 20, fg = "green", bg="black", label="test", bd=1, troughcolor="green")
   # slide1.pack()
    slide1.grid(row = 1, column=0, sticky=tk.EW)
    slide2 = tk.Scale(distortionframe, from_= 0, to = 100, resolution = 1, orient = tk.HORIZONTAL, length = 500, width = 20, fg = "yellow", bg="black", relief=tk.RIDGE)
    #slide2.pack()
    slide2.grid(row = 2, column=0, sticky=tk.EW)
    slide3 = tk.Scale(distortionframe, from_= 0, to = 100, resolution = 1, orient = tk.HORIZONTAL, length = 500, width = 20, fg = "light blue", bg="black", bd = 0)
    #slide3.pack()
    slide3.grid(row = 3, column=0, sticky=tk.EW)
    """
    distortionframe.grid(row=0, column=0, sticky=tk.NSEW)
    return distortionframe

window = tk.Tk()
window.geometry('800x480')#Pixels
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight = 1)
plusFont = font.Font(family="Arial", size=50, weight="bold")
wordFont = font.Font(family="Arial", size=20, weight="bold")
sliderFont = font.Font(family="Arial", size=20) 
titleFont = font.Font(family="Arial", size=27)
createHomeFrame(window)
#createDistortionFrame(window)
window.mainloop()
