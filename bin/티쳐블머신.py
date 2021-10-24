# from keras.models import load_model
import tensorflow as tf 
from PIL import Image, ImageOps
import numpy as np

# Load the model
model = tf.keras.models.load_model('jinhwan/teachable_machine/conference_file/keras_model.h5')
# model = load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Replace this with the path to your image

# 1. 파일을 가져올수도있고
# 2. 캠을 이용할 수도 있고.
# 특정 사이트의 링크에 있
image = Image.open('bin/campractice/dateset/bin.0.2.jpg')


#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
image_array = np.asarray(image)

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
# Load the image into the array
data[0] = normalized_image_array

with open('jinhwan/teachable_machine/conference_file/labels.txt', 'r') as f:
    labels = f.readlines()

label_dict = {}
for label in labels:
    num = label.split(' ', maxsplit=1)[0].strip()
    value = label.split(' ', maxsplit=1)[1].strip()
    label_dict[num] = value

# run the inference
prediction = model.predict(data)

## 할일 몇 번째가 높은지? 그리고 그 때 이름이 뭔지?
ans = label_dict[str(prediction[0].argmax())]
print(f'당신이 보여준 그림은 {ans}입니다.')