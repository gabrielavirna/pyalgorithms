# create winow, resize, minimize, maximize, close, bring it back
# with that window, create a frame

from tkinter import *
from PIL import Image, ImageTk


class Window(Frame):
    def __init__(self, master=None):  # initialization; this is our parent widget, main window
        Frame.__init__(self, master)
        self.master = master  # main frame,master widget

        self.init_window()

    def init_window(self):  # initialize the window

        self.master.title("GUI")  # set a title for window

        self.pack(fill=BOTH, expand=1)  # fill up the window and adjust the size as needed

        # quitButton = Button(self, text="Quit", command=self.client_exit)
        # quitButton.place(x=0,y=0)            # place the button upper left


        '''
        Create a menu bar (part of our main frame)
        '''
        menu = Menu(self.master)  # menu of the main window
        self.master.config(menu=menu)  # we defined the menu

        file = Menu(menu)
        file.add_command(label='Save', command=self.client_exit)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)  # cascade of options

        '''
        edit = Menu(menu)
        edit.add_command(label='Undo')
        menu.add_cascade(label='Edit', menu=edit)
        '''

        edit = Menu(menu)
        edit.add_command(label='Show Image', command=self.showImg)
        edit.add_command(label='Show Text', command=self.showTxt)
        menu.add_cascade(label='Edit',menu=edit)


        # IntallPillow, a replacement for PIL:Python Image Library, http://www.lfd.uci.edu/~gohlke/pythonlibs/

    '''
    Addition of labels=image/text)
    '''

    def showImg(self):
        load = Image.open('robotics.jpg')
        render = ImageTk.PhotoImage(load)


        # use labels to display images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)


    def showTxt(self):
        text = Label(self, text='Hey there!')
        text.pack()


    def client_exit(self):
        exit()


root = Tk()  # Tk window
root.geometry("400x300")  # set dimensions of the window
app = Window(root)
root.mainloop()  # initializes&generates our window
