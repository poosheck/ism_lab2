from math import log10, sqrt
import cv2
import numpy as np
import glob
import json

def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if (mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

if __name__ == "__main__":
    file_list = []
    results = []

    original = cv2.imread("original_image.jpg")
    for name in glob.glob('./compressed_*.jpg'):
        file_list.append(name)

    for file in file_list:
        compressed = cv2.imread(file)
        psnr = PSNR(original, compressed)
        results.append({
            'filename': file,
            'PSNR': psnr
        })
        print("PSNR for {} is {}".format(file, psnr))

    with open('psnr.json', 'w') as f:
        json.dump(results, f, indent=2)



