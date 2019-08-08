from src.gui.gif_loader import *
import tkinter as tk
#TODO: Hide GUI until centered
#TODO: Setup the text to write over the gif at the top(Probably need multi-threading)
#https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter
#Tried alpha - doesnt work on linux

def center(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def createGUI():
    canvasWidth = 540
    canvasHeight = 720

    window = tk.Tk()


    canvas = tk.Canvas(window)
    window.attributes('-alpha', 0.0)
    # canvas = ResizingCanvas(canvasWidth,canvasHeight,highlightthickness=0)
    canvas.pack(fill='both', expand='yes')

    window.title("rsText")

    window.geometry(str(canvasWidth) + 'x' + str(canvasHeight))

    xOffset = canvasWidth / 2
    yOffset = canvasHeight / 2

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

    lbl = ImageButton(canvas, text='Play Now', compound=tk.TOP, state="disabled")
    lbl.pack(fill='both', expand='yes')
    lbl.load('images/rs_homepage.gif')
    window.resizable(False, False)
    center(window)
    window.attributes('-alpha', 1.0)
    window.mainloop()
