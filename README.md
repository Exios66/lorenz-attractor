# Lorenz Attractor Visualization (Fixed)

This repository visualizes the Lorenz Attractor using Python. It includes functionality to simulate the system, generate charts, and create live illustrations.

## Features

- Simulate the Lorenz Attractor
- Generate charts
- Create live illustrations

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/lorenz-attractor.git
   ```

2. Install dependencies:

   ```bash
   pip install numpy matplotlib
   ```

## Usage

1. Simulate the Lorenz Attractor:

   ```python
   import numpy as np
   from matplotlib import pyplot as plt

   def lorenz(x, y, z, s=10, r=28, b=2.667):
       x_dot = s*(y - x)
       y_dot = r*x - y - x*z
       z_dot = x*y - b*z
       return x_dot, y_dot, z_dot

   dt = 0.01
   num_steps = 10000

   # Choose random starting points for x, y, and z
   np.random.seed(1)
   xs = np.random.uniform(-10, 10, num_steps)
   ys = np.random.uniform(-10, 10, num_steps)
   zs = np.random.uniform(-10, 10, num_steps)

   # Initialize arrays to store the results
   xs_store = []
   ys_store = []
   zs_store = []

   # Simulate the Lorenz Attractor
   for i in range(num_steps):
       x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
       xs[i+1] = xs[i] + (x_dot * dt)
       ys[i+1] = ys[i] + (y_dot * dt)
       zs[i+1] = zs[i] + (z_dot * dt)
       xs_store.append(xs[i+1])
       ys_store.append(ys[i+1])
       zs_store.append(zs[i+1])

   # Plot the results
   fig = plt.figure()
   ax = fig.add_subplot(projection='3d')
   ax.plot(xs_store, ys_store, zs_store, lw=0.5)
   ax.set_xlabel("X Axis")
   ax.set_ylabel("Y Axis")
   ax.set_zlabel("Z Axis")
   ax.set_title("Lorenz Attractor")
   plt.show()
   ```

2. Generate charts:

   ```python
   import matplotlib.pyplot as plt

   # Example data
   x = np.linspace(0, 10, 100)
   y = np.sin(x)

   # Create a line chart
   plt.plot(x, y, label='Sine Wave')
   plt.xlabel('X-axis')
   plt.ylabel('Y-axis')
   plt.title('Sine Wave Example')
   plt.legend()
   plt.show()
   ```

3. Create live illustrations:

   ```python
   import matplotlib.pyplot as plt
   import numpy as np
   from mpl_toolkits.mplot3d import Axes3D

   def lorenz(x, y, z, s=10, r=28, b=2.667):
       x_dot = s*(y - x)
       y_dot = r*x - y - x*z
       z_dot = x*y - b*z
       return x_dot, y_dot, z_dot

   dt = 0.01
   num_steps = 10000

   # Choose random starting points for x, y, and z
   np.random.seed(1)
   xs = np.random.uniform(-10, 10, num_steps)
   ys = np.random.uniform(-10, 10, num_steps)
   zs = np.random.uniform(-10, 10, num_steps)

   # Initialize arrays to store the results
   xs_store = []
   ys_store = []
   zs_store = []

   # Simulate the Lorenz Attractor
   for i in range(num_steps):
       x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
       xs[i+1] = xs[i] + (x_dot * dt)
       ys[i+1] = ys[i] + (y_dot * dt)
       zs[i+1] = zs[i] + (z_dot * dt)
       xs_store.append(xs[i+1])
       ys_store.append(ys[i+1])
       zs_store.append(zs[i+1])

   # Create a live plot
   fig = plt.figure()
   ax = fig.add_subplot(projection='3d')
   line, = ax.plot([], [], [], lw=0.5)
   ax.set_xlabel("X Axis")
   ax.set_ylabel("Y Axis")
   ax.set_zlabel("Z Axis")
   ax.set_title("Lorenz Attractor")

   def animate(i):
       line.set_data(xs_store[:i], ys_store[:i])
       line.set_3d_properties(zs_store[:i])
       return line,

   ani = animation.FuncAnimation(fig, animate, frames=num_steps, interval=10)

   plt.show()
   ```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## 2024 Lucius J. Morningstar

## Morningstar Developments LLC Copyright All Rights Reserved
