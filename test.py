#%%
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px

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

#%%
fig_1 = px.histogram(df, x=df.iloc[:, -1], labels={"x": "Gender"}, color=df.iloc[:, -1])
fig_1.show()

#%%
df_est = pd.read_csv("Data/Estado de estudiantes.csv")
# Rename column names
df_est.rename(columns={"MATR�CULA": "MATRÍCULA", "G�nero": "GÉNERO"}, inplace=True)
#%%
df_est.to_csv("Data/Estado Estudiantes.csv", index=False)

#%%
fig_2, ax = plt.subplots(figsize=(10, 8))
ax.hist(df.iloc[:, 3], bins=30)
plt.show()


