import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 5))
ax.axvspan(-1, 1, color='red', alpha=0.12)
ax.text(0.0, 0.2, r"Infeasible region ($x<1$)", color='red', fontsize=9, ha='center', va='bottom')
ax.axvspan(1, 3, color='blue', alpha=0.12)
ax.text(2.0, 0.2, r"Feasible region ($x\geq 1$)", color='blue', fontsize=9, ha='center', va='bottom')


# Feasible region: g(x) = x^2
xf = np.linspace(1, 3, 200)
ax.plot(xf, xf**2, 'b', lw=2)
ax.text(2.2, 6, r"$g(x)=x^2$", color='blue', fontsize=9, ha='center', va='bottom')
ax.plot(1, 1, 'bo', markersize=9)
ax.annotate("(1, 1)", xy=(1, 1), xytext=(1.05, 0.6), fontsize=9)

# Infeasible region: +infinity
for xa in [-0.6, 0.0, 0.6]:
    ax.annotate("", xy=(xa, 9.5), xytext=(xa, 2),
                arrowprops=dict(arrowstyle="-|>", color='red', lw=2))
ax.text(0.0, 9.7, r"$g(x)=+\infty$", color='red', fontsize=9,
        ha='center', va='bottom')

# Constraint boundary
ax.axvline(1, ls='--', color='gray')

ax.set_xlim(-1, 3)
ax.set_ylim(0, 11)
ax.set_xlabel("x")
ax.set_ylabel("g(x)")
ax.grid(True, alpha=0.4)
plt.tight_layout()
plt.show()

mu = np.linspace(0, 5, 200)
fig, ax = plt.subplots(figsize=(6, 4.5))
for xv, c in [(2, 'b'), (1.5, 'c'), (1, 'k'), (0.5, 'orange'), (0, 'r'), (-0.5, 'darkred')]:
    ax.plot(mu, xv**2 + mu*(1 - xv), color=c, label=f"x = {xv}")
ax.plot(0, 4, 'bo'); ax.plot(0, 2.25, 'co')
ax.set_xlabel(r"$\mu$"); ax.set_ylabel(r"$L(\mu,x)$"); ax.legend(); ax.grid(True)
plt.show()