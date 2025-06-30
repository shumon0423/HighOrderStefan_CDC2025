import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D


def plot_results(time, s_t, u_t, qc_t):
    plt.figure()
    plt.plot(time / 60, s_t * 100, linewidth=2)
    plt.xlim([time[0] / 60, (time[time.size - 1] + 1) / 60])
    plt.ylim([min(s_t) * 100, max(s_t) * 100])
    plt.xlabel("Time [min]", fontsize=14)
    plt.ylabel("Interface position [cm]", fontsize=14)
    plt.xticks(fontsize=16) # Increase font size of x-axis
    plt.yticks(fontsize=16) # Increase font size of y-axis
    plt.show()

    plt.figure()
    plt.plot(time / 60, u_t[0, :], linewidth=2)
    plt.xlim([time[0] / 60, (time[time.size - 1] + 1) / 60 / 2])
    plt.ylim(bottom=0)
    plt.xlabel("Time [min]", fontsize=14)
    plt.ylabel("Boundary temperature [C]", fontsize=14)
    plt.xticks(fontsize=16) # Increase font size of x-axis
    plt.yticks(fontsize=16) # Increase font size of y-axis
    plt.show()

    plt.figure()
    plt.plot(time / 60, qc_t, linewidth=2)
    plt.xlim([time[0] / 60, (time[time.size - 1] + 1) / 60 / 20])
    plt.ylim(bottom=0)
    plt.xlabel("Time [min]", fontsize=14)
    plt.ylabel("Controlled boundary heat flux [W/m^2]", fontsize=14)
    plt.xticks(fontsize=16) # Increase font size of x-axis
    plt.yticks(fontsize=16) # Increase font size of y-axis
    plt.show()

    plt.figure()
    plt.contour(time / 60, range(u_t.shape[0]), u_t, linewidths=2)
    # plt.xlim([time[0] / 60, (time[time.size - 1] + 1) / 60])
    # plt.ylim([0, u_t.shape[0]])
    plt.xlabel("Time [min]", fontsize=14)
    plt.ylabel("Temperature [C]", fontsize=14)
    plt.xticks(fontsize=16) # Increase font size of x-axis
    plt.yticks(fontsize=16) # Increase font size of y-axis
    plt.show()
    
    
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    # Make data.
    division = 10
    X = time[:math.floor(len(time)/division)] / 60
    Y = range(u_t.shape[0])
    X, Y = np.meshgrid(X, Y)
    Z = u_t[:, :math.floor(len(time)/division)]

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

    # Customize the z axis.
    # ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    # A StrMethodFormatter is used automatically
    ax.zaxis.set_major_formatter('{x:.02f}')

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()