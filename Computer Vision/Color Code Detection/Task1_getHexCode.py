import cv2
import numpy as np

# load image
img = cv2.imread("opb48.jpg")   #Enter image path here
img = cv2.resize(img, (800, 600))


# function to calculate hexcode from rgb
def get_hexcode(r, g, b):
    return "#{:02X}{:02X}{:02X}".format(r, g, b)


def get_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        b, g, r = img[y,x]
        print(r, g, b)
        hex = get_hexcode(r, g, b)
        print("HexCode:",hex)

        cv2.circle(img, (x, y), 1, (0,0,255), -1)
        cv2.rectangle(img, (x-170, y-35),(x-5, y-5), (0,255,),3)
        cv2.putText(img,hex, (x-168,y-15), cv2.FONT_ITALIC, 0.7, (235, 136, 61), 2 )


cv2.namedWindow('image')
cv2.setMouseCallback('image', get_color)
while (1):
    cv2.imshow('image', img)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
