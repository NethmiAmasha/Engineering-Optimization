import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3.8))

# Left graph: L(mu, x*) against mu
mu = np.linspace(0, 4, 200)
ax1.plot(mu, 1 + mu*(1 - 1), 'b', lw=2, label=r"$L(\mu,x^*)=1$")
ax1.plot(2, 1, 'bo', markersize=7, label=r"$L(\mu^*,x^*)=1$")
ax1.set_xlabel(r"$\mu$"); ax1.set_ylabel(r"$L(\mu,x^*)$")
ax1.set_ylim(0, 2.5)
ax1.set_title(r"(a) $L(\mu,x^*)$ against $\mu$")
ax1.legend(loc="upper left", fontsize=9); ax1.grid(True, alpha=0.4)

# Right graph: L(mu*, x) against x
x = np.linspace(-1, 3, 200)
ax2.plot(x, (x - 1)**2 + 1, 'b', lw=2, label=r"$L(\mu^*,x)=(x-1)^2+1$")
ax2.plot(1, 1, 'bo', markersize=7, label=r"$L(\mu^*,x^*)=1$")
ax2.set_xlabel("x"); ax2.set_ylabel(r"$L(\mu^*,x)$")
ax2.set_title(r"(b) $L(\mu^*,x)$ against $x$")
ax2.legend(loc="upper center", fontsize=9); ax2.grid(True, alpha=0.4)

plt.tight_layout()
plt.show()