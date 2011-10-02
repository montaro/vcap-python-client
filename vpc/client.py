'''
Created on Sep 28, 2011

@author: arefaey
'''
import constants
import re
from httplib2 import Http
import simplejson
import restclient

class VPC(object):        
# Initialize new client to the target_uri with optional auth_token
    def __init__(self, target_url=constants.DEFAULT_TARGET, auth_token=None):
        self.version = constants.VERSION
        self.target = None
        self.host = None
        self.user = None
        self.proxy = None
        self.auth_token = None
        self.http = Http()
        if not target_url:
            raise Exception("Invalid target URL")
        if not (re.match('^https?', target_url)):
                target_url = "http://%s" %target_url
        re.sub('/\/+$/', '', target_url)
        self.target =  target_url
        self.auth_token = auth_token
        
    def info(self):
        _, _, headers = self.request('GET', constants.INFO_PATH, constants.DEFAULT_CONTENT_TYPE)
        headers = simplejson.loads(headers)
        return headers
    
    def perform_http_request(self, req):
        response, content = getattr(restclient, req['method'].upper())(url=req['url'], params=req['params'], headers=req['headers'], resp=True, async=False)
        return (response['status'], response, content)

    def request(self, method, path, content_type = None, params = None, headers = {}):
        if self.auth_token:    headers['AUTHORIZATION'] = self.auth_token
        if self.proxy:    headers['PROXY-USER'] = self.proxy 
        if content_type:
            headers['Content-Type'] = content_type
            headers['Accept'] = content_type
        req = {
          'method':method,
          'url': '%s%s' % (self.target, path),
          'headers' : headers,
          'params':params
        }
        status, body, response_headers = self.perform_http_request(req)
        return (status, body, response_headers)