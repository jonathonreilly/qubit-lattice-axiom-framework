"""OBS-3: (1) kernel identity K_fl(c,c',a) = I_00(c',a) for covariant on-site carriers, to all digits, over N and bracket;
(2) up-flat with on-site carriers: d-row(Q) = kbar <delta^d, R^d - mean> is kernel-independent -> scan (P_g, D_g) for zeros;
(3) beyond one loop (suggested): corner non-universality of two-loop flavour words for the equal-modulus realisation B-gen."""
import numpy as np, itertools
from obs3_core import *
P = print
np.set_printoptions(precision=4, linewidth=150)
mx = 0
for N in (32, 48, 64, 96):
    for (m, D) in BRACKET:
        I, syms = load_kin(N, m, D, 'sym'); opt, cov = load_flav(N, m, D)
        own, partner, third = opt
        # K(x,y) along (x,y,z) = (own, partner, third) should equal I_00(e_y) along (x,y,z)
        Iy = I['y']['00']
        mx = max(mx, abs(own - Iy[0]) / abs(Iy[0]), abs(partner - Iy[1]) / abs(Iy[1]), abs(third - Iy[2]) / abs(Iy[2]))
P(f"(1) max relative |K_fl(x,y,a) - I_00(e_y,a)| over N in 32..96 and the bracket: {mx:.1e}")
for (m, D) in BRACKET:
    I, syms = load_kin(96, m, D, 'sym'); k = I['x']['00']
    P(f"    N=96 m0={m} D={D}: kappa_par {k[0]:+.6e} kappa_perp {k[1]:+.6e}  Delta-kappa {k[0]-k[1]:+.2e}  kbar {k.mean():+.6e}")
# (2) up-flat, on-site carriers: Q-part of the d isotropic row = kbar * sum_c delta^d_c (R^Q_c - mean), R^Q = diag(H_u + H_d)
V = INPUTS['pdg24']['V']; yu = INPUTS['pdg24']['mu'] / VEV; yd = INPUTS['pdg24']['md'] / VEV
def perm(p):
    M = np.zeros((3, 3)); M[np.arange(3), p] = 1; return M
vals = []
for pg in itertools.permutations(range(3)):
    for p1 in np.linspace(0, 2 * np.pi, 181):
        for p2 in np.linspace(0, 2 * np.pi, 181):
            Wu = F @ perm(pg) @ np.diag(np.exp(1j * np.array([0, p1, p2]))); Wd = Wu @ V
            Rq = (np.abs(Wu)**2 @ yu**2) + (np.abs(Wd)**2 @ yd**2)
            dd = np.abs(Wd[:, 0])**2 - 1 / 3
            vals.append((np.dot(dd, Rq - Rq.mean()), pg, p1, p2, np.abs(Rq - Rq.mean()).max()))
v = np.array([x[0] for x in vals])
P(f"(2) up-flat: <delta^d, R^Q - mean> over P_g x D_g grid: min {v.min():+.3e} max {v.max():+.3e} (y_b^2 = {yd[2]**2:.3e}); "
  f"sign changes: {'yes' if v.min() < 0 < v.max() else 'no'};  min over grid of max_c |R^Q_c - mean| = {min(x[4] for x in vals):.3e} (= {min(x[4] for x in vals)/yd[2]**2:.4f} y_b^2)")
# (3) two-loop words for B-gen
try:
    z = np.load('univ_B_gen.npz')
    Yu, Yd = z['Yu'], z['Yd']
    Hu, Hd = Yu @ Yu.conj().T, Yd @ Yd.conj().T
    def spread(M):
        d = np.diag(M).real; return np.abs(d - d.mean()).max()
    P("(3) equal-modulus realisation B-gen, corner-diagonal non-universality max_c |diag - mean| of flavour words:")
    for name, M in (('H_u + H_d (one loop, Q)', Hu + Hd), ('Y_u^dag Y_u (one loop, u^c)', Yu.conj().T @ Yu), ('Y_d^dag Y_d (one loop, d^c)', Yd.conj().T @ Yd),
                    ('H_u^2', Hu @ Hu), ('H_d^2', Hd @ Hd), ('H_u H_d + H_d H_u', Hu @ Hd + Hd @ Hu), ('(Y_u^dag Y_u)^2', (Yu.conj().T @ Yu) @ (Yu.conj().T @ Yu))):
        P(f"    {name:28s}: spread {spread(M):.3e}   mean {np.diag(M).real.mean():.3e}")
    P(f"    one-loop scale kbar ~ 1.15e-2; a two-loop coefficient ~ kbar^2 ~ 1.3e-4 (SUGGESTED estimate) times the spreads above")
except FileNotFoundError:
    P("(3) univ_B_gen.npz not found")
