from PIL import Image
import os
import matplotlib.pyplot as plt
import numpy as np

from keras.applications import vgg16
from keras.preprocessing.image import load_img,img_to_array
from keras.models import Model
from keras.applications.imagenet_utils import preprocess_input


from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

