import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("C:\\Users\\david\\Documents\\Programming\\Python\\MaturaArbeit\\NeuralNetworkCriticalTimes")

alpha = float(input("Alpha: "))
beta = float(input("Beta: "))

a = np.array([[alpha, beta]])
a_pred = model.predict(a)[0][0]
print(f"Predicted critical time: {a_pred}s")