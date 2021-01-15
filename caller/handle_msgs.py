import numpy as np

class VideoHandler:
    def getVideo(msg:str) -> np.ndarray:
        video = np.array(
            [
                [
                    [int(n) for n in pix.split(' ')] for pix in row.split('|')
                ] for row in msg.split('#') # Rows
            ]
        )
        return video
    def makeVideo(video:np.ndarray) -> str:
        msg = ""
        for rowIdx, row in enumerate(video):
            for pixIdx, pix in enumerate(row):
                for valIdx, val in enumerate(pix):
                    msg += str(val)
                    if valIdx != 2:
                        msg += " "
                if pixIdx != len(row) - 1:
                    msg += "|"
            if rowIdx != len(video) - 1:
                msg += "#"
        return msg

class Addresser:
    def toSendableVideos(self, videos:dict) -> str:
        sendable = ""
        for idx, addr in enumerate(videos.keys()):
            sendable += f"{addr}:{videos[addr]}"
            if idx != len(videos.keys()) - 1:
                sendable += ";"
        return sendable
    
    def fromSentString(self, videos:str) -> dict:
        pass