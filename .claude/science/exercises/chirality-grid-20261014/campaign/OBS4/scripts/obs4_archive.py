"""OBS-4 archive: everything needed to reproduce the readings (realisations, mass bases, carrier images, M* rows)."""
import numpy as np
from obs4_core import *
from obs4_r1 import realisations, physical, vev_dicts, worst
A = {}
R = realisations()
try:
    rs = np.load('refit_solutions.npz')
    for n, (tag, p) in enumerate(zip(rs['tags'], rs['p'])):
        R[f'refit{n}_{tag}'] = masses_from_p(p, 'gen120' in str(tag))
except FileNotFoundError:
    pass
for name, (Mu0, Md0) in R.items():
    Mu, Md, cj = physical(Mu0, Md0); mb = mass_basis(Mu, Md); Pu, Pd = carrier_hats(Mu, Md, mb)
    k = name.replace(' ', '_').replace('(', '').replace(')', '').replace('=', '').replace('#', 'n')
    A[f'{k}__Mu'] = Mu; A[f'{k}__Md'] = Md; A[f'{k}__conjugated'] = cj
    for key in ('Wu', 'Xu', 'Wd', 'Xd', 'mu', 'md', 'V'):
        A[f'{k}__{key}'] = mb[key]
    for K in CARRIERS:
        A[f'{k}__Phat_u_{K}'] = Pu[K]; A[f'{k}__Phat_d_{K}'] = Pd[K]
    for cls in ('D3', 'D6'):
        for s in (1.0, 0.5):
            m, r = worst(Pu, Pd, cls, np.ones(4 if cls == 'D3' else 7), s, Mu, Md, pen=False)
            A[f'{k}__Mstar_eq_{cls}_x{s}'] = np.array([r[x] for x in ROWS])
A['ROWS'] = np.array(list(ROWS)); A['VEV'] = VEV
np.savez('obs4_archive.npz', **A)
print(f"saved {len(A)} arrays; realisations: {list(R)}")
