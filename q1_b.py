import numpy as np
import matplotlib.pyplot as plt

mu = np.linspace(0, 4, 400)
d = mu - mu**2/4

plt.plot(mu, d, label=r"$d(\mu)=\mu-\mu^2/4$")
mu_pts = np.array([0, 1, 2, 3])
plt.plot(mu_pts, mu_pts - mu_pts**2/4, 'o', color='gray')
plt.xlabel(r"$\mu$"); plt.ylabel(r"$d(\mu)$")
plt.legend(); plt.grid(True); plt.show()