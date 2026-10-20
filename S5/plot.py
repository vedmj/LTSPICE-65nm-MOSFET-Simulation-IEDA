import pandas as pd
import matplotlib.pyplot as plt

# (name, unit, [low, nominal, high]) in the same order as the table, exp 1 to 14
params = [
    ("VTH0",  "V",         ["0.30", "0.423", "0.55"]),
    ("TOXE",  "nm",        ["1.5", "1.85", "2.5"]),
    ("L",     "nm",        ["55", "65", "100"]),
    ("XL",    "nm",        ["-35", "-30", "-15"]),
    ("LINT",  "nm",        ["2", "5.25", "8"]),
    ("W",     "µm",        ["0.5", "1", "2"]),
    ("WINT",  "nm",        ["0", "5", "40"]),
    ("NDEP",  "cm$^{-3}$", ["1.5e18", "2.54e18", "4e18"]),
    ("NSD",   "cm$^{-3}$", ["5e19", "2e20", "5e20"]),
    ("XJ",    "nm",        ["10", "19.6", "30"]),
    ("NGATE", "cm$^{-3}$", ["1e19", "2e20", "1e21"]),
    ("U0",    "cm$^2$/V·s", ["300", "491", "700"]),
    ("VSAT",  "cm/s",      ["0.8e7", "1.24e7", "2e7"]),
    ("RDSW",  "Ω·µm",      ["50", "165", "400"]),
]

colors = ["tab:blue", "k", "tab:red"]          # low, nominal, high

for n, (name, unit, vals) in enumerate(params, start=1):
    vg = pd.read_csv(f"S5/S5_Id_Vg_exp_{n}.txt", sep="\t")
    vd = pd.read_csv(f"S5/S5_Id_Vd_exp_{n}.txt", sep="\t")

    # column 1 = nominal, 2 = low, 3 = high (names differ per file, so use position)
    order = [(2, 0), (1, 1), (3, 2)]            # (column index, index in vals) -> low, nominal, high
    labels = [f"{name} = {v} {unit}" + (" (nominal)" if k == 1 else "")
              for k, v in enumerate(vals)]

    fig, ax = plt.subplots(1, 3, figsize=(15, 4))
    for col, k in order:
        ax[0].plot(vg.iloc[:, 0], vg.iloc[:, col] * 1e6, color=colors[k], lw=2, label=labels[k])
        ax[1].semilogy(vg.iloc[:, 0], vg.iloc[:, col], color=colors[k], lw=2, label=labels[k])
        ax[2].plot(vd.iloc[:, 0], vd.iloc[:, col] * 1e6, color=colors[k], lw=2, label=labels[k])

    ax[0].set(xlabel="$V_G$ (V)", ylabel="$I_D$ (µA/µm)", title="$I_D$-$V_G$ (linear), $V_{DS}$ = 0.4 V")
    ax[1].set(xlabel="$V_G$ (V)", ylabel="$I_D$ (A/µm)", title="$I_D$-$V_G$ (log), $V_{DS}$ = 0.4 V")
    ax[2].set(xlabel="$V_D$ (V)", ylabel="$I_D$ (µA/µm)", title="$I_D$-$V_D$, $V_{GS}$ = 1.1 V")
    for a in ax:
        a.grid(alpha=0.3)
        a.legend(fontsize=8)
    plt.suptitle(f"Exp {n}: variation of {name}")
    plt.tight_layout()
    plt.savefig(f"s5_exp{n}_{name}.png", dpi=200)
    plt.close()