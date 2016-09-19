#import basic packages
import os

#import special packages
import yaml

#import internal config
from config import RAWDATAPATH,FLATDATAPATH,DATACATEGORIES

#import internal function
import common_utility


class ReadData():
    """
    Put data into dataholder.
    """
    def __init__(self):
        self.dataholder = {}
        
    def readRawData_zhao(self):
        """
        Data reader for zhao project
        """
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
                    # Loop over all subfolders inside the category
                    for entity in os.scandir(datapath.path):
                        person_dict = {} #temp dict for each person
                        # Loop the person's folder
                        for doc in os.scandir(entity.path):
                            if doc.name == 'brief.yaml':
                                person_dict.update(yaml.safe_load(open(doc.path,'r')))
                            elif doc.name == 'portrait.png':
                                person_dict.update({'Portrait' : doc.path})
                        temp_list.append(person_dict)
                    self.dataholder[category_name] = temp_list
                    
                    del temp_list
                    del person_dict
                elif category_name == 'family':
                    temp_list = []
                    ## Each 'family' entry is an YAML file, filename is the person's name, file info is his/her family relationship
                    for doc in os.scandir(datapath.path):
                        family_dict = yaml.safe_load(open(doc.path,'r'))
                        temp_list.append(family_dict)
                    self.dataholder[category_name] = temp_list
                    
                    del temp_list
                    del family_dict
                elif category_name == 'company':
                    temp_list = []
                    ## Each company folder contains one yaml file
                    for entity in os.scandir(datapath.path):
                        for doc in os.scandir(entity.path):
                            company_dict = yaml.safe_load(open(doc.path,'r'))
                            temp_list.append(company_dict)
                    self.dataholder[category_name] = temp_list
                    
                    del temp_list
                    del company_dict
                else:
                    print("Warning: unknown data folder name {0}").format(datapath.name)
        #common_utility.print_obj(self.dataholder)        
    """    
    with open("/home/long/Desktop/projects/bloodbread/src/test.yaml") as file:
        test_person = yaml.safe_load(file)
    
    print(test_person)
    """
    
    def parseRawData_zhao(self):
        pass
    