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


if __name__ == "__main__":

    SCRIPTNAME = os.path.basename(sys.argv[0])
    OUTFILE = sys.argv[1]
    INFILES = sys.argv[2:]

    #bsdict is the dictionary of biosample types with values that are Counter
    #objects to count the number of occurences of each metadata term
    bsdict = defaultdict(Counter)
    
    #tagcount counts global occurrences of tags
    tagcount = Counter()
    samplesprocessed = 0 #Total number of samples from all input files
    print "Processing " + str(len(INFILES)) + " files"
    for xmlFile in INFILES:
        # Parse the file
        parser = etree.XMLParser(ns_clean=True)
        tree = etree.parse(xmlFile, parser)

        #Do a few preliminary checks
        #Make sure all elements have a biosample_type
        badelements = tree.xpath(\
        '/MINiML/Sample[not(Channel/Characteristics/@tag="biomaterial_type")]')
        if badelements :
            print SCRIPTNAME + ": Warning " + xmlFile + \
            " has samples with no biomaterial_type"
            print len(badelements)

        # Pull out all the "Sample" elements from the current file
        samples = tree.xpath('//Sample')
        print "Found " + str(len(samples)) + " samples in " + xmlFile
        samplesprocessed += len(samples) #Keep track of total number of samples
        # Iterate through the samples
        for sample in samples :
            #Biosample types are in Characteristics/tag=biomaterial_type
            bstype = sample.xpath('Channel/Characteristics[@tag="biomaterial_type"]')
            #This pulls all the Characterstics tags for this sample
            tags = sample.xpath('Channel/Characteristics/@tag')
            #and this updates the global counts for the tags
            tagcount.update(tags)
            #and this updates the tag counts for the current biosample type
            bsdict[bstype[0].text].update(tags)

    print "Tallied these biosample types "
    print bsdict.keys()
    print "Processed " + str(samplesprocessed) + " samples"
    print "Found " + str(len(tagcount)) + " unique tags"

    #Write the tab-delimited output file
    print "Writing output to file " + OUTFILE
    with open(OUTFILE,"w") as f:
        headerstr = "characteristic\texample values\t"
        for bs in bsdict.keys() :
            headerstr += (bs.strip() + "\t")
        headerstr += "total"
        print >> f, headerstr
        for tag, i in tagcount.iteritems():
            linestr = tag + "\t\t"
            for bs in bsdict.keys() :
                countdict = bsdict[bs]
                bscount = countdict[tag]
                linestr += str(str(bscount) + "\t")
            linestr += str(i)
            print >> f, linestr
