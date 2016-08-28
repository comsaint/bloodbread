## File of configurations.

# Import packages
import os

# Define the place where raw data are stored
RAWDATAPATH = os.path.dirname(os.getcwd()) + '/data'

# Define the path to data in flat format
FLATDATAPATH = os.path.dirname(os.getcwd()) + '/flatdata'

# Define data categories
DATACATEGORIES = {
                  'person':['brief.yaml','portrait.png'],
                  'family':[],
                  'company':[]
                  }