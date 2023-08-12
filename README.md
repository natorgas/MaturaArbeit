# Maturaarbeit
Für das Ausführen aller Programme muss [Python](https://www.python.org/downloads/) installiert sein.
Zur Nutzung der hier hinterlegten Programme sollte am besten das ganze Repository heruntergeladen werden. Dazu muss [Git](https://git-scm.com/downloads) installiert sein. Danach wird 
folgendermassen in einem beliebigen Ordner ein Repository initialisiert:
```
git init
```
Anschliessend kann das gesamte Repository mit Inhalt wie folgt in den Zielordner importiert werden:
```
git clone https://github.com/natorgas/MaturaArbeit.git
```
Installation aller benötigten Pakete mit [pip](https://pip.pypa.io/en/stable/):
```
pip install numpy scipy sympy pandas scikit-learn tensorflow
```

## DoublePendulumAnimation
Um die Animation starten zu können muss die Animationssoftware ManimCE für [Windows](https://docs.manim.community/en/stable/installation/windows.html) oder für [macOS](https://docs.manim.community/en/stable/installation/macos.html) installiert werden.
Danach wird mit dem Terminal in den Ordner DoublePendulumAnimation navigiert. Folgender Befehl startet dann die Animation:
```
manim main_double_pendulum.py -pqh
```
## LinearRegressionCriticalTimes
Um dieses Modell zu testen muss im entsprechenden Ordner folgender Befehl ausgeführt werden:
```
py LinearRegressionModel.py
```
## NeuralNetworkCriticalTimes
Um eine Vorhersage mit dem in der Arbeit erwähnten Modell zu tätigen:
```
py LoadNeuralNetworkCriticalTimes.py
```




