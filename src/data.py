from __future__ import print_function

import os
import numpy as np

import cv2

#data_path = './'

image_rows = 420
image_cols = 580

data_dir = os.environ['DATA_DIR'] + '/'
imgs_train_file_name = 'imgs_train.npy'
imgs_mask_train_file_name = 'imgs_mask_train.npy'
imgs_test_file_name = 'imgs_test.npy'
imgs_id_file_name = 'imgs_id_test.npy'
imgs_train_file_path = data_dir + 'imgs_train.npy'
imgs_mask_train_file_path = data_dir + 'imgs_mask_train.npy'
imgs_test_file_path = data_dir + 'imgs_test.npy'
imgs_id_file_path = data_dir + 'imgs_id_test.npy'


def create_train_data():
    data_dir = data_dir = os.environ['DATA_DIR'] + '/'
    train_data_path = os.path.join(data_dir, 'train')
    images = os.listdir(train_data_path)
    total = len(images) / 2

    imgs = np.ndarray((int(total), 1, image_rows, image_cols), dtype=np.uint8)
    imgs_mask = np.ndarray((int(total), 1, image_rows, image_cols), dtype=np.uint8)

    i = 0
    print('-'*30)
    print('Creating training images...')
    print('-'*30)
    for image_name in images:
        if 'mask' in image_name:
            continue
        image_mask_name = image_name.split('.')[0] + '_mask.tif'
        img = cv2.imread(os.path.join(train_data_path, image_name), cv2.IMREAD_GRAYSCALE)
        img_mask = cv2.imread(os.path.join(train_data_path, image_mask_name), cv2.IMREAD_GRAYSCALE)

        img = np.array([img])
        img_mask = np.array([img_mask])

        imgs[i] = img
        imgs_mask[i] = img_mask

        if i % 100 == 0:
            print('Done: {0}/{1} images'.format(i, total))
        i += 1
    print('Loading done.')

    imgs_train_file_path = data_dir + 'imgs_train.npy'
    imgs_mask_train_file_path = data_dir + 'imgs_mask_train.npy'

    np.save(imgs_train_file_path', imgs)
    np.save(imgs_mask_train_file_path, imgs_mask)
    print('Saving to .npy files done.')


def load_train_data():
    data_dir = data_dir = os.environ['DATA_DIR'] + '/'
    imgs_train_file_name = 'imgs_train.npy'
    imgs_mask_train_file_name = 'imgs_mask_train.npy'
    imgs_train = np.load(imgs_train_file_path)
    imgs_mask_train = np.load(imgs_mask_train_file_path)
    return imgs_train, imgs_mask_train


def create_test_data():
    data_dir = data_dir = os.environ['DATA_DIR'] + '/'
    train_data_path = os.path.join(data_dir, 'test')
    images = os.listdir(train_data_path)
    total = len(images)

    imgs = np.ndarray((total, 1, image_rows, image_cols), dtype=np.uint8)
    imgs_id = np.ndarray((total, ), dtype=np.int32)

    i = 0
    print('-'*30)
    print('Creating test images...')
    print('-'*30)
    for image_name in images:
        img_id = int(image_name.split('.')[0])
        img = cv2.imread(os.path.join(train_data_path, image_name), cv2.IMREAD_GRAYSCALE)

        img = np.array([img])

        imgs[i] = img
        imgs_id[i] = img_id

        if i % 100 == 0:
            print('Done: {0}/{1} images'.format(i, total))
        i += 1
    print('Loading done.')

    imgs_test_file_path = data_dir + 'imgs_test.npy'
    imgs_id__test_file_path = data_dir + 'imgs_id_test.npy'
        
    np.save(imgs_test_file_path, imgs)
    np.save(imgs_id_test_file_path, imgs_id)
    print('Saving to .npy files done.')


def load_test_data():
    data_dir = data_dir = os.environ['DATA_DIR'] + '/'
    imgs_test_file_name = 'imgs_test.npy'
    imgs_id_file_name = 'imgs_id_test.npy'
    imgs_test = np.load(imgs_test_file_path')
    imgs_id = np.load(imgs_id_test_file_path)
    return imgs_test, imgs_id

if __name__ == '__main__':
    create_train_data()
    create_test_data()
