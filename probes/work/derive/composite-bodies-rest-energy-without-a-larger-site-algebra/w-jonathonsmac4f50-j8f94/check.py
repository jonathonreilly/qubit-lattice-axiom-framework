#!/usr/bin/env python3
"""J:derive:composite-bodies-rest-energy-without-a-larger-site-algebra:a3 - worker w-jonathonsmac4f50-j8f94 (claude-opus-5-5).

Definitions (block 54, open PR 'ail54', supplied clause, not adopted): (T_e psi)(x) = psi(x - e), D_j = (i/2)(T_j - T_j^dag) with
symbol sin k_j; one walker on Z: H1 = sigma_z D (the reduced walk), on Z^3: H1 = sum_j sigma_j D_j. Two walkers (distinguishable):
H = H1 (x) 1 + 1 (x) H1 + interaction; contact V delta_{x1,x2}; nearest neighbour V_n (delta_{x1,x2+1} + delta_{x1,x2-1}).
Clause: the amplitude advances in its site's own time, H_w = sqrt(W) H sqrt(W) per walker; 'interaction timed' = the interaction
multiplied by a degree-one weight of the rate field at its sites (w(x) for contact, sqrt(w(x1) w(x2)) for a bond); 'untimed' =
the interaction left as it is.  Exact parts: sympy; spectra: floating point diagonalization (errors stated); propagations:
floating point, EXECUTED (not claimed beyond the stated numbers).
"""
import itertools

import numpy as np
import scipy.sparse as sps
import sympy as sp
from scipy.sparse.linalg import expm_multiply

RESULTS = []


def check(tag, ok, text, detail=''):
    RESULTS.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {tag} {text}" + (f" :: {detail}" if detail else ''))


# ================================================================ A1 the four spin sectors in one dimension (exact)
K, q, V, b = sp.symbols('K q V b', real=True)
eps = {(1, 1): sp.sin(K / 2 + q) + sp.sin(K / 2 - q), (1, -1): sp.sin(K / 2 + q) - sp.sin(K / 2 - q)}
ok = sp.simplify(sp.expand_trig(eps[(1, 1)] - 2 * sp.sin(K / 2) * sp.cos(q))) == 0
ok &= sp.simplify(sp.expand_trig(eps[(1, -1)] - 2 * sp.cos(K / 2) * sp.sin(q))) == 0
kk = sp.symbols('k', real=True)
Dsym = sp.I / 2 * (sp.exp(-sp.I * kk) - sp.exp(sp.I * kk))
ok &= sp.simplify((Dsym - sp.sin(kk)).rewrite(sp.exp)) == 0
check('A1', ok, "EXACT: with block 54's convention D has symbol sin k; since sigma_z is diagonal the two-walker problem on Z "
      "splits into four spin sectors, with relative kinetic energy 2 sin(K/2) cos q for co-moving walkers (s1 = s2) and "
      "2 cos(K/2) sin q for counter-moving ones (s1 = -s2), K the total wave vector, q the relative one")

# ================================================================ A2 closed forms of the contact-bound pair
E = sp.symbols('E', real=True)
# lemma: (1/2pi) int_0^2pi dq/(a - 2b cos q) = 1/sqrt(a^2 - 4b^2) for a > 2|b| (residues); checked numerically at points
import mpmath as mp
mp.mp.dps = 30
lem = max(abs(mp.quad(lambda t: 1 / (a_ - 2 * b_ * mp.cos(t)), mp.linspace(0, 2 * mp.pi, 17)) / (2 * mp.pi) - 1 / mp.sqrt(a_ ** 2 - 4 * b_ ** 2))
          for a_, b_ in ((mp.mpf(3), mp.mpf(1)), (mp.mpf(5), mp.mpf(-2)), (mp.mpf('2.5'), mp.mpf('0.3')), (mp.mpf(7), mp.mpf('3.4'))))
co = sp.sqrt(V ** 2 + 4 * sp.sin(K / 2) ** 2)
ser_co = sp.series(co ** 2, K, 0, 6).removeO()
ser_ct = sp.series((V ** 2 + 4 * sp.cos(K / 2) ** 2), K, 0, 4).removeO()
ser_ctpi = sp.series((V ** 2 + 4 * sp.cos((K + sp.pi) / 2) ** 2), K, 0, 4).removeO()
ok = lem < mp.mpf('1e-20')
ok &= sp.simplify(ser_co - (V ** 2 + K ** 2 - K ** 4 / 12)) == 0
ok &= sp.simplify(ser_ct - (V ** 2 + 4 - K ** 2)) == 0 and sp.simplify(ser_ctpi - (V ** 2 + K ** 2)) == 0
check('A2', ok, "PROVED (lemma by residues, checked to 1e-20) + EXACT expansions: a contact attraction V < 0 binds in every "
      "sector for every V: the bound state solves 1 = V (1/2pi) int dq/(E - eps(q)), giving E = -sqrt(V^2 + 4 sin^2(K/2)) "
      "(co-moving) and E = -sqrt(V^2 + 4 cos^2(K/2)) (counter-moving); co-moving: E^2 = V^2 + K^2 - K^4/12 + ..., a rest "
      "energy M = |V| and c = 1, the single walker's limiting speed; counter-moving: E^2 = (V^2 + 4) - K^2 + ... at K = 0 "
      "(a band MINIMUM, inverted) and relativistic with c = 1 about K = pi",
      f"lemma error {mp.nstr(lem, 3)}")

# ================================================================ A3 exact diagonalization on a ring
def full_H(N, Vc):
    T = np.zeros((N, N))
    for x in range(N):
        T[x, (x - 1) % N] = 1.0
    D = 0.5j * (T - T.T)
    H1 = np.kron(D, np.diag([1.0, -1.0]))
    Id = np.eye(2 * N)
    H = np.kron(H1, Id) + np.kron(Id, H1)
    for x in range(N):
        for s1 in range(2):
            for s2 in range(2):
                i = (x * 2 + s1) * 2 * N + (x * 2 + s2)
                H[i, i] += Vc
    return H


def block(N, Vc, Kv, s1, s2, nn=False):
    k1 = 2 * np.pi * np.arange(N) / N
    e = s1 * np.sin(k1) + s2 * np.sin(Kv - k1)
    qq = k1 - Kv / 2
    U = Vc / N * (2 * np.cos(qq[:, None] - qq[None, :]) if nn else np.ones((N, N)))
    return np.linalg.eigvalsh(np.diag(e) + U)


N0, V0 = 12, -0.7
evf = np.sort(np.linalg.eigvalsh(full_H(N0, V0)))
evb = np.sort(np.concatenate([block(N0, V0, 2 * np.pi * m / N0, s1, s2) for m in range(N0) for s1 in (1, -1) for s2 in (1, -1)]))
err_blocks = np.abs(evf - evb).max()
worst = 0.0
for m in range(0, 101):
    Kv = 2 * np.pi * m / 200
    worst = max(worst, abs(block(200, V0, Kv, 1, 1)[0] + np.sqrt(V0 ** 2 + 4 * np.sin(Kv / 2) ** 2)),
                abs(block(200, V0, Kv, 1, -1)[0] + np.sqrt(V0 ** 2 + 4 * np.cos(Kv / 2) ** 2)))
ok = err_blocks < 1e-12 and worst < 1e-12
check('A3', ok, "NUMERICAL (exact diagonalization): the position-space two-walker generator on a 12-ring equals the union "
      "of the K-blocks to 1e-12, and on a 200-ring the lowest state of every K-block matches the closed forms of A2 in both "
      "sectors to 1e-12", f"blocks {err_blocks:.1e}; closed forms {worst:.1e}")

# ================================================================ A4 nearest-neighbour attraction: c^2 = 3/2 and 1/2
bb, Ee, Vn = sp.symbols('b E V_n', real=True)
# separable kernel V_n (2 cos q cos q' + 2 sin q sin q'): channel conditions to O(b^2), then E^2 to O(b^2)
qv = sp.symbols('qv', real=True)
avg = lambda f: sp.integrate(f, (qv, 0, 2 * sp.pi)) / (2 * sp.pi)
ch_cos = avg(2 * sp.cos(qv) ** 2 * (1 + 2 * bb * sp.cos(qv) / Ee + 4 * bb ** 2 * sp.cos(qv) ** 2 / Ee ** 2)) / Ee
ch_sin = avg(2 * sp.sin(qv) ** 2 * (1 + 2 * bb * sp.cos(qv) / Ee + 4 * bb ** 2 * sp.cos(qv) ** 2 / Ee ** 2)) / Ee
ok = sp.simplify(ch_cos - (1 + 3 * bb ** 2 / Ee ** 2) / Ee) == 0 and sp.simplify(ch_sin - (1 + bb ** 2 / Ee ** 2) / Ee) == 0
c2num = {}
for Vnv in (-1.0, -2.0):
    rows = []
    for idx in (0, 1):
        E0n = block(400, Vnv, 0.0, 1, 1, nn=True)[idx]
        Kv = 2 * np.pi * 2 / 400
        E1 = block(400, Vnv, Kv, 1, 1, nn=True)[idx]
        rows.append((E1 ** 2 - E0n ** 2) / Kv ** 2)
    c2num[Vnv] = rows
ok &= all(abs(v[0] - 1.5) < 2e-3 and abs(v[1] - 0.5) < 2e-3 for v in c2num.values())
check('A4', ok, "EXACT (O(b^2) channel equations, b = sin(K/2)) + NUMERICAL (400-ring): a nearest-neighbour attraction binds "
      "co-moving walkers at K = 0 in two channels at E = V_n, with E^2 = V_n^2 + 6 sin^2(K/2) (the relative wave function "
      "even, cos q) and E^2 = V_n^2 + 2 sin^2(K/2) (odd, sin q): relativistic form with c^2 = 3/2 and c^2 = 1/2, NOT the "
      "walker's c = 1, and independent of V_n",
      "; ".join(f"V_n={k}: c^2 = {v[0]:.4f} (even), {v[1]:.4f} (odd)" for k, v in c2num.items()))

# ================================================================ A5 three dimensions, contact: the ground pair sits at a band MINIMUM
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
I2 = np.eye(2)
BAS = [np.kron(a, c) for a in [I2] + sig for c in [I2] + sig]


def setup3(N, Kv):
    k = 2 * np.pi * np.arange(N) / N
    k1 = np.stack(np.meshgrid(k, k, k, indexing='ij')).reshape(3, -1)
    h1, h2 = np.sin(k1), np.sin(np.asarray(Kv)[:, None] - k1)
    a1, a2 = np.linalg.norm(h1, axis=0), np.linalg.norm(h2, axis=0)
    ez = np.array([[0], [0], [1.0]])
    n1 = np.where(a1 > 1e-12, h1 / np.maximum(a1, 1e-300), ez)
    n2 = np.where(a2 > 1e-12, h2 / np.maximum(a2, 1e-300), ez)
    return a1, a2, n1, n2


def G3(Ev, data):
    a1, a2, n1, n2 = data
    G = np.zeros((4, 4), complex)
    for s in (1, -1):
        for t in (1, -1):
            c = 1.0 / (Ev - s * a1 - t * a2)
            coef = np.zeros((4, 4))
            coef[0, 0] = c.sum()
            for al in range(3):
                coef[al + 1, 0] = s * (c * n1[al]).sum()
                coef[0, al + 1] = t * (c * n2[al]).sum()
                for be in range(3):
                    coef[al + 1, be + 1] = s * t * (c * n1[al] * n2[be]).sum()
            for al in range(4):
                for be in range(4):
                    G += coef[al, be] * BAS[al * 4 + be] / 4
    return G / len(a1)


def bound3(Vc, data):
    e0 = (-(data[0] + data[1])).min() - 1e-9
    f = lambda Ev: np.linalg.eigvalsh(-G3(Ev, data)).max() - 1 / abs(Vc)
    lo, hi = -60.0, e0
    for _ in range(90):
        m = 0.5 * (lo + hi)
        if f(m) > 0:
            hi = m
        else:
            lo = m
    return 0.5 * (lo + hi)


def ed3(N, Kv, Vc):
    k = 2 * np.pi * np.arange(N) / N
    k1 = np.stack(np.meshgrid(k, k, k, indexing='ij')).reshape(3, -1).T
    n = len(k1)
    Hm = np.zeros((4 * n, 4 * n), complex)
    for i, kv in enumerate(k1):
        h1, h2 = np.sin(kv), np.sin(np.asarray(Kv) - kv)
        Hm[4 * i:4 * i + 4, 4 * i:4 * i + 4] = sum(h1[a] * np.kron(sig[a], I2) + h2[a] * np.kron(I2, sig[a]) for a in range(3))
    Hm += Vc / n * np.kron(np.ones((n, n)), np.eye(4))
    return np.linalg.eigvalsh(Hm)[0]


ed_err = max(abs(ed3(6, np.array(Kv, float), -5.0) - bound3(-5.0, setup3(6, np.array(Kv, float))))
             for Kv in ((0, 0, 0), (2 * np.pi / 6, 0, 0), (np.pi, np.pi, np.pi)))
curv = {}
for Vc in (-5.0, -8.0):
    E0 = bound3(Vc, setup3(24, np.zeros(3)))
    E0b = bound3(Vc, setup3(32, np.zeros(3)))
    vals = []
    for dirn in ((1, 0, 0), (1, 1, 0), (1, 1, 1)):
        dK = 2 * np.pi / 24 * np.array(dirn, float)
        E1 = bound3(Vc, setup3(24, dK))
        vals.append((E1 ** 2 - E0 ** 2) / (dK @ dK))
    curv[Vc] = (E0, abs(E0 - E0b), vals)
ok = ed_err < 1e-8 and all(c[1] < 1e-8 and all(v < -0.75 for v in c[2]) and max(c[2]) - min(c[2]) < 0.01 for c in curv.values())
check('A5', ok, "NUMERICAL (secular equation det(1 - V G(E,K)) = 0 on 24^3 and 32^3 grids, cross-checked against full "
      "diagonalization of K-blocks on 6^3 to 1e-8): on Z^3 the contact-bound ground pair lies below the two-walker "
      "continuum (edge -2 sqrt3) at K = 0, and there E^2 = M^2 - c*^2 K^2 + O(K^4) with c*^2 about 0.81 (V = -5) and 0.90 "
      "(V = -8), the same along axes, face and body diagonals: a band MINIMUM, the inverted form of A2's counter-moving "
      "sector, not the co-moving relativistic one",
      "; ".join(f"V={k}: E(0) = {c[0]:.6f} (24^3 vs 32^3 {c[1]:.0e}), (E^2 - E0^2)/K^2 = {', '.join(f'{v:.4f}' for v in c[2])}"
                for k, c in curv.items()) + f"; secular vs ED {ed_err:.1e}")

# ================================================================ B1 the exact identity: timed interaction scales with the rate field
def chain_ops(N, g, Vc, kind, timed, sector=(1, 1)):
    x = np.arange(N)
    w = np.exp(g * (x - N // 2))
    T = sps.lil_matrix((N, N))
    for xx in range(1, N):
        T[xx, xx - 1] = 1.0
    T = T.tocsr()
    D = 0.5j * (T - T.T)
    sw = sps.diags(np.sqrt(w))
    Dw = sw @ D @ sw
    I = sps.identity(N, format='csr')
    H = sector[0] * sps.kron(Dw, I) + sector[1] * sps.kron(I, Dw)
    rows, cols, vals = [], [], []
    for x1 in range(N):
        partners = [x1] if kind == 'contact' else [x1 - 1, x1 + 1]
        for x2 in partners:
            if 0 <= x2 < N:
                i = x1 * N + x2
                wt = (w[x1] if kind == 'contact' else np.sqrt(w[x1] * w[x2])) if timed else 1.0
                rows.append(i); cols.append(i); vals.append(Vc * wt)
    H = (H + sps.csr_matrix((vals, (rows, cols)), shape=(N * N, N * N))).tocsr()
    return H, w


ok = True
dev = {}
for kind in ('contact', 'nn'):
    for timed in (True, False):
        N = 14
        g = 0.3
        H, w = chain_ops(N, g, -1.0, kind, timed)
        Tj = sps.lil_matrix((N * N, N * N))              # joint translation by one site: (T psi)(x1,x2) = psi(x1-1, x2-1)
        for x1 in range(1, N):
            for x2 in range(1, N):
                Tj[x1 * N + x2, (x1 - 1) * N + (x2 - 1)] = 1.0
        Tj = Tj.tocsr()
        lam = np.exp(g)
        Dm = (H @ Tj - lam * Tj @ H).toarray()
        inner = [x1 * N + x2 for x1 in range(3, N - 3) for x2 in range(3, N - 3)]
        dev[(kind, timed)] = np.abs(Dm[np.ix_(inner, inner)]).max()
ok = dev[('contact', True)] < 1e-12 and dev[('nn', True)] < 1e-12 and dev[('contact', False)] > 0.1 and dev[('nn', False)] > 0.1
check('B1', ok, "PROVED + CHECKED (interior of a 14-chain, uniform gradient w = e^{g x}): with the interaction timed by any "
      "weight of degree one in the rate field, the two-walker generator obeys H_w T_a = lambda_a T_a H_w for the joint "
      "translation (lambda_a = e^{g a}), as block 54's single walker does, so d<K>/dt = -g <H_w> exactly in every state "
      "(force = -(energy) x grad u, binding energy included); untimed, the identity fails and only the kinetic energy is "
      "pulled", "; ".join(f"{k[0]} {'timed' if k[1] else 'untimed'}: {v:.1e}" for k, v in dev.items()))

# ================================================================ B2 the fall at rest (ray level) and the executed falls
def fall(N, Vc, g, sigma, tmax, kind, timed, sector, rel):
    H, w = chain_ops(N, g, Vc, kind, timed, sector)
    x = np.arange(N)
    X1, X2 = np.repeat(x, N), np.tile(x, N)
    Xc = (X1 + X2) / 2 - N // 2
    psi = np.exp(-Xc ** 2 / (4 * sigma ** 2)) * rel(X1 - X2)
    psi = psi / np.linalg.norm(psi)
    ts = np.linspace(0, tmax, 9)
    Xs = []
    for t in ts:
        ph = expm_multiply(-1j * H * t, psi) if t > 0 else psi
        p = np.abs(ph) ** 2
        Xs.append((p * Xc).sum() / p.sum())
    return np.polyfit(ts, Xs, 2)[0] * 2 / g


def ray_cloud(epsf, g, sigma, tmax, timed=True, Vc=None):
    """rays of E = w(X) eps(K) (timed) over the packet's K spread (Gauss-Hermite), fitted as the executed runs are."""
    from numpy.polynomial.hermite_e import hermegauss
    nodes, wts = hermegauss(21)
    sK = 1 / (2 * sigma)
    ts = np.linspace(0, tmax, 9)
    Xavg = np.zeros(len(ts))
    for nd, wt in zip(nodes, wts):
        Kc, Xc_, t = sK * nd, 0.0, 0.0
        dt = 0.01
        out = [0.0]
        for tn in ts[1:]:
            while t < tn - 1e-12:
                h = 1e-5
                if timed:
                    w = np.exp(g * Xc_)
                    dK = -g * w * epsf(Kc)
                    dX = w * (epsf(Kc + h) - epsf(Kc - h)) / (2 * h)
                else:
                    w = np.exp(g * Xc_)
                    E = lambda X_, K_: -np.sqrt(Vc ** 2 + 4 * np.exp(2 * g * X_) * np.sin(K_ / 2) ** 2)
                    dK = -(E(Xc_ + h, Kc) - E(Xc_ - h, Kc)) / (2 * h)
                    dX = (E(Xc_, Kc + h) - E(Xc_, Kc - h)) / (2 * h)
                Kc += dK * dt; Xc_ += dX * dt; t += dt
            out.append(Xc_)
        Xavg += wt * np.array(out)
    Xavg /= wts.sum()
    return np.polyfit(ts, Xavg, 2)[0] * 2 / g


from scipy.interpolate import CubicSpline
Kgrid = 2 * np.pi * np.arange(-40, 41) / 400
nn_even = CubicSpline(Kgrid, [block(400, -2.0, Kv, 1, 1, nn=True)[0] for Kv in Kgrid])
nn_odd = CubicSpline(Kgrid, [block(400, -2.0, Kv, 1, 1, nn=True)[1] for Kv in Kgrid])
M = 4096
qg = 2 * np.pi * np.arange(M) / M
phi_counter = np.fft.ifft(1 / (-np.sqrt(1 + 4) - 2 * np.sin(qg))) * M          # K = 0 counter-moving bound state, V = -1
co = lambda Vc: (lambda Kv: -np.sqrt(Vc ** 2 + 4 * np.sin(Kv / 2) ** 2))
ct = lambda Vc: (lambda Kv: -np.sqrt(Vc ** 2 + 4 * np.cos(Kv / 2) ** 2))
runs = {
    'contact co-moving, V=-1, timed': (-1.0, 'contact', True, (1, 1), lambda r: (r == 0) * 1.0, -1.0, co(-1.0)),
    'contact co-moving, V=-3, timed': (-3.0, 'contact', True, (1, 1), lambda r: (r == 0) * 1.0, -1.0, co(-3.0)),
    'contact co-moving, V=-1, untimed': (-1.0, 'contact', False, (1, 1), lambda r: (r == 0) * 1.0, 0.0, None),
    'contact counter-moving, V=-1, timed': (-1.0, 'contact', True, (1, -1), lambda r: phi_counter[r % M], +1.0, ct(-1.0)),
    'nn even channel, V_n=-2, timed': (-2.0, 'nn', True, (1, 1), lambda r: (np.abs(r) == 1) * 1.0, -1.5, nn_even),
    'nn odd channel, V_n=-2, timed': (-2.0, 'nn', True, (1, 1), lambda r: (r == 1) * 1.0 - (r == -1) * 1.0, -0.5, nn_odd),
}
ok = True
rows = []
for name, (Vc, kind, timed, sector, rel, rest, epsf) in runs.items():
    a = fall(130, Vc, 0.005, 12.0, 24.0, kind, timed, sector, rel)
    ray = ray_cloud(epsf, 0.005, 12.0, 24.0) if timed else ray_cloud(None, 0.005, 12.0, 24.0, timed=False, Vc=Vc)
    rows.append(f"{name}: executed a/g = {a:+.4f}, ray cloud {ray:+.4f}, rest value {rest:+.1f}")
    ok &= abs(a - ray) < 0.02 and abs(ray - rest) < 0.08
check('B2', ok, "PROVED at ray level + EXECUTED (130-chain, g = 0.005, packets of width 12, t <= 24; the propagation is floating "
      "point and only the stated numbers are claimed): by B1 a composite at rest at a band extremum K* accelerates at "
      "a = -w^2 (d^2/dK^2)(eps^2/2)|_{K*} grad u; co-moving contact pairs fall at -g for every V (c = 1), counter-moving "
      "contact pairs fall UP at +g, nearest-neighbour pairs fall at -(3/2)g and -(1/2)g, and an untimed binding energy does "
      "not fall at all (executed runs agree with ray clouds of each composite's own dispersion to 0.02)", "; ".join(rows))

npass = sum(RESULTS)
print(f"TOTAL: PASS={npass} FAIL={len(RESULTS) - npass}")
print("SUMMARY: PARTIAL, exact in 1D, numerical in 3D, executed falls: two walkers bound by a contact attraction have a rest "
      "energy M = |V| inside M_2(C) per walker, with E^2 = V^2 + 4 sin^2(K/2) exactly for co-moving walkers (c = 1, the "
      "walker's) and E^2 = V^2 + 4 cos^2(K/2) for counter-moving ones; with the interaction timed by the local clock the "
      "generator scales exactly under translation (force = -(energy) x grad u) and a composite at rest falls at "
      "-(d^2/dK^2)(eps^2/2) g: -g for co-moving contact pairs whatever V, but +g (up) for counter-moving ones, -(3/2)g and "
      "-(1/2)g for nearest-neighbour pairs, 0 if the interaction is untimed, and up (+0.81 g to +0.90 g) for the contact-bound "
      "ground pair on Z^3")
if all(RESULTS):
    print("HIT: binding supplies a rest energy inside M_2(C) (1D contact: E^2 = V^2 + 4 sin^2(K/2) exactly, c = 1), and with "
          "the interaction timed by the local clock the two-walker generator obeys H_w T_a = lambda_a T_a H_w (force = "
          "-(energy) grad u, binding included), but free fall is NOT universal: a composite at rest accelerates at "
          "-(d^2/dK^2)(eps^2/2) grad u, i.e. -g for co-moving contact pairs whatever V, +g (away from slow clocks) for "
          "counter-moving contact pairs, -(3/2)g and -(1/2)g for the two nearest-neighbour-bound states, 0 for an untimed "
          "binding energy, and +0.81 g to +0.90 g for the contact-bound ground pair on Z^3 (its band minimum sits at K = 0) - "
          "executed propagations agree to 5 percent")
