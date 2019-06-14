from keras.models import Sequential,load_model
from keras.layers import Dense, Activation, BatchNormalization
from keras.optimizers import rmsprop
from keras.callbacks import ModelCheckpoint

hidden_layer_size = 150
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
    # Dense(hidden_layer_size),
    # Activation('relu'),
    # BatchNormalization(),
    Dense(num_outputs),
    Activation('sigmoid'),
])

# model.compile(optimizer=rmsprop(lr=0.001), loss='mse')
model.compile(optimizer=rmsprop(lr=0.001), loss='binary_crossentropy', metrics=['accuracy'])

# Input and Label generation
import numpy as np
import pandas as pd

training_data = pd.read_csv('training-data-normalized-processed.csv', delimiter=',')
training_label = pd.read_csv('training-label-classification.csv', delimiter=',')
# training_label = pd.read_csv('training-label.csv', delimiter=',')

cv_data = pd.read_csv('cv-data-normalized-processed.csv', delimiter=',')
cv_label = pd.read_csv('cv-label-classification.csv', delimiter=',')
# cv_label = pd.read_csv('cv-label.csv', delimiter=',')

savemodel = ModelCheckpoint('model4.h5', monitor='val_acc', verbose=1, save_best_only=True, save_weights_only=False, mode='auto', period=1)
# savemodel = ModelCheckpoint('model4.h5', monitor='val_loss', verbose=1, save_best_only=True, save_weights_only=False, mode='auto', period=1)

# Train the model
# epochs = number of time the training process will go through the dataset
# batch_size = #training samples (matches/games) per training step
model.fit(training_data, training_label, epochs=100, batch_size=32, 
          validation_data=(cv_data, cv_label), callbacks=[savemodel])

# Evaluated the generated model with tests
cv_score = model.evaluate(cv_data, cv_label, batch_size=32)
print(cv_score)

testing_data = pd.read_csv('testing-data-normalized-processed.csv', delimiter=',')
testing_label = pd.read_csv('testing-label-classification.csv', delimiter=',')
# testing_label = pd.read_csv('testing-label.csv', delimiter=',')

model = load_model('model4.h5')

testing_score = model.evaluate(testing_data, testing_label, batch_size=32)
print(testing_score)

testing_output = model.predict(testing_data)
output = open("testing_out.csv", 'w+')

for e in testing_output:
  output.write(str(e[0]) + '\n')

output.close()
