import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure

BoltzConst = 8.617333262145e-5


A = [1.2, 1e-26, 2e10*BoltzConst/1e6]
B = [0.6, 1e-26, 2e11*BoltzConst/1e6]
C = [0.6, 1e-26, 2e10*BoltzConst/1e6]
D = [0.6, 1e-26, 2e09*BoltzConst/1e6]
E = [0.6, 1e-25, 2e10*BoltzConst/1e6]
F = [0.6, 1e-27, 2e10*BoltzConst/1e6]
G = [0.3, 1e-26, 2e10*BoltzConst/1e6]

ms = 10
area = 200
colors = 'red'


fig, ax = plt.subplots(1,3, figsize=(20,5))

plt.subplots_adjust(wspace = 0.02)

ax[1].scatter( B[2], B[1], s=area, c=colors, marker='o')
ax[1].scatter( C[2], C[1], s=area, c=colors, marker='o')
ax[1].scatter( D[2], D[1], s=area, c=colors, marker='o')
ax[1].scatter( E[2], E[1], s=area, c=colors, marker='o')
ax[1].scatter( F[2], F[1], s=area, c=colors, marker='o')

ax[0].scatter( A[2], A[1], s=area, c=colors, marker='o')
ax[2].scatter( G[2], G[1], s=area, c=colors, marker='o')

txt = ['A', 'B', 'C (fiducial)', 'D', 'E', 'F', 'G']

font = {"fontsize": 20}
ax[1].annotate(txt[1], (B[2]*1.1, B[1]*1.1), **font)
ax[1].annotate(txt[2], (C[2]*1.1, C[1]*1.1), **font)
ax[1].annotate(txt[3], (D[2]*1.1, D[1]*1.1), **font)
ax[1].annotate(txt[4], (E[2]*1.1, E[1]*1.1), **font)
ax[1].annotate(txt[5], (F[2]*1.1, F[1]*1.1), **font)

ax[0].annotate(txt[0], (A[2]*1.1, A[1]*1.1), **font)
ax[2].annotate(txt[6], (G[2]*1.1, G[1]*1.1), **font)


ax[0].set_xlabel('Temperature (MeV)' ,fontsize=20)
ax[1].set_xlabel('Temperature (MeV)' ,fontsize=20)
ax[2].set_xlabel('Temperature (MeV)' ,fontsize=20)
ax[0].set_ylabel('Density (g/cm$^3$)',fontsize=20)

ax[0].set_xscale('log')
ax[1].set_xscale('log')
ax[2].set_xscale('log')
ax[0].set_yscale('log')
ax[1].set_yscale('log')
ax[2].set_yscale('log')

ax[0].set_xlim(D[2]*0.8, B[2]*1.5)
ax[1].set_xlim(D[2]*0.8, B[2]*1.5)
ax[2].set_xlim(D[2]*0.8, B[2]*1.5)
ax[0].set_ylim(F[1]*0.8, E[1]*1.7)
ax[1].set_ylim(F[1]*0.8, E[1]*1.7)
ax[2].set_ylim(F[1]*0.8, E[1]*1.7)

ax[0].tick_params(axis='both', which='major', direction='in', labelsize=20, bottom=True, top=True, left=True, right=True, length=5)
ax[0].tick_params(axis='both', which='minor', direction='in', labelsize=20, bottom=True, top=True, left=True, right=True, length=3)
ax[1].tick_params(axis='both', which='major', direction='in', labelsize=20, bottom=True, top=True, left=True, right=True, length=5, labelleft=False)
ax[1].tick_params(axis='both', which='minor', direction='in', labelsize=20, bottom=True, top=True, left=True, right=True, length=3, labelleft=False)
ax[2].tick_params(axis='both', which='major', direction='in', labelsize=20, bottom=True, top=True, left=True, right=True, length=5, labelleft=False)
ax[2].tick_params(axis='both', which='minor', direction='in', labelsize=20, bottom=True, top=True, left=True, right=True, length=3, labelleft=False)

plt.savefig( "fig__jet_parameters.png", bbox_inches='tight', pad_inches=0.1, format="png" )
