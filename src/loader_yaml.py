#import basic packages
import os
import pprint

#import special packages
import yaml

#import internal config
from config import RAWDATAPATH,FLATDATAPATH,DATACATEGORIES


class RawData2Flat():
    """
    Copy the original folder/filename structure to flat.
    """
    
    pass


class ReadData():
    """
    Put data into dataholder.
    """
    def __init__(self):
        self.dataholder = {}
        
    def readRawData(self):
        # Loop all things in DATAPATH
        for datapath in os.scandir(RAWDATAPATH):
            # If we find an interesting category...
            if datapath.is_dir() and datapath.name in DATACATEGORIES.keys():
                # Add a new key to dataholder, which contains an empty list to be assigned
                category_name = datapath.name
                temp_list = []
                # Put content into dataholder
                if category_name == 'person':
                    ## Each 'person' entry is a folder, contains a 'brief.yaml' and (sometimes) 'portrait.png'
                    # Then loop over all subfolders inside the category
                
                    for entity in os.scandir(datapath.path):
                        #print(entity)
                        person_dict = {}
                        # Loop the person's folder
                        for doc in os.scandir(entity.path):
                            if doc.name == 'brief.yaml':
                                #print(doc.path)
                                person_dict.update(yaml.safe_load(open(doc.path,'r')))
                            elif doc.name == 'portrait.png':
                                person_dict.update({'Portrait' : doc.path})
                        temp_list.append(person_dict)
                    self.dataholder[category_name] = temp_list
                    #pprint.pprint(temp_list)
                    del temp_list
                    del person_dict
                elif category_name == 'family':
                    pass
                elif category_name == 'company':
                    pass
                else:
                    print("Warning: unknown data folder name {0}").format(datapath.name)
                    
    """    
    with open("/home/long/Desktop/projects/bloodbread/src/test.yaml") as file:
        test_person = yaml.safe_load(file)
    
    print(test_person)
    """
    