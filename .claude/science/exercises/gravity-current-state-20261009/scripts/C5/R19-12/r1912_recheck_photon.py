"""R19-12 (4') root-photon identity on the open zone (|q| < pi; q = +-pi is the odd symbol's branch point, where
the two codes pick opposite signs of the same value, |d(pi)| = (pi + c)/2)."""
import os, sys, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); A = os.path.join(HERE, '..', 'arch')
sys.path.insert(0, os.path.join(A, 'R16-10')); sys.path.insert(1, os.path.join(A, 'R16-10', 'arch', 'R16-2'))
from r1610_laws import photon
sys.path.insert(0, os.path.join(A, 'R18-5')); import photon as ph185
q = np.linspace(-np.pi, np.pi, 200001)[1:-1]
for c in (2.9435, 2.9378):
    pr = ph185.photonGw(c, np.pi - c); dG = photon('Gph', c)
    print('c=%.4f: max|sig_R18-5 - d_Gph| on |q|<pi = %.2e ; |d(pi)| both: %.6f %.6f ; (pi+c)/2 = %.6f' % (c, np.abs(pr.sig(q) - dG(q)).max(), pr.dpi, abs(float(dG(np.array(np.pi - 1e-12)))), (np.pi + c)/2))
