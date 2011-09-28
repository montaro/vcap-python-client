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
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()