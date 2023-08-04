import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

# Pfad zur Excel Datei mit den Daten festlegen
data = pd.read_csv("C:\\Users\\david\\Documents\\Programming\\Python\\MaturaArbeit\\ExcelFile\\DoublePendulum2.csv", sep=",")

data = data[["Alpha", "Beta", "Times"]]  # Relevante Daten festlegen
predict = "Times"

X = data.drop(columns=["Times"])
Y = np.array(data[predict])

# Aufteilen der Daten
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.1)

model = tf.keras.models.Sequential()

# Anzahl Schichten und Neuronen festlegen
model.add(tf.keras.layers.Dense(units=10, input_shape=(2,)))
model.add(tf.keras.layers.Dense(units=200, activation='elu'))
model.add(tf.keras.layers.Dense(units=100, activation='elu'))
model.add(tf.keras.layers.Dense(units=200, activation='elu'))
model.add(tf.keras.layers.Dense(units=40, activation='relu'))
model.add(tf.keras.layers.Dense(units=1))

model.compile(optimizer="nadam", loss="mean_absolute_error")

# Modell trainieren
model.fit(x_train, y_train, epochs=300)

# Auswertung
y_pred = model.predict(x_test)
mae = mean_absolute_error(y_test, y_pred)
print("Mean absolute Error:", mae)

r2 = r2_score(y_test, y_pred)
print(f"r2 = {r2}")

# Speichern des Modells in gewünschtem Ordner
model.save("C:\\Users\\david\\Programming\\MyPython\\PycharmProjects\\MaturaArbeit\\NeuralNetwork")