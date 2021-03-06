import os
import numpy as np
from utils import misc_utils as mu

### change me ###
root_dir = '/media/peter/HDD 1/ICIAR2018_BACH_Challenge/'

###

data_dir = root_dir + 'BACH_normalized'
save_dir_train = root_dir + 'Train_set'
save_dir_val = root_dir + 'Val_set'
save_dir_test = root_dir + 'Test_set'
save_dir_mini = root_dir + 'Mini_set'

classes = ('Benign', 'InSitu', 'Invasive', 'Normal')
prefixes = {'Benign': 'b', 'InSitu': 'is', 'Invasive': 'iv', 'Normal': 'n'}

perm = np.random.permutation(100)
train_idx = perm[:60]
val_idx = perm[60:80]
test_idx = perm[80:]


###

def get_patches(img, save_path_sub):
    cnt = 1
    for i in range(5):
        for j in range(7):
            patch = img[256 * i:256 * i + 512, 256 * j:256 * j + 512]
            mu.save_aspng(patch, save_path_sub + '_patch' + mu.i2str(cnt) + '.png', compression=1)
            cnt += 1


###

for c in classes:
    for i in train_idx:
        filename = prefixes[c] + mu.i2str(i + 1) + '_normalized.png'
        print('Doing Image {}'.format(filename))
        path = os.path.join(data_dir, c, filename)
        image = mu.read_image(path)

        sub = os.path.join(save_dir_train, c, prefixes[c] + mu.i2str(i + 1))
        get_patches(image, sub)

for c in classes:
    for i in val_idx:
        filename = prefixes[c] + mu.i2str(i + 1) + '_normalized.png'
        print('Doing Image {}'.format(filename))
        path = os.path.join(data_dir, c, filename)
        image = mu.read_image(path)

        sub = os.path.join(save_dir_val, c, prefixes[c] + mu.i2str(i + 1))
        get_patches(image, sub)

for c in classes:
    for i in test_idx:
        filename = prefixes[c] + mu.i2str(i + 1) + '_normalized.png'
        print('Doing Image {}'.format(filename))
        path = os.path.join(data_dir, c, filename)
        image = mu.read_image(path)

        sub = os.path.join(save_dir_test, c, prefixes[c] + mu.i2str(i + 1))
        mu.save_aspng(image, sub + '.png', compression=1)

### mini set just for debugging

for c in classes:
    filename = prefixes[c] + mu.i2str(1) + '_normalized.png'
    path = os.path.join(data_dir, c, filename)
    image = mu.read_image(path)

    sub = os.path.join(save_dir_mini, c, prefixes[c] + mu.i2str(1))
    get_patches(image, sub)
