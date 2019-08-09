from src.gui.gif_loader import *
import tkinter as tk

#TODO: Place animated text ON TOP of gif - Don't think I need multi-threading

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
    # Sets canvas size
    canvasWidth = 540
    canvasHeight = 720

    # Creates window, makes it transparent
    window = tk.Tk()
    window.wait_visibility(window)
    window.attributes('-alpha', 0.0)
    window.title("rsText")
    window.geometry(str(canvasWidth) + 'x' + str(canvasHeight))

    # Creates canvas container
    canvas = tk.Canvas(window)
    # canvas = ResizingCanvas(canvasWidth,canvasHeight,highlightthickness=0)
    canvas.pack(fill='both', expand='yes')

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

    lbl = ImageButton(canvas, text='Play Now', compound=tk.BOTTOM, state="normal")
    lbl.pack(fill='both', expand='yes')
    lbl.load('images/rs_homepage.gif')
    window.resizable(False, False)
    center(window)
    window.attributes('-alpha', 1.0)
    window.mainloop()
