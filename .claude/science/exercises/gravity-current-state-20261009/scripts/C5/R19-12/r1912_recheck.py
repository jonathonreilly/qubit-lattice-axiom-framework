"""R19-12 recheck of archived runners before use (all imported UNMODIFIED from ../arch/).
(1) R16-10 point functions vs R16-2/R13-7 runners (r1610_validate 'exact' logic, N=32).
(2) R16-10 scan rows reproduced: D1(1.0,1/sqrt3)+Gph(3.0) [-5.1692], G(2.6)+Gph(3.0) [-1.1126] at N=48 (r1610_scan_N48.out:17,47).
(3) R16-2 photon moments reproduced: G12 D1(1.0,0.2) m=0.05 N=128 [+0.0993]; G0 G(1.0) m=0.05 N=128 [-0.0988].
(4) The root photon gammaG_w(2.9435, 0.198093) (R18-5 photon.py) equals R16-10's Gph(2.9435) (SymG h): max |d diff|.
(5) Root npy contents; scalar U rows and Dirac UD rows at the refined root vs R18-9's table (C5_R18-9_report.md:225-227)."""
import os, sys, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); A = os.path.join(HERE, '..', 'arch')
sys.path.insert(0, os.path.join(A, 'R16-10')); sys.path.insert(1, os.path.join(A, 'R16-10', 'arch', 'R16-2'))
t0 = time.time()
from r1610_eval import *
from r1610_laws import *
cwd = os.getcwd(); os.chdir(os.path.join(A, 'R16-10', 'arch', 'R16-2'))
import r162_scalar, r137_onshell, r162_laws
from r101_dirac_moment_copy import moment
os.chdir(cwd)
# (1)
N = 32; m = 0.1; lam = 0.05; h = 0.02
L = r162_laws.GScal(1.4, 1.0, 2.0, m); ref = r162_scalar.dc_scalar(L, N, lam, h)
mine = lattice_part(0, N, m, lam, L.u, L.d, -2.0, -1.0, h)
print('(1) scalar G(1.4) ph(1,2) N=32: runner %+.10f | pointwise %+.10f | archived out: -2.4249903748' % (ref[0], mine[0]))
L = r162_laws.D1Law(1.4, 1/np.sqrt(3), 0.7, 1.4, m); c2, ct, dE0 = r137_onshell.ce2_minus_1(L, N, lam, h)
mine = lattice_part(0.5, N, m, lam, (L.S, L.W), L.d, -2.0, -1.0, h)
print('(1) Dirac D1(1.4,1/sqrt3) ph(0.7,1.4) N=32: runner %+.10f | pointwise %+.10f | archived out: -9.8481846559' % (c2/2*U, mine[0]), flush=True)
# (2)
for mat, ref in [(('D1', 1.0, 1/np.sqrt(3)), -5.1692), (('G', 2.6), -1.1126)]:
    d = photon('Gph', 3.0); box = min(3.0, mat[1]); r1 = min(0.75*box, 0.9); r0 = 0.35*r1
    if mat[0] == 'G': spin, matter, mm = 0, scalar_G(mat[1]), 0.0
    else: spin, matter, mm = 0.5, dirac_D1(mat[1], mat[2]), 1e-6
    lp, tp = lattice_part(spin, 48, mm, 0.0, matter, d, r0, r1, h=0.02)
    print('(2) %s Gph(3.0) N=48: F(0+) = %+.4f (archived %+.4f)' % (str(mat[:2]), K[spin] + lp, ref), flush=True)
# (3)
G12 = moment(r162_laws.D1Law(1.0, 0.2, 1.0, 2.0, 0.05), 128)['tot']
G0 = r162_scalar.photon_moment(r162_laws.GScal(1.0, 1.0, 2.0, 0.05), 128)
print('(3) G12 D1(1.0,0.2) m=0.05 N=128 = %+.4f (archived +0.0993); G0 G(1.0) = %+.4f (archived -0.0988)' % (G12, G0), flush=True)
# (4)
sys.path.insert(0, os.path.join(A, 'R18-5'))
import photon as ph185
q = np.linspace(-np.pi, np.pi, 200001)
pr = ph185.photonGw(2.9435, np.pi - 2.9435); dG = photon('Gph', 2.9435)
print('(4) root photon: w = pi - 2.9435 = %.6f; max|sig_R18-5 - d_Gph| = %.2e; max d\' = %.6f, min d\' = %.2e, d(pi) = %.6f'
      % (np.pi - 2.9435, np.abs(pr.sig(q) - dG(q)).max(), pr.maxdp, pr.mindp, pr.dpi), flush=True)
# (5)
r9 = np.load(os.path.join(A, 'R18-9', 'root4k_N224.npy')); r13 = np.load(os.path.join(A, 'R18-13', 'root_refR18-9.npy'))
print('(5) root4k_N224.npy (b_s,b_f,r,a,fr,b_g,fw,m) =', r9); print('    root_refR18-9.npy =', r13)
from content4 import scalw
from smud_lib import dirac, NS, ND, NV
bs, bf, r, a = r13[:4]
Sv = scalw(bs, 1.0, 0.01, vert='U')[0]; Fv = dirac(bf, r, m=0.01, q=(4, 10))
print('    per real scalar (T,E,muE) %+.6e %+.6e %+.6e  [R18-9 table: -6.2776e-4 -3.6216e-4 +1.06276e-2]' % tuple(Sv[:3]))
print('    per Dirac (T,E,muE,muT2)  %+.6e %+.6e %+.6e %+.3e [R18-9 table: +1.98457e-3 +1.3215e-4 -1.70941e-2 ~0]' % tuple(Fv))
print('    counts NS, ND, NV =', NS, ND, NV)
print('elapsed %.1fs' % (time.time() - t0))
