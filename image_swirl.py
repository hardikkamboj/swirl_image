import cv2
from skimage.transform import warp
import numpy as np
 
def swirl_fn(xy, x0, y0, R):
    r = np.sqrt((xy[:,1]-x0)**2 + (xy[:,0]-y0)**2)
    a = np.pi * r / R
    xy[:, 1] = (xy[:, 1]-x0)*np.cos(a) + (xy[:, 0]-y0)*np.sin(a) + x0
    xy[:, 0] = -(xy[:, 1]-x0)*np.sin(a) + (xy[:, 0]-y0)*np.cos(a) + y0
    return xy


im = cv2.imread('potrait2.jpeg')

a = np.arange(1,100)
b = (np.arange(1,100)**2) + 100

list_values = np.append(a,b)


for radius in list_values:
    im_swirl = warp(im, swirl_fn, map_args={'x0':im.shape[0]//2, 'y0':im.shape[1]//2, 'R':radius})
    cv2.imshow("Image",im_swirl)
    cv2.waitKey(0)
cv2.destroyAllWindows()




