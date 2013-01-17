import sys, string
import re
from ucscGb.gbData.ordereddict import OrderedDict
from ucscGb.gbData.ra.raFile import RaFile
from ucscGb.gbData import ucscUtils
import collections


rafile = RaFile('../data/cvJan15.ra')
childOf = None
term = None
relationship = None

for key in rafile.keys():
    thisstanza = rafile[key]


    if thisstanza['type'] == 'Cell Line':
        if 'childOf' not in thisstanza:
            thisstanza['childOf'] = 'NA'
            relationship = 'NA'
        else: relationship = 'childOf'
        print thisstanza['term'],"\t",thisstanza['childOf'],"\t",relationship
