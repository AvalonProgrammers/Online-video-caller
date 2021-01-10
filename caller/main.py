import cv2
print("Running opencv", cv2.__version__)
cap = cv2.VideoCapture(0)

ret, img = cap.read()
simplified = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(
    len(simplified),
    len(simplified[0])
)
cv2.imshow('frame', simplified)

cap.release()
cv2.destroyAllWindows()