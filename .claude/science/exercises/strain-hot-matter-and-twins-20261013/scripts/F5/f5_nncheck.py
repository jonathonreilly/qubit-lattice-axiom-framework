"""F5 check: R19-35 Lemma R1 rank-one form Hess(nn) = -(w/12)<p_z^4/E^3> (w = -2 per Dirac field) on the GL octant grid,
against the finite-difference SF Hessian in f5_nn_156.out; plus the E_g row by the registered formula (dfam muE)."""
import numpy as np, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f5_lib import *
for n, hm, mph in ((4, 0.35, 3), (6, 0.25, 6)):
    F = Ferm(*ROOT, mflow=0.01)
    br = mkbreaks(ROOT[0], CPH, mph); x, w = panels(br, n, hm)
    X, Y = x[:, None, None], x[None, :, None]
    tot = 0.0; totE = 0.0
    for i0 in range(0, len(x), 16):
        Z = x[None, None, i0:i0+16]; WW = w[:, None, None]*w[None, :, None]*w[None, None, i0:i0+16]
        M = 0.01 + F.W(X) + F.W(Y) + F.W(Z); E = np.sqrt(F.s(X)**2 + F.s(Y)**2 + F.s(Z)**2 + M*M)
        pz = F.s(Z)*F.ds(Z) + M*F.dW(Z)
        tot += float((WW*pz**4/E**3).sum())
    print('%d nodes: rank-one form -(w/12)<p_z^4/E^3> = %+.7e  (R19-35: +2.164325e-2)' % (len(x), (2/12)*tot), flush=True)
