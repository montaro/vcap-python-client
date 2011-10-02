'''
Created on Sep 28, 2011

@author: arefaey
'''
import unittest
from vpc.client import VPC
from vpc import constants
from urllib import urlencode

class TestClient(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_initialize(self):
        client = VPC()
        self.assertEqual(constants.DEFAULT_TARGET, client.target)
        
    def test_info(self):
        client = VPC()
        info = client.info()
        self.assertEqual('{"name":"vcap","build":2222,"support":"http://support.cloudfoundry.com","version":"0.999","description":"VMware\'s Cloud Application Platform","allow_debug":false}', info)
        
    def test_perform_http_request(self):
        req = {'url':'http://www.google.com',
               'method':'get',
               'params':{},
               'headers':{}
               }
        client = VPC()
        status, body, response_headers = client.perform_http_request(req)
        self.assertEqual('200', status)
        
        req = {'url':'http://www.google.com',
               'method':'post',
               'params':{},
               'headers':{}
               }
        status, body, response_headers = client.perform_http_request(req)
        self.assertEqual('405', status)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()