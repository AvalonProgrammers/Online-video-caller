import cv2
import numpy as np
from rgb2hsv import rgb2hsv

print("Running opencv", cv2.__version__)
cap = cv2.VideoCapture(0)

ret, img = cap.read()

print(
    len(img),
    len(img[0])
)

print(
np.array([
    [
        [
            channelVal//20 for channelVal in rgb2hsv(*pix)
        ] for pix in col
    ] for col in img
]))

# Up-down, then side to side
# 
# p1 p2 p3
# p1 p2 p3
# p1 p2 p3

while True:
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()