from utilities import *
import shelve
from random import randint

class Entry(dict):

    def __init__(self,*args,
                content='',author='',place='',
                category='',subject='',activity='',collection='',
                links=[],custom_fields={},
                **kwargs):
        super().__init__(*args,**kwargs)

        self['id'] = 'ENT'+now()[1]+'_{:0>4}'.format(randint(0,9999))
        self['content'] = content
        self['author'] = author
        self['creation_date'] = now()[0]
        self['place'] = place
        self['category'] = category
        self['activity'] = activity
        self['subject'] = subject
        self['collection'] = collection
        self['links'] = links 

        self['custom_fields'] = custom_fields  

    @classmethod
    def make_from_dicts(cls,std_fields,cus_fields):

        entry = cls(content = std_fields['content'],
        author= std_fields['author'],
        place = std_fields['place'],
        category = std_fields['category'],
        activity = std_fields['activity'],
        subject = std_fields['subject'],
        collection = std_fields['collection'],
        custom_fields =  cus_fields)

        return entry       

    def save(self,archive=entry_archive):
        try:
            with shelve.open(archive) as outfile:
                outfile[self['id']] = self
            return True
        except Exception as e:
            print(e)
            return False         

