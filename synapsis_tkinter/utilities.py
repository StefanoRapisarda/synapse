import time
import os
import shelve

entry_archive = os.path.join(os.getcwd(),'storage/entries')
link_archive = os.path.join(os.getcwd(),'storage/links')

def now():
    tmp = time.localtime()
    string = '{:4}{:0>2}{:0>2}{:0>2}{:0>2}{:0>2}'.\
        format(tmp.tm_year,tmp.tm_mon,tmp.tm_mday,
               tmp.tm_hour,tmp.tm_min,tmp.tm_sec)
    return time.ctime(),string

def list_entry_ids(sorting=True):
    if os.path.isfile(entry_archive+'.db'):
        with shelve.open(entry_archive) as entries:
            ids = list(entries)
        if sorting: ids.sort()
    else:
        print('I could not find {}'.format(entry_archive))
        ids = []
    return ids

def list_field(id_list,field):
    if not isinstance(id_list,list): id_list = [id_list]
    fields = []
    if os.path.isfile(entry_archive+'.db'):
        with shelve.open(entry_archive,'r') as entries: 
            for entry_id in id_list:
                if not entry_id in entries: continue
                entry_dict = entries[entry_id]
                for key,value in entry_dict.items():
                    if key == field:
                        if field == 'custom_fields':
                            try:
                                fields += [value[i] for i in value.keys()]
                            except KeyError:
                                print('Entry {} does not have custom fields'.format(id))
                        else:
                            fields += [value]    
    fields = list(set(fields))                         
    return fields

def read_entry_fields(entry_id,target='entries'):
    '''
    Return all the fields corresponding to entry id in a single dictionary
    '''

    if target == 'entries':
        archive = entry_archive
    elif target == 'links':
        archive = link_archive

    with shelve.open(archive,'r') as entries: 
        try:
            entry = entries[entry_id]
        except Exception as e:
            print(e)
            print('Could not find ID: {}'.format(entry_id))
            return {}

    std_fields = {}
    cus_fields = {}
    for key,item in entry.items():
        if key == 'custom_fields': 
            cus_fields = item
        else:
            std_fields[key] = item

    return std_fields,cus_fields


def read_entries(field_list):
    '''
    Read all the entries and return the fields specified in the field
    list in list
    '''

    result = []
    if os.path.isfile(entry_archive+'.db'):
        with shelve.open(entry_archive,'r') as entries: 
            ids = list(entries)
            for id in ids:
                line = ['' for i in range(len(field_list))]
                entry = entries[id]
                for f in range(len(field_list)):
                    field =field_list[f]
                    if field in entry.keys():
                        line[f] = entry[field]
                result+=[line]
    return result

def id_to_date(id):
    date = '{} {} {}, {}:{}:{}'.format(
    id[3:7],id[7:9],id[9:11],id[11:13],id[13:15],id[15:17])
    return date

def intersect_dict(dict_list):
    '''
    Return a dictionary containing keys and items that are identical
    among all the dictionaries from the input list
    '''

    if isinstance(dict_list,dict):
        dict_list = [dict_list]

    intersection = {}
    if len(dict_list) > 1:
        tmp_dict = dict_list[0]
        for i in range(1,len(dict_list)):
            curr_dict = dict_list[i]

            common_keys = tmp_dict.keys() & curr_dict.keys()
            if len(common_keys) == 0: return {}

            leftovers = [key for key in tmp_dict.keys() if not key in common_keys]
            for key in leftovers: del tmp_dict[key]

            for key in common_keys:
                if tmp_dict[key]!=curr_dict[key]: del tmp_dict[key]
    elif len(dict_list) == 1:
        tmp_dict = dict_list[0]
    else:
        tmp_dict = {}

    return tmp_dict

def update_fields(ids,std_fields=None,cus_fields=None,opt='entries',clean=True):
    '''
    note: when updating a dictionary, existing keys are updated to corresponding
          items in the dictionary inside update(). Additional keys are not changed
    note: using update you can only add items, not removing
    '''

    if isinstance(ids,str): ids = [ids]

    if opt == 'entries':
        archive = entry_archive
    elif opt == 'links':
        archive = link_archive

    for single_id in ids:
        # First, updating existing keys
        with shelve.open(archive,writeback=True) as infile:
            if not std_fields is None:
                infile[single_id].update(std_fields)
            if not cus_fields is None:
                infile[single_id]['custom_fields'].update(cus_fields)
        # Second, removing not matching keys
        if clean:
            with shelve.open(archive,writeback=True) as infile:
                if not cus_fields is None:
                    common_keys = infile[single_id]['custom_fields'].keys() and cus_fields.keys()
                    to_delete = []
                    for key in infile[single_id]['custom_fields'].keys():
                        if not key in common_keys: to_delete += [key]
                    for key in to_delete:
                        del infile[single_id]['custom_fields'][key]

def edit_field(id_list,std_field=None,cus_field=None,opt='entries'):

    if isinstance(id_list,str): id_list = [id_list]

    if opt == 'entries':
        archive = entry_archive
    elif opt == 'links':
        archive = link_archive

    for single_id in id_list:
        with shelve.open(archive,writeback=True) as infile:
            if not std_field is None:
                infile[single_id][std_field['field']] = std_field['value']
            if not cus_field is None:
                if cus_field['value'] is None:
                    del infile[single_id]['custom_fields'][cus_field['field']] 
                else:
                    infile[single_id]['custom_fields'][cus_field['field']] = cus_field['value']


        





