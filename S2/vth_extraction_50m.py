import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv(r"S2/vd_50m.txt", sep="\t")


g_m = np.gradient(data['Id(M1)'], data['V1'])
m_index = np.argmax(g_m)
m,c = np.polyfit(data['V1'].iloc[m_index-1:m_index+1],data['Id(M1)'].iloc[m_index-1:m_index+1],1)
plt.figure(figsize=(10,6))
plt.plot(data['V1'],data['Id(M1)'],lw=4)
plt.title('Threshold Voltage Calculation')
plt.xlabel('$V_{gs}$')
plt.ylabel('$I_{d}$')
plt.tight_layout()
plt.grid(True, linestyle='--',alpha=0.6)
vt = -c / m
print(vt)
x_filtered = data['V1'][data['V1'] >= vt]
plt.plot(x_filtered,x_filtered*m+c)
plt.savefig('Vth_Vd_50m.png',dpi=100)
plt.show()