import numpy as np
import matplotlib.pyplot as plt

mu = np.linspace(0, 4, 400)
lines = {
    0: (mu, r"$x=0$:  $L=\mu$", 'tab:orange'),
    1: (np.ones_like(mu), r"$x=1$:  $L=1$", 'tab:green'),
    2: (4 - mu, r"$x=2$:  $L=4-\mu$", 'tab:purple'),
}

fig, ax = plt.subplots(figsize=(6.5, 4.5))
for xv, (L, label, color) in lines.items():
    ax.plot(mu, L, color=color, lw=1.5, label=label)

env = np.minimum.reduce([v[0] for v in lines.values()])
ax.plot(mu, env, 'k', lw=2, label="lower envelope")
ax.plot(mu, mu - mu**2/4, 'r--', lw=1.5, label=r"true $d(\mu)=\mu-\mu^2/4$")

ax.set_xlabel(r"$\mu$"); ax.set_ylabel(r"$L(\mu,x)$")
ax.set_ylim(-0.5, 4.5)
ax.legend(fontsize=8, loc="upper right"); ax.grid(True, alpha=0.4)
plt.tight_layout()
plt.savefig("fig_q3b_envelope.png", dpi=200)
plt.show()