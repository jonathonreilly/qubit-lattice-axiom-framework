"""R19-9: whole-zone v_max of the scalar edge (archived zz.ZLaw.vmax, as R18-9) at the O(q) root and the exact-vertex roots."""
import os, sys, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'arch18'))
from zz import ZLaw
S = np.load('resolve_sols.npy'); fr, m = 1.0, 0.01
for row in S:
    bs = row[1]; wA = fr*(np.pi - bs); law = ZLaw([1.0, 0.0], [bs + wA/2], wA)
    print(f'r = {row[0]:<5}: b_s = {bs:.10f}  scalar v_max = {law.vmax(m):.9f} ; Dirac r_D = {row[3]:.10f} < 1/sqrt3 = {1/np.sqrt(3):.6f}: {row[3] < 1/np.sqrt(3)}')
