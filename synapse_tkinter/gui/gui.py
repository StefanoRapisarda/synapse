import tkinter as tk
from tkinter import ttk

from utilities import *
from entries import *

class EntryPanel(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.title("Main Window")
        self.entry_panel_index = 1

        frame = tk.Frame(self)
        frame.grid(column=0,row=0,sticky='nswe')

        labelframe = tk.LabelFrame(frame,text='Choose an option')
        labelframe.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')

        entry_panel_b = tk.Button(labelframe,text='New Entry Panel',width=15,height=3,
        command=self._new_entry_panel)
        entry_panel_b.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')

        edit_panel_b = tk.Button(labelframe,text='Edit Panel',width=15,height=3,
        command=self._new_edit_panel)
        edit_panel_b.grid(column=1,row=0,padx=5,pady=5,sticky='nswe')

    def _new_entry_panel(self):
        # Show a Write Entry panel
        new = tk.Toplevel(self)
        new.title("Entry panel {}".format(self.entry_panel_index))
        WriteEntry(new,self)        
        self.entry_panel_index += 1

    def _new_edit_panel(self):
        new = tk.Toplevel(self)
        new.title("Edit panel")
        EditEntry(new,self)        

 

class WriteEntry:

    def __init__(self,root,controller):

        self.root = root
        self.controller = controller

        self.frame = tk.Frame(self.root)
        self.frame.grid(column=0,row=0,sticky='nswe')

        frame1 = tk.LabelFrame(self.frame,text='Your content goes here')
        frame1.grid(column=0,row=1,padx=5,pady=5,sticky='nswe')

        self.text = tk.Text(frame1,width=124,height=10)
        self.text.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')

        frame2 = tk.LabelFrame(self.frame,text='Your review goes here')
        frame2.grid(column=0,row=2,padx=5,pady=5,sticky='nswe')

        self.review = tk.Text(frame2,width=124,height=10)
        self.review.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')

        self.categories = []
        self.activities = []

        self._entries1()
        self._custom_field_panel()
        self._low_buttons()

        self._update_attributes()

    def _low_buttons(self):
        frame = tk.LabelFrame(self.root,text='Edit Buttons')
        frame.grid(column=0,row=3,padx=5,pady=5,sticky='nswe')

        add_button = tk.Button(frame,text='Add Entry',width=15,height=3,
        command=self._add_entry)
        add_button.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')  

        review_button = tk.Button(frame,text='Review Entry',width=15,height=3,
        command=self._review_entry)
        review_button.grid(column=1,row=0,padx=5,pady=5,sticky='nswe')        

    def _custom_field_panel(self):
        # Variables
        self.custom_fields = {}

        self.field_panel = tk.Toplevel(self.root)
        self.field_panel.title('Entry panel {}'.format(self.controller.entry_panel_index))
        
        frame = tk.Frame(self.field_panel)
        frame.grid(column=0,row=0,sticky='nswe')

        box = tk.LabelFrame(frame,text='Custom Field')
        box.grid(column=0,row=0,padx=5,pady=5,sticky='nwe')

        self.fields_to_show = ttk.Combobox(box,values=list(self.custom_fields.keys()),width=29)
        self.fields_to_show.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')

        add_button = tk.Button(box,text='+',width=3,command=lambda: self._add_custom_field(str(self.fields_to_show.get())))
        add_button.grid(column=1,row=0,padx=5,pady=5,sticky='nswe')

        #del_button = tk.Button(box,text='-',width=3,command=lambda: self._pm_custom_field('del'))
        #del_button.grid(column=1,row=0,padx=5,pady=5,sticky='nswe')

        hist_button = tk.Button(box,text='Load Most Recent',width=3,command=self._load_recent_fields)
        hist_button.grid(column=0,row=1,padx=5,pady=5,columnspan=2,sticky='nswe')

    def _load_recent_fields(self):
        ids = list_entry_ids()
        tmp = list_field(ids,'custom_fields')
        if len(tmp) != 0:
            self.fields_to_show['values']=tmp
            self.fields_to_show.current(0)
        else:
            self.fields_to_show['values']=0           
        self._update_attributes()

    def _add_custom_field(self,field_name):

        if field_name != '':
            
            # Checking if a box with the field name already exists in the panel
            flag = False
            for field in self.field_panel.winfo_children():
                if hasattr(field,'tag'):
                    if field.tag == field_name: flag = True
            
            # Creating a new box for the new field
            if not flag:

                # Initializing the self.custom_fields dictionary
                self.custom_fields[field_name] = [tk.StringVar(),'']
                
                box = tk.LabelFrame(self.field_panel,text=field_name)
                box.tag = field_name
                box.grid(column=0,row=len(self.custom_fields)+1,padx=5,pady=5,sticky='nwe')

                #var.trace_add('write', self._update_var(key))
                entry = tk.Entry(box,textvariable=self.custom_fields[box.tag][0],width=30,
                validate='focusout',validatecommand=lambda: self._update_var(box.tag))
                entry.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')  
                self.custom_fields[field_name][1]=entry 

                del_button = tk.Button(box,width=3,text='-',command=lambda: self._del_custom_field(box.tag))
                del_button.grid(column=1,row=0,padx=5,pady=5,sticky='nswe') 

                # Updating fields to show
                self.fields_to_show['values']=list(self.custom_fields.keys())
                self.fields_to_show.current(0)

    def _del_custom_field(self,key):
        for field in self.field_panel.winfo_children():
            if hasattr(field,'tag'):
                if field.tag == key: field.destroy() 
        del self.custom_fields[key]
        if len(list(self.custom_fields.keys())) != 0:
            self.fields_to_show['values']=list(self.custom_fields.keys())           
        else:
            self.fields_to_show['values'] = ['']
        self.fields_to_show.current(0)

    def _update_var(self,key):
        self.custom_fields[key][0].set(str(self.custom_fields[key][1].get()))

    def _update_attributes(self):
        ids = list_entry_ids()
        self.categories = list_field(ids,'category')
        self.activities = list_field(ids,'activity')
        self.combo1['values'] = self.categories
        self.combo2['values'] = self.activities

    def _head_buttons(self):
        
        frame = tk.Frame(self.frame)
        frame.grid(column=0,row=0,sticky='nwe')

        add_button = tk.Button(frame,text='Add Entry',command=self._add_entry)
        add_button.grid(column=0,row=0,padx=5,pady=5,sticky='nws')   

    def _review_entry(self):
        custom_fields = {}
        for key,value in self.custom_fields.items():
            if value != '':
                custom_fields[key] = str(value[0].get())
        id, entry = create_entry(content = str(self.text.get(1.0,tk.END)),
                                 author = str(self.author.get()),
                                 place = str(self.place.get()),
                                 category = str(self.combo1.get()),
                                 activity = str(self.combo2.get()),
                                 custom_fields = custom_fields)
        self.review.delete(1.0,tk.END)
        for key,value in entry.items():      
            string = '{}: {}\n'.format(key,value)
            self.review.insert(tk.END,string)


    def _add_entry(self):
        custom_fields = {}
        for key,value in self.custom_fields.items():
            if value != '':
                custom_fields[key] = str(value[0].get())
        id, entry = create_entry(content = str(self.text.get(1.0,tk.END)),
                                 author = str(self.author.get()),
                                 place = str(self.place.get()),
                                 category = str(self.combo1.get()),
                                 activity = str(self.combo2.get()),
                                 custom_fields = custom_fields)
        save_entry(id,entry)
        self._update_attributes()

    def _entries1(self):

        frame = tk.Frame(self.frame)
        frame.grid(column=0,row=0,sticky='nwe')

        box1 = tk.LabelFrame(frame,text='Author')
        box1.grid(column=0,row=0,padx=5,pady=5,sticky='new')

        self.author = tk.StringVar()
        self.author.set('Stefano Rapisarda')
        entry1 = tk.Entry(box1,textvariable=self.author)
        entry1.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')

        box2 = tk.LabelFrame(frame,text='Place')
        box2.grid(column=1,row=0,padx=5,pady=6,sticky='new')

        self.place = tk.StringVar()
        self.place.set('Uppsala (Sweden)')
        entry2 = tk.Entry(box2,textvariable=self.place)
        entry2.grid(column=0,row=0,padx=5,pady=5,sticky='nswe') 

        box3 = tk.LabelFrame(frame,text='Category')
        box3.grid(column=2,row=0,padx=5,pady=5,sticky='new')

        self.combo1 = ttk.Combobox(box3,values=self.categories)
        self.combo1.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')

        box4 = tk.LabelFrame(frame,text='Activity')
        box4.grid(column=3,row=0,padx=5,pady=6,sticky='new')

        self.combo2 = ttk.Combobox(box4,values=self.activities)
        self.combo2.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')   

class EditEntry:

    def __init__(self,root,controller):

        self.root = root
        self.controller = controller

        self.frame = tk.Frame(self.root)
        self.frame.grid(column=0,row=0,sticky='nswe')

        self._entry_panels()
        self._link_panel()
        self._text_panels()

    def _link_panel(self):
        link_frame = tk.Frame(self.frame)
        link_frame.grid(column=1,row=0,sticky='we')

        button_box = tk.LabelFrame(link_frame,text='links')
        button_box.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')

        make_button = tk.Button(button_box,text='make')
        make_button.grid(column=0,row=0,sticky='nswe')

        remove_button = tk.Button(button_box,text='remove')
        remove_button.grid(column=0,row=1,sticky='nswe') 

        show_button = tk.Button(button_box,text='show')
        show_button.grid(column=0,row=2,sticky='nswe')

        edit_button = tk.Button(button_box,text='edit')
        edit_button.grid(column=0,row=3,sticky='nswe')               

    def _entry_panels(self):

        columns = ('date','category','subject','activity','links')
        col_width = [200,100,100,100,50]

        # Left side
        # ===================================================================
        entries_left_frame = tk.Frame(self.frame)
        entries_left_frame.grid(column=0,row=0,sticky='nswe')

        button_bar_left = tk.Frame(entries_left_frame)
        button_bar_left.grid(column=0,row=0,sticky='nswe')
        # ---
        search_field_box1 = tk.LabelFrame(button_bar_left,text='Search Field')
        search_field_box1.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')
        entry_field1 = tk.Entry(search_field_box1)
        entry_field1.grid(column=0,row=0,sticky='nswe')
        button_field1 = tk.Button(search_field_box1,text='#',width=3,height=2)
        button_field1 .grid(column=1,row=0,sticky='nswe')
        # ---
        search_text_box1 = tk.LabelFrame(button_bar_left,text='Search text')
        search_text_box1.grid(column=1,row=0,padx=5,pady=5,sticky='nswe')  
        entry_text1 = tk.Entry(search_text_box1)
        entry_text1.grid(column=0,row=0,sticky='nswe')
        button_text1 = tk.Button(search_text_box1,text='#',width=3,height=2)
        button_text1 .grid(column=1,row=0,sticky='nswe')    
        # --
         
        entry_box_left = tk.LabelFrame(entries_left_frame,text='Entries')
        entry_box_left.grid(column=0,row=1,padx=5,pady=5,sticky='nswe') 
        self.entries_left = ttk.Treeview(entry_box_left, columns=columns,show='headings')
        self.entries_left.grid(column=0,row=0,sticky='nswe')
        for c in range(len(columns)):
            self.entries_left.column(columns[c],width=col_width[c])
            self.entries_left.heading(columns[c],text=columns[c],
            command=lambda _col=columns[c]: self._sort_column(self.entries_left,_col,False))
        #self.entries_left.heading('1',text='date')
        #self.entries_left.heading('2',text='category')
        #self.entries_left.heading('3',text='subject')
        #self.entries_left.heading('4',text='activity')
        #self.entries_left.heading('5',text='links')     

        self._dummy_print_entry('left')
        # ===================================================================

        # Right side 
        # ===================================================================
        entries_right_frame = tk.Frame(self.frame)
        entries_right_frame.grid(column=2,row=0,sticky='nswe')

        button_bar_right = tk.Frame(entries_right_frame)
        button_bar_right.grid(column=0,row=0,sticky='nswe')
        # --
        search_field_box3 = tk.LabelFrame(button_bar_right,text='Search Field')
        search_field_box3.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')
        entry_field3 = tk.Entry(search_field_box3)
        entry_field3.grid(column=0,row=0,sticky='nswe')
        button_field3 = tk.Button(search_field_box3,text='#',width=2,height=2)
        button_field3 .grid(column=1,row=0,sticky='nswe')
        # --
        search_text_box4 = tk.LabelFrame(button_bar_right,text='Search text')
        search_text_box4.grid(column=1,row=0,padx=5,pady=5,sticky='nswe')     
        entry_text4 = tk.Entry(search_text_box4)
        entry_text4.grid(column=0,row=0,sticky='nswe')          
        button_text4 = tk.Button(search_text_box4,text='#',width=2,height=2)
        button_text4 .grid(column=1,row=0,sticky='nswe')  
        # --

        entry_box_right = tk.LabelFrame(entries_right_frame,text='Entries')
        entry_box_right.grid(column=0,row=1,padx=5,pady=5,sticky='nswe')
        self.entries_right = ttk.Treeview(entry_box_right)
        self.entries_right.grid(column=0,row=0,sticky='nswe')
        self.entries_right['columns'] = ('1','2','3','4','5')
        self.entries_right['show'] = 'headings'
        self.entries_right.column('1',width=200)
        self.entries_right.column('2',width=100)
        self.entries_right.column('3',width=100)
        self.entries_right.column('4',width=100)
        self.entries_right.column('5',width=50)
        self.entries_right.heading('1',text='date')
        self.entries_right.heading('2',text='category')
        self.entries_right.heading('3',text='subject')
        self.entries_right.heading('4',text='activity')
        self.entries_right.heading('5',text='links')     

        self._dummy_print_entry('right')

    def _dummy_print_entry(self,opt):
        lines = read_entries(['creation_date','category','subject','activity','links'])
        counter=0
        if opt=='left':
            tree = self.entries_left
        elif opt=='right':
            tree = self.entries_right
        for line in lines:
            tree.insert('','end',text=str(counter),values=line)
            counter+=1

    def _sort_column(self,tree,col,reverse):
        l = [(tree.set(k,col),k) for k in tree.get_children('')]
        l.sort(reverse=reverse)

        for index, (val,k) in enumerate(l):
            tree.move(k,'',index)

        tree.heading(col, command=lambda: self._sort_column(tree,col,not reverse))

    def _text_panels(self):
        frame = tk.Frame(self.frame)
        frame.grid(column=0,row=1,columnspan=3,sticky='nswe')

        left_text_box = tk.LabelFrame(frame,text='Text')
        left_text_box.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')

        right_text_box = tk.LabelFrame(frame,text='Text')
        right_text_box.grid(column=1,row=0,padx=5,pady=5,sticky='nswe')      

        left_info_box = tk.LabelFrame(frame,text='Info')
        left_info_box.grid(column=0,row=1,padx=5,pady=5,sticky='nswe')

        right_info_box = tk.LabelFrame(frame,text='Info')
        right_info_box.grid(column=1,row=1,padx=5,pady=5,sticky='nswe')   

if __name__ == '__main__':
    app = EntryPanel()
    app.mainloop()