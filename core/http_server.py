"""
http_server.py - Simple HTTP Server

Date: 29-05-2014
Version: 0.1
"""

import SimpleHTTPServer
import SocketServer
import sys
import os
from shutil import rmtree
from api.std import *


class http_server(object):
    """Simple HTTP Server"""

    def __init__(self, port, index):
        self.port = port
        self.server_index = index


    def _pre_server(self):
        if not os.path.exists(self.server_index):
            notify("[*] INDEX - %s created.." %(self.server_index))
            os.mkdir(self.server_index)
        else:
            pass
    
    def cleanup(self):
        if os.path.exists(index):
            rmtree(index)
        else:
            pass
        notify("[*] cleanup..")

    def _run_server_(self):
        os.chdir(self.server_index)
        try:
            self.http_handler = SimpleHTTPServer.SimpleHTTPRequestHandler
            self.httpd = SocketServer.TCPServer(("", self.port), self.http_handler)
            notify("[*] Serving HTTP Server on localhost:%d..." %(self.port))
            notify("\nPut files or index.html in: %s (:" %(self.server_index))
            self.httpd.serve_forever()
        except KeyboardInterrupt:
            self.cleanup()
            sys.exit(1)
        except Exception as e:
            self.cleanup()
            sys.exit(1)

index = "/tmp/sb0x-HTTPServer"

def httpd(port):
    if port == 80:
        #if (is_root):
        if (is_root == True):
            pass
        elif not is_root():
            error("To use port: 80 run sb0x as root.")
            sys.exit(1)
    elif port > 65535:
        error("Port Range: 1-65535")
        sys.exit(1)
    else:
        warning("if you getting errors please choose  different port")
    start = http_server(port, index)
    start._pre_server()      
    start._run_server_()
