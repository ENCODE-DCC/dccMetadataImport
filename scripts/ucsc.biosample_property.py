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
        if 'tier' not in thisstanza:
            thisstanza['tier'] = 'missing'
        if 'age' not in thisstanza:
            thisstanza['age'] = 'missing'
        if 'orderUrl' not in thisstanza:	
            thisstanza['orderUrl'] = 'missing'
        if 'karyotype' not in thisstanza:	
            thisstanza['karyotype'] = 'missing'
        print thisstanza['term'],"\torderUrl\t",thisstanza['orderUrl'],"\n",thisstanza['term'],"\tsex\t",thisstanza['sex'],"\n",thisstanza['term'],"\tage\t",thisstanza['age'],"\n",thisstanza['term'],"\tkaryotype\t",thisstanza['karyotype'],"\n",thisstanza['term'],"\ttier\t",thisstanza['tier']
