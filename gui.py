import tkinter as tk
# TODO: Make canvas/widgets autosize
# class ResizingCanvas(tk.Canvas):
#     def __init__(self,parent,**kwargs):
#         tk.Canvas.__init__(self,parent,**kwargs)
#         self.bind("<Configure>", self.on_resize)
#         self.height = self.winfo_reqheight()
#         self.width = self.winfo_reqwidth()
#
#     def on_resize(self,event):
#         # determine the ratio of old width/height to new width/height
#         wscale = float(event.width)/self.width
#         hscale = float(event.height)/self.height
#         self.width = event.width
#         self.height = event.height
#         # resize the canvas
#         self.config(width=self.width, height=self.height)
#         # rescale all the objects tagged with the "all" tag
#         self.scale("all",0,0,wscale,hscale)

def createGUI():
    canvasWidth = 750
    canvasLength = 700

    window = tk.Tk()
    canvas = tk.Canvas(window)

    #canvas = ResizingCanvas(canvasWidth,canvasLength,highlightthickness=0)
    canvas.pack(fill='both',expand='yes')

    window.title("rsText")

    window.geometry(str(canvasWidth) + 'x' + str(canvasLength))

    xOffset = canvasWidth / 2
    yOffset = canvasLength / 2

    title_text = "Welcome to rsText"
    canvas_text = canvas.create_text(xOffset, yOffset, text='')

    # Time delay between chars, in milliseconds
    delta = 300
    delay = 0

    # Animates text
    for i in range(len(title_text) + 1):
        s = title_text[:i]
        update_text = lambda s=s: canvas.itemconfigure(canvas_text, text=s)
        canvas.after(delay, update_text)
        delay += delta

    canvas.addtag_all("all")
    window.mainloop()
