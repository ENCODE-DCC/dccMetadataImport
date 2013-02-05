import sys, string
import re

docName = None
docType = "RUN_DOCUMENT"
docLabel = None
docFileName = "Future UCSD address"
description = None



techDocFile = open(sys.argv[1], "r")
allTechDocs = []
label = []

for line in techDocFile.readlines():
    allTechDocs.append(line)

for i in range (0,len(allTechDocs)):

# This stanza was used to break up the file name for metadata
#    rs = re.findall('[A-Z][^A-Z]*',allTechDocs[i])
#    fs = ""
#    for word in rs:
#        fs += "\t"+word
#    print fs

    docName = allTechDocs[i]
    label = docName.split("\t")

    print label[0],"\tRUN_DOCUMENT\t",label[1],"\tFuture UCSD address\tTechnical run document for the data file associated with",label[0]

#wgEncodeCshlLongRnaSeqA549CytosolPapProtocolRep4.pdf.gz
#wgEncodeCshlLongRnaSeqA549NucleusPapProtocolRep3.pdf.gz
