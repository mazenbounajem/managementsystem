
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
        second_frame.place(x=0,y=0,width=1400,height=400)

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
        
        
        table.pack(padx=90)
        
        
        self.icon_new=PhotoImage(file="images/iconsglobal/add.png")
        
        btn_new = ttk.Button(second_frame,image=self.icon_new,bootstyle=('outline'))
        btn_new.place(x=0,y=0)
        self.icon_duplicate=PhotoImage(file="images/iconsglobal/duplicate.png")
        btn_duplicate = ttk.Button(second_frame,image=self.icon_duplicate,bootstyle=('outline'))
        btn_duplicate.place(x=0,y=80)
        self.icon_undo=PhotoImage(file="images/iconsglobal/undo.png")
        btn_undo = ttk.Button(second_frame,image=self.icon_undo,bootstyle=('outline'))
        btn_undo.place(x=0,y=145)
        self.icon_delete=PhotoImage(file="images/iconsglobal/delete.png")
        btn_delete = ttk.Button(second_frame,image=self.icon_delete,bootstyle=('outline'))
        btn_delete.place(x=0,y=245)
        self.icon_print=PhotoImage(file="images/iconsglobal/print.png")
        btn_print = ttk.Button(second_frame,image=self.icon_print,bootstyle=('outline'))
        btn_print.place(x=0,y=265)
        self.icon_refresh=PhotoImage(file="images/iconsglobal/refresh.png")
        btn_refresh = ttk.Button(second_frame,image=self.icon_refresh,bootstyle=('outline'))
        btn_refresh.place(x=0,y=325)
        self.icon_search=PhotoImage(file="images/iconsglobal/search.png")
        btn_search= ttk.Button(second_frame,image=self.icon_search,bootstyle=('outline'))
        btn_search.place(x=0,y=385)
        

        
       
        

     




if __name__=="__main__":    
    root=tb.Window(themename="superhero")
    obj=CustomerClass(root)
    root.mainloop()