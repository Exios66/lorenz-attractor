import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Lorenz system parameters
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

def lorenz(state, sigma, rho, beta):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return np.array([dx, dy, dz])

def rk4_step(state, dt, sigma, rho, beta):
    k1 = lorenz(state, sigma, rho, beta)
    k2 = lorenz(state + 0.5 * dt * k1, sigma, rho, beta)
    k3 = lorenz(state + 0.5 * dt * k2, sigma, rho, beta)
    k4 = lorenz(state + dt * k3, sigma, rho, beta)
    return state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

def simulate_lorenz(initial_state, num_steps, dt, sigma, rho, beta):
    trajectory = np.empty((num_steps + 1, 3))
    trajectory[0] = initial_state
    state = initial_state
    for i in range(1, num_steps + 1):
        state = rk4_step(state, dt, sigma, rho, beta)
        trajectory[i] = state
    return trajectory

def plot_lorenz(trajectory):
    x = trajectory[:, 0]
    y = trajectory[:, 1]
    z = trajectory[:, 2]

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, lw=0.5, color='blue')
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")
    plt.show()

# Example execution
if __name__ == "__main__":
    initial_state = np.array([0.0, 1.0, 1.05])
    dt = 0.01
    num_steps = 10000
    trajectory = simulate_lorenz(initial_state, num_steps, dt, sigma, rho, beta)
    plot_lorenz(trajectory)