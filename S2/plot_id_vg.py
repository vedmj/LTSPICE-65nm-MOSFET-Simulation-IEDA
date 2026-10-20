import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv(r"S2/vd_50m.txt", sep="\t")
df2 = pd.read_csv(r"S2/vd_1.1.txt", sep="\t")

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(df1['V1'], df1['Id(M1)'] * 1e6, lw=2, label="$V_{DS}$ = 50 mV")
ax[0].plot(df2['V1'], df2['Id(M1)'] * 1e6, lw=2, label="$V_{DS}$ = 1.1 V")
ax[0].set(xlabel="$V_G$ (V)", ylabel="$I_D$ (µA/µm)", title="Linear")
ax[1].semilogy(df1['V1'], df1['Id(M1)'], lw=2, label="$V_{DS}$ = 50 mV")
ax[1].semilogy(df2['V1'], df2['Id(M1)'], lw=2, label="$V_{DS}$ = 1.1 V")
ax[1].set(xlabel="$V_G$ (V)", ylabel="$I_D$ (A/µm)", title="Log")
for a in ax:
    a.grid(alpha=0.3)
    a.legend()
plt.suptitle("$I_D$-$V_G$ at $V_{DS}$ = 50 mV and 1.1 V")
plt.tight_layout()
plt.savefig("s2_overlay.png", dpi=200)
plt.show()