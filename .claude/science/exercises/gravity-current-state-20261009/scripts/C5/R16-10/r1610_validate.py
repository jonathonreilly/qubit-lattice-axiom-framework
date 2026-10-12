"""R16-10 validation: (1) point functions reproduce the archived runners exactly (chi = 0, same grid);
(2) the split F = BZ(1-chi) + cont(chi) reproduces the direct runners at finite (m, lam) and large N."""
import numpy as np, sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'arch', 'R16-2'))
os.chdir(os.path.join(HERE, 'arch', 'R16-2'))
import r162_scalar, r137_onshell, r162_laws
from r85_box_qed_copy import Law
os.chdir(HERE)
from r1610_eval import *
from r1610_laws import *
t0 = time.time()
mode = sys.argv[1]
if mode == 'exact':
    N = 32; m = 0.1; lam = 0.05; h = 0.02
    L = r162_laws.GScal(1.4, 1.0, 2.0, m)
    ref = r162_scalar.dc_scalar(L, N, lam, h)
    mine = lattice_part(0, N, m, lam, L.u, L.d, -2.0, -1.0, h)   # chi = 0 everywhere in the BZ
    print('scalar G(1.4) ph(1,2) N=32 m=0.1 lam=0.05: runner %+.10f (sea %+.10f) | mine %+.10f (sea %+.10f)' % (ref[0], ref[1], mine[0], mine[1]))
    L = r162_laws.D1Law(1.4, 1/np.sqrt(3), 0.7, 1.4, m)
    c2, ct, dE0 = r137_onshell.ce2_minus_1(L, N, lam, h)
    mine = lattice_part(0.5, N, m, lam, (L.S, L.W), L.d, -2.0, -1.0, h)
    print('Dirac D1(1.4,1/sqrt3) ph(0.7,1.4) N=32: runner %+.10f (tad %+.10f) | mine %+.10f (tad %+.10f)' % (c2/2*U, ct/2*U, mine[0], mine[1]))
if mode == 'split':
    for spin, lab in [(0, 'G(1.4) ph(1,2)'), (0.5, 'D1(1.4,1/sqrt3) ph(0.7,1.4)')]:
        for (m, lam) in [(0.1, 0.05), (0.2, 0.05)]:
            if spin == 0:
                L = r162_laws.GScal(1.4, 1.0, 2.0, m); mat = L.u; r0, r1 = 0.25, 0.85
            else:
                L = r162_laws.D1Law(1.4, 1/np.sqrt(3), 0.7, 1.4, m); mat = (L.S, L.W); r0, r1 = 0.2, 0.6
            cp = cont_part(spin, m, lam, r0, r1, h=0.004)
            for N in (48, 64, 96):
                lp, tp = lattice_part(spin, N, m, lam, mat, L.d, r0, r1, h=0.02)
                print('%-28s m=%.2f lam=%.2f N=%3d | split: lattice %+9.5f + cont %+9.5f = %+9.5f' % (lab, m, lam, N, lp, cp, lp + cp), flush=True)
            for N in (96, 128):
                if spin == 0:
                    ref = r162_scalar.dc_scalar(L, N, lam, r162_scalar.hstep(m, lam))[0]
                else:
                    ref = r137_onshell.ce2_minus_1(L, N, lam, r162_scalar.hstep(m, lam))[0]/2*U
                print('%-28s m=%.2f lam=%.2f N=%3d | direct runner %+9.5f' % (lab, m, lam, N, ref), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
