import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

files = {"Normal (all models on)": "S4/S4_normal.txt",
         "UA = UB = 0 (no Enormal)": "S4/S4_ua_ub_0.txt",
         "VSAT × 100 (no HighFieldSaturation)": "S4/S4_vsat100.txt"}

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
for label, f in files.items():
    df = pd.read_csv(f, sep="\t")
    ax[0].plot(df['V1'], df['Id(M1)'] * 1e6, lw=2, label=label)
    ax[1].semilogy(df['V1'], df['Id(M1)'], lw=2, label=label)
ax[0].set(xlabel="$V_G$ (V)", ylabel="$I_D$ (µA/µm)", title="Linear")
ax[1].set(xlabel="$V_G$ (V)", ylabel="$I_D$ (A/µm)", title="Log")
for a in ax:
    a.grid(alpha=0.3)
    a.legend()
plt.suptitle("$I_D$-$V_G$ at $V_{DS}$ = 1.1 V: physics check")
plt.tight_layout()
plt.savefig("s4_overlay.png", dpi=200)
plt.show()