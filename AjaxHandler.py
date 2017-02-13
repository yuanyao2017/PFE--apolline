#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.server  
      
callback = None  
      
class AjaxHandler(http.server.BaseHTTPRequestHandler):  
    def do_GET(self):  
        contenttype = callback(self.path)  
        self.send_response(200)  
        self.send_header("Content-type", contenttype[1])  
        self.end_headers()  
        self.wfile.write(contenttype[0])