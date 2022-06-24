import json
import time
from flask import Flask, jsonify, Response, render_template, stream_with_context
import socket
from HorizonParser import GetParsedPacket

app = Flask(__name__)

@app.route('/api')
def hello_world():
    pp = None
    try:
        lsock = socket.socket(family=socket.AddressFamily.AF_INET, type=socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)
        lsock.bind(('', 5300))
        lsock.setblocking(False)
        lsock.settimeout(0.1)
        pp = GetParsedPacket(lsock.recv(324))
    except:
        pp = None
        pass
    finally:
        lsock.close()
        return jsonify(pp)