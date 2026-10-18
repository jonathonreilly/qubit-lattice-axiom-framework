"""Bundle the arrays needed to reproduce OBS-3's readings into obs3_archive.npz."""
import numpy as np, json, glob, os
from obs3_core import *
A = {}
A['V_pdg24'] = INPUTS['pdg24']['V']; A['mu'] = INPUTS['pdg24']['mu']; A['md'] = INPUTS['pdg24']['md']; A['F'] = F
A['E1_Wu'] = np.load('escape_E1_Wu.npy')
for tag in ('gen', 'sym', 'gen120'):
    z = np.load(f'univ_B_{tag}.npz')
    for k in z.files: A[f'B_{tag}_{k}'] = z[k]
z = np.load('univ_A_M1.npz')
for k in z.files: A[f'A_M1_{k}'] = z[k]
for (m, D) in BRACKET:
    for N in (48, 96):
        I, s = load_kin(N, m, D, 'sym'); A[f'I00_N{N}_m{m}_D{D}'] = np.array([I[c]['00'] for c in 'xyz'])
        A[f'Kfl_N{N}_m{m}_D{D}'] = np.array(load_flav(N, m, D)[0])
u = np.load('upflat_results.npy', allow_pickle=True)
A['upflat_table'] = np.array([[str(x) for x in row[:5]] for row in u])
np.savez('obs3_archive.npz', **A)
print(len(A), 'arrays ->', os.path.getsize('obs3_archive.npz'), 'bytes')
