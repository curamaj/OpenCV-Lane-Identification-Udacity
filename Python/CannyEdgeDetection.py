# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 19:02:26 2017

@author: Ajay Curam
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

image = mpimg.imread('exit-ramp.jpg')
plt.imshow(image)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #grayscale conversion
plt.imshow(gray, cmap='gray')