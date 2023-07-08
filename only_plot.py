import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('scores_result.csv', parse_dates=['timestamp'])
df.plot(x='timestamp',y='total_pp')
plt.grid(True)
plt.show()
