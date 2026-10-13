"""R19-11 recheck: photon VWa coefficients at the root photon edge (massless; m-independent), via R18-9's lib9.phot_quad (unmodified)."""
import sys, os, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'arch9'))
import lib9 as L
N = int(sys.argv[1]); t0 = time.time()
P = L.phot_quad(2.9435, 1.0, N)
print('N=%d T %r E %r muE %r  [%.0fs]' % (N, P['T2g'].tolist(), P['Eg'].tolist(), P['muE'], time.time()-t0), flush=True)
np.save(os.path.join(HERE, 'phq_N%d.npy' % N), np.r_[P['T2g'], P['Eg'], P['muE']])
