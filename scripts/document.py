import sys, string
import re
from ucscGb.gbData.ordereddict import OrderedDict
from ucscGb.gbData.ra.raFile import RaFile
from ucscGb.gbData import ucscUtils
import collections


rafile = RaFile('../data/cvJan15.ra')
protocol = None
description = None
validation = None
antibodyDescription = None
targetDescription = None
label = None
term = None
vendorName = None
vendorId = None

for key in rafile.keys():
    thisstanza = rafile[key]

    if thisstanza['type'] == 'Cell Line':
        if 'protocol' not in thisstanza:
            thisstanza['protocol'] = 'NA'
        print thisstanza['protocol'],"\tBIOSAMPLE_DOCUMENT\t",thisstanza['term'],thisstanza['vendorName'],thisstanza['vendorId'],thisstanza['description']

    if thisstanza['type'] == 'Antibody':
        if 'validation' not in thisstanza:
            thisstanza['validation'] = 'NA'
        if 'label' not in thisstanza:
            thisstanza['label'] = 'NA'
        print thisstanza['validation'],"\tANTIBODY_DOCUMENT\t",thisstanza['label'],"  antibodyDescription  ",thisstanza['antibodyDescription'],"  targetDescription  ",thisstanza['targetDescription']

