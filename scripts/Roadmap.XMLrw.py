# XMLrw
# Read XML file, extract relevant data, write to file
# This script is being written by Drew Erickson for the
# Roadmap Epigenomics metadata transformation project.

# 'os' is used to find files
import os
# 'lxml' is used to read in and extract XML data
from lxml import etree
# 'csv' is used to write csv files
import csv


def main():

    # get list of files in directory
    # LIMITATION: requires knowledge of file location.  should allow for input.
    dirfiles = "./../data/roadmap/"     # specific data directory
    filesin = os.listdir(dirfiles)

    # Get metadata from XML files (SPECIFICALLY, 'Sample' entries)
    inputlist = GetMetadata(dirfiles,filesin)

    # Get metadata lists for Antibodies
    [entrylist,entrylist_unique] = GetAntibody(inputlist)

    # write data to CSV file
    CSVw(entrylist,dirfiles,'Antibody.List.Complete.csv')
    CSVw(entrylist_unique,dirfiles,'Antibody.List.Unique.csv')


# A class for 
class Metadata(list):
    """
    A list of metadata in an ElementTree.
    
    This class could be sued to add structures needed for transformations
    
    For future development; not yet utilized
    """

  
def GetMetadata(dirfiles,filesin):
    """
    Reads in an XML file to an ElementTree
    """

    # iterate of the list of files, find the XML files, then save them as etree
    inputlist = []
    for filenext in filesin:
        # LIMITATION: should allow for search term instead of fixed .xml extension
        if filenext.endswith(".xml") and type(filenext) == type(''):
            root = etree.parse(dirfiles + filenext)
            
            # LIMITATION: requires knowledge of namespace.  Need to search XML for namespace value.
            # LIMITATION: GEO-Specific.  finds instances of 'Sample' for easier parsing later.  should be more generic.
            samples = root.xpath('//ns:Sample',namespaces={'ns':'http://www.ncbi.nlm.nih.gov/geo/info/MINiML'})
            for sample in samples:
                inputlist.append(sample)

    return inputlist


def GetAntibody(inputlist):
    """
    Finds entries for Antibodies and returns them in complete and unique lists.
    """

    # for each list element, extract the relevant antibody data
    # LIMITATION: requires knowledge of namespace.  Need to search XML for namespace value.
    # LIMITATION: requires knowledge of element tree.  Need to determine structure.
    # LIMITATION: requires knowledge of attribute names.  Need to find attributes.
    antibody_list = []
    antibody_list_unique = []
    for element in inputlist:
        if element.xpath('ns:Channel/ns:Characteristics/@tag="chip_antibody"',namespaces={'ns':'http://www.ncbi.nlm.nih.gov/geo/info/MINiML'}):
            antibody_name = element.find('ns:Channel/*[@tag="chip_antibody"]',namespaces={'ns':'http://www.ncbi.nlm.nih.gov/geo/info/MINiML'}).text
            antibody_provider = element.find('ns:Channel/*[@tag="chip_antibody_provider"]',namespaces={'ns':'http://www.ncbi.nlm.nih.gov/geo/info/MINiML'}).text
            antibody_catalog = element.find('ns:Channel/*[@tag="chip_antibody_catalog"]',namespaces={'ns':'http://www.ncbi.nlm.nih.gov/geo/info/MINiML'}).text
            antibody_lot = element.find('ns:Channel/*[@tag="chip_antibody_lot"]',namespaces={'ns':'http://www.ncbi.nlm.nih.gov/geo/info/MINiML'}).text
            antibody_list.append([element.attrib.get('iid'),antibody_name,antibody_provider,antibody_catalog,antibody_lot])
            antibody_list_unique.append([antibody_name,antibody_provider,antibody_catalog,antibody_lot])
        elif element.xpath('ns:Channel/ns:Characteristics/@tag="medip_antibody"',namespaces={'ns':'http://www.ncbi.nlm.nih.gov/geo/info/MINiML'}):
            antibody_name = element.find('ns:Channel/*[@tag="medip_antibody"]',namespaces={'ns':'http://www.ncbi.nlm.nih.gov/geo/info/MINiML'}).text
            antibody_provider = element.find('ns:Channel/*[@tag="medip_antibody_provider"]',namespaces={'ns':'http://www.ncbi.nlm.nih.gov/geo/info/MINiML'}).text
            antibody_catalog = element.find('ns:Channel/*[@tag="medip_antibody_catalog"]',namespaces={'ns':'http://www.ncbi.nlm.nih.gov/geo/info/MINiML'}).text
            antibody_lot = element.find('ns:Channel/*[@tag="medip_antibody_lot"]',namespaces={'ns':'http://www.ncbi.nlm.nih.gov/geo/info/MINiML'}).text
            antibody_list.append([element.attrib.get('iid'),antibody_name,antibody_provider,antibody_catalog,antibody_lot])
            antibody_list_unique.append([antibody_name,antibody_provider,antibody_catalog,antibody_lot])

    antibody_list_unique = [list(entry) for entry in set(tuple(entry) for entry in antibody_list_unique)]
 
    
    return antibody_list, antibody_list_unique


def CSVw(entrylist,dirfiles,outfile):
    """
    Writes list to CSV file.
    """

    writer = csv.writer(open(dirfiles + outfile, 'wb'))

    for row in entrylist:
        writer.writerow(row)


if __name__ == '__main__':
    main()