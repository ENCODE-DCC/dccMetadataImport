import sys, string
import re
from ucscGb.gbData.ordereddict import OrderedDict
from ucscGb.gbData.ra.raFile import RaFile
from ucscGb.gbData import ucscUtils
import collections


rafile = RaFile('../data/cvJan15.ra')
protocol = None
term = None

for key in rafile.keys():
    thisstanza = rafile[key]


    if thisstanza['type'] == 'Cell Line':
        if 'protocol' not in thisstanza:
            thisstanza['protocol'] = 'NA'
        print thisstanza['term'],"\t",thisstanza['protocol']
