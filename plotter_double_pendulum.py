from matplotlib import pyplot as plt
import numpy as np
import scipy.io
import scienceplots
from mpl_toolkits import mplot3d
plt.style.use(["science", "notebook", "grid"])

plot = int(input(r"Plot pendulum trajectories[0], Plot 3D phase space[1], Plot Energies[2]: "))


def time_x_axis():
    time = int(input(r"Plot time on the x-axis? Yes[0], No[1]: "))
    if time == 0:
        return True
    else:
        return False


time = time_x_axis()

from equationsolver_double_pendulum import many_pendulums, t

number_of_pendulums = int(input("Number of plendulums: "))
starting_angle_alpha = float(input("Starting angle alpha: "))
starting_angle_beta = float(input("Starting angle beta: "))
increment_alpha = np.radians(float(input("Increment alpha in degrees: ")))
increment_beta = np.radians(float(input("Increment beta in degrees: ")))

values = np.degrees(many_pendulums(number_of_pendulums, starting_angle_alpha, starting_angle_beta, increment_alpha, increment_beta))


# TEXTFILE TO IMPORT INTO SCILAB
angle_list = (list(values[0].T[0]))
with open("C:\\Users\\david\\Documents\\Schule\\MA\\MA_NonePython\\Latex\\Arbeit\\array.txt",
          "w") as file:
    for i in range(len(angle_list)):
        file.write(str(angle_list[i]) + "\n")
    pass

# TRAJECTORY WITH TIME ON THE X-AXIS
if plot == 0 and time:
    print("Alpha[0], Beta[1], Alphadot[2], Betadot[3]")
    plot_choice_y = int(input("Y-Axis plotting value: "))

    for i in range(number_of_pendulums):
        plt.plot(t, (values[i].T[plot_choice_y]), color="blue", linewidth="4.5")

    plt.xlabel(r"Zeit[s]")
    plt.ylabel(r"Alpha[Grad]")
    plt.title(r"Beta(t)", fontsize=55, y=1.025)
    ax = plt.gca()

    plt.show()

# TRAJECTORY WITHOUT TIME ON THE X-AXIS
elif plot == 0 and not time:
    print("Alpha[0], Beta[1], Alphadot[2], Betadot[3]")
    plot_choice_x = int(input("X-Axis plotting value: "))
    plot_choice_y = int(input("Y-Axis plotting value: "))

    for i in range(number_of_pendulums):
        plt.plot((values[i].T[plot_choice_x]), (values[i].T[plot_choice_y]))

    plt.show()

# 3D PHASE SPACE
elif plot == 1:
    for i in range(number_of_pendulums):
        ax = plt.axes(projection="3d")
        ax.plot((values[i].T[0]), (values[i].T[1]), (values[i].T[2]))
        ax.scatter(values[i].T[0][0], values[i].T[1][0], values[i].T[2][0], color="red")

    ax.set_xlabel("Alpha")
    ax.set_ylabel("Beta")
    ax.set_zlabel("Alphadot")

    plt.show()

