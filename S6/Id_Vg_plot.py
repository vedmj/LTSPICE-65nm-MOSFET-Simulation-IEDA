import pandas as pd
import matplotlib.pyplot as plt

sp = pd.read_csv(r"S6/Id_vg_tuned.txt", sep="\t")
tc = pd.read_csv(r"S6/Id_vs_Vg(vd_0.4).csv").iloc[:, :2]
tc.columns = ["Vg", "Id"]

fig, ax = plt.subplots(figsize=(6, 4))

ax.plot(
    tc.Vg[tc.Vg <= 3.0],
    tc.Id[tc.Vg <= 3.0] * 1e6,
    "o", ms=4, mfc="none", label="TCAD"
)

ax.plot(
    sp["V1"][sp["V1"] <= 3.0],
    sp["Id(M1)"][sp["V1"] <= 3.0] * 1e6,
    lw=2, label="SPICE fit"
)

ax.set(
    xlabel="$V_G$ (V)",
    ylabel="$I_D$ (µA/µm)",
    title="$V_{DS}$ = 0.4 V"
)

ax.grid(alpha=0.3)
ax.legend()

plt.tight_layout()
plt.savefig("s6_idvg_overlay.png", dpi=200)
plt.show()