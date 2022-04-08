import tkinter as tk
from gui.synapsis_dialogue_tkinter import *
from utilities import *
from entries import *
from links import *

class App:
    def __init__(self):
        self.ui = MainWindow()
        self.ui.geometry('1450x800')

        self.author = 'Stefano Rapisarda'
        self.place  = 'Uppsala (Sweden)'

        # General dimensions of window
        self.entry_width = 20

        # Initialize info variables
        self._init_vars()
        self._set_author_place()

        # Displaying entries
        self._entry_headings()
        self._populate_entries('left')
        self._populate_entries('right')

        self._connect_entry_panels()

        self._bind_search_buttons()
        self._bind_entry_buttons()
        self._bind_edit_buttons()
        self._bind_link_buttons()

        print('author first',self.link_std_fields['author'])

        self.ui.mainloop()

    def _init_vars(self):
        self.std_fields_left = {}
        self.cus_fields_left = {}
        self.entry_ids_left = []
        self.link_ids_left = []

        self.entry_text_left = ''

        self.pre_entry_selection_left = ''

        self.clicked_left = False

        # ---

        self.std_fields_right = {}
        self.cus_fields_right = {}
        self.entry_ids_right = []
        self.link_ids_right = []

        self.entry_text_right = ''

        self.pre_entry_selection_right = ''

        self.clicked_right = False

        # ---

        self.link_std_fields = {}
        self.link_cus_fields = {}

    def _set_author_place(self):
        self.std_fields_left['author'] = self.author
        self.std_fields_left['place'] = self.place
        self.std_fields_right['author'] = self.author
        self.std_fields_right['place'] = self.place
        self.link_std_fields['author'] = self.author
        self.link_std_fields['place'] = self.place

    def _entry_headings(self):
        '''
        Initialize treeview headings in the left and right panel, name and width.
        Allows to sort columns with a click on the heading.
        '''

        # This is for sorting columns
        def _sort_column(tree,col,reverse):
            l = [(tree.set(k,col),k) for k in tree.get_children('')]
            l.sort(reverse=reverse)

            for index, (val,k) in enumerate(l):
                tree.move(k,'',index)

            tree.heading(col, command=lambda: self._sort_column(tree,col,not reverse))  

        columns = ('date','category','subject','collection','activity','links','id')
        col_width = [200,100,100,100,100,180,180]

        self.ui.entries_left['columns'] = columns
        self.ui.entries_right['columns'] = columns

        for i in range(len(columns)):
            
            # Left side
            self.ui.entries_left.column(columns[i],minwidth=col_width[i],
                width=self.entry_width,stretch=True)
            self.ui.entries_left.heading(columns[i],text=columns[i],
                command= lambda _col=columns[i]: _sort_column(self.ui.entries_left,_col,False))
            
            # Right side
            self.ui.entries_right.column(columns[i],minwidth=col_width[i],
                width=self.entry_width,stretch=True)
            self.ui.entries_right.heading(columns[i],text=columns[i],
                command= lambda _col=columns[i]: _sort_column(self.ui.entries_right,_col,False))

        # This is for removing the first column, but will also remove the possibility
        # to expand the window
        #self.ui.entries_left['show'] = 'headings'
        #self.ui.entries_right['show'] = 'headings'
   

    def _populate_entries(self,opt,id_list=None):
        '''
        Fill left and right treeviews with reading all the entries in the archive
        Entries are initially sorted according to ID
        If id_list is specified, only entries with ids in the list will populate
        the treeview
        '''

        if opt=='left':
            tree = self.ui.entries_left
        elif opt=='right':
            tree = self.ui.entries_right

        lines = read_entries(['creation_date','category','subject','collection','activity','links','id'])
        lines = sorted(lines,key=lambda x: x[6],reverse=True)

        for i in range(len(lines)):
            line = lines[i]
            # Skipping entry if not in id_list
            if not id_list is None:
                if not line[-1] in id_list: continue

            # Display only the number of links, not the links theirself
            links = line[5]
            line[5] = str(len(links))

            row = tree.insert('','end',text='',values=line)

            # If there are links, inserting them in an opening menu
            if len(links)>0:
                for link in links:
                    sub_line = ['' for j in range(len(line))]
                    sub_line[5] = link 
                    sub_line[6] = line[-1]
                    tree.insert(row,'end',text='',values=sub_line)

    def _refresh_entries(self,opt,id_list=None):
        '''
        Removes all the entries from treeviews and re-populate them
        '''
        self.ui._clean_entries(opt)
        self._populate_entries(opt,id_list)   

    def _connect_entry_panels(self):
        self.ui.entries_left.bind("<<TreeviewSelect>>",self._evaluate_selection_left)
        self.ui.entries_right.bind("<<TreeviewSelect>>",self._evaluate_selection_right) 

    def _evaluate_selection_left(self,event):

        self.clicked_left = True
        self.clicked_right = False

        self.entry_ids_left = []
        self.link_ids_left = []

        sel_left = self.ui.entries_left.selection()

        if len(sel_left) > 0:

            if sel_left == self.pre_entry_selection_left:
                print('Identical left selection already present')
                for sel in sel_left:
                    self.ui.entries_left.selection_remove(sel)
                self.ui._clean_fields('left')
                if hasattr(self.ui,'link_panel'):
                    self.ui._clean_link_std_fields('left')
                self.pre_entry_selection_left = ''
            else:
                for sel in sel_left:   
                    entry_id = self.ui.entries_left.item(sel)['values'][6]
                    link_id = self.ui.entries_left.item(sel)['values'][5]
                    self.entry_ids_left += [entry_id]
                    self.link_ids_left += [link_id]       

                tmp = [entry_id for entry_id in self.entry_ids_left if 'ENT' in entry_id]
                self.entry_ids_left = list(set(tmp))

                flag = False
                for link_id in self.link_ids_left:
                    if isinstance(link_id,int): flag = True
                tmp = [link_id for link_id in self.link_ids_left if not isinstance(link_id,int)]
                self.link_ids_left = tmp
                if flag: self.link_ids_left = []

                print('Left selection')
                print(self.entry_ids_left)
                print(self.link_ids_left)
                print()
                
                self._get_info('left')
                self._update_widgets('left')

                self.pre_entry_selection_left = sel_left

    def _evaluate_selection_right(self,event):

        self.clicked_left = False
        self.clicked_right = True

        self.entry_ids_right = []
        self.link_ids_right = []

        sel_right = self.ui.entries_right.selection()

        if len(sel_right) > 0:

            if sel_right == self.pre_entry_selection_right:
                for sel in sel_right:
                    self.ui.entries_right.selection_remove(sel)
                self.ui._clean_fields('right')
                if hasattr(self.ui,'link_panel'):
                    self.ui._clean_link_std_fields('right')
                self.pre_entry_selection_right = ''
            else:
                for sel in sel_right:   
                    entry_id = self.ui.entries_right.item(sel)['values'][6]
                    link_id = self.ui.entries_right.item(sel)['values'][5]
                    self.entry_ids_right += [entry_id]
                    self.link_ids_right += [link_id]       

                tmp = [entry_id for entry_id in self.entry_ids_right if 'ENT' in entry_id]
                self.entry_ids_right = list(set(tmp))

                flag = False
                for link_id in self.link_ids_right:
                    if isinstance(link_id,int): flag = True
                tmp = [link_id for link_id in self.link_ids_right if not isinstance(link_id,int)]
                self.link_ids_right = tmp
                if flag: self.link_ids_right = []

                print('right selection')
                print(self.entry_ids_right)
                print(self.link_ids_right)
                print()

                self._get_info('right')
                self._update_widgets('right')

                self.pre_entry_selection_right = sel_right

    def _update_widgets(self,opt):

        entry_std_field_names = ['author','place',
                                 'category','activity',
                                 'subject','collection']
        self.ui._clean_fields(opt)
        entry_text = ''
        
        if opt == 'left':

            std_vars = [self.ui.author_var_left,self.ui.place_var_left,
                        self.ui.category_entry_left,self.ui.activity_entry_left,
                        self.ui.subject_entry_left,self.ui.collection_entry_left]
            text_box = self.ui.text_left

            entry_std_fields = self.std_fields_left
            entry_cus_fields = self.cus_fields_left
            
            add_cus_field = self.ui._add_left_field_box

        elif opt == 'right':

            std_vars = [self.ui.author_var_right,self.ui.place_var_right,
                        self.ui.category_entry_right,self.ui.activity_entry_right,
                        self.ui.subject_entry_right,self.ui.collection_entry_right]         
            text_box = self.ui.text_right

            entry_std_fields = self.std_fields_right
            entry_cus_fields = self.cus_fields_right

            add_cus_field = self.ui._add_right_field_box
            

        for field,var in zip(entry_std_field_names,std_vars):
            try:
                var.set(entry_std_fields[field])
            except Exception as e:
                print('Could not find field {} while populating std fields'.format(field))
        for key,item in entry_cus_fields.items():
            add_cus_field(field_name=key, field_value=item)
        if 'content' in list(entry_std_fields): 
            entry_text = entry_std_fields['content']
        text_box.insert(tk.INSERT,entry_text)

        if hasattr(self.ui,'link_panel'):

            self.ui._clean_link_std_fields('left')
            self.ui._clean_link_std_fields('right')
            self.ui._clean_link_cus_fields()

            link_std_field_names = ['author','place',
                                    'description',
                                    'relation','direction']
            link_std_vars = [self.ui.link_author,self.ui.link_place,
                             self.ui.link_description,
                             self.ui.link_relation,self.ui.link_direction] 

            for field,var in zip(link_std_field_names,link_std_vars):
                if field == 'description':
                    try:
                        var.insert(tk.END,self.link_std_fields[field])
                    except Exception as e:
                        print('Count not write link description')
                else:
                    try:
                        var.set(self.link_std_fields[field])
                    except Exception as e:
                        print(f'Could not write link standard field {field}')
            for key,item in self.link_cus_fields.items():
                self.ui._add_link_field(field_name=key, field_value=item)

            if len(self.entry_ids_left) == 1 and \
                 len(self.link_ids_left) >= 1 and \
                    opt == 'left':
                self.ui.first_entry.insert(tk.INSERT,self.entry_ids_left[0]+'\n')
                for link_id in self.link_ids_left:
                    std,cus = read_entry_fields(link_id,'links')
                    link_id = std['edges']
                    link_id.remove(self.entry_ids_left[0])
                    self.ui.second_entry.insert(tk.INSERT,link_id[0]+'\n')
            else:
                for entry_id in self.entry_ids_left:
                    self.ui.first_entry.insert(tk.INSERT,entry_id+'\n')

            if len(self.entry_ids_right) == 1 and \
                 len(self.link_ids_right) >= 1 and \
                    opt == 'right':
                self.ui.second_entry.insert(tk.INSERT,self.entry_ids_right[0]+'\n')
                for link_id in self.link_ids_right:
                    std,cus = read_entry_fields(link_id,'links')
                    link_id = std['edges']
                    link_id.remove(self.entry_ids_right[0])
                    self.ui.first_entry.insert(tk.INSERT,link_id[0]+'\n')
            else:
                for entry_id in self.entry_ids_right:
                    self.ui.second_entry.insert(tk.INSERT,entry_id+'\n')            
                
    def _get_info(self,opt):
        
        tmp_std = []
        tmp_cus = []
        for entry_id in self.entry_ids_left:
            std,cus = read_entry_fields(entry_id,'entries')
            tmp_std += [std]
            tmp_cus += [cus]
        self.std_fields_left = intersect_dict(tmp_std)
        self.cus_fields_left = intersect_dict(tmp_cus)

        tmp_std = []
        tmp_cus = []
        for entry_id in self.entry_ids_right:
            std,cus = read_entry_fields(entry_id,'entries')
            tmp_std += [std]
            tmp_cus += [cus]
        self.std_fields_right = intersect_dict(tmp_std)
        self.cus_fields_right = intersect_dict(tmp_cus)

        if opt == 'left':
            ids = self.link_ids_left 
        elif opt == 'right':
            ids = self.link_ids_right
        tmp_std = []
        tmp_cus = []
        for link_id in ids:
            std,cus = read_entry_fields(link_id,'links')
            tmp_std += [std]
            tmp_cus += [cus]
        self.link_std_fields = intersect_dict(tmp_std)
        self.link_cus_fields = intersect_dict(tmp_cus)   

        self._set_author_place() 

    def _bind_search_buttons(self):
        self.ui.search_field_button_left.configure(command=lambda: self._search('left','field'))
        self.ui.search_field_button_right.configure(command=lambda: self._search('right','field'))
        self.ui.search_text_button_left.configure(command=lambda: self._search('left','text'))
        self.ui.search_text_button_right.configure(command=lambda: self._search('right','text'))
    
    def _bind_edit_buttons(self):
        '''
        Bind buttons in the edit entry tool bar to corresponding functions
        '''
        self.ui.reset_entry_button_left.configure(command=lambda: self._reset_entry('left'))
        self.ui.edit_entry_button_left.configure(command=lambda: self._edit_entry('left'))
        self.ui.create_entry_button_left.configure(command=lambda: self._create_entry('left'))
        self.ui.delete_entry_button_left.configure(command=lambda: self._delete_entry('left'))

        self.ui.reset_entry_button_right.configure(command=lambda: self._reset_entry('right'))
        self.ui.edit_entry_button_right.configure(command=lambda: self._edit_entry('right'))
        self.ui.create_entry_button_right.configure(command=lambda: self._create_entry('right'))
        self.ui.delete_entry_button_right.configure(command=lambda: self._delete_entry('right'))

    def _bind_entry_buttons(self):
        '''
        Binds 'Refresh' buttons on the treeview heading with self._refresh_entries
        '''
        self.ui.refresh_button_left.configure(command=lambda: self._refresh_entries('left'))
        self.ui.refresh_button_right.configure(command=lambda: self._refresh_entries('right'))

    def _read_entry_standard_fields(self,opt):
        print('Reading standard fields')
        std_fields = {}
        if opt == 'left':
            std_fields['author'] = self.ui.author_var_left.get()
            std_fields['place'] = self.ui.place_var_left.get()
            std_fields['category'] = self.ui.category_entry_left.get()
            std_fields['activity'] = self.ui.activity_entry_left.get()
            std_fields['subject'] = self.ui.subject_entry_left.get()
            std_fields['collection'] = self.ui.collection_entry_left.get()
        elif opt == 'right':
            std_fields['author'] = self.ui.author_var_right.get()
            std_fields['place'] = self.ui.place_var_right.get()
            std_fields['category'] = self.ui.category_entry_right.get()
            std_fields['activity'] = self.ui.activity_entry_right.get()
            std_fields['subject'] = self.ui.subject_entry_right.get()
            std_fields['collection'] = self.ui.collection_entry_right.get()
        return std_fields

    def _read_entry_custom_fields(self,opt):
        if opt == 'left':
            container = self.ui.inner_fields_frame_left
        elif opt == 'right':
            container = self.ui.inner_fields_frame_right

        print('Reading link custom fields')
        cus_fields = {}
        for child in container.winfo_children():
            if isinstance(child,tk.LabelFrame):
                if hasattr(child,'label'):
                    cus_fields[child.field.get()] = child.value.get()

        to_delete = []
        for key,item in cus_fields.items():
            if key == '' or item == '': 
                to_delete += [key]
        for key in to_delete: del cus_fields[key]
        for key,item in cus_fields.items():
            print('{}: {}'.format(key,item))
        return cus_fields

    def _edit_entry(self,opt):
        if opt == 'left':
            entry_ids = self.entry_ids_left
            text = self.ui.text_left.get('1.0',tk.END)
            old_std_fields = self.std_fields_left 
            old_cus_fields = self.cus_fields_left
        elif opt == 'right':
            entry_ids = self.entry_ids_right
            text = self.ui.text_right.get('1.0',tk.END)
            old_std_fields = self.std_fields_right
            old_cus_fields = self.cus_fields_right

            print('These are the old std fields')
            for key,item in old_std_fields.items():
                print('{}: {}'.format(key,item))
       

        if len(entry_ids) > 0:

            std_fields = self._read_entry_standard_fields(opt)
            cus_fields = self._read_entry_custom_fields(opt)

            print('These are the new std fields')
            for key,item in std_fields.items():
                print('{}: {}'.format(key,item))     

            if len(entry_ids) == 1:
                std_fields['content'] = text   

            if len(entry_ids) == 1:
                for key,item in std_fields.items():
                    edit_field(entry_ids,std_field={'field':key,'value':item})  
            else:
                for key,item in std_fields.items():
                    if item != '':
                        edit_field(entry_ids,std_field={'field':key,'value':item})                           

            # Editing existing keywords
            updated = []
            for key,item in old_cus_fields.items():
                if key in cus_fields.keys():
                    edit_field(entry_ids,cus_field={'field':key,'value':item})
                    updated += [key]
                else:
                    edit_field(entry_ids,cus_field={'field':key,'value':None}) 

            # Adding new ones
            for key,item in cus_fields.items():
                if not key in updated:
                    edit_field(entry_ids,cus_field={'field':key,'value':item})        
            
            #update_fields(entry_ids,std_fields,cus_fields,clean=False)

        self.ui._clean_entries('left')
        self._populate_entries('left')
        self.ui._clean_entries('right')
        self._populate_entries('right')

    def _delete_entry(self,opt):
        if opt == 'left':
            entries = self.entry_ids_left
        elif opt == 'right':
            entries = self.entry_ids_right

        if len(entries) > 0:
            for entry_id in entries:
                std,cus = read_entry_fields(entry_id,target='entries')
                links = std['links']

                # Deleting associated links
                with shelve.open(link_archive,writeback=True) as infile:
                    for link in links:
                        try:
                            del infile[link]
                        except Exception as e:
                            print(f'Could not delete link {link} of entry {entry_id}')

                # Then, deleting entry itself
                with shelve.open(entry_archive,writeback=True) as infile:
                    del infile[entry_id]           
        
        self.ui._clean_entries('left')
        self._populate_entries('left')
        self.ui._clean_entries('right')
        self._populate_entries('right')
        self._init_vars()
        self._set_author_place()
        self._update_widgets('left')
        self._update_widgets('right')

    def _create_entry(self,opt):
        if opt == 'left':
            text = self.ui.text_left.get('1.0',tk.END)
        elif opt == 'right':
            text = self.ui.text_right.get('1.0',tk.END)
        
        std_fields = self._read_entry_standard_fields(opt)
        std_fields['content'] = text
        cus_fields = self._read_entry_custom_fields(opt)

        entry = Entry.make_from_dicts(std_fields,cus_fields)
        entry.save()

        self.ui._clean_entries('left')
        self._populate_entries('left')
        self.ui._clean_entries('right')
        self._populate_entries('right')

    def _reset_entry(self,opt):
        self.ui._clean_custom_fields(opt)
        self.ui._clean_custom_fields(opt)
        self.ui._clean_text(opt)
        self._update_widgets(opt)

    def _bind_link_buttons(self):
        self.ui.panel_link_button.configure(command=self._open_link_window)
        self.ui.show_link_button_left.configure(command=lambda: self._show_links('left'))  
        self.ui.show_link_button_right.configure(command=lambda: self._show_links('right'))
        self.ui.remove_link_button.configure(command=self._remove_link)  

    def _open_link_window(self):
        '''
        Open the link window and bind buttons to corresponding commands
        '''
        self.ui._open_new_window(LinkWindow)
        self.ui.create_link.configure(command=self._create_link)
        self.ui.edit_link.configure(command=self._edit_link)
        self._get_info('left')
        self._get_info('right')
        self._update_widgets('left')
        self._update_widgets('right')

    def _read_link_cus_fields(self):
        container = self.ui.link_cus_fields

        print('Reading link custom fields')
        cus_fields = {}
        pair = 0
        for child in container.winfo_children():
            if isinstance(child,tk.Entry):
                field_name = child.get()
                pair += 1
            elif isinstance(child,tk.LabelFrame):
                for gchild in child.winfo_children():
                    if isinstance(gchild,tk.Entry):        
                        field_value = gchild.get()
                        pair += 1
            if pair == 2:
                print(field_name,field_value)
                cus_fields[field_name] = field_value
                pair = 0

        to_delete = []
        for key,item in cus_fields.items():
            if key == '' or item == '': 
                to_delete += [key]
        for key in to_delete: del cus_fields[key]
        return cus_fields

    def _read_link_std_fields(self):
        std_fields = {}
        std_fields['author']      = self.ui.link_author.get()
        std_fields['place']       = self.ui.link_place.get()
        std_fields['relation']    = self.ui.link_relation.get()
        std_fields['description'] = self.ui.link_description.get('1.0',tk.END)
        std_fields['direction']   = self.ui.link_direction.get() 
        return std_fields

    def _edit_link(self):
        if self.clicked_left:
            link_ids = self.link_ids_left
        elif self.clicked_right:
            link_ids = self.link_ids_right

        std_fields = self._read_link_std_fields()
        cus_fields = self._read_link_cus_fields()

        update_fields(link_ids,std_fields,cus_fields,opt='links',clean=False)

    def _create_link(self):
        left_selection = self.ui.entries_left.selection()
        right_selection = self.ui.entries_right.selection()

        author = self.ui.link_author.get()
        place = self.ui.link_place.get()

        relation = self.ui.link_relation.get()
        direction = self.ui.link_direction.get()
        description = self.ui.link_description.get('1.0',tk.END)

        cus_fields = self._read_link_cus_fields()

        print('n entries',len(self.entry_ids_left),len(self.entry_ids_right))
        if len(self.entry_ids_left) > 0 and len(self.entry_ids_right) > 0:
            for left_id in self.entry_ids_left:
                for right_id in self.entry_ids_right:
                    print(left_id,right_id)

                    link = Link(author = author,
                                place = place,
                                relation = relation,
                                description = description,
                                edges = [left_id,right_id],
                                custom_fields = cus_fields,
                                direction=direction)
                    link.save()
                    print(link['id'])

                    try:
                        with shelve.open(entry_archive,writeback=True) as infile:
                            infile[right_id]['links'] += [link['id']]
                    except Exception as e:
                        print('Could not write link {} in entry {}'.\
                            format(link['id'],right_id))   

                    try:
                        with shelve.open(entry_archive,writeback=True) as infile:
                            infile[left_id]['links'] += [link['id']]
                    except Exception as e:
                        print('Could not write link {} in entry {}'.\
                            format(link['id'],left_id))  



        self.ui._clean_entries('left')
        self._populate_entries('left')
        self.ui._clean_entries('right')
        self._populate_entries('right')

    def _remove_link(self):
        link_ids = list(set(self.link_ids_left + self.link_ids_right))

        if len(link_ids) > 0:
            for link_id in link_ids:
                std,cus = read_entry_fields(link_id,'links')
                entry1 = std['edges'][0]
                entry2 = std['edges'][1]

                # Removing link from link archive
                try:
                    with shelve.open(link_archive) as outfile:
                        del outfile[link_id]
                except Exception as e:
                    print(f'Could not remove {link_id}') 

                try:
                    with shelve.open(entry_archive,writeback=True) as outfile:
                        if link_id in outfile[entry1]['links']: outfile[entry1]['links'].remove(link_id)
                        if link_id in outfile[entry2]['links']: outfile[entry2]['links'].remove(link_id)
                except Exception as e:
                    print(f'Could not remove {link_id} either from {entry1} or {entry2}')         

        self.ui._clean_entries('left')
        self._populate_entries('left')
        self.ui._clean_entries('right')
        self._populate_entries('right')
        self._init_vars()
        self._set_author_place()
        self._update_widgets('left')
        self._update_widgets('right')         

    def _show_links(self,opt):

        if opt == 'left':
            entries = self.entry_ids_left
            other = 'right'
        elif opt == 'right':
            entries = self.entry_ids_right
            other = 'left'

        if len(entries) > 0:
            other_entries = []
            for entry_id in entries:
                std,cus = read_entry_fields(entry_id,target='entries')
                links = std['links']
                for link_id in links:
                    lstd,lcus = read_entry_fields(link_id,target='links')
                    other_entry = lstd['edges']
                    other_entry.remove(entry_id)
                    other_entries += [other_entry[0]]
            other_entries = list(set(other_entries))

            if len(other_entries)>0:
                self.ui._clean_entries(other)
                self._populate_entries(other,other_entries)

    def _search(self,side,opt):
        if side == 'left':
            if opt == 'field': to_search = self.ui.field_to_search_left.get()
            if opt == 'text': to_search = self.ui.text_to_search_left.get()
            tree = self.ui.entries_left
        elif side == 'right':
            if opt == 'field': to_search = self.ui.field_to_search_right.get()
            if opt == 'text': to_search = self.ui.text_to_search_right.get()            
            tree = self.ui.entries_right

        entry_ids = []
        for child in tree.get_children():
            #print(tree.item(child))
            entry_ids += [tree.item(child)['values'][-1]]
        
        ids_to_show = []
        for entry_id in entry_ids:
            std,cus = read_entry_fields(entry_id)
            if opt == 'text':
                if to_search in std['content']: ids_to_show += [entry_id]
            elif opt == 'field':
                flag_std = False
                flag_cus = False
                for key,item in std.items():
                    if key == 'custom_fields': continue
                    if to_search in item: flag_std = True
                for key,item in cus.items():
                    if to_search in item: flag_cus = True
                if flag_std or flag_cus: ids_to_show += [entry_id]

        self.ui._clean_entries(side)
        self._populate_entries(side,ids_to_show)
            
if __name__ == '__main__':
    app = App()
