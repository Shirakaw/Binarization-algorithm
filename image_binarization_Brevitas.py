import tensorflow as tf
# print("tensorflow version:" ,tf.__version__)
import os
import tensorflow_datasets
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from keras import layers
from keras.datasets import mnist
from keras.models import Model

input_dir = tensorflow_datasets.load(name = "/Users/apple/Downloads/RedNet-master/binarization/")
