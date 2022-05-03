import tkinter as tk
from turtle import home
import tkinter.font as font
window_height = 800
window_width = 480
#homeNames = ["distortion", "+", "+", "+", "+", "+"]
# format for states: 
# (name, value1, value2, value3, CCodeObject(N/A for rn))
DEFAULT_NAME = "+"
homeState = [None for i in range(6)]
posNum = -1
dark_gray = "#303030"

def distortionButtonOnClick(window, frameToForget, createFrame, sliders):
    global posNum
    for j in sliders: 
        print(j.get()) 
    homeState[posNum] = tuple(["Distortion"] + [s.get() for s in sliders])
    print(homeState)
    onClickGeneric(window, frameToForget, createFrame)
def clearButton(window, frameToForget,createFrame):
    homeState[posNum] = None
    onClickGeneric(window,frameToForget, createFrame)
def onClickGeneric(window, frameToForget, createFrame):
    frameToForget.grid_forget()
    createFrame(window)
def onClick(window,homeframe, buttonNum):
    global posNum
    homeframe.grid_forget()
    posNum = buttonNum
    createMenuFrame(window)
def onClicktwo(window,menuframe):
    menuframe.grid_forget()
    createDistortionFrame(window)
def createHomeFrame(window):
    homeframe = tk.Frame(window, bg="black", width = window_width, height = window_height)
    homeframe.columnconfigure(0, weight=1, uniform="ia-h")
    homeframe.columnconfigure(1, weight=1, uniform="ia-h")
    homeframe.columnconfigure(2, weight=1, uniform="ia-h")
    homeframe.rowconfigure(0, weight = 1, uniform="ia-h")
    homeframe.rowconfigure(1, weight = 1, uniform="ia-h")
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
        tk.Button(temp, text= homeState[i][0] if homeState[i] else DEFAULT_NAME, bg="black" , fg="white", bd = 0,  font=wordFont if homeState[i] else plusFont,
            command=lambda i=i: onClick(window,homeframe,i)).grid(row = 1, column = 1, sticky=tk.NSEW)
    homeframe.grid(row=0, column=0, sticky=tk.NSEW)
    return homeframe
def createMenuFrame(window):
    menuframe = tk.Frame(window, bg="black", width = window_width, height = window_height)
    menuframe.columnconfigure(0, weight=1, uniform="ia")
    menuframe.columnconfigure(1, weight=5)
    menuframe.columnconfigure(2, weight=1, uniform="ia")
    menuframe.rowconfigure(0, weight = 1)
    menuframe.rowconfigure(1, weight = 1)
    menuframe.rowconfigure(2, weight = 1)
    menuframe.rowconfigure(3, weight = 1)
    menuframe.rowconfigure(4, weight = 1)
    menuframe.rowconfigure(5, weight = 1)
    menuframe.rowconfigure(6, weight=1)
   
    text = tk.Label(menuframe, text="Select Effect", bg="black", fg="white", font=titleFont)
    text.grid(row = 0, column = 1, sticky=tk.NSEW)
    homeBorder = tk.Frame(menuframe, highlightbackground="white", highlightthickness=2, bd = 0)
    tk.Button(homeBorder, text = "home", fg="white", bg=dark_gray, command=lambda: onClickGeneric(window, menuframe, createHomeFrame), padx=30).pack()
    homeBorder.grid(row=0, column=0)
    #topFrame.grid(row=0, column=0, sticky=tk.EW)
    names = ["Distortion", "Fuzz", "Overdrive"]
    for i in range(5):
        if i <= 2:
            tk.Button(menuframe, text= names[i], bg="black"if i%2!=0 else dark_gray, fg="white",
                command=lambda: onClicktwo(window,menuframe)).grid(row = i+1, column = 0, sticky=tk.NSEW, columnspan=3)
        else: 
            tk.Label(menuframe, text = "                ", bg = "black" if i%2!=0 else dark_gray).grid(row= i+1, column=0, sticky=tk.NSEW, columnspan=3)
    clearBorder = tk.Frame(menuframe, highlightbackground="white", highlightthickness=2, bd = 0)
    tk.Button(clearBorder, text="Clear", fg="white", bg=dark_gray, command=lambda:clearButton(window,menuframe,createHomeFrame), padx=30).pack()
    clearBorder.grid(row=6, columnspan=3)
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
    slider = [None for i in range(3)]
    for i, l in enumerate(sliderLabels):
        slider[i] = tk.Scale(distortionframe,  from_= 0, to = 100, resolution = 1, orient = tk.HORIZONTAL, 
                        length = 500, width = 15, fg = colors[i], bg="black", label=names[i], bd=1, troughcolor=colors[i],
                        font=sliderFont, showvalue=0,  command=lambda event, label=l: label.config(text=str(event)))
        slider[i].set(homeState[posNum][i+1] if homeState[posNum] else 0)
    for i, s in enumerate(slider): 
        s.grid(row=i+1, column=0, sticky=tk.EW)
        sliderLabels[i].grid(row=i+1, column=1, stick=tk.NSEW)
    tk.Button(distortionframe, text= "Add Effect", bg="black", fg="white",
            command=lambda:distortionButtonOnClick(window,distortionframe, createHomeFrame, slider)).grid(row = 2, column = 2, sticky=tk.EW)
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
window.mainloop()
