import numpy as np
import pandas as pd
import random
import skimage.io
import matplotlib.pyplot as plt
from subprocess import check_output
from skimage import morphology
from skimage.viewer import ImageViewer

# print(check_output(["ls", "data/"]).decode("utf8"))

def read_image_labels(image_id):
    # most of the content in this function is taken from 'Example Metric Implementation' kernel 
    # by 'William Cukierski'
    image_file = "data/stage1_train/{}/images/{}.png".format(image_id,image_id)
    mask_file = "data/stage1_train/{}/masks/*.png".format(image_id)
    image = skimage.io.imread(image_file)
    masks = skimage.io.imread_collection(mask_file).concatenate()    
    height, width, _ = image.shape
    num_masks = masks.shape[0]
    maxValue = np.max(image)
    for index in range(0, num_masks):
        contour = np.logical_xor(masks[index], morphology.binary_erosion(masks[index]) )
        image[contour > 0] = maxValue
    return image

# def save_image(image, filename):
#     with open(filename, 'wb') as image_file:
        

def plot_images_masks(image_ids):
    # plt.close('all')
    # fig, ax = plt.subplots(nrows=len(image_ids),ncols=1, figsize=(256,256))
    
    for ax_index, image_id in enumerate(image_ids):
        image = read_image_labels(image_id)
        print image.shape
        filepath = 'data/processed/'
        skimage.io.imsave(filepath+image_id+'.png', image)
        # ax[ax_index].imshow(image)
        # viewer = ImageViewer(image)
        # viewer.show()

def main():
    image_ids = check_output(["ls", "data/stage1_train/"]).decode("utf8").split()
    print("Total Images in Training set: {}".format(len(image_ids)))
    # random_image_ids = random.sample(image_ids, 16)
    print("Randomly Selected Images: {}, their IDs: {}".format(len(image_ids), image_ids))
    plot_images_masks(image_ids)

if __name__ == '__main__':
    main()