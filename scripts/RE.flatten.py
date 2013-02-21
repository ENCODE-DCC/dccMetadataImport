#!/usr/bin/env python

"""
Script to take Roadmap Epigenomics metadata as any number of XML files 
from GEO and count the number
of times each metadata term is used, by experiment, and write the result
to a tab-delimited file

Use:    termcount oufile.tsv infile1.xml infile2.xml ...

If outfile exists it will be over-written
"""

import sys, os, string
from collections import Counter, defaultdict
from lxml import etree      

#characteristic_fields = ["Sex", "batch", "biomaterial_provider", "biomaterial_type", "blood_type", "cell type", "cell_type", "collection_method", "culture_conditions", "differentiation_method", "differentiation_stage", "disease", "donor_age", "donor_ethnicity", "donor_heal\
#th_status", "donor_id", "donor_sex", "karyotype", "line", "lineage", "location", "markers", "medium", "note", "parity", "passage", "passage_if_expanded", "sample alias", "sex", "tissue_depot", "tissue_type"]
characteristic_fields = ["biomaterial_type", "cell_type", "cell type", "tissue_type", "sample common name","lineage", "sample alias", "batch"]
if __name__ == "__main__":

    SCRIPTNAME = os.path.basename(sys.argv[0])
    OUTFILE = sys.argv[1]
    INFILES = sys.argv[2:]

    #sampledict is the dictionary of GEO samples that will be built from
    #the XML.  Keys will be GEO "GSM" numbers, each values will be a dictionary
    #of metadata terms, values
    sampledict = defaultdict(dict)
    
    #tagcount counts global occurrences of tags
    tagcount = Counter()
    samplesprocessed = 0 #Total number of samples from all input files
    print "Processing " + str(len(INFILES)) + " files"
    with open(OUTFILE, "w") as f:
        for xmlFile in INFILES:
            # Parse the file
            parser = etree.XMLParser(ns_clean=True)
            tree = etree.parse(xmlFile, parser)

            # Pull out all the "Sample" elements from the current file
            samples = tree.xpath('//Sample')
            print "Found " + str(len(samples)) + " samples in " + xmlFile
            samplesprocessed += len(samples) #Keep track of total number of samples
            # Iterate through the samples
            for sample in samples :
                ss = ""
                ss += sample.xpath("@iid")[0]
                ss += "\t" + sample.findtext('Status/Submission-Date')
                ss += "\t" + sample.findtext('Status/Release-Date')
                ss += "\t" + sample.findtext('Status/Last-Update-Date')
                ss += "\t" + sample.findtext('Title')
                ss += "\t" + sample.findtext('Accession')
                ss += "\t" + sample.findtext('Channel/Source')
                ss += "\t" + sample.xpath('Channel/Organism/@taxid')[0]
                for fieldname in characteristic_fields :
                    ss += "\t"
                    result = sample.findtext('Channel/Characteristics[@tag="' + fieldname + '"]')
                    if result:
                        ss += result.strip()
#                ss += "\t" + sample.findtext('Description').strip()
#                ss += "\t" + sample.findtext('Library-Strategy')
#                ss += "\t" + sample.findtext('Library-Source')
#                ss += "\t" + sample.findtext('Library-Selection')
#                print ss[:10]
                print >> f, ss
