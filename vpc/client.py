'''
Created on Sep 28, 2011

@author: arefaey
'''
import constants
import re
import simplejson
from httplib2 import Http

class VPC(object):        
# Initialize new client to the target_uri with optional auth_token
    def __init__(self, target_url=constants.DEFAULT_TARGET, auth_token=None):
        self.version = constants.VERSION
        self.target = None
        self.host = None
        self.user = None
        self.proxy = None
        self.auth_token = None
        if not target_url:
            raise Exception("Invalid target URL")
        if not (re.match('^https?', target_url)):
                target_url = "http://%s" %target_url
        re.sub('/\/+$/', '', target_url)
        self.target =  target_url
        self.auth_token = auth_token
        self.http = Http()
        
    def info(self):
        _, _, content = self.request('GET', constants.INFO_PATH, constants.DEFAULT_CONTENT_TYPE)
        content = simplejson.loads(content)
        return content
    
    def login(self, user, password):
        path =  '%s/%s/tokens' % (constants.USERS_PATH, user)
        status, response, content = self.request('POST', path, content_type=constants.DEFAULT_CONTENT_TYPE, params={'password':password})
        self.auth_token = simplejson.loads(content)['token'] if content else None
        return (status, response, content)

    def perform_http_request(self, req):
        body = simplejson.dumps(req['params']) if req['params'] else ''
        response, content = self.http.request(req['url'], req['method'], body, req['headers'])
        return (response['status'], response, content)

    def request(self, method, path, content_type = None, params = None, headers = {}):
        if self.auth_token:    headers['AUTHORIZATION'] = self.auth_token
        if self.proxy:    headers['PROXY-USER'] = self.proxy 
        if content_type:
            headers['Content-Type'] = content_type
            headers['Accept'] = content_type
            headers['X-VCAP-Trace'] = '22'
        req = {
          'method':method,
          'url': '%s%s' % (self.target, path),
          'headers' : headers,
          'params':params
        }
        status, response, content = self.perform_http_request(req)
        return (status, response, content)