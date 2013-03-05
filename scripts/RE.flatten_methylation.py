#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Script to take Roadmap Epigenomics metadata as any number of XML files 
from GEO and count the number
of times each metadata term is used, by experiment, and write the result
to a tab-delimited file

Use:    termcount oufile.tsv infile1.xml infile2.xml ...

If outfile exists it will be over-written
"""

import sys, os, string, codecs
from collections import Counter, defaultdict
from lxml import etree      

#This is all of the possible fields
characteristic_fields = ["Sex", "batch", "biomaterial_provider", "biomaterial_type", "bisulfite_conversion_percent", "bisulfite_conversion_protocol", "blood_type", "cdna_preparation_first_strand_purification", "cdna_preparation_first_strand_synthesis_enzyme", "cdna_preparation_fragment_size_range", "cdna_preparation_fragmentation", "cdna_preparation_initial_rna_qnty", "cdna_preparation_polya_rna/", "cdna_preparation_purification", "cdna_preparation_second_strand_synthesis_dntp_mix", "cdna_preparation_second_strand_synthesis_enzyme", "cell type", "cell_type", "chip_antibody", "chip_antibody_catalog", "chip_antibody_lot", "chip_antibody_provider", "chip_protocol", "chip_protocol_antibody_amount", "chip_protocol_bead_amount", "chip_protocol_bead_type", "chip_protocol_chromatin_amount", "collection_method", "culture_conditions", "differentiation_method", "differentiation_stage", "disease", "dna_preparation_adaptor", "dna_preparation_adaptor_ligation_protocol", "dna_preparation_adaptor_sequence", "dna_preparation_fragment_size_range", "dna_preparation_initial_dna_qnty", "dna_preparation_post-ligation_fragment_size_selection", "dna_preparation_uracil_dna_glycosylase_digestion", "dnase_protocol", "donor_age", "donor_ethnicity", "donor_health_status", "donor_id", "donor_sex", "experiment_type", "extraction_protocol", "extraction_protocol_fragmentation", "extraction_protocol_mrna_enrichment", "extraction_protocol_smrna_enrichment", "extraction_protocol_sonication_cycles", "extraction_protocol_type_of_sonicator", "karyotype", "library_fragment_size_range", "library_fragmentation", "library_generation_pcr_f_primer_sequence", "library_generation_pcr_number_cycles", "library_generation_pcr_polymerase_type", "library_generation_pcr_primer", "library_generation_pcr_primer_conc", "library_generation_pcr_product_isolation_protocol", "library_generation_pcr_r_primer_sequence", "library_generation_pcr_template", "library_generation_pcr_template_conc", "library_generation_pcr_thermocycling_program", "line", "lineage", "location", "markers", "medip_antibody", "medip_antibody_catalog", "medip_antibody_lot", "medip_antibody_provider", "medip_protocol", "medip_protocol_antibody_amount", "medip_protocol_bead_amount", "medip_protocol_bead_type", "medip_protocol_dna_amount", "medium", "molecule", "mre_protocol", "mre_protocol_chromatin_amount", "mre_protocol_restriction_enzyme", "mre_protocol_size_fraction", "mrna_preparation_fragment_size_range", "mrna_preparation_initial_mrna_qnty", "note", "parity", "passage", "passage_if_expanded", "rna_preparation_3'_rna adapter_ligation_protocol", "rna_preparation_3'_rna_adapter_ligation_protocol", "rna_preparation_3'_rna_adapter_sequence", "rna_preparation_5'_dephosphorylation", "rna_preparation_5'_phosphorylation", "rna_preparation_5'_rna_adapter_ligation_protocol", "rna_preparation_5'_rna_adapter_sequence", "rna_preparation_initial_rna_qlty", "rna_preparation_initial_rna_qnty", "rna_preparation_reverse_transcription_primer_sequence", "rna_preparation_reverse_transcription_protocol", "sample alias", "sex", "size_fraction", "smrna_preparation_initial_smrna_qlty", "smrna_preparation_initial_smrna_qnty", "tissue_depot", "tissue_type", "sample common name"]


#characteristic_fields = ["Sex", "batch", "biomaterial_provider", "biomaterial_type", "blood_type", "cell type", "cell_type", "collection_method", "culture_conditions", "differentiation_method", "differentiation_stage", "disease", "donor_age", "donor_ethnicity", "donor_heal\
#th_status", "donor_id", "donor_sex", "karyotype", "line", "lineage", "location", "markers", "medium", "note", "parity", "passage", "passage_if_expanded", "sample alias", "sex", "tissue_depot", "tissue_type"]
#characteristic_fields = ["biomaterial_type", "cell_type", "cell type", "tissue_type", "sample common name","lineage", "sample alias", "batch"]

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
    with codecs.open(OUTFILE, mode='w', encoding='utf-8') as f:
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
                result = sample.findtext('Channel/Characteristics[@tag="experiment_type"]')
#                print result
                if result and "DNA Methylation" in result:
                    ss = ""
                    ss += sample.xpath("@iid")[0]
                    ss += "\t" + sample.findtext('Status/Submission-Date')
                    ss += "\t" + sample.findtext('Status/Release-Date')
                    ss += "\t" + sample.findtext('Status/Last-Update-Date')
                    ss += "\t" + sample.findtext('Title')
                    ss += "\t" + sample.findtext('Accession')
                    ss += "\t" + sample.findtext('Channel/Source')
                    ss += "\t" + sample.xpath('Channel/Organism/@taxid')[0]
                    ss += "\t\"" + sample.findtext('Description') + "\""
                    ss += "\t\"" + sample.findtext('Data-Processing') + "\""
                    ss += "\t\"" + sample.findtext('Library-Strategy') + "\""
                    ss += "\t\"" + sample.findtext('Library-Source') + "\""
                    ss += "\t\"" + sample.findtext('Instrument-Model') + "\""
                    for fieldname in characteristic_fields :
                        ss += "\t"
                        result = sample.findtext('Channel/Characteristics[@tag="' + fieldname + '"]')
                        if result:
                            ss += "\"" + result.strip() + "\""
#                   ss += "\t" + sample.findtext('Description').strip()
#                   ss += "\t" + sample.findtext('Library-Strategy')
#                   ss += "\t" + sample.findtext('Library-Source')
#                   ss += "\t" + sample.findtext('Library-Selection')
#                   print ss[:10]
                    print >> f, ss
