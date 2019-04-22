import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
#%matplotlib inline 
from keras import models, layers
from keras.layers import Input, Dense
from keras.models import Model
from keras import applications
import glob2 as glob
from numpy import random
from sklearn.model_selection import train_test_split

encoding_dim = 70
data = pd.read_csv("../../data/multi-cohortd.csv")
train, test = train_test_split(data, test_size=0.2)

encoded = Dense(encoding_dim, activation='relu')(train)
decoded = Dense(784, activation='sigmoid')(encoded.value())
autoencoder = Model(input_img, decoded)
encoder = Model(train, encoded)

encoded_input = Input(shape=(encoding_dim,))
decoder_layer = autoencoder.layers[-1]
decoder = Model(encoded_input, decoder_layer(encoded_input))

autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')

autoencoder.fit(train, train,
                epochs=50,
                batch_size=256,
                shuffle=True,
                validation_data=(test, test))

encoded = encoder.predict(test)
decoded = decoder.predict(encoded)
decoded
plt.show()
