"""R19-9: full-precision photon axial coefficients (R18-9 lib9.phot_quad, unmodified) at N = 224 for the root edge, saved to .npy
(the solve4k_N224.out header prints only 7 digits, which moves the ill-conditioned b_s direction by ~1e-4)."""
import os, sys, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'arch18_9'))
import lib9 as L9
t0 = time.time(); N = int(sys.argv[1])
P = L9.phot_quad(2.9435, 1.0, N)
np.save(f'photquad_N{N}.npy', np.r_[P['T2g'], P['Eg'], P['muE']])
print(f'N={N}: T {P["T2g"].tolist()} E {P["Eg"].tolist()} muE {P["muE"]!r} [{time.time()-t0:.0f}s]')
