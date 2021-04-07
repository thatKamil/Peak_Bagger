import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])

fig, ax = plt.subplots(2, 2)

ax[0, 0].plot(x, x)
ax[0, 1].plot(x, x * x)
ax[1, 0].plot(x, x * x * x)
ax[1, 1].plot(x, x * x * x * x)

ax[0, 0].set_title("Linear")
ax[0, 1].set_title("Square")
ax[1, 0].set_title("Cube")
ax[1, 1].set_title("Fourth power")
plt.subplot_tool()
plt.show()