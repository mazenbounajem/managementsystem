
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.style import *
from tkinter import *
from ttkbootstrap.style import *

class CustomerClass:
    def __init__(self,root, title='',themename='superhero', iconphoto='.images/conphoto.png', size=None, position=None, minsize=None, maxsize=None, resizable=None, hdpi=True, scaling=None, transient=None, overrideredirect=False, alpha=1.0):
        self.root=root
        self.root.title('Customer')
        self.root.iconbitmap('./images/conphoto.png')
        self.root.geometry("1400x800+0+0")
        
        
        #second_frame =tb.Frame(self.root,bootstyle='info')
        #second_frame.place(x=0,y=100,width=maxsize,height=maxsize)




        






if __name__=="__main__":    
    root=tb.Window(themename="superhero")
    obj=CustomerClass(root)
    root.mainloop()