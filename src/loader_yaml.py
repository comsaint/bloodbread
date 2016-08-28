#import basic packages
import os

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
        for entry in os.scandir(RAWDATAPATH):
            # If we find an interesting category...
            if entry.is_dir() and entry.name in DATACATEGORIES.keys():
                # Add a new key to dataholder, which contains an empty list to be assigned
                self.dataholder[entry.name] = []
                # Then loop over all subfolders inside the category
                for entity in os.scandir(entry.path):
                    # Put content into dataholder
                    if entry.name == 'person':
                        ## Each 'person' entry is a folder, contains a 'brief.yaml' and (optional) 'portrait.png'
                        # Create a dict with the person's name as key
                        person_dict = {entity.name:{}}
                        
                        # Loop the person's folder
                        for doc in os.scandir(entity.path):
                            if doc.name in DATACATEGORIES[entry.name] and '.yaml' in doc.name:
                                person_dict[entity.name]['Brief'] = yaml.safe_load(open(entity.path+'/'+DATACATEGORIES[entry.name][i],'r'))
                            #elif '.png' in DATACATEGORIES[entry.name][i]:
                            #    person_dict[entity.name]['Portrait'] = entity.path+'/'+DATACATEGORIES[entry.name][i]
                            #else:
                            #    break
                    elif entry.name == 'family':
                        pass
                    elif entry.name == 'company':
                        pass
                    
    """    
    with open("/home/long/Desktop/projects/bloodbread/src/test.yaml") as file:
        test_person = yaml.safe_load(file)
    
    print(test_person)
    """
    