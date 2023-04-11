import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([[0, 0, 0], [3, 6, 9]]), columns = ["A", "B", "C"])
df.plot()
plt.show()