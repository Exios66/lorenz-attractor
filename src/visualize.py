import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

def animate_lorenz(trajectory):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    def update(num, trajectory, line):
        line.set_data(trajectory[:num, 0:2].T)
        line.set_3d_properties(trajectory[:num, 2])
        return line,

    x = trajectory[:, 0]
    y = trajectory[:, 1]
    z = trajectory[:, 2]
    line, = ax.plot(x, y, z, lw=0.5, color='blue')

    ani = animation.FuncAnimation(fig, update, frames=len(trajectory), fargs=(trajectory, line), interval=30, blit=True)
    plt.show()

# Example usage:
if __name__ == "__main__":
    from lorenz_attractor import simulate_lorenz, sigma, rho, beta

    initial_state = np.array([0.0, 1.0, 1.05])
    dt = 0.01
    num_steps = 10000
    trajectory = simulate_lorenz(initial_state, num_steps, dt, sigma, rho, beta)
    animate_lorenz(trajectory)
