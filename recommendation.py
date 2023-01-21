from PIL import Image
import os
import matplotlib.pyplot as plt
import numpy as np

from keras.applications import vgg16
from keras.utils import load_img,img_to_array
from keras.models import Model
from keras.applications.imagenet_utils import preprocess_input

from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

myImage = Image.open("image.png")   

def retrieve_most_similar_products(given_img):
    print("-----------------------------------------------------------------------")
    print("original product:")

    original = load_img(given_img, target_size=(imgs_model_width, imgs_model_height))
    plt.imshow(original)
    plt.show()

    print("-----------------------------------------------------------------------")
    print("most similar products:")

    closest_imgs = cos_similarities_df[given_img].sort_values(ascending=False)[1:nb_closest_images+1].index
    closest_imgs_scores = cos_similarities_df[given_img].sort_values(ascending=False)[1:nb_closest_images+1]

    for i in range(0,len(closest_imgs)):
        original = load_img(closest_imgs[i], target_size=(imgs_model_width, imgs_model_height))
        plt.imshow(original)
        plt.show()
        print("similarity score : ",closest_imgs_scores[i])

# image importing 
imgs_path = "/kaggle/input/fashion-product-images-dataset/fashion-dataset/fashion-dataset/images/"
imgs_model_width, imgs_model_height = 224, 224 # size of image

# file filtering and limiting of size
files = [imgs_path + x for x in os.listdir(imgs_path) if "jpg" in x]
files=files[0:100]


# Model loading
vgg_model = vgg16.VGG16(weights='imagenet')

# remove the last layers in order to get features instead of predictions
feat_extractor = Model(inputs=vgg_model.input, outputs=vgg_model.get_layer("fc2").output)

importedImages = []

for f in files:
    filename = f
    original = load_img(filename, target_size=(224, 224))
    numpy_image = img_to_array(original)
    image_batch = np.expand_dims(numpy_image, axis=0)
    
    importedImages.append(image_batch)

#img_features = feat_extractor.predict(processed_image)
    
images = np.vstack(importedImages)

processed_imgs = preprocess_input(images.copy())

imgs_features = feat_extractor.predict(processed_imgs)

imgs_features.shape

cosSimilarities = cosine_similarity(imgs_features)

# store the results into a pandas dataframe

cos_similarities_df = pd.DataFrame(cosSimilarities, columns=files, index=files)
cos_similarities_df.head()

# function to retrieve the most similar products for a given one

retrieve_most_similar_products()