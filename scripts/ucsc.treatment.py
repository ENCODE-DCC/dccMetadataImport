import sys, string
import re
from ucscGb.gbData.ordereddict import OrderedDict
from ucscGb.gbData.ra.raFile import RaFile
from ucscGb.gbData import ucscUtils
import collections


rafile = RaFile('../data/cvJan15.ra')
treatment = 0

for key in rafile.keys():
    thisstanza = rafile[key]


    if thisstanza['type'] == 'treatment':
        print thisstanza['term']
