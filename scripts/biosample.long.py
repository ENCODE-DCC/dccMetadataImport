import sys, string
import re
from ucscGb.gbData.ordereddict import OrderedDict
from ucscGb.gbData.ra.raFile import RaFile
from ucscGb.gbData import ucscUtils
import collections


rafile = RaFile('../data/cvJan15.ra')
metaObject = 0
expId = 0
term = 0
type = 0

for key in rafile.keys():
    thisstanza = rafile[key]


    if thisstanza['type'] == 'Cell Line':
        if 'category' not in thisstanza:	
            thisstanza['category'] = 'missing'
        if 'treatment' not in thisstanza:	
            thisstanza['treatment'] = 'missing'
        if 'lots' not in thisstanza:
            thisstanza['lots'] = 'missing'
        if 'subcellularLoc' not in thisstanza:	
            thisstanza['subcellularLoc'] = 'missing'
        if 'tier' not in thisstanza:
            thisstanza['tier'] = 'missing'
        if 'age' not in thisstanza:
            thisstanza['age'] = 'missing'
        if 'orderUrl' not in thisstanza:	
            thisstanza['orderUrl'] = 'missing'
        if 'karyotype' not in thisstanza:	
            thisstanza['karyotype'] = 'missing'
        print thisstanza['termId'],"\t",thisstanza['term'],"\t",thisstanza['tag'],"\t",thisstanza['category'],"\t",thisstanza['organism'],"\t",thisstanza['treatment'],"\t",thisstanza['vendorName'],"\t",thisstanza['vendorId'],"\t",thisstanza['lots'],"\t",thisstanza['subcellularLoc'],"\t",thisstanza['orderUrl'],"\t",thisstanza['sex'],"\t",thisstanza['age'],"\t",thisstanza['protocol'],"\t",thisstanza['karyotype'],"\t",thisstanza['tier']
