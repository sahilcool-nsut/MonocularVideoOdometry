import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os
from odometry import MonocularVideoOdometery

img_path = 'C:\\Users\\schaw\\OneDrive\\Documents\\SC Docs\\Sahil documents\\ARES\\Ares-CV\\sequence_14\\images\\'
pose_path = 'C:\\Users\\schaw\\OneDrive\\Documents\\SC Docs\\Sahil documents\\ARES\\Ares-CV\\sequence_14\\groundTruthSync.txt'


vo = MonocularVideoOdometery(img_path, pose_path)

while(vo.checkNextFrame()):

    frame = vo.current_frame

    cv.imshow('Video Frame', frame)
    k = cv.waitKey(1)
    if k == 27:
        break

    vo.process_frame()  
    mono_coord = vo.get_mono_coordinates()  
    print("X: {}, Y: {}, Z: {}".format(*[str(pt) for pt in mono_coord]))   

cv.destroyAllWindows()
