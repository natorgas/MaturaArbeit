import numpy as np
from scipy.integrate import odeint
from Algebra import v1_dot, v2_dot


duration = float(input("Duration(s): "))
fps = 30
number_of_steps = duration * fps

# Parameter festlegen
g = 9.81
l1 = float(input("Länge1(m): "))
l2 = float(input("Länge2(m): "))
m1 = float(input("Masse1(kg): "))
m2 = float(input("Masse2(kg): "))


def dSdt(S, t): # Funktion mit allen Ableitungen, für numerische Lösung
    alpha, beta, v1, v2 = S
    f = [v1,
         v2,
         v1_dot(g, m1, m2, alpha, beta, l1, l2, v1, v2),
         v2_dot(g, m1, m2, alpha, beta, l1, l2, v1, v2)]
    return f


t = np.arange(0, duration + duration/number_of_steps, duration/number_of_steps)

# Anfangswinkel festlegen
alpha0_1 = np.radians(float(input("alpha0_1 = ")))
beta0_1 = np.radians(float(input("beta0_1 = ")))
alpha0_2 = np.radians(float(input("alpha0_2 = ")))
beta0_2 = np.radians(float(input("beta0_2 = ")))

v1_0_1, v1_0_2, v2_0_1, v2_0_2 = 0, 0, 0, 0  # Anfangsgeschwindigkeiten festlegen

S0_1 = (alpha0_1, beta0_1, v1_0_1, v2_0_1)  # Vektor mit allen Anfangsbedingungen
S0_2 = (alpha0_2, beta0_2, v1_0_2, v2_0_2)

#
sol1 = odeint(dSdt, y0=S0_1, t=t)  # Numerisches Lösen
sol2 = odeint(dSdt, y0=S0_2, t=t)


# USED FOR PLOTTER
def many_pendulums(number_of_pendulums, starting_angle_alpha, starting_angle_beta, increment_alpha, increment_beta):
    solutions = []
    for i in range(number_of_pendulums):
        solutions.append(odeint(dSdt, y0=(np.radians(starting_angle_alpha) + i * increment_alpha, np.radians(starting_angle_beta) + i * increment_beta, 0, 0), t=t))
    return solutions
