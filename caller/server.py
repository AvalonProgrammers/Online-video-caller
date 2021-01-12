from pyNetSocket import Server, getThisIP

from handle_msgs import *

IP = getThisIP()

myServer = Server(IP, 5050, 10)
latestVids = {}

def encodeVids():
    pass

def handleVideo(addr, conn, msg:str):
    if msg[0] == 'v':
        msg = msg[1:]
        latestVids[addr] = msg

myServer.onMessage(handleVideo)


