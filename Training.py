import cv2, os, numpy as np
from PIL import Image

wajahDir = 'dataset'
latihDir =  'datatraining'

def getImageLabel(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    faceIDs = []
    for imagePaths in imagePaths:
        