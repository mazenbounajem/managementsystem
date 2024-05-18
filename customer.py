
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.style import *
from tkinter import *
from ttkbootstrap.style import *
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame


class CustomerClass():
    def __init__(self,root, title='',themename='superhero', iconphoto='.images/conphoto.png', size=None, position=None, minsize=None, maxsize=None, resizable=None, hdpi=True, scaling=None, transient=None, overrideredirect=False, alpha=1.0):
        self.root=root
        self.root.title('Customer')
        self.root.iconbitmap('./images/conphoto.png')
        self.root.geometry("1800x800+0+150")
    #     colors=root.style.colors
    
        second_frame =tb.Frame(self.root)
        second_frame.place(x=50,y=0,width=1400,height=400)

        row_data = [
            ('mazen','1','ghaboun','76352915','mazenbounajem@gmail.com','2024-05-17','2024-05-17','2024-05-17','100000','1')
            ]
        

    
        columns=[
            {"text":"Name","stretch":True},
            {"text":"Customer ID","stretch":True},
            {"text":"Address","stretch":True},
            {"text":"Phone Number","stretch":True},
            {"text":"Email","stretch":True},
            {"text": "First Sales Date","stretch":True},
            {"text":"Last payment Date","stretch":True},
            {"text":"Last Sales Date","stretch":True},
            {"text":"Balance L.L","stretch":True},
            {"text":"Balance USD","stretch":True}
               ]
        table =Tableview(
            master=second_frame,
            coldata=columns,
            rowdata=row_data,
            paginated=True,
            searchable=True,
            autofit=True,
            bootstyle=PRIMARY,
            stripecolor=(None),
            autoalign=LEFT
            
        )
        
        
        table.pack(fill='x',)

        self.buttonFrame=tb.Frame(self.root)
        self.buttonFrame.place(x=0,y='y',width=50,height=800)

        
        
       
        

     




if __name__=="__main__":    
    root=tb.Window(themename="superhero")
    obj=CustomerClass(root)
    root.mainloop()