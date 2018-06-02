"""
Lorenz 63 model from wikipedia
https://en.wikipedia.org/wiki/Lorenz_system
"""
import numpy as np
from scipy.integrate import odeint
from scipy.io import savemat


def f(state, t):
    rho = 28.0
    sigma = 10.0
    beta = 8.0 / 3.0

    x, y, z = state  # unpack the state vector
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # derivatives


def generate_lorenz_trajectory(state0):
    t = np.arange(0.0, 400.0, 0.01)
    return odeint(f, state0, t)


def random_init_conds(n):
    for i in range(n):
        yield np.random.rand(3)


burn_in_time = 1000
number_init_conds = 100

trajectories = []
for i, u0 in enumerate(random_init_conds(number_init_conds)):
    print("Trajectory ", i)
    y = generate_lorenz_trajectory(u0)
    trajectories.append(y)

trajectories = np.stack(trajectories, axis=0)

known = trajectories[:, :burn_in_time]
secret = trajectories[:, burn_in_time:]

savemat("known.mat", {"x": known})
savemat("secret.mat", {"x": trajectories})
