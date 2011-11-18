'''
Created on Sep 28, 2011

@author: arefaey
'''
import unittest
from vpc.client import VPC
from vpc import constants

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
        self.assertEqual(info['name'], 'vcap')
        self.assertEqual(info['support'], 'http://support.cloudfoundry.com')
        
    def test_perform_http_request(self):
        req = {'url':'http://www.google.com',
               'method':'get',
               'params':'',
               'headers':{}
               }
        client = VPC()
        status, _, _ = client.perform_http_request(req)
        self.assertEqual('200', status)
        
        req = {'url':'https://www.google.com',
               'method':'post',
               'params':{'x':'y'},
               'headers':{}
               }
        status, _, _ = client.perform_http_request(req)
        self.assertEqual('405', status)
        
    def test_request(self):
        client = VPC()
        status, _, _ = client.request('get', constants.INFO_PATH, constants.DEFAULT_CONTENT_TYPE)
        self.assertEqual('200', status)
        
    def test_login(self):
        client = VPC()
        self.assertEqual(None, client.auth_token)
        status, _, _ = client.login('c9.cf.poc@gmail.com', 'cloud9ers')
        self.assertEqual('200', status)
        self.assertNotEqual(None, client.auth_token)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
