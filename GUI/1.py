#!/usr/bin/python3

import urllib.request
import cv2
import numpy as np
import os
import time


#print(os.getpid())

URL = "http://192.168.0.10:8080/photo.jpg"

while True:
    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
    img = cv2.imdecode(img_arr,-1)

    if img is None:
        continue
    else:
        cv2.imshow('MATFcamera',img)
        cv2.imwrite('./nesto.jpg', img)
    cv2.waitKey(1)
   