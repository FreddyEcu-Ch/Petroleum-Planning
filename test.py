#%%
import pandas as pd
import matplotlib.pyplot as plt

#%%
df = pd.read_excel("Data/Estado de estudiantes.xlsx")
print(df)

#%%
fig, ax = plt.subplots(figsize=(10, 8))
g = [n for n in df.iloc[:, -1].value_counts()]
values, bins, bars = plt.hist(x=df.iloc[:, -1])
ax.set_xlabel("Gender", fontsize=16)
ax.set_ylabel("Amount", fontsize=16)
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)
ax.set_title("Students per Gender", fontsize=18, fontweight="bold")
plt.bar_label(bars)
plt.tight_layout()
plt.show()