"""R18-13: check the own-direction placement identities (proved in the report):
 d face2/d wo = -Pi_T2g(0)/2, d face1/d wo = -Pi_T2g(0)/4, d face1/d wd = -Pi_Eg(0)/8, d face2/d wd = 0, axial rows blind,
with Pi_e(0) = -<W_e/E> at q = 0 (photon, VWa-geo, R18-9 root edge)."""
import os, sys, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'arch18'))
import vwface as V
from photon import photonGw
law = photonGw(2.9435, np.pi - 2.9435); a = -0.1760950036
for N in (96, 128):
    out = {}
    for pol in ('T2g', 'Eg'):
        W0, E0 = V.pair_W(law, N, (0, 0, 0), V.POL[pol], a, ((0.0, 0.0),))
        out[pol] = -np.mean(W0[0]/E0)
    print('N=%d Pi_T2g(0) %+.8e Pi_Eg(0) %+.8e -> predicted d face2/d wo %+.6e, d face1/d wo %+.6e, d face1/d wd %+.6e'
          % (N, out['T2g'], out['Eg'], -out['T2g']/2, -out['T2g']/4, -out['Eg']/8), flush=True)
