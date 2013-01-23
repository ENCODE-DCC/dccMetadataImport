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
            #print "mouse\tMus\tmusculus\t",thisstanza['strain'],"\t",thisstanza['term'],"10090"
            print "mouse\tMus\tmusculus\t",thisstanza['strain'],"\tnull\t","10090"
            #the listOfAllMouseTerms came from this script just printing thisstanza['term'],",\n"
            #queried metaDb with a bash script for buried strains
            #where MICE= "listOfAllMouseTerms"
            #for i in $MICE; do /cluster/bin/x86_64/mdbPrint mm9 -vars="cell=$i" | grep 'strain' | sort -u >> ORGANISM_STRAINS.txt; done
            #added in the few "buried strains"            
