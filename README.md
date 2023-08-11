# Maturaarbeit
Zur Nutzung der hier hinterlegten Programme sollte am besten das ganze Repository heruntergeladen werden. Dazu muss [Git](https://git-scm.com/downloads) auf dem PC installiert sein. Ebenfalls sollte für später auch [pip](https://pip.pypa.io/en/stable/) installiert werden. Danach wird 
folgendermassen in einem beliebigen Ordner ein Repository initialisiert:
```
git init
```
Anschliessend kann das gesamte Repository mit Inhalt wie folgt in den Zielordner importiert werden:
```
git clone https://github.com/natorgas/MaturaArbeit.git
```
Für das Ausführen aller Programme muss [Python](https://www.python.org/downloads/) installiert sein.

## DoublePendulumAnimation
Um die Animation starten zu können muss die Animationssoftware ManimCE für [Windows](https://docs.manim.community/en/stable/installation/windows.html) oder für [macOS](https://docs.manim.community/en/stable/installation/macos.html) installiert werden.
Mithilfe von pip werden danach alle benötigten Pakete installiert:
```
pip install numpy
```
```
pip install scipy
```
```
pip install sympy
```
Danach wird mit dem Terminal in den Ordner DoublePendulumAnimation navigiert. Folgender Befehl startet dann die Animation:
```
manim main_double_pendulum.py -pqh
```
## LinearRegressionCriticalTimes
Auch hier werden erst die benötigten Pakete installiert:
```
pip install pandas
```
```
pip install sscikit-learn
```
Um dieses Modell selbst zu testen muss man im entsprechenden Ordner folgender Befehl ausgeführt werden:
```
py LinearRegressionModel.py
```
## NeuralNetworkCriticalTimes
### 
