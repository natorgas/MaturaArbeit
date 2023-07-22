import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("C:\\Users\\david\\Documents\\Programming\\Python\\MaturaArbeit\\NeuralNetworkCriticalTimes")
model2 = tf.keras.models.load_model("C:\\Users\\david\\Documents\\Programming\\Python\\MaturaArbeit\\NeuralNetworkLyapunovExponents")

alpha = float(input("Alpha: "))
beta = float(input("Beta: "))

a = np.array([[alpha, beta]])
t_pred = model.predict(a)[0][0]
print(f"Predicted critical time: {t_pred}s")

b = np.array([[alpha, beta, t_pred]])
lpnv_pred = model2.predict(b)[0][0]
print(f"Predicted Lypaunov Exponent: {lpnv_pred}")