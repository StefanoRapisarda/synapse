from utilities import *
from entries import *
import shelve

class Link(dict):

    def __init__(self,*args,
                author='',date='',place='',
                relation='',description='',
                edges=['',''],direction=0,
                custom_fields={},**kwargs):
        super().__init__(*args,**kwargs)

        self['id'] = 'LNK'+now()[1]+'_{:0>4}'.format(randint(0,9999))
        self['author'] = author
        self['creation_date'] = now()[0]
        self['place'] = place
        self['relation'] = relation
        self['description'] = description
        self['edges'] = edges
        self['direction'] = direction

        self['custom_fields'] = custom_fields  

    def save(self,archive=link_archive):
        try:
            with shelve.open(archive) as outfile:
                outfile[self['id']] = self
            return True
        except Exception as e:
            print(e)
            return False   

