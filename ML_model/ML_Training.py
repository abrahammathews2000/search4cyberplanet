import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers
from PIL import Image
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

x_dir  = './generatedData/lc_dict.npy'
x = np.load(x_dir)

y_dir  = './generatedData/shape_dict.npy'
y = np.load(y_dir)
y = y/255.0

# Noise addition
np.random.seed(100000)
stds = np.array([0.005,0.001,0.0005])
X_Noise = []
for el in x:
    i = np.random.randint(0,len(stds),1)
    noisearr = np.random.normal(1, stds[i], len(el))
    X_Noise.append(np.multiply(el, noisearr))

X_Noise = np.array(X_Noise)

xTrain, xTest, yTrain, yTest = train_test_split(X_Noise, y, test_size=0.20, random_state=1)
print(xTrain.shape, xTest.shape, yTrain.shape, yTest.shape)

inputs = keras.Input(shape=(500,))
x = layers.Dense(2500, activation="relu")(inputs)
x = layers.Dense(5000, activation="relu")(x)
x = layers.Dense(5000, activation="relu")(x)
x = layers.Dense(7500, activation="relu")(x)
x = layers.Dense(7500, activation="relu")(x)
x = layers.Dense(7500, activation="relu")(x)
x = layers.Dense(5000, activation="relu")(x)
x = layers.Dense(5000, activation="relu")(x)
x = layers.Dense(5000, activation="relu")(x)
x = layers.Dense(2500, activation="relu")(x)
x = layers.Dense(2500, activation="relu")(x)
outputs = layers.Dense(1024)(x)
outputs2D = layers.Reshape(target_shape=(32, 32),name='reshape_3')(outputs)
model = keras.Model(inputs=inputs, outputs=outputs2D, name="predict_shape_from_LC")
model.summary()

model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.0001), loss='mse')
model.fit(xTrain, yTrain, epochs=100)
model.evaluate(xTest, yTest)

yPredictonTest = model.predict(xTest)
plt.imshow(yPredictonTest[0],cmap='gray')
plt.imshow(yTest[0],cmap='gray')