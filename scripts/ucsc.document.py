import sys, string
import re
from ucscGb.gbData.ordereddict import OrderedDict
from ucscGb.gbData.ra.raFile import RaFile
from ucscGb.gbData import ucscUtils
import collections


rafile = RaFile('../data/cvJan15.ra')
protocol = None
protocolPhrase = None
source = None
fileName = None
cell = None

for key in rafile.keys():
    thisstanza = rafile[key]

    if thisstanza['type'] == 'Cell Line':
        if 'protocol' not in thisstanza:
            thisstanza['protocol'] = 'null'
            continue
        protocolPhrase = thisstanza['protocol'].split()
        for i in range (0, len(protocolPhrase)):
            if 'missing' not in protocolPhrase[i]:
                source = protocolPhrase[i].split(":")
                cell = source[1].split("_")

        print source[1],"\tBIOSAMPLE_DOCUMENT\t",cell[0],"protocol\t","Future UCSD address","\tProtocol for the",cell[0],"biosample from",source[0]
        
            #Stam:HBMEC_Stam_protocol.pdf
        
