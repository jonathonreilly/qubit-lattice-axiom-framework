"""T10 - compare with the recorded tau0=6, nk=2 series  A = .135/.508/.806/.981,
B = .037/.209/.434/.629  for L = 6/8/10/12, and probe polarisation dependence."""
import numpy as np, sys; sys.path.insert(0,".")
from bridge_fit import *
pol = {'TT  (0,1,-1,0)':[0,1,-1,0], 'conf(1,1,1,1)':[1,1,1,1],
       'long(1,0,0,0)':[1,0,0,0],  'tran(0,1,0,0)':[0,1,0,0]}
for name,AL in pol.items():
    print(f"\nT10 polarisation {name},  plain Delta, m=0, amp=0.03, nk=2, tau0=6"); print(HDR)
    for L in (6,8,10,12):
        for d in run(L,0.03,2,AL,[(6.0,0.0,False)]): print(line(d), flush=True)
