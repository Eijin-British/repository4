######################################################################################
### Author/Developer: Nicolas CHEN
### Filename: export.py
### Version: 1.0
### Field of research: Deep Learning in medical imaging
### Purpose: This Python script creates the CSV file from XML files.
### Output: This Python script creates the file "test.csv"
### with all data needed: filename, class_name, x1,y1,x2,y2

######################################################################################
### HISTORY
### Version | Date          | Author       | Evolution
### 1.0     | 17/11/2018    | Nicolas CHEN | Initial version
######################################################################################

import os, sys, random
import xml.etree.ElementTree as ET
from glob import glob
import pandas as pd
from shutil import copyfile

annotations = glob('Harmonia-axyridis/Annotations/*.xml')

df = []
cnt = 0
for file in annotations:
    #filename = file.split('/')[-1].split('.')[0] + '.jpg'
    #filename = str(cnt) + '.jpg'
    filename = file.split('