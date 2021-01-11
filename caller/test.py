import cv2


print("Running opencv", cv2.__version__)
cap = cv2.VideoCapture(0)

ret, img = cap.read()

# Up-down, then side to side
# 
# p1 p2 p3
# p1 p2 p3
# p1 p2 p3

print(
    len(img),
    len(img[0])
)
cv2.imshow('frame', img)

cap.release()
cv2.destroyAllWindows()