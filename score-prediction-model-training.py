from keras.models import Sequential
from keras.layers import Dense, Activation, BatchNormalization
from keras.optimizers import rmsprop

hidden_layer_size = 100
num_features = 20
num_outputs = 1

# This statement specifies the structure of the network
# 1 input layer of size num_features
# 1 hidden layer of size hidden_layer_size
# 1 output layer of size num_outputs
# DO NOT CHANGE THE ACTIVATION FUNCTION (YET)
model = Sequential([
    Dense(hidden_layer_size, input_shape=(num_features,)),
    Activation('relu'),
    BatchNormalization(),
    Dense(hidden_layer_size),
    Activation('relu'),
    BatchNormalization(),
    Dense(hidden_layer_size),
    Activation('relu'),
    BatchNormalization(),
    Dense(hidden_layer_size),
    Activation('relu'),
    BatchNormalization(),
    Dense(num_outputs),
    Activation('sigmoid'),
])

model.compile(optimizer=rmsprop(learning_rate=0.01), loss='mse')

# Input and Label generation
import numpy as np
data = np.random.random((1000, 100))
labels = np.random.randint(2, size=(1000, 1))

# Train the model
# epochs = number of time the training process will go through the dataset
# batch_size = #training samples (matches/games) per training step
model.fit(data, labels, epochs=30, batch_size=32)

# Evaluated the generated model with tests
score = model.evaluate(x_test, y_test, batch_size=32)
