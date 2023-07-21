from equationsolver_double_pendulum import many_pendulums
import numpy as np

v1_0_1, v1_0_2, v2_0_1, v2_0_2 = 0, 0, 0, 0

times = []
a_angles = []
b_angles = []

for g in range(101, 180):
    for j in range(0, 180):

        print(g, j)

        a0 = g  # Alpha
        b0 = j  # Beta

        solutions = np.degrees(many_pendulums(2, a0, b0, np.radians(0.01), 0))

        sol1 = solutions[0].T[0]
        sol2 = solutions[1].T[0]

        differences = (abs(sol1-sol2))

        for i in range(len(differences)):
            if differences[i] > 5:
                print(i/30)
                times.append(i/32)
                a_angles.append(g)
                b_angles.append(j)
                break

with open("C:\\Users\\david\\Programming\\MyPython\\PycharmProjects\\times.txt",
          "w") as file:
    for i in range(len(times)):
        file.write(str(times[i]) + "\n")
    pass

with open("C:\\Users\\david\\Programming\\MyPython\\PycharmProjects\\a_angles.txt",
          "w") as file:
    for i in range(len(a_angles)):
        file.write(str(a_angles[i]) + "\n")
    pass

with open("C:\\Users\\david\\Programming\\MyPython\\PycharmProjects\\b_angles.txt",
          "w") as file:
    for i in range(len(b_angles)):
        file.write(str(b_angles[i]) + "\n")
    pass