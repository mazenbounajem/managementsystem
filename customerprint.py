from tkinter import messagebox
from tkinter.ttk import Treeview
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.style import *
from tkinter import *
from ttkbootstrap.style import *
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from connection import connection
from nicegui import ui
class CustomerPrint:
    def __init__(self,root):
        self.root=root
        w = self.root.winfo_reqwidth()
        h = self.root.winfo_reqheight()
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws) 
        y = (hs)
        print (w,h,ws,hs)
        self.root.geometry("1600x700+200+150")
        self.root.resizable(False, False)
        
        self.root.title('Customer Print')
        
        self.frame1=tb.Frame(self.root)
        self.frame1.place(x=100,y=0)
        

        self.lbltitle=tb.Label(self.frame1,bootstyle='danger',text="Please Select a title for your report:",font=("times new roman",'10','bold'),background='white')
        self.lbltitle.grid(row=1,column=0,padx=50,pady=50)

        self.cmbreport=tb.Combobox(self.frame1,bootstyle='success',values=['customer info','customer statment','customer bought products'],state='readonly')
        self.cmbreport.grid(row=1,column=1,padx=50,pady=50)
        self.cmbreport.current(0)
       
        self.frame2=tb.Frame(self.root)
        self.frame2.place(x=0, y=200)

        self.lblfield=tb.Label(self.frame2,text="Field Name",bootstyle="daner")
        self.lblfield.grid(row=1,column=0,padx=50,pady=50)

        self.lblcondition=tb.Label(self.frame2,text="Condition",bootstyle="daner")
        self.lblcondition.grid(row=1,column=1,padx=100,pady=50)

        self.lblvalue=tb.Label(self.frame2,text="Value",bootstyle="daner")
        self.lblvalue.grid(row=1,column=2,padx=150,pady=50)


       

        columns = [
            {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
            {'name': 'age', 'label': 'Age', 'field': 'age', 'sortable': True},
        ]
        rows = [
            {'name': 'Alice', 'age': 18},
            {'name': 'Bob', 'age': 21},
            {'name': 'Carol'},
        ]
        ui.table(columns=columns, rows=rows, row_key='name')

        ui.run()

        
        
        










if __name__=="__main__":    
    root=tb.Window(themename="superhero")
    obj=CustomerPrint(root)
    root.mainloop()