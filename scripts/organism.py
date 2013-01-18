import sys, string
import re
from ucscGb.gbData.ordereddict import OrderedDict
from ucscGb.gbData.ra.raFile import RaFile
from ucscGb.gbData import ucscUtils
import collections


rafile = RaFile('../data/cvJan15.ra')
strain = None
term = None
organism = None
type = None

for key in rafile.keys():
    thisstanza = rafile[key]

    if thisstanza['type'] == 'Cell Line':
        if thisstanza['organism'] == 'mouse':
            print "mouse\tMus\tmusculus\t",thisstanza['strain'],"\t",thisstanza['term'],"10090"
