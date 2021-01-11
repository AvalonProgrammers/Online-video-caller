import numpy as np

def getVideo(msg:str):
    video = np.array(
        [
            [
                [int(n) for n in pix.split(' ')] for pix in col.split('|')
            ] for col in msg.split('#') # Columns
        ]
    )
    return video
