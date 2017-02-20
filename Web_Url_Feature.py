import re
import urllib,urllib2
from xml.dom import minidom
import csv
import pygeoip
from urlparse import urlparse
class Apidata:
    def __init__(self):
        self.url_rank = []
        self.app_req = {}
        pass
    def Fetchinfo(self,api_dom,api_element,api_attrib):
        for child in api_dom.getElementsByTagName(api_element):
            if child.hasAttribute(api_attrib):
                return child.attributes[api_attrib].value
                break
        return -1
    def Urlrank(self,url_host):
        #print url_host
        self.api_path = 'http://data.alexa.com/data?cli=10&dat=snbamz&url='+url_host
        try:
            self.api_xml = urllib2.urlopen(self.api_path)
            self.api_dom = minidom.parse(self.api_xml)
            self.url_rank.append(self.Fetchinfo(self.api_dom,'REACH','RANK'))
            self.url_rank.append(self.Fetchinfo(self.api_dom,'COUNTRY','RANK'))
            return self.url_rank
        except :
            return[-1,-1]
    def Urlsafebrowsing(self,url_address):
        self.app_api_key = "ABQIAAAA8C6Tfr7tocAe04vXo5uYqRTEYoRzLFR0-nQ3fRl5qJUqcubbrw"
        self.app_name = "Phishing-Website-Detector"
        self.app_ver = "1.0"
        self.app_req = {}
        self.app_req["client"] = self.app_name
        self.app_req["apikey"] = self.app_api_key
        self.app_req["appver"] = self.app_ver
        self.app_req["pver"] = "3.0"
        self.app_req["url"] = url_address #change to check type of url

        try:
            self.url_params = urllib.urlencode(self.app_req)
            self.app_req_url = "https://sb-ssl.google.com/safebrowsing/api/lookup?"+self.url_params
            self.app_res = urllib2.urlopen(self.app_req_url)
            if self.app_res.code==200:
                print "The queried URL is either phishing, malware or both, see the response body for the specific type."
                return 1
            elif self.app_res.code==204:
                print "The requested URL is legitimate, no response body returned."
                return 0
            elif self.app_res.code==400:
                print "Bad Request The HTTP request was not correctly formed."

            elif self.app_res.code==401:
                print "Not Authorized The apikey is not authorized"
            else:
                print "Service Unavailable The server cannot handle the request. Besides the normal server failures, it could also indicate that the client has been throttled by sending too many requests"
        except:
            return -1
class Weburlfeature():
    def __init__(self):
        self.feature_extracted = {}
        self.token_words = ""
        self.url_netloc = ""
        self.url_path = ""
        self.url_rank = []
        pass
    def Urlsecurity(self,url_token):
        url_security_words=['confirm', 'account', 'banking', 'secure', 'ebayisapi', 'webscr', 'login', 'signin']
        count  = 0
        for child in url_security_words:
            if child in url_token:
                count+=1;
        return count
    def Checkipexistence(self,url_token):
        count = 0
        for child in url_token:
            if unicode(child).isnumeric():
                count = count+1
            else:
                if count >= 4:
                    return 1
                else:
                    count = 0
        if count >=4 :
            return 1
        return 0
    def Urlasn(self,url_host):
        try:
            urlgeo = pygeoip.GeoIP('GeoIPASNum.dat')
            urlasn=int(urlgeo.org_by_name(url_host).split()[0][2:])
            return urlasn
        except:
            return  -1
    def Urlexe(self,url_address):
        pass
    def Urltokendata(self,url_address):
        if len(url_address)==0:
            return[0,0,0]
        token_data = re.split('\W+',url_address)
        total_count=0
        total_sum=0
        maximum=0
        for child in token_data:
            total_sum = total_sum+len(child)
            if len(child)!=0:
                total_count =total_count+1
            if maximum < len(child):
                maximum = len(child)
        try:
            return [float(total_sum)/total_count,total_count,maximum]
        except:
            return [0,total_count,maximum]
    def gettingFeature(self,url_address):
        self.feature_extracted = {}
        self.token_words = re.split('\W+',url_address)
        self.url_info_reference = urlparse(url_address)
        self.url_netloc = self.url_info_reference.netloc
        self.url_path = self.url_info_reference.path
        self.feature_extracted['url_address'] = url_address
        self.feature_extracted['url_host'] = self.url_netloc
        self.feature_extracted['url_path'] = self.url_path
        self.api_data =Apidata()
        self.web_feature_reference = Weburlfeature()
        self.url_rank = self.api_data.Urlrank(self.url_netloc)
        self.feature_extracted['rank_url_host'] = self.url_rank[0]
        self.feature_extracted['rank_country_url'] = self.url_rank[1]
        self.feature_extracted['url_host_len'] = len(self.url_netloc)
        self.feature_extracted['url_len'] = len(url_address)
        self.feature_extracted['url_asn_no']= self.web_feature_reference.Urlasn(self.url_netloc)
        self.feature_extracted['avg_url_token_len'],self.feature_extracted['url_token_count'],self.feature_extracted['url_token_max'] =self.web_feature_reference.Urltokendata(url_address)
        self.feature_extracted['avg_url_host_len'],self.feature_extracted['url_host_count'],self.feature_extracted['url_host_max'] =self.web_feature_reference.Urltokendata(self.url_netloc)
        self.feature_extracted['avg_url_path_len'],self.feature_extracted['url_path_count'],self.feature_extracted['url_path_max'] =self.web_feature_reference.Urltokendata(self.url_path)
        self.feature_extracted['url_safe_browsing'] =self.api_data.Urlsafebrowsing(url_address)
        self.feature_extracted['url_dots'] = url_address.count('.')
        self.feature_extracted['url_security_words_count'] = self.web_feature_reference.Urlsecurity(self.token_words)
        self.feature_extracted['ipaddress_existence'] = self.web_feature_reference.Checkipexistence(self.token_words)
        #print self.feature_extracted['rank_url_host']
        #print self.feature_extracted['rank_country_url']
        return self.feature_extracted
        pass
