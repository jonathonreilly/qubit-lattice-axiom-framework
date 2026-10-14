"""F5 validation of f5_lib (general-h SF law) against F1's unmodified f1_lib, plus T2g symmetry/domain checks.
(1) h = E_g on F1's octant grid: f5 dm_gen vs f1 dm_sf at t = 0, 0.003, 0.006 (must agree to rounding).
(2) h = E_g on the half-zone domain x in [-pi, pi] (evenness in q_x used by F1 is then not assumed).
(3) h = T2g: evenness dm(t) = dm(-t) (C4 about z maps h_xy -> -h_xy); domain x in [-pi,pi], y in [0,pi], z in [0,pi]
    against the larger domain x, y in [-pi, pi] (uses only C2 about z and q_z parity).
(4) free-band SF rows: e''(0) of -2<E o Phi_t> per Dirac field for E_g and T2g on a midpoint grid vs dfam.evaluate (R18-5,
    unmodified) at a non-root D1 so mu_T2 is not ~0; this fixes the T2g unit normalization against the registered rows."""
import numpy as np, time, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f5_lib import *
import f1_lib
t00 = time.time()
n, hm, mph = 6, 0.25, 6
br = mkbreaks(ROOT[0], CPH, mph)
xo = panels(br, n, hm); xs = panels_sym(br, n, hm)
F = Ferm(*ROOT, mflow=0.01); G = Phot(CPH)
F1F = f1_lib.Ferm(*ROOT, mflow=0.01); F1G = f1_lib.Phot(CPH); g1 = f1_lib.Grid(br, n, hm)
print('(1) E_g octant, %d nodes/axis: f5 vs f1' % len(xo[0]), flush=True)
for t in (0.0, 0.003, 0.006):
    a = dm_gen(F, G, H_EG, xo, xo, xo, t, nrk=2); b = f1_lib.dm_sf(F1F, F1G, g1, t, nrk=2)
    print('   t=%.3f  f5 %+.13e  f1 %+.13e  diff %.1e' % (t, a, b, a - b), flush=True)
print('(2) E_g, x on [-pi,pi]:', flush=True)
for t in (0.0, 0.003):
    a = dm_gen(F, G, H_EG, xs, xo, xo, t, nrk=2)
    print('   t=%.3f  %+.13e' % (t, a), flush=True)
# coarser grid for T2g domain checks
n2, hm2, mph2 = 4, 0.35, 3
br2 = mkbreaks(ROOT[0], CPH, mph2)
xo2 = panels(br2, n2, hm2); xs2 = panels_sym(br2, n2, hm2)
print('(3) T2g, coarse grid %d nodes/half-axis' % len(xo2[0]), flush=True)
for t in (0.003, -0.003):
    a = dm_gen(F, G, H_T2, xs2, xo2, xo2, t, nrk=2)
    b = dm_gen(F, G, H_T2, xs2, xs2, xo2, t, nrk=2)
    print('   t=%+.3f  dom[-pi,pi]x[0,pi]x[0,pi] %+.13e   dom[-pi,pi]^2x[0,pi] %+.13e  diff %.1e' % (t, a, b, a - b), flush=True)
a0 = dm_gen(F, G, H_T2, xs2, xo2, xo2, 0.0)
b0 = dm_gen(F, G, H_EG, xo2, xo2, xo2, 0.0)
print('   t=0: T2g-domain %+.13e  octant %+.13e  diff %.1e' % (a0, b0, a0 - b0), flush=True)
# (4) free rows
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'arch'))
import dfam
def free_row(Fb, h, N=96, d=0.01):
    k = (np.arange(N) + 0.5)*2*np.pi/N - np.pi
    X, Y, Z = np.meshgrid(k, k, k, indexing='ij')
    def e(t):
        a, b, c = flow3(Fb, h, X, Y, Z, t, 4)
        M = Fb.mflow + Fb.W(a) + Fb.W(b) + Fb.W(c)
        E = np.sqrt(Fb.s(a)**2 + Fb.s(b)**2 + Fb.s(c)**2 + M*M)
        return -2*E.mean()
    e0 = e(0.0); e1 = e(d); e2 = e(-d); e3 = e(2*d); e4 = e(-2*d)
    h1 = (e1 - 2*e0 + e2)/d**2; h2 = (e3 - 2*e0 + e4)/(2*d)**2
    return (4*h1 - h2)/3
def mu_rows(law, m, npan=2, ngl=8, Nc=4):   # 96 nodes/axis (memory: < 1 GB)
    """dfam.evaluate's muE / muT2 lines (R18-5, registered row formulas) evaluated with D1's own symbol methods."""
    k, wq = dfam.gl_nodes([0.0, law.b, np.pi - law.b, np.pi], npan, ngl)
    S, Sp, Spp, W, Wp, Wpp = law.S(k), law.dS(k), law.d2S(k), law.W(k), law.dW(k), law.d2W(k)
    wt = wq[:, None, None]*wq[None, :, None]*wq[None, None, :]
    mean = lambda f: float(np.sum(wt*f))
    Sx, Sy, Sz = S[:, None, None], S[None, :, None], S[None, None, :]
    M = m + W[:, None, None] + W[None, :, None] + W[None, None, :]
    E = np.sqrt(Sx**2 + Sy**2 + Sz**2 + M**2)
    px = Sx*Sp[:, None, None] + M*Wp[:, None, None]; py = Sy*Sp[None, :, None] + M*Wp[None, :, None]
    Hxx = (Sp**2 + S*Spp + Wp**2)[:, None, None] + M*Wpp[:, None, None]
    Hyy = (Sp**2 + S*Spp + Wp**2)[None, :, None] + M*Wpp[None, :, None]
    Hxy = Wp[:, None, None]*Wp[None, :, None]
    return -Nc*(-0.125*mean((Hxx - Hyy)*(px**2 - py**2)/E)), -Nc*(-0.5*mean(Hxy*px*py/E))
for (bb, rr) in ((1.4, 1/np.sqrt(3)), ROOT):
    Fb = Ferm(bb, rr, mflow=0.01)
    muE, muT2 = mu_rows(D1(bb, rr), 0.01)
    print('(4) D1(%.4f, %.4f) m=0.01: registered row formulas muE %+.6e  muT2 %+.6e' % (bb, rr, muE, muT2), flush=True)
    for N in (64, 80):
        print('     N=%d midpoint: e"(0) E_g %+.6e   T2g %+.6e' % (N, free_row(Fb, H_EG, N), free_row(Fb, H_T2, N)), flush=True)
print('time %.0f s' % (time.time() - t00))
