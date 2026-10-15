import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 3, 400)
for mu in [0, 1, 2, 3]:
    L = x**2 + mu*(1 - x)
    line, = plt.plot(x, L, label=f"µ = {mu}")
    xm = mu/2
    plt.plot(xm, xm**2 + mu*(1 - xm), 'o', color=line.get_color())
plt.axvline(1, ls='--', color='gray')   # constraint boundary x = 1
plt.xlabel("x"); plt.ylabel("L(µ, x)"); plt.legend(); plt.grid(True)
plt.show()