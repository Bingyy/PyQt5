import numpy as np
import cv2

canvas = np.zeros((300,300,3),dtype = 'uint8')

green = (0,255,0) # BGR
cv2.line(canvas,(0,0),(300,300),green)
cv2.imshow('canvas',canvas)
cv2.waitKey(0)

