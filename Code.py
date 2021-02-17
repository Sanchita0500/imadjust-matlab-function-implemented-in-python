import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
%matplotlib inline

def dehaze(img):
    img.astype("int32")
    
    low_in=np.min(img)
    high_in=np.max(img)
    gamma=0.5
    new_img=255*np.power(np.divide(np.subtract(img,low_in),high_in-low_in),gamma)
    
    return new_img
    
plt.figure(figsize=(15,15))    

img = cv2.imread('..\\haze1.tif')
new_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.subplot(2,2,1)
plt.title("input image")
plt.imshow(new_img)

gamma = dehaze(img)
gamma=cv2.cvtColor(gamma.astype("uint8"),cv2.COLOR_BGR2RGB)
plt.subplot(2,2,2)
plt.title("adjusted image")
plt.imshow(gamma)

img = cv2.imread('..\\haze2.tif')
new_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.subplot(2,2,3)
plt.title("input image")
plt.imshow(new_img)

gamma = dehaze(img)
gamma=cv2.cvtColor(gamma.astype("uint8"),cv2.COLOR_BGR2RGB)
plt.subplot(2,2,4)
plt.title("adjusted image")
plt.imshow(gamma)
    
