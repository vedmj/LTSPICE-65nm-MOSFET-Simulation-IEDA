import pandas as pd
import matplotlib.pyplot as plt

sp = pd.read_csv(r"S6/Id_vs_Vd_spice.txt", sep="\t")
tc = pd.read_csv(r"S6/Id_vs_Vd(Vg_0.9).csv").iloc[:, :2]
tc.columns = ["Vd", "Id"]

fig, ax = plt.subplots(figsize=(6, 4))

ax.plot(
    tc.Vd[tc.Vd <= 2.5],
    tc.Id[tc.Vd <= 2.5] * 1e6,
    "o", ms=4, mfc="none", label="TCAD"
)

ax.plot(
    sp["V2"][sp["V2"] <= 2.5],
    sp["Id(M1)"][sp["V2"] <= 2.5] * 1e6,
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
plt.savefig("s6_idvd_overlay.png", dpi=200)
plt.show()