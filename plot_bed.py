import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.array(pd.read_csv("bed.txt", delimiter=" "))
ax = plt.figure().add_subplot(projection="3d")
xx, yy = np.meshgrid(range(7), range(6))
z = data
ax.plot_surface(xx, yy, z, alpha=0.5)

plt.show()
