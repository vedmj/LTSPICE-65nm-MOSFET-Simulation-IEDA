import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

files = {0.3: "S3/vg_0.3.txt", 0.6: "S3/vg_0.6.txt",
         0.9: "S3/vg_0.9.txt", 1.5: "S3/vg_1.5.txt"}

fig, ax = plt.subplots(figsize=(6, 4))
for vg, f in files.items():
    df = pd.read_csv(f, sep="\t")
    ax.plot(df['V2'], df['Id(M1)'] * 1e6, lw=2, label=f"$V_{{GS}}$ = {vg} V")
ax.set(xlabel="$V_D$ (V)", ylabel="$I_D$ (µA/µm)", title="$I_D$-$V_D$ family")
ax.grid(alpha=0.3)
ax.legend()
plt.tight_layout()
plt.savefig("s3_family.png", dpi=200)
plt.show()

# gds and ro at VGS = 1.5 V
df = pd.read_csv(files[1.5], sep="\t")
gds = np.gradient(df['Id(M1)'], df['V2'])        # S/µm
ro = 1 / gds[-1] * 1e-3                          # kΩ·µm
print(f"gds = {gds[-1]:.4e} S/µm")
print(f"ro  = {ro:.3f} kΩ·µm")