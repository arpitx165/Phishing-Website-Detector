import logging as log
import csv as CS
from Web_Url_Feature import Weburlfeature as WF
#import trainer as TR
class Fileoutput:
    def __init__(self):
        self.terminator = 0
    def outputWriter(self,list_url_feature,output_file):
        self.file_writer = open(output_file,'wb')
        self.terminator = 0
        for self.child in list_url_feature:
            #print child.keys()
            self.write_mode = CS.DictWriter(self.file_writer,self.child.keys())
            if self.terminator == 0 :
                self.write_mode.writeheader()
                self.terminator = 1
            self.write_mode.writerow(self.child)
        self.file_writer.close()
class Webmain:
    def __init__(self):
        self.list_url_feature = []
        self.url_address = ""
        self.url_features_dict = {}
    def TestUrl(self,url_address,output_file):
        self.url_address = url_address.strip()
        if len(self.url_address)!=0:
            print "Processig Request......"
            #self.url_features_reference = WF()
            #self.url_features_dict=self.url_features_reference.gettingFeature(self.url_address)
            self.url_features_dict = {}
            self.web_feature_reference = WF()
            self.url_features_dict = self.web_feature_reference.gettingFeature(self.url_address)
            #self.url_features_dict = WF.feature_extract(self.url_address)
            self.list_url_feature.append(self.url_features_dict)
            print self.url_features_dict
        self.file_output_reference = Fileoutput()
        self.file_output_reference.outputWriter(self.list_url_feature,output_file)
    def testUrlfile(self,input_file,output_file):
        self.file_reader = open(input_file,'r')
        for self.child in self.file_reader:
            self.url_address = self.child.strip()
            if len(self.url_address)!=0:
                print "Processig Request......"
                #self.url_features_reference = WF()
                #self.url_features_dict=self.url_features_reference.gettingFeature(self.url_address)
                self.url_features_dict = {}
                self.web_feature_reference = WF()
                self.url_features_dict = self.web_feature_reference.gettingFeature(self.url_address)
                #self.url_features_dict = WF.feature_extract(self.url_address)
                self.list_url_feature.append(self.url_features_dict)
                print self.url_features_dict
        self.file_reader.close()
        self.file_output_reference = Fileoutput()
        self.file_output_reference.outputWriter(self.list_url_feature,output_file)
if __name__ == '__main__':
    caller = Webmain()
    caller.testUrlfile('test.txt','test_features.csv')
    pass
