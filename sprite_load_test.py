import tensorflow as tf
from tensorflow import keras
import pathlib
import numpy as np
from shutil import copyfile

model = keras.models.load_model('model.h5')

class_names = ['nonsprite', 'sprite']

img_height = 180
img_width = 180

data_dir = pathlib.Path('Raw_Data')
for sprite in data_dir.glob('*.jpg'):

    img = keras.preprocessing.image.load_img(
    sprite, target_size=(img_height, img_width)
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )

    if np.argmax(score) == 1:
        copyfile(sprite, 'found_sprites' + str(sprite)[str(sprite).find('/'):])