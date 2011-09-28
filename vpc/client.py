'''
Created on Sep 28, 2011

@author: arefaey
'''
from constants import *
import re
from httplib2 import Http

class VPC(object):        
# Initialize new client to the target_uri with optional auth_token
    def __init__(self, target_url=DEFAULT_TARGET, auth_token=None):
        self.version = VERSION
        self.target = None
        self.host = None
        self.user = None
        self.proxy = None
        self.auth_token = None
        self.http = Http()
        if not (re.match('^https?', target_url)):
                target_url = "http://%s" %target_url
        re.sub('/\/+$/', '', target_url)
        self.target =  target_url
        self.auth_token = auth_token
        
    def info(self):
        _, content =  self.http.request(self.target+INFO_PATH)
        return content