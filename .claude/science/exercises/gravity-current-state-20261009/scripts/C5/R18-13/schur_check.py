"""R18-13: q = 0 Schur identities used in Lemma S (superpotential invariance of d1, d2):
Pi_face1(0) = (3 Pi_Eg(0) + Pi_T2g(0))/4 and Pi_face2(0) = Pi_T2g(0), Pi_body(0) = (Pi_Eg(0) + 2 Pi_T2g(0))/3 (photon VWa-geo, root edge)."""
import os, sys, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'arch18'))
import vwface as V
from photon import photonGw
law = photonGw(2.9435, np.pi - 2.9435); a = -0.1760950036
N = 96; P = {}
for pol in ('T2g', 'Eg', 'face1', 'face2', 'body'):
    W0, E0 = V.pair_W(law, N, (0, 0, 0), V.POL[pol], a, ((0.0, 0.0),)); P[pol] = -np.mean(W0[0]/E0)
print('N=%d Pi(0): ' % N + ' '.join('%s %+.10e' % kv for kv in P.items()))
print('face1 - (3Eg+T2g)/4 = %+.2e ; face2 - T2g = %+.2e ; body - (Eg+2T2g)/3 = %+.2e'
      % (P['face1'] - (3*P['Eg'] + P['T2g'])/4, P['face2'] - P['T2g'], P['body'] - (P['Eg'] + 2*P['T2g'])/3))
