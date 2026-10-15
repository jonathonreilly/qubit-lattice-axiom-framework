"""OBS-3 controls C1-C3 (PREREG.md 'Runs')."""
import numpy as np, itertools
from obs3_core import *
np.set_printoptions(precision=4, linewidth=150)
P = print
# ---- C1: reproduce OBS-2 branch-B c_TT^d (N=24, m0=0.1, Delta=0, sym, trace, OBS-2 inputs)
for D in ('0.0', '0.5'):
    for symm in (True, False):
        I = {}
        for var in ('sym', 'int', 'ext'):
            I[var], syms = load_kin(24, '0.1', D, var, symmetrise=symm)
        tabs = dict(I=I, syms=syms, opt=(0, 0, 0))
        Vb = INPUTS['obs2']['V']
        real = dict(Wu=F, Xu=F, Xd=F @ Vb, carrier='M1', var='sym', y0mode='trace')
        o = evaluate(real, tabs, inputs='obs2')
        P(f"C1 N=24 m0=0.1 Delta={D} C3-symmetrised={symm}: c_TT^d = {o['d']['cTT']:+.8e}  d_TT^d = {o['d']['dTT']:+.8e}"
          f"   (referee {'-2.10666629e-08 / +7.02222097e-09' if D == '0.0' else '-2.11755110e-08 / +7.05850371e-09'})")
# ---- C3a: C3 covariance of the archived tables
mx = 0
for N in (24, 32, 48, 64, 96):
    for (m, D) in BRACKET:
        for var in ('sym', 'int', 'ext'):
            mx = max(mx, c3_violation(N, m, D, var))
P(f"C3a max C3[111] violation of archived kin tables over N in 24..96, bracket, variants: {mx:.2e} (abs)")
mxf = max(load_flav(N, m, D)[1] for N in (32, 48, 64, 96) for (m, D) in BRACKET)
P(f"C3a flavon table: Qxy vs Qxz (own/partner/third) covariance max |diff| = {mxf:.2e}")
# ---- C2: circulant inputs give zero residual (V = 1; Hermitian circulant textures), M1 and M2, all variants
rng = np.random.default_rng(7)
def perm(p):
    M = np.zeros((3, 3)); M[np.arange(3), p] = 1; return M
worst = {'M1': 0, 'M2': 0}; worst_nonherm = 0; worst_nonherm_iso = 0
for (m, D) in BRACKET:
    tabs = get_tabs(96, m, D)
    for car in ('M1', 'M2'):
        for var in ('sym', 'int', 'ext'):
            for y0mode in ('trace', 'selective'):
                Wu = F @ perm([0, 2, 1])
                real = dict(Wu=Wu, Xu=Wu, Xd=Wu, carrier=car, var=var, y0mode=y0mode)
                o = evaluate(real, tabs, inputs='circ')
                for f, (iso, tet, r) in o['fields'].items():
                    scale = max(abs(iso), 1e-300)
                    worst[car] = max(worst[car], np.abs(r).max() / scale)
        # non-Hermitian circulant: X = W D (complex eigenvalue phases)
        Dm = np.diag(np.exp(1j * rng.uniform(0, 2 * np.pi, 3)))
        real = dict(Wu=F, Xu=F @ Dm, Xd=F @ Dm.conj(), carrier='M2', var='sym', y0mode='trace')
        o = evaluate(real, tabs, inputs='circ')
        for f, (iso, tet, r) in o['fields'].items():
            worst_nonherm = max(worst_nonherm, np.abs(r).max() / max(abs(iso), 1e-300))
            worst_nonherm_iso = max(worst_nonherm_iso, np.abs(r.mean(axis=1)).max() / max(abs(iso), 1e-300))
P(f"C2 Hermitian circulant up and down (V = 1), N=96, bracket x variants x splits: max |residual|/|universal iso|  M1 {worst['M1']:.1e}  M2 {worst['M2']:.1e}")
P(f"C2' non-Hermitian circulant (X = W D), M2: max |residual|/|iso| = {worst_nonherm:.2e}; per-corner isotropic part only: {worst_nonherm_iso:.1e}")
# ---- C3b: assembly covariance under the corner cyclic permutation (rows of W, X permuted; axes permuted)
tabs = get_tabs(96, '0.05', '0.5')
def haar(rng):
    Z = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / np.sqrt(2); Q, R = np.linalg.qr(Z)
    return Q * (np.diag(R) / abs(np.diag(R)))
Pc = perm([2, 0, 1])   # (P W)[c] = W[c-1]: corner c-1 -> c, i.e. x->y->z
mx = 0
for t in range(5):
    Wu, Xu, Xd = haar(rng), haar(rng), haar(rng)
    for car in ('M1', 'M2'):
        for var in ('sym', 'int'):
            o1 = evaluate(dict(Wu=Wu, Xu=Xu, Xd=Xd, carrier=car, var=var), tabs)
            o2 = evaluate(dict(Wu=Pc @ Wu, Xu=Pc @ Xu, Xd=Pc @ Xd, carrier=car, var=var), tabs)
            for f in ('Q', 'uc', 'dc'):   # leptons are not permuted (fixed circulant); their r is roundoff
                r1 = o1['fields'][f][2]; r2 = o2['fields'][f][2]
                # r2[sigma c][sigma a] = r1[c][a], sigma: 0->1->2->0
                s = [1, 2, 0]
                r1p = np.zeros((3, 3))
                for c in range(3):
                    for a in range(3):
                        r1p[s[c], s[a]] = r1[c, a]
                mx = max(mx, np.abs(r1p - r2).max() / max(np.abs(r1).max(), 1e-300))
            for nm in ('u', 'd', 's', 'b'):
                mx = max(mx, abs(o1[nm]['cring'] - o2[nm]['cring']) / max(abs(o1[nm]['cring']), 1e-300))
P(f"C3b assembly covariance under the corner 3-cycle (random W_u, X_u, X_d; M1/M2): max relative mismatch {mx:.1e}")
