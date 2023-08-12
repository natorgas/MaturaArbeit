import tensorflow as tf
import numpy as np
import os

dir = os.path.dirname(os.path.abspath(__file__))

model = tf.keras.models.load_model(dir)

alpha = float(input("Alpha: "))
beta = float(input("Beta: "))

input = np.array([[alpha, beta]])
a_pred = model.predict(input)[0][0]
print(f"Predicted critical time: {a_pred}s")