import tkinter as tk 
from tkinter import ttk 
from PIL import ImageTk, Image 

# The containers do not need to be class attributes
# Widget to be initialized must be class attributes

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        #self.image1 = ImageTk.PhotoImage(Image.open(
        #    '../pictures/synapse2.jpeg'))

        left_frame = tk.Frame(self)
        left_frame.grid(row=0,column=0,rowspan=2,padx=5,pady=5,sticky='nsw')
        self._init_left_frame(left_frame)

        middle_upper_panel = tk.Frame(self)
        middle_upper_panel.grid(row=0,column=1,padx=5,pady=5,sticky='nwse')
        self._init_middle_upper_panel(middle_upper_panel)

        middle_lower_panel = tk.Frame(self)
        middle_lower_panel.grid(row=1,column=1,padx=5,pady=5,sticky='nwse')  
        middle_lower_panel.columnconfigure(0, weight=1)
        middle_lower_panel.columnconfigure(1, weight=1)
        self._init_middle_lower_panel(middle_lower_panel)     

        right_frame = tk.Frame(self)
        right_frame.grid(row=0,column=2,rowspan=2,padx=5,pady=5,sticky='nse')  
        self._init_right_frame(right_frame)  

    def _init_middle_upper_panel(self,parent):

        # Central link box
        # ----------------------------------------------------------------------------

        link_box = tk.LabelFrame(parent,text='links')
        link_box.grid(row=0,column=1,rowspan=2,padx=5,pady=5,sticky='we')   

        button_width = 10
        self.panel_link_button = tk.Button(link_box,text='open panel',width=button_width)
        self.panel_link_button.grid(row=0,column=0,padx=5,pady=5,sticky='nswe')

        box_show_buttons = tk.LabelFrame(link_box,text='show',labelanchor='n')
        box_show_buttons.grid(row=1,column=0,padx=5,pady=5,sticky='nswe')
        self.show_link_button_left = tk.Button(box_show_buttons,text='-->',width=5,height=2)
        self.show_link_button_left.grid(row=0,column=1,sticky='we')
        self.show_link_button_right = tk.Button(box_show_buttons,text='<--',width=5,height=2)
        self.show_link_button_right.grid(row=0,column=0,sticky='we')

        #self.refresh_link_button = tk.Button(link_box,text='refresh',width=button_width)
        #self.refresh_link_button.grid(row=2,column=0,padx=5,pady=5,sticky='nswe')

        self.remove_link_button = tk.Button(link_box,text='remove',width=button_width)
        self.remove_link_button.grid(row=2,column=0,padx=5,pady=5,sticky='nswe')

        # ----------------------------------------------------------------------------

        # Left frame
        # ----------------------------------------------------------------------------

        frame_left = tk.Frame(parent)
        frame_left.grid(row=0,column=0,padx=(0,0),sticky='nswe')    

        # Top research buttons
        search_box_left = tk.Frame(frame_left)
        search_box_left.grid(row=0,column=0,sticky='nsew')

        search_field_left_box = tk.LabelFrame(search_box_left,text='search field')
        search_field_left_box.grid(row=0,column=0,sticky='nsew')

        self.field_to_search_left = tk.StringVar()
        self.field_to_search_left.set('')
        entry_search_field_box = tk.Entry(search_field_left_box,width=15,
                                 textvariable=self.field_to_search_left)
        entry_search_field_box.grid(row=0,column=0,sticky='nsew')

        self.search_field_button_left = tk.Button(search_field_left_box,text='#',width=2,height=2)
        self.search_field_button_left.grid(row=0,column=1,sticky='nsew')

        search_text_left_box = tk.LabelFrame(search_box_left,text='search text')
        search_text_left_box.grid(row=0,column=1,sticky='nsew')

        self.text_to_search_left = tk.StringVar()
        self.text_to_search_left.set('')
        entry_search_text_box = tk.Entry(search_text_left_box,width=15,
                                         textvariable=self.text_to_search_left)
        entry_search_text_box.grid(row=0,column=0,padx=1,sticky='nsew')

        self.search_text_button_left = tk.Button(search_text_left_box,text='#',width=2,height=2)
        self.search_text_button_left.grid(row=0,column=1,sticky='nsew')  

        # Edit buttons
        edit_box_left = tk.Frame(frame_left)
        edit_box_left.grid(row=1,column=0,pady=5,sticky='nsew')

        edit_entry_box = tk.LabelFrame(edit_box_left,text='Entry Edit Options')
        edit_entry_box.grid(row=0,column=0,sticky='nswe')        

        width_edit_button = 10
        self.reset_entry_button_left = tk.Button(edit_entry_box,text='reset',width=width_edit_button)
        self.reset_entry_button_left.grid(row=0,column=2,padx=1,sticky='nswe')
        self.edit_entry_button_left = tk.Button(edit_entry_box,text='edit',width=width_edit_button)
        self.edit_entry_button_left.grid(row=0,column=1,padx=1,sticky='nswe')
        self.create_entry_button_left = tk.Button(edit_entry_box,text='create',width=width_edit_button)
        self.create_entry_button_left.grid(row=0,column=0,padx=1,sticky='nswe')
        self.delete_entry_button_left = tk.Button(edit_entry_box,text='delete',width=width_edit_button)
        self.delete_entry_button_left.grid(row=0,column=3,padx=1,sticky='nswe')     

        # Entry List
        box_left = tk.Frame(frame_left)
        entry_label_left = tk.Label(box_left,text='Entries')
        entry_label_left.grid(row=0,column=0,sticky='nswe')
        self.refresh_button_left = tk.Button(box_left,text='refresh')
        self.refresh_button_left.grid(row=0,column=1,sticky='nswe')

        entry_box_left = tk.LabelFrame(frame_left,labelwidget=box_left)   
        entry_box_left.grid(column=0,row=2,sticky='nswe')

        self.entries_left = ttk.Treeview(entry_box_left,height=12,selectmode='extended')
        self.entries_left.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')
        
        ysb_left = ttk.Scrollbar(entry_box_left,orient='vertical',command = self.entries_left.yview)
        ysb_left.grid(row=0,column=1,sticky='nse')
        xsb_left = ttk.Scrollbar(entry_box_left,orient='horizontal',command = self.entries_left.xview)
        xsb_left.grid(row=1,column=0,sticky='we')

        self.entries_left.configure(yscrollcommand=lambda f, l:self.autoscroll(ysb_left,f,l), 
                                    xscrollcommand=lambda f, l:self.autoscroll(xsb_left,f,l))
        # ----------------------------------------------------------------------------

        # Right frame
        # ----------------------------------------------------------------------------
        frame_right = tk.Frame(parent)
        frame_right.grid(row=0,column=2,padx=(0,0),sticky='nswe')   

        # Search buttons
        search_box_right = tk.Frame(frame_right)
        search_box_right.grid(row=0,column=0,sticky='nsew')

        search_field_right_box = tk.LabelFrame(search_box_right,text='search field')
        search_field_right_box.grid(row=0,column=0,sticky='nsew')

        self.field_to_search_right = tk.StringVar()
        self.field_to_search_right.set('')
        entry_search_field_box = tk.Entry(search_field_right_box,width=15,
                                          textvariable=self.field_to_search_right)
        entry_search_field_box.grid(row=0,column=0,sticky='nsew')

        self.search_field_button_right = tk.Button(search_field_right_box,text='#',width=1,height=2)
        self.search_field_button_right.grid(row=0,column=1,sticky='nsew')

        search_text_right_box = tk.LabelFrame(search_box_right,text='search text')
        search_text_right_box.grid(row=0,column=1,sticky='nsew')

        self.text_to_search_right = tk.StringVar()
        self.text_to_search_right.set('')
        entry_search_text_box = tk.Entry(search_text_right_box,width=15,
                                         textvariable=self.text_to_search_right)
        entry_search_text_box.grid(row=0,column=0,sticky='nsew')

        self.search_text_button_right = tk.Button(search_text_right_box,text='#',width=1,height=2)
        self.search_text_button_right.grid(row=0,column=1,sticky='nsew') 

        # Edit buttons
        edit_box_right = tk.Frame(frame_right)
        edit_box_right.grid(row=1,column=0,pady=5,sticky='nsew')

        edit_entry_box = tk.LabelFrame(edit_box_right,text='Entry Edit Options')
        edit_entry_box.grid(row=0,column=0,sticky='nswe')        

        width_edit_button = 10
        self.reset_entry_button_right = tk.Button(edit_entry_box,text='reset',width=width_edit_button)
        self.reset_entry_button_right.grid(row=0,column=2,padx=1,sticky='nswe')
        self.edit_entry_button_right = tk.Button(edit_entry_box,text='edit',width=width_edit_button)
        self.edit_entry_button_right.grid(row=0,column=1,padx=1,sticky='nswe')
        self.create_entry_button_right = tk.Button(edit_entry_box,text='create',width=width_edit_button)
        self.create_entry_button_right.grid(row=0,column=0,padx=1,sticky='nswe')
        self.delete_entry_button_right = tk.Button(edit_entry_box,text='delete',width=width_edit_button)
        self.delete_entry_button_right.grid(row=0,column=3,padx=1,sticky='nswe')    

        # Entry list
        box_right = tk.Frame(frame_right)
        entry_label_right = tk.Label(box_right,text='Entries')
        entry_label_right.grid(row=0,column=0,sticky='nswe')
        self.refresh_button_right = tk.Button(box_right,text='refresh')
        self.refresh_button_right.grid(row=0,column=1,sticky='nswe')

        entry_box_right = tk.LabelFrame(frame_right,labelwidget=box_right)   
        entry_box_right.grid(column=0,row=2,sticky='nswe')

        self.entries_right = ttk.Treeview(entry_box_right,height=12,selectmode='extended')
        self.entries_right.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')

        ysb_right = ttk.Scrollbar(entry_box_right,orient='vertical',command = self.entries_right.yview)
        ysb_right.grid(row=0,column=1,sticky='ns')
        xsb_right = ttk.Scrollbar(entry_box_right,orient='horizontal',command = self.entries_right.xview)
        xsb_right.grid(row=1,column=0,sticky='we')

        self.entries_right.configure(yscrollcommand=lambda f, l:self.autoscroll(ysb_right,f,l), 
                                    xscrollcommand=lambda f, l:self.autoscroll(xsb_right,f,l))
        # ----------------------------------------------------------------------------

    def _open_new_window(self,NewWindow):
        new = tk.Toplevel(self)
        NewWindow(new,self)

    def autoscroll(self, sbar, first, last):
        """Hide and show scrollbar as needed."""
        first, last = float(first), float(last)
        if first <= 0 and last >= 1:
            sbar.grid_remove()
        else:
            sbar.grid()
        sbar.set(first, last)

    def _init_middle_lower_panel(self,parent):

        width_panel = 58
        height_text = 8
        width_entries = 17

        # Left Frame
        # ----------------------------------------------------------------------------

        # Text box
        box_left = tk.Frame(parent)
        label_left = tk.Label(box_left,text='Text')
        label_left.grid(row=0,column=0,sticky='nswe')
        button_left = tk.Button(box_left,text='clear',
                        command=lambda: self._clean_text('left'))
        button_left.grid(row=0,column=1,sticky='nswe')
        text_box_left = tk.LabelFrame(parent,labelwidget=box_left)
        text_box_left.grid(column=0,row=0,sticky='nsw')
        self.text_left = tk.Text(text_box_left,width=width_panel,height=height_text)
        self.text_left.grid(column=0,row=0,sticky='nsw')

        # Standard Field box
        box_left = tk.Frame(parent)
        label_left = tk.Label(box_left,text='Standard Fields')
        label_left.grid(row=0,column=0,sticky='nswe')
        #label_left.image = self.image1
        button_left = tk.Button(box_left,text='clear',
                        command=lambda: self._clean_standard_fields('left'))
        button_left.grid(row=0,column=1,sticky='nswe')
        other_fields_box_left = tk.LabelFrame(parent,labelwidget=box_left)
        other_fields_box_left.grid(column=0,row=1,pady=5,sticky='nsw')

        ## Author box
        author_box_left = tk.LabelFrame(other_fields_box_left,text='author')
        author_box_left.grid(column=0,row=0,padx=5,pady=5,sticky='nsew')
        self.author_var_left = tk.StringVar()
        self.author_var_left.set('')
        author_entry_left = tk.Entry(author_box_left,width=width_entries,textvariable=self.author_var_left)
        author_entry_left.grid(column=0,row=0,padx=5,pady=5,sticky='nsew')

        ## Place box
        place_box_left = tk.LabelFrame(other_fields_box_left,text='place')
        place_box_left.grid(column=1,row=0,padx=5,pady=5,sticky='nsew')
        self.place_var_left = tk.StringVar()
        self.place_var_left.set('')       
        place_entry_left = tk.Entry(place_box_left,width=width_entries,textvariable=self.place_var_left)
        place_entry_left.grid(column=1,row=0,padx=5,pady=5,sticky='nsew')        

        ## Category box
        category_box_left = tk.LabelFrame(other_fields_box_left,text='category')
        category_box_left.grid(column=0,row=1,padx=5,pady=5,sticky='nsew')
        self.category_entry_left = ttk.Combobox(category_box_left,width=width_entries)
        self.category_entry_left.grid(column=0,row=0,padx=5,pady=5,sticky='nsew')

        ## Activity box
        activity_box_left = tk.LabelFrame(other_fields_box_left,text='activity')
        activity_box_left.grid(column=1,row=1,padx=5,pady=5,sticky='nsew')
        self.activity_entry_left = ttk.Combobox(activity_box_left,width=width_entries)
        self.activity_entry_left.grid(column=0,row=0,padx=5,pady=5,sticky='nsew')

        ## Subject box
        subject_box_left = tk.LabelFrame(other_fields_box_left,text='subject')
        subject_box_left.grid(column=0,row=2,padx=5,pady=5,sticky='nsew')
        self.subject_entry_left = ttk.Combobox(subject_box_left,width=width_entries)
        self.subject_entry_left.grid(column=0,row=0,padx=5,pady=5,sticky='nsew')

        ## Collection box
        collection_box_left = tk.LabelFrame(other_fields_box_left,text='collection')
        collection_box_left.grid(column=1,row=2,padx=5,pady=5,sticky='nsew')
        self.collection_entry_left = ttk.Combobox(collection_box_left,width=width_entries)
        self.collection_entry_left.grid(column=0,row=0,padx=5,pady=5,sticky='nsew')

        # ----------------------------------------------------------------------------

        # Right Frame
        # ----------------------------------------------------------------------------

        box_right= tk.Frame(parent)

        # Text box
        label_right = tk.Label(box_right,text='Text')
        label_right.grid(row=0,column=0,sticky='nswe')
        button_right = tk.Button(box_right,text='clear',
                        command=lambda: self._clean_text('right'))
        button_right.grid(row=0,column=1,sticky='nswe')
        text_box_right = tk.LabelFrame(parent,labelwidget=box_right)
        text_box_right.grid(column=1,row=0,sticky='nse')
        self.text_right = tk.Text(text_box_right,width=width_panel,height=height_text)
        self.text_right.grid(column=0,row=0,sticky='nse')

        # Standard Field Box
        box_right = tk.Frame(parent)
        label_right = tk.Label(box_right,text='Standard Fields')
        label_right.grid(row=0,column=0,sticky='nswe')
        button_right = tk.Button(box_right,text='clear',
                        command=lambda: self._clean_standard_fields('right'))
        button_right.grid(row=0,column=1,sticky='nswe')
        other_fields_box_right = tk.LabelFrame(parent,labelwidget=box_right)
        other_fields_box_right.grid(column=1,row=1,pady=5,sticky='nse')   

        ## Author box
        author_box_right = tk.LabelFrame(other_fields_box_right,text='author')
        author_box_right.grid(column=0,row=0,padx=5,pady=5,sticky='nsew')
        self.author_var_right = tk.StringVar()
        self.author_var_right.set('')
        author_entry_right = tk.Entry(author_box_right,width=width_entries,textvariable=self.author_var_right)
        author_entry_right.grid(column=0,row=0,padx=5,pady=5,sticky='nsew')

        ## Place box
        place_box_right = tk.LabelFrame(other_fields_box_right,text='place')
        place_box_right.grid(column=1,row=0,padx=5,pady=5,sticky='nsew')
        self.place_var_right = tk.StringVar()
        self.place_var_right.set('')
        place_entry_right = tk.Entry(place_box_right,width=width_entries,textvariable=self.place_var_right)
        place_entry_right.grid(column=1,row=0,padx=5,pady=5,sticky='nsew')        

        ## Category box
        category_box_right = tk.LabelFrame(other_fields_box_right,text='category')
        category_box_right.grid(column=0,row=1,padx=5,pady=5,sticky='nsew')
        self.category_entry_right = ttk.Combobox(category_box_right,width=width_entries)
        self.category_entry_right.grid(column=0,row=0,padx=5,pady=5,sticky='nsew')

        ## Activity box
        activity_box_right = tk.LabelFrame(other_fields_box_right,text='activity')
        activity_box_right.grid(column=1,row=1,padx=5,pady=5,sticky='nsew')
        self.activity_entry_right = ttk.Combobox(activity_box_right,width=width_entries)
        self.activity_entry_right.grid(column=0,row=0,padx=5,pady=5,sticky='nsew')

        ## Subject box
        subject_box_right = tk.LabelFrame(other_fields_box_right,text='subject')
        subject_box_right.grid(column=0,row=2,padx=5,pady=5,sticky='nsew')
        self.subject_entry_right = ttk.Combobox(subject_box_right,width=width_entries)
        self.subject_entry_right.grid(column=0,row=0,padx=5,pady=5,sticky='nsew')

        ## Collection box
        collection_box_right = tk.LabelFrame(other_fields_box_right,text='collection')
        collection_box_right.grid(column=1,row=2,padx=5,pady=5,sticky='nsew')
        self.collection_entry_right = ttk.Combobox(collection_box_right,width=width_entries)
        self.collection_entry_right.grid(column=0,row=0,padx=5,pady=5,sticky='nsew')
        # ----------------------------------------------------------------------------


    def _init_left_frame(self,parent):

        add_fields_box = tk.LabelFrame(parent,text='Add Field')
        add_fields_box.grid(row=0,column=0,padx=5,pady=5,sticky='nswe')

        self.fields_combobox_left = ttk.Combobox(add_fields_box,width=18)
        self.fields_combobox_left.grid(row=0,column=0,padx=5,pady=5,sticky='nswe')

        self.add_field_button_left = tk.Button(add_fields_box,text='+',width=3)
        self.add_field_button_left.grid(row=0,column=1,padx=5,pady=5,sticky='nswe')
        self.add_field_button_left.config(command=self._add_left_field_box)

        box = tk.Frame(parent)
        label = tk.Label(box,text='Custom Fields')
        label.grid(row=0,column=0,sticky='nswe')
        button = tk.Button(box,text='clear',
                        command=lambda: self._clean_custom_fields('left'))
        button.grid(row=0,column=1,sticky='nswe')
        self.fields_box_left = tk.LabelFrame(parent,labelwidget=box)
        self.fields_box_left.grid(row=1,column=0,padx=5,pady=5,sticky='nswe')

        self.fields_canvas_left = tk.Canvas(self.fields_box_left,borderwidth=0,background='#ffffff',
        height=675,width=220)
        self.fields_canvas_left.grid(row=0,column=0,sticky='nswe')

        self.inner_fields_frame_left = tk.Frame(self.fields_canvas_left,background='#ffffff') 
        self.inner_fields_frame_left.grid(row=0,column=0,sticky='nswe')
        self.inner_fields_frame_left.bind("<Configure>", self.on_frame_configure_left)
        vsb = ttk.Scrollbar(self.fields_box_left, orient='vertical', command=self.fields_canvas_left.yview)
        vsb.grid(row=0,column=1,sticky='nse')
        self.fields_canvas_left.configure(yscrollcommand=vsb.set)
        self.fields_canvas_left.create_window((4,4),window=self.inner_fields_frame_left,anchor='nw',tags='fields_box')

    def _add_left_field_box(self,index=None,field_name=None,field_value=None):

        row = len(self.inner_fields_frame_left.winfo_children())

        label_var = tk.StringVar()
        if not field_name is None: label_var.set(field_name)

        mini_entry = tk.Entry(self.inner_fields_frame_left,width=8,textvariable=label_var)   
        
        box = tk.LabelFrame(self.inner_fields_frame_left,labelwidget=mini_entry)
        box.grid(column=0,row=row,padx=5,pady=5,sticky='nwe')

        entry_var = tk.StringVar()
        if not field_value is None: entry_var.set(field_value)

        entry = tk.Entry(box,width=15,textvariable=entry_var)
        entry.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')  

        button = tk.Button(box,width=3,text='-',command=box.destroy)
        button.grid(column=1,row=0,padx=5,pady=5,sticky='nswe') 

        box.label = 'box'
        box.field = label_var
        box.value = entry_var

    def on_frame_configure_left(self, event):
        self.fields_canvas_left.configure(scrollregion=self.fields_canvas_left.bbox('all'))


    def _init_right_frame(self,parent):

        add_fields_box = tk.LabelFrame(parent,text='Add Field')
        add_fields_box.grid(row=0,column=0,padx=5,pady=5,sticky='nswe')

        self.fields_combobox_right = ttk.Combobox(add_fields_box,width=18)
        self.fields_combobox_right.grid(row=0,column=0,padx=5,pady=5,sticky='nswe')

        self.add_field_button_right = tk.Button(add_fields_box,text='+',width=3)
        self.add_field_button_right.grid(row=0,column=1,padx=5,pady=5,sticky='nswe')
        self.add_field_button_right.config(command=self._add_right_field_box)

        box = tk.Frame(parent)
        label = tk.Label(box,text='Custom Fields')
        label.grid(row=0,column=0,sticky='nswe')
        button = tk.Button(box,text='clear',
                        command=lambda: self._clean_custom_fields('right'))
        button.grid(row=0,column=1,sticky='nswe')
        self.fields_box_right = tk.LabelFrame(parent,labelwidget=box)
        self.fields_box_right.grid(row=1,column=0,padx=5,pady=5,sticky='nswe')
        self.displayed_fields_right = {}

        self.fields_canvas_right = tk.Canvas(self.fields_box_right,borderwidth=0,background='#ffffff',
        height=675,width=220)
        self.fields_canvas_right.grid(row=0,column=0,sticky='nswe')

        self.inner_fields_frame_right = tk.Frame(self.fields_canvas_right,background='#ffffff') 
        self.inner_fields_frame_right.grid(row=0,column=0,sticky='nswe')
        self.inner_fields_frame_right.bind("<Configure>", self.on_frame_configure_right)
        vsb = ttk.Scrollbar(self.fields_box_right, orient='vertical', command=self.fields_canvas_right.yview)
        vsb.grid(row=0,column=1,sticky='nse')
        self.fields_canvas_right.configure(yscrollcommand=vsb.set)
        self.fields_canvas_right.create_window((4,4),window=self.inner_fields_frame_right,anchor='nw',tags='fields_box')

    def _add_right_field_box(self,field_name=None,field_value=None):

        row = len(self.inner_fields_frame_right.winfo_children())

        label_var = tk.StringVar()
        if not field_name is None: label_var.set(field_name)

        mini_entry = tk.Entry(self.inner_fields_frame_right,width=8,textvariable=label_var)   
        
        box = tk.LabelFrame(self.inner_fields_frame_right,labelwidget=mini_entry)
        box.grid(column=0,row=row,padx=5,pady=5,sticky='nwe')

        entry_var = tk.StringVar()
        if not field_value is None: entry_var.set(field_value)

        entry = tk.Entry(box,width=15,textvariable=entry_var)
        entry.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')  

        button = tk.Button(box,width=3,text='-',command=box.destroy)
        button.grid(column=1,row=0,padx=5,pady=5,sticky='nswe') 

        box.label = 'box'
        box.field = label_var
        box.value = entry_var

    def on_frame_configure_right(self, event):
        self.fields_canvas_right.configure(scrollregion=self.fields_canvas_right.bbox('all'))              

    def _clean_custom_fields(self,opt):
        if opt=='left':
            frame = self.inner_fields_frame_left
        elif opt=='right':
            frame = self.inner_fields_frame_right
        for children in frame.winfo_children():
            children.destroy()  

    def _clean_standard_fields(self,opt):
        if opt=='left':
            self.author_var_left.set('')
            self.place_var_left.set('')   
            self.category_entry_left.set('') 
            self.activity_entry_left.set('') 
            self.subject_entry_left.set('') 
            self.collection_entry_left.set('')  
        elif opt=='right':
            self.author_var_right.set('')
            self.place_var_right.set('')   
            self.category_entry_right.set('') 
            self.activity_entry_right.set('') 
            self.subject_entry_right.set('') 
            self.collection_entry_right.set('')  

    def _clean_text(self,opt):
        if opt == 'left':
            self.text_left.delete('1.0',tk.END)   
        elif opt == 'right':
            self.text_right.delete('1.0',tk.END) 

    def _clean_fields(self,opt):
        self._clean_standard_fields(opt)
        self._clean_custom_fields(opt)
        self._clean_text(opt)

    def _clean_entries(self,opt):
        if opt == 'left':
            self.entries_left.delete(*self.entries_left.get_children())   
        elif opt == 'right':
            self.entries_right.delete(*self.entries_right.get_children())   

    def _reset_dict_index(self,old_dict,side):
        new_dict = {}
        i = 0
        for key,item in old_dict.items():
            new_dict[i] = item
            new_dict[i]['box'].index = i
            i += 1     

        if side == 'left':
            self.custom_fields_left = new_dict
        elif side == 'right':
            self.custom_fields_right = new_dict  

    def _update_cus_fields(self,box,side,field=None,value=None):
        print('Updating custom field')
        if side == 'left':
            field_dict = self.custom_fields_left
        elif side == 'right':
            field_dict = self.custom_fields_right

        if not field is None:
            field_dict[box.index][value] = field
        if not field is None:
            field_dict[box.index][value] = value



          

class LinkWindow:

    def __init__(self,parent,controller):
        self.parent = parent
        self.controller = controller

        self.controller.link_panel = 'on'
        self.controller._add_link_field = self._add_field_box
        self.controller._clean_link_std_fields = self._clean_standard_fields
        self.controller._clean_link_cus_fields = self._clean_custom_fields

        left_frame = tk.Frame(self.parent)
        left_frame.grid(row=0,column=0,padx=5,pady=5,sticky='nsw')
        self._init_left_frame(left_frame)

        right_frame = tk.Frame(self.parent)
        right_frame.grid(row=0,column=1,padx=5,pady=5,sticky='nsw')
        self._init_right_frame(right_frame)

    def _init_left_frame(self,parent):

        add_fields_box = tk.LabelFrame(parent,text='Add Field')
        add_fields_box.grid(row=0,column=0,padx=5,pady=5,sticky='nswe')

        self.controller.field_combobox = ttk.Combobox(add_fields_box,width=18)
        self.controller.field_combobox.grid(row=0,column=0,padx=5,pady=5,sticky='nswe')

        self.controller.add_field = tk.Button(add_fields_box,text='+',width=3)
        self.controller.add_field.grid(row=0,column=1,padx=5,pady=5,sticky='nswe')
        self.controller.add_field.config(command=self._add_field_box)

        box = tk.Frame(parent)
        label = tk.Label(box,text='Custom Fields')
        label.grid(row=0,column=0,sticky='nswe')
        button = tk.Button(box,text='clear',
                        command=lambda: self._clean_custom_fields('left'))
        button.grid(row=0,column=1,sticky='nswe')
        field_box = tk.LabelFrame(parent,labelwidget=box)
        field_box.grid(row=1,column=0,padx=5,pady=5,sticky='nswe')

        self.field_canvas = tk.Canvas(field_box,borderwidth=0,background='#ffffff',
        height=330,width=220)
        self.field_canvas.grid(row=0,column=0,sticky='nswe')

        self.controller.link_cus_fields = tk.Frame(self.field_canvas,background='#ffffff') 
        self.controller.link_cus_fields.grid(row=0,column=0,sticky='nswe')
        self.controller.link_cus_fields.bind("<Configure>", self.on_frame_configure_left)
        vsb = ttk.Scrollbar(field_box, orient='vertical', command=self.field_canvas.yview)
        vsb.grid(row=0,column=1,sticky='nse')
        self.field_canvas.configure(yscrollcommand=vsb.set)
        self.field_canvas.create_window((4,4),window=self.controller.link_cus_fields,anchor='nw',tags='fields_box')

    def _add_field_box(self,field_name=None,field_value=None):

        print('Adding custom fields')
        row = len(self.controller.link_cus_fields.winfo_children())

        label_var = tk.StringVar()
        if not field_name is None: label_var.set(field_name)
        mini_entry = tk.Entry(self.controller.link_cus_fields,width=8,textvariable=label_var)   
        box = tk.LabelFrame(self.controller.link_cus_fields,labelwidget=mini_entry)
        box.grid(column=0,row=row,padx=5,pady=5,sticky='nwe')

        entry_var = tk.StringVar()
        if not field_value is None: entry_var.set(field_value)
        entry = tk.Entry(box,width=15,textvariable=entry_var)
        entry.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')  

        button = tk.Button(box,width=3,text='-',
        command=box.destroy)
        button.grid(column=1,row=0,padx=5,pady=5,sticky='nswe') 

    def on_frame_configure_left(self, event):
        self.field_canvas.configure(scrollregion=self.field_canvas.bbox('all'))       

    def _init_right_frame(self,parent):               

        box_relation = tk.LabelFrame(parent,text='Relation')
        box_relation.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')

        self.controller.link_relation = tk.StringVar()
        self.controller.link_relation.set('')
        relation = tk.Entry(box_relation,textvariable=self.controller.link_relation)
        relation.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')

        box_direction = tk.LabelFrame(parent,text='Direction')
        box_direction.grid(column=1,row=0,padx=5,pady=5,sticky='nswe')

        self.controller.link_direction = tk.IntVar(self.controller)
        self.controller.link_direction.set(0)
        both = tk.Radiobutton(box_direction, text='<->', variable=self.controller.link_direction, value=0)
        both.grid(column=1,row=0,padx=5,pady=5,sticky='nswe')
        left = tk.Radiobutton(box_direction, text='<--', variable=self.controller.link_direction, value=1)
        left.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')
        right = tk.Radiobutton(box_direction, text='-->', variable=self.controller.link_direction, value=2)
        right.grid(column=2,row=0,padx=5,pady=5,sticky='nswe') 
        
        box_first_entry = tk.LabelFrame(parent,text='First Entry')
        box_first_entry.grid(column=0,row=1,padx=5,pady=5,sticky='nswe')   
        self.controller.first_entry = tk.Text(box_first_entry,width=25,height=6)      
        self.controller.first_entry.grid(column=0,row=0,padx=5,pady=5,sticky='nsew')

        box_second_entry = tk.LabelFrame(parent,text='Second Entry')
        box_second_entry.grid(column=1,row=1,padx=5,pady=5,sticky='nswe')   
        self.controller.second_entry = tk.Text(box_second_entry,width=25,height=6)      
        self.controller.second_entry.grid(column=0,row=0,padx=5,pady=5,sticky='nsew')        

        box_description = tk.LabelFrame(parent,text='Description')
        box_description.grid(column=0,row=2,columnspan=2,padx=5,pady=5,sticky='nswe')

        self.controller.link_description = tk.Text(box_description,width=60,height=6)
        self.controller.link_description.grid(column=0,row=0,padx=5,pady=5,sticky='nswe')

        author_box = tk.LabelFrame(parent,text='Author')
        author_box.grid(column=0,row=3,padx=5,pady=5,sticky='nsew')
        self.controller.link_author = tk.StringVar()
        self.controller.link_author.set('')
        author = tk.Entry(author_box,textvariable=self.controller.link_author)
        author.grid(column=0,row=0,padx=5,pady=5,sticky='nsew')

        place_box = tk.LabelFrame(parent,text='Place')
        place_box.grid(column=1,row=3,padx=5,pady=5,sticky='nsew')
        self.controller.link_place = tk.StringVar()
        self.controller.link_place.set('') 
        place = tk.Entry(place_box,textvariable=self.controller.link_place)
        place.grid(column=1,row=0,padx=5,pady=5,sticky='nsew')

        box_buttons = tk.LabelFrame(parent,text='Link Options')
        box_buttons.grid(column=0,row=4,columnspan=2,padx=5,pady=5,sticky='nswe')

        button_width = 16
        self.controller.create_link = tk.Button(box_buttons,text='create',width=button_width)
        self.controller.create_link.grid(column=0,row=0,sticky='we')
        self.controller.edit_link = tk.Button(box_buttons,text='edit',width=button_width)
        self.controller.edit_link.grid(column=1,row=0,sticky='we')
        #self.controller.refresh_link = tk.Button(box_buttons,text='remove',width=button_width)
        #self.controller.refresh_link.grid(column=2,row=0,sticky='we')

    def _clean_custom_fields(self):
        frame = self.controller.link_cus_fields
        for children in frame.winfo_children():
            children.destroy()  

    def _clean_standard_fields(self,opt):
        self.controller.link_author.set('')
        self.controller.link_place.set('')
        self.controller.link_relation.set('')
        self.controller.link_description.delete('1.0',tk.END)
        if opt == 'left':
            self.controller.first_entry.delete('1.0',tk.END)
        elif opt == 'right':
            self.controller.second_entry.delete('1.0',tk.END)  
