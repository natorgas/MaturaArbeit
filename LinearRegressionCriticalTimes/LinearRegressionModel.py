import pandas as pd
import sklearn
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error

# Pfad zur Excel Datei mit den Daten festlegen
data = pd.read_csv("C:\\Users\\david\\Documents\\Programming\\Python\\MaturaArbeit\\ExcelFile\\DoublePendulum2.csv", sep=",")

data = data[["Alpha", "Beta", "Times"]]  # Relevante Daten festlegen
predict = "Times"

X = data.drop(columns=["Times"])
Y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)  # Aufteilen der Daten

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)  # Modell trainieren

#Auswertung
y_pred = linear.predict(x_test)

mae = mean_absolute_error(y_test, y_pred)

determinationskoeffizient = linear.score(x_test, y_test)
print(f"Determinationskoeffizient = {determinationskoeffizient * 100}%")

print(f"Koeffizienten: {linear.coef_}")
print(f"Achsenabschnitt: {linear.intercept_}")
print(f"Mittlerer absoluter Fehler = {mae}s")

