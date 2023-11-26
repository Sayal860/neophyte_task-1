import cv2

def point_capture(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Coordinate of Image: ({x}, {y})")
        cv2.putText(image, f'({x}, {y})', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
        cv2.imshow('nature', image)

image=cv2.imread("VSSUT LOGO.png")
cv2.imshow("nature", image)
cv2.setMouseCallback('nature', point_capture)
cv2.waitKey(0)
cv2.destroyAllWindows()