import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 5.0, 0.2)
print(t)

# multiple line with different formatting in same graph
# for separating line and dot color for the same line use different formatting two times with one type (here (t, t+6))
plt.plot(t, t, 'r*', t, t+3, 'bs-', t, t+6, 'g-', t, t+6, 'mo', markersize=5)
plt.show()