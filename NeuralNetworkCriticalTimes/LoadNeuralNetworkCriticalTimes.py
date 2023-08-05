import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("SPECIFY PATH TO THE FOLDER CONTAINING THE MODEL")  # FESTLEGEN DES PFADES ZUM ORDNER, WELCHER DAS MODELL ENTHÄLT

alpha = float(input("Alpha: "))
beta = float(input("Beta: "))

input = np.array([[alpha, beta]])
a_pred = model.predict(input)[0][0]
print(f"Predicted critical time: {a_pred}s")