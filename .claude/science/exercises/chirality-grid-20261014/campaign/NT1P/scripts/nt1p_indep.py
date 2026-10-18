"""NT-1' numerics cross-check (same construction, different numerics): plain polar transport Ns = 64 (no Richardson),
anomaly derivative R by central finite differences (not the analytic formula), Gauss-Legendre (12 nodes) for the u-integrals
instead of Simpson; modulus against |det D_ov(1)|^2 |det D_ov(2)|^(1/2).  Compared with Measure.logrho on 6 kernel nodes.
usage: python3 nt1p_indep.py POOL.npz"""
import numpy as np, sys
from nt1p_lib import *
from lat2d import Geom, nodes
S = Strip(4, 4); G = Geom(4, 4, False, -1); z = np.load(sys.argv[1]); U = [{'x': z['ux'][i], 't': z['ut'][i]} for i in range(len(z['ux']))]
rng = np.random.default_rng(3); J = []
for (a, b) in [(0, 1), (4, 9), (11, 2)][:3]:
    a, b = a % len(U), b % len(U); ph, w = nodes(G, U[a], U[b], 0.6, 4, 'hard'); J.append(S.joined(U[a], U[b], ph[rng.choice(len(w), 2, replace=False)]))
J = S.canon(np.concatenate(J)); P = len(J); n = S.N // 2; model = MODELS['11112']; coef = {1: 4, 2: -2}
w0, V0 = eig_H(S, np.zeros((1, S.nl))); V0 = {'L': V0[0][:, n:], 'R': V0[0][:, :n]}; rows = {'L': S.g5 > 0, 'R': S.g5 < 0}
# --- W0: plain transport, Ns = 64 ---
Ns = 64; V = {(e, c): np.repeat(V0[c][None], P, 0) for (e, c, m) in model}
for j in range(1, Ns + 1):
    for e in (1, 2):
        w, Q = eig_H(S, (j / Ns) * e * J)
        for (ee, c, m) in model:
            if ee != e: continue
            Qs = Q[:, :, n:] if c == 'L' else Q[:, :, :n]; u_, s_, vh = np.linalg.svd(np.conj(np.swapaxes(Qs, 1, 2)) @ V[(e, c)]); V[(e, c)] = Qs @ (u_ @ vh)
W0 = np.zeros(P, complex)
for (e, c, m) in model:
    sg, ld = np.linalg.slogdet(V[(e, c)][:, rows[c], :]); W0 += m * (ld + np.log(sg.astype(complex)))
# --- kbb with GL nodes and finite-difference R ---
xg, wg = np.polynomial.legendre.leggauss(12); ug = 0.5 * (xg + 1); wg = 0.5 * wg
F, Wl = S.FW(J); kap = np.zeros((P, S.np_, S.nl)); Abar = np.zeros((P, S.ns)); eps = 1e-5
for u, wu in zip(ug, wg):
    R = np.zeros((P, S.ns, S.nl)); qt = np.zeros((P, S.ns))
    for e in (1, 2):
        qt += coef[e] * q_of(S, *eig_H(S, u * e * J))
        for l in range(S.nl):
            Bp = u * J.copy(); Bp[:, l] += eps; Bm = u * J.copy(); Bm[:, l] -= eps
            R[:, :, l] += coef[e] * (q_of(S, *eig_H(S, e * Bp)) - q_of(S, *eig_H(S, e * Bm))) / (2 * eps)
    gup = np.einsum('pxl,ql->pqx', R, S.Sup); gdn = np.einsum('pxl,ql->pqx', R, S.Sdn); g = np.where(S.use_up[None], gup, gdn)
    m_ = g.sum(-1); kp = np.einsum('qls,pqs->pql', S.PK, g - m_[:, :, None] * S.corners[None])
    kap += wu * (1 - u) * kp; Abar += wu * qt
kloc = np.einsum('pq,pql->pl', F, kap); kbb = kloc + S.Q(Abar - S.div(kloc))
Wi = W0 - 1j * np.sum(J * kbb, 1)
Wm, r, _ = Measure(S, '11112', sk=-1).logrho(J, parts=True)
d = Wi - Wm; print(f"independent-numerics ln rho minus main ln rho: Re {np.abs(d.real - d.real[0]).max():.2e} (after removing a constant), "
                   f"Im mod 2pi {np.abs(np.angle(np.exp(1j * (d.imag - d.imag[0])))).max():.2e}; |kbb diff| {np.abs(kbb - r['kbb']).max():.2e}")
lm = 2 * vec_logdet(S, J, 0.0, 1)[0].real + 0.5 * vec_logdet(S, J, 0.0, 2)[0].real
print(f"modulus factorization: Re ln rho - [2 ln|det D(1)| + 0.5 ln|det D(2)|] spread {np.ptp(Wm.real - lm):.2e}")
print(f"phase of rho over the 6 nodes (main, relative to node 0): " + " ".join(f"{v:+.4f}" for v in np.angle(np.exp(1j * (Wm.imag - Wm.imag[0])))))
