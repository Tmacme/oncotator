"""
# By downloading the PROGRAM you agree to the following terms of use:
#
# BROAD INSTITUTE SOFTWARE LICENSE AGREEMENT
# FOR ACADEMIC NON-COMMERCIAL RESEARCH PURPOSES ONLY
#
# This Agreement is made between the Broad Institute, Inc. with a principal address at 7 Cambridge Center, Cambridge, MA 02142 ("BROAD") and the LICENSEE and is effective at the date the downloading is completed ("EFFECTIVE DATE").
# WHEREAS, LICENSEE desires to license the PROGRAM, as defined hereinafter, and BROAD wishes to have this PROGRAM utilized in the public interest, subject only to the royalty-free, nonexclusive, nontransferable license rights of the United States Government pursuant to 48 CFR 52.227-14; and
# WHEREAS, LICENSEE desires to license the PROGRAM and BROAD desires to grant a license on the following terms and conditions.
# NOW, THEREFORE, in consideration of the promises and covenants made herein, the parties hereto agree as follows:
#
# 1. DEFINITIONS
# 1.1	"PROGRAM" shall mean copyright in the object code and source code known as Oncotator and related documentation, if any, as they exist on the EFFECTIVE DATE and can be downloaded from http://www.broadinstitute.org/cancer/cga/oncotator on the EFFECTIVE DATE.
#
# 2. LICENSE
# 2.1   Grant. Subject to the terms of this Agreement, BROAD hereby grants to LICENSEE, solely for academic non-commercial research purposes, a non-exclusive, non-transferable license to: (a) download, execute and display the PROGRAM and (b) create bug fixes and modify the PROGRAM.
# LICENSEE hereby automatically grants to BROAD a non-exclusive, royalty-free, irrevocable license to any LICENSEE bug fixes or modifications to the PROGRAM with unlimited rights to sublicense and/or distribute.  LICENSEE agrees to provide any such modifications and bug fixes to BROAD promptly upon their creation.
# The LICENSEE may apply the PROGRAM in a pipeline to data owned by users other than the LICENSEE and provide these users the results of the PROGRAM provided LICENSEE does so for academic non-commercial purposes only.  For clarification purposes, academic sponsored research is not a commercial use under the terms of this Agreement.
# 2.2  No Sublicensing or Additional Rights. LICENSEE shall not sublicense or distribute the PROGRAM, in whole or in part, without prior written permission from BROAD.  LICENSEE shall ensure that all of its users agree to the terms of this Agreement.  LICENSEE further agrees that it shall not put the PROGRAM on a network, server, or other similar technology that may be accessed by anyone other than the LICENSEE and its employees and users who have agreed to the terms of this agreement.
# 2.3  License Limitations. Nothing in this Agreement shall be construed to confer any rights upon LICENSEE by implication, estoppel, or otherwise to any computer software, trademark, intellectual property, or patent rights of BROAD, or of any other entity, except as expressly granted herein. LICENSEE agrees that the PROGRAM, in whole or part, shall not be used for any commercial purpose, including without limitation, as the basis of a commercial software or hardware product or to provide services. LICENSEE further agrees that the PROGRAM shall not be copied or otherwise adapted in order to circumvent the need for obtaining a license for use of the PROGRAM.
#
# 3. OWNERSHIP OF INTELLECTUAL PROPERTY
# LICENSEE acknowledges that title to the PROGRAM shall remain with BROAD. The PROGRAM is marked with the following BROAD copyright notice and notice of attribution to contributors. LICENSEE shall retain such notice on all copies.  LICENSEE agrees to include appropriate attribution if any results obtained from use of the PROGRAM are included in any publication.
#
# Copyright 2012 Broad Institute, Inc.
# Notice of attribution:  The Oncotator program was made available through the generosity of the Cancer Genome Analysis group at the Broad Institute, Inc.
#
# LICENSEE shall not use any trademark or trade name of BROAD, or any variation, adaptation, or abbreviation, of such marks or trade names, or any names of officers, faculty, students, employees, or agents of BROAD except as states above for attribution purposes.
#
# 4. INDEMNIFICATION
# LICENSEE shall indemnify, defend, and hold harmless BROAD, and their respective officers, faculty, students, employees, associated investigators and agents, and their respective successors, heirs and assigns, ("Indemnitees"), against any liability, damage, loss, or expense (including reasonable attorneys fees and expenses) incurred by or imposed upon any of the Indemnitees in connection with any claims, suits, actions, demands or judgments arising out of any theory of liability (including, without limitation, actions in the form of tort, warranty, or strict liability and regardless of whether such action has any factual basis) pursuant to any right or license granted under this Agreement.
#
# 5. NO REPRESENTATIONS OR WARRANTIES
# THE PROGRAM IS DELIVERED "AS IS."  BROAD MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND CONCERNING THE PROGRAM OR THE COPYRIGHT, EXPRESS OR IMPLIED, INCLUDING, WITHOUT LIMITATION, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NONINFRINGEMENT, OR THE ABSENCE OF LATENT OR OTHER DEFECTS, WHETHER OR NOT DISCOVERABLE. BROAD EXTENDS NO WARRANTIES OF ANY KIND AS TO PROGRAM CONFORMITY WITH WHATEVER USER MANUALS OR OTHER LITERATURE MAY BE ISSUED FROM TIME TO TIME.
# IN NO EVENT SHALL BROAD OR ITS RESPECTIVE DIRECTORS, OFFICERS, EMPLOYEES, AFFILIATED INVESTIGATORS AND AFFILIATES BE LIABLE FOR INCIDENTAL OR CONSEQUENTIAL DAMAGES OF ANY KIND, INCLUDING, WITHOUT LIMITATION, ECONOMIC DAMAGES OR INJURY TO PROPERTY AND LOST PROFITS, REGARDLESS OF WHETHER BROAD SHALL BE ADVISED, SHALL HAVE OTHER REASON TO KNOW, OR IN FACT SHALL KNOW OF THE POSSIBILITY OF THE FOREGOING.
#
# 6. ASSIGNMENT
# This Agreement is personal to LICENSEE and any rights or obligations assigned by LICENSEE without the prior written consent of BROAD shall be null and void.
#
# 7. MISCELLANEOUS
# 7.1 Export Control. LICENSEE gives assurance that it will comply with all United States export control laws and regulations controlling the export of the PROGRAM, including, without limitation, all Export Administration Regulations of the United States Department of Commerce. Among other things, these laws and regulations prohibit, or require a license for, the export of certain types of software to specified countries.
# 7.2 Termination. LICENSEE shall have the right to terminate this Agreement for any reason upon prior written notice to BROAD. If LICENSEE breaches any provision hereunder, and fails to cure such breach within thirty (30) days, BROAD may terminate this Agreement immediately. Upon termination, LICENSEE shall provide BROAD with written assurance that the original and all copies of the PROGRAM have been destroyed, except that, upon prior written authorization from BROAD, LICENSEE may retain a copy for archive purposes.
# 7.3 Survival. The following provisions shall survive the expiration or termination of this Agreement: Articles 1, 3, 4, 5 and Sections 2.2, 2.3, 7.3, and 7.4.
# 7.4 Notice. Any notices under this Agreement shall be in writing, shall specifically refer to this Agreement, and shall be sent by hand, recognized national overnight courier, confirmed facsimile transmission, confirmed electronic mail, or registered or certified mail, postage prepaid, return receipt requested.  All notices under this Agreement shall be deemed effective upon receipt.
# 7.5 Amendment and Waiver; Entire Agreement. This Agreement may be amended, supplemented, or otherwise modified only by means of a written instrument signed by all parties. Any waiver of any rights or failure to act in a specific instance shall relate only to such instance and shall not be construed as an agreement to waive any rights or fail to act in any other instance, whether or not similar. This Agreement constitutes the entire agreement among the parties with respect to its subject matter and supersedes prior agreements or understandings between the parties relating to its subject matter.
# 7.6 Binding Effect; Headings. This Agreement shall be binding upon and inure to the benefit of the parties and their respective permitted successors and assigns. All headings are for convenience only and shall not affect the meaning of any provision of this Agreement.
# 7.7 Governing Law. This Agreement shall be construed, governed, interpreted and applied in accordance with the internal laws of the Commonwealth of Massachusetts, U.S.A., without regard to conflict of laws principles.
#"""
from TestUtils import TestUtils
from oncotator.input.VcfInputMutationCreator import VcfInputMutationCreator


"""
Created on Nov 8, 2012

@author: lichtens
"""
import unittest

import logging 
from oncotator.utils.ConfigUtils import ConfigUtils
from oncotator.MutationData import MutationData
from oncotator.Annotator import Annotator
from oncotator.output.TcgaMafOutputRenderer import TcgaMafOutputRenderer
from oncotator.utils.OncotatorCLIUtils import OncotatorCLIUtils
import os
from oncotator.utils.GenericTsvReader import GenericTsvReader
from oncotator.DatasourceCreator import DatasourceCreator

TestUtils.setupLogging(__file__, __name__)
class TcgaMafOutputRendererTest(unittest.TestCase):
    _multiprocess_can_split_ = True

    """ These are the default overrides for generating a TCGA MAF file.  These will appear on all mutations, but are here for a test.
        These were taken from version 0.5.25.0 of Oncotator.
    """
    TCGA_MAF_DEFAULTS = {'NCBI_Build':'37','Strand':"+",'Center':'broad.mit.edu','source':'Capture', 'status':'Somatic', 'phase':'Phase_I', 'sequencer':'Illumina GAIIx',
                  'Tumor_Validation_Allele1': '', 'Tumor_Validation_Allele2': '', 'Match_Norm_Validation_Allele1': '', 'Match_Norm_Validation_Allele2': '',
                  'Verification_Status': '','Validation_Status': '', 'Validation_Method': '', 'Score': '', 'BAM_file': '',
                  'Match_Norm_Seq_Allele1':'', 'Match_Norm_Seq_Allele2':''}

    def setUp(self):
        self.logger = logging.getLogger(__name__)
        self.config = TestUtils.createUnitTestConfig()
        pass

    def tearDown(self):
        pass

    def _createGafDataSource(self):
        
        self.logger.info("Initializing gaf 3.0")
        return TestUtils.createGafDatasource(self.config)

    def testSimpleVersionString(self):
        tmp = TcgaMafOutputRenderer('dummy', configFile='configs/tcgaMAF2.4_output.config')
        tmp.getOncotatorHeaderVersionString()
        pass


    def _validateTcgaMafContents(self, filename):
        """ This is a utility, private method for unit tests to get a semblance that a valid maf file was created.  
        
        Note: This method has nothing to do with the TCGA validator.
        
        """
        configFile = ConfigUtils.createConfigParser('configs/tcgaMAF2.4_output.config')
        statinfo = os.stat(filename)
        self.assertTrue(statinfo.st_size > 0, "Generated MAF file (" + filename + ") is empty.")
        
        tsvReader = GenericTsvReader(filename)
        
        self.assertTrue(tsvReader.getComments().find('#version') <> -1, "First line did not specify a version number")

        ctr = 1
        for lineDict in tsvReader:
            if lineDict['Entrez_Gene_Id'] == "0":
                self.assertTrue(lineDict['Hugo_Symbol'] == "Unknown", "Entrez_Gene_Id was zero, but Hugo Symbol was not 'Unknown'.  Line: " + str(ctr))
            
            unknownKeys = []
            for k in lineDict.keys():
                if lineDict[k] == "__UNKNOWN__":
                    unknownKeys.append(k)

                self.assertTrue('\r' not in lineDict[k], "Carriage return character found in an annotation value.")

                requiredColumns = configFile.get("general", "requiredColumns")
                optionalColumns = configFile.get("general", "optionalColumns")
                exposedColumns = configFile.get("general", "exposedColumns")
                if (k not in requiredColumns) and (k not in optionalColumns) and (k not in exposedColumns):
                    self.assertTrue(k.startswith("i_"), "Internal column was not prepended with 'i_'")
                
            unknownKeys.sort()
            self.assertTrue(len(unknownKeys) == 0, "__UNKNOWN__ values (" + str(len(unknownKeys)) + ") seen on line " + str(ctr) + ", in fields: " + ", ".join(unknownKeys))
            
            ctr += 1

    def _determine_db_dir(self):
        return self.config.get('DEFAULT',"dbDir")

    def _annotateTest(self, inputFilename, outputFilename, datasource_dir, inputFormat="MAFLITE", outputFormat="TCGAMAF", default_annotations=TCGA_MAF_DEFAULTS, override_annotations={}):
        self.logger.info("Initializing Annotator...")
        annotator = Annotator()
        runSpec = OncotatorCLIUtils.create_run_spec(inputFormat, outputFormat, inputFilename, outputFilename, defaultAnnotations=default_annotations, datasourceDir=datasource_dir, globalAnnotations=override_annotations)
        annotator.initialize(runSpec)
        self.logger.info("Annotation starting...")
        return annotator.annotate()

    def testVersionString(self):
        """ Simple test of the Oncotator header string """   
        gafDatasource = TestUtils.createGafDatasource(self.config)
        outputRenderer = TcgaMafOutputRenderer("out/testVersion.maf.tsv", configFile='configs/tcgaMAF2.4_output.config', datasources=[gafDatasource.title + gafDatasource.version])
        tmp = outputRenderer.getOncotatorHeaderVersionString()
        print tmp
    
    def testFullSNPOutput(self):
        """ Create a TCGA MAF from a SNP TSV file."""
        self.logger.info("Initializing Maflite SNP Test...")
        
        testOutputFilename = self._annotateTest('testdata/maflite/Patient0.snp.maf.txt', "out/testSNP_v2.4.maf.tsv", self._determine_db_dir())

        # Sanity checks to make sure that the generated maf file is not junk.
        self._validateTcgaMafContents(testOutputFilename)

    def testFullIndelOutput(self):
        """ Create a TCGA MAF from an Indel TSV file."""
        self.logger.info("Initializing Maflite indel Test...")
        
        testOutputFilename = self._annotateTest('testdata/maflite/Patient0.indel.maf.txt', "out/testIndel_v2.4.maf.tsv", self._determine_db_dir())
        
        # Sanity checks to make sure that the generated maf file is not junk.
        self._validateTcgaMafContents(testOutputFilename)

    def testEmptyInput(self):
        """ Create a TCGA MAF from an empty maflite file."""

        testOutputFilename = self._annotateTest('testdata/maflite/empty.maflite', "out/empty.maf.tsv", self._determine_db_dir())

        # Sanity checks to make sure that the generated maf file is not junk.
        self._validateTcgaMafContents(testOutputFilename)


    def testInternalFields(self):
        """ Test that an annotation that is not listed explicitly in the required or optional columns is rendered with i_ prepended """
        outputFilename = "out/testInternalFields_v2.4.maf.tsv"
        m = MutationData()
        m.createAnnotation("TEST", "THIS IS A TEST", "TESTING")
        
        # The next annotation is real and should not be considered internal.
        m.createAnnotation("gene", "EGFR")
        
        outputRenderer = TcgaMafOutputRenderer(outputFilename, configFile='configs/tcgaMAF2.4_output.config')
        outputRenderer.renderMutations(iter([m]), ['No comments'])
        
        configFile = ConfigUtils.createConfigParser('configs/tcgaMAF2.4_output.config')
        requiredColumns = configFile.get("general", "requiredColumns")
        self.assertTrue("Hugo_Symbol" in requiredColumns, " This test assumes that Hugo_Symbol is a required column in the TCGA MAF.  If not, the test must be modified.")

        statinfo = os.stat(outputFilename)
        self.assertTrue(statinfo.st_size > 0, "Generated MAF file (" + outputFilename + ") is empty.")
        
        tsvReader = GenericTsvReader(outputFilename)
        headers = tsvReader.getFieldNames()
        self.assertTrue("Hugo_Symbol" in headers, "Hugo_Symbol not found in output headers")
        self.assertTrue("TEST" not in headers, "TEST was found in output headers when it should have been renamed to i_TEST")
        self.assertTrue("i_TEST" in headers, "i_TEST not found in output headers")
        
    def testMutationDatasources(self):
        """ Test that we can create a simple TSV output from all of the current datasources (specified in the config file).  Note that no validation is done.  Simply that the output file was created. 
        TODO: This unit test needs to be moved."""
        testOutputFilename = self._annotateTest('testdata/maflite/Patient0.snp.maf.txt', "out/testsimpleSNP.maf.tsv", self._determine_db_dir(), outputFormat="SIMPLE_TSV")
        self.assertTrue(os.path.exists(testOutputFilename))

    def testExposedColumns(self):
        """Test that columns listed in the config file as exposed do not get the i_ prepend"""
        testOutputFilename = self._annotateTest('testdata/maflite/tiny_maflite.maf.txt', "out/testExposedCols.maf.tsv", self._determine_db_dir())

        # Sanity checks to make sure that the generated maf file is not junk.
        self._validateTcgaMafContents(testOutputFilename)

        # Check the columns, since the input has a couple of exposed columns.
        tsvReader = GenericTsvReader(testOutputFilename)
        headers = tsvReader.getFieldNames()
        headersToCheck = ['t_alt_count', 't_ref_count']
        for h in headersToCheck:
            self.assertFalse(("i_" + h) in headers, "i_ was prepended to " + h)
            self.assertTrue(h in headers, h + " not found.")

    def testProperConversionVcfToMaf(self):
        """Test that ref, alt, and positions are properly populated in a TCGA MAF generated from a VCF """

        # For this conversion, you must specify the barcodes manually
        override_annotations = TcgaMafOutputRendererTest.TCGA_MAF_DEFAULTS
        override_annotations.update({'tumor_barcode':'Patient0-Tumor', 'normal_barcode':'Patient0-Normal'})

        outputFilename = self._annotateTest('testdata/vcf/Patient0.somatic.strelka.indels.vcf', "out/testConversionFromVCF.maf.annotated", self._determine_db_dir(), inputFormat="VCF", outputFormat="TCGAMAF", override_annotations=override_annotations)

        # Sanity checks to make sure that the generated maf file is not junk.
        self._validateTcgaMafContents(outputFilename)

        # Check to make sure that the ref and alt are correct for a TCGA MAF.
        tsvReader = GenericTsvReader(outputFilename)

        ctr = 0

        for line_dict in tsvReader:
            ref = line_dict['Reference_Allele']
            alt = line_dict['Tumor_Seq_Allele2']

            # INS
            if len(alt) > len(ref):
                self.assertTrue(ref == "-", "Invalid insertion with " + ref + "  " + alt)

            # DEL
            if len(ref) > len(alt):
                self.assertTrue(alt == "-", "Invalid deletion with " + ref + "  " + alt)

            self.assertTrue(line_dict['Start_position'] in ["10089935", "57493929", "155301010", "64948170", "64948167"])
            self.assertTrue(line_dict['Reference_Allele'] in ["-", "TC", "A", "TTT"])
            self.assertTrue(line_dict['Tumor_Seq_Allele2'] in ["-", "TC", "G", "T"])
            self.assertTrue(line_dict['Matched_Norm_Sample_Barcode'] == "Patient0-Normal")
            self.assertTrue(line_dict['Matched_Norm_Sample_UUID'] == "Patient0-Normal")
            self.assertTrue(line_dict['Tumor_Sample_Barcode'] == "Patient0-Tumor")
            self.assertTrue(line_dict['Tumor_Sample_UUID'] == "Patient0-Tumor")
            ctr += 1

        self.assertTrue(ctr == 8, str(ctr) + " mutations found, but should have been 8." )

    def testProperConversionVcfToMafWithThirdSample(self):
        """Test that ref, alt, and positions are properly populated in a TCGA MAF generated from a VCF and that the NORMAL is ignored. """

        # For this conversion, you must specify the barcodes manually
        override_annotations = TcgaMafOutputRendererTest.TCGA_MAF_DEFAULTS
        override_annotations.update({'tumor_barcode':'Patient0-Tumor', 'normal_barcode':'Patient0-Normal'})

        outputFilename = self._annotateTest('testdata/vcf/Patient0.somatic.strelka.indels.met.vcf', "out/testConversionFromVCFv2.maf.annotated", self._determine_db_dir(), inputFormat="VCF", outputFormat="TCGAMAF", override_annotations=override_annotations)

        # Sanity checks to make sure that the generated maf file is not junk.
        self._validateTcgaMafContents(outputFilename)

        # Check to make sure that the ref and alt are correct for a TCGA MAF.
        tsvReader = GenericTsvReader(outputFilename)

        ctr = 0

        for line_dict in tsvReader:
            self.assertTrue(line_dict['Matched_Norm_Sample_Barcode'] == "Patient0-Normal")
            self.assertTrue(line_dict['Matched_Norm_Sample_UUID'] == "Patient0-Normal")
            self.assertTrue(line_dict['Tumor_Sample_Barcode'] == "Patient0-Tumor")
            self.assertTrue(line_dict['Tumor_Sample_UUID'] == "Patient0-Tumor")
            ctr += 1

        self.assertTrue(ctr == 16, str(ctr) + " mutations found, but should have been 16." )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSimpleVersionString']
    unittest.main()