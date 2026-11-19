#!/usr/bin/env python3
"""Zoom families: CL-1's cube tick read one rung up (b = 2: a 2x2x2 block of cells as one coarse site).

A. Exact zoom: the coarse Floquet fibre is the union of eight fine fibres; the cell kinetic D has |D|^2 = (2/3) sum(1 - cos K),
   so no coarse zone corner carries a kinetic zero; the cell slab rebuilt on the 64-site block has no coarse-corner wall node.
B. The fine zone corners, which fold into one coarse site: near the copy-mass closure Mc -> 2 eps they carry a Wilson-type
   mass ladder m_n = mu + n (delta - mu)/3 (delta = 2 eps - Mc) at the light speed; masses, zero crossings, turn triplets,
   ordering, and the copy-mass interval that isolates the X triplet.
Supplied model; free fields; pre-set criteria in the note (written before the first run) and in each check line.
"""
import itertools, time, resource
import numpy as np
from scipy.linalg import expm, logm
from scipy.optimize import minimize_scalar

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
rng = np.random.default_rng(20261023)
NP = [0, 0]
def check(tag, ok, msg, det=""):
    NP[0 if ok else 1] += 1
    print(f"{'PASS' if ok else 'FAIL'}: {tag} {msg}" + (f"  [{det}]" if det else ""))

OM = np.exp(2j * np.pi / 3)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1.]).astype(complex)
SIG = [sx, sy, sz]; E3 = np.eye(3, dtype=int)

# ---------------------------------------------------------------- CL-1 tick on an L^3 block (L = 2 cell, L = 4 zoom b = 2)
def eta(x, i): return [1, (-1) ** int(x[0]), (-1) ** int(x[0] + x[1])][i]
def build(L):
    sites = list(itertools.product(range(L), repeat=3)); idx = {s: n for n, s in enumerate(sites)}
    def pairs(par):
        out = []
        for c in itertools.product(range(0, L, 2), repeat=3):
            for o in itertools.product((0, 1), repeat=3):
                A = np.array(c) + np.array(o) + par
                for i in range(3):
                    if not o[i]: out.append((A, A + E3[i], eta(A, i), i))
        return out
    return dict(L=L, sites=sites, idx=idx, PE=pairs(0), PO=pairs(1),
                EPS=np.diag([(-1.) ** sum(x) for x in sites]).astype(complex))
def hops(B, pp, k):
    L = B['L']; n = len(B['sites']); W = [np.zeros((n, n), complex) for _ in range(3)]
    for x, y, a, i in pp:
        ia = B['idx'][tuple(x % L)]; ib = B['idx'][tuple(y % L)]
        ph = a * np.exp(-1j * k @ (x // L - y // L)); W[i][ia, ib] += ph; W[i][ib, ia] += np.conj(ph)
    return W
def parts(B, k):
    We = hops(B, B['PE'], k); Wo = hops(B, B['PO'], k)
    Re = sum(We) / np.sqrt(3); Ro = sum(Wo) / np.sqrt(3); s = 1j * We[0] @ We[1] @ We[2] @ Re
    return We, Wo, Re, Ro, s
def floq(B, k, eps, mu, Mc):
    _, _, Re, Ro, s = parts(B, k); I = np.eye(len(Re)); C = expm(1j * (Mc / 4) * (I - s) @ Re)
    return expm(1j * (eps + mu / 2) * Ro) @ C @ expm(-1j * (eps - mu / 2) * Re) @ C
qe = lambda U: np.angle(np.linalg.eigvals(U))
B2, B4 = build(2), build(4)
CORN = {n: [np.pi * np.array(c, float) for c in itertools.product((0, 1), repeat=3) if sum(c) == n] for n in range(4)}

print("== A. exact zoom b = 2 (64-site coarse site); coarse zone corners")
d1 = 0
for eps, mu, Mc in [(0.3, 0.05, 0.2), (0.9, 0.0, 1.1)]:
    Q = rng.uniform(-np.pi, np.pi, 3)
    c = np.sort(qe(floq(B4, Q, eps, mu, Mc)))
    f = np.sort(np.concatenate([qe(floq(B2, (Q + 2 * np.pi * np.array(n)) / 2, eps, mu, Mc)) for n in itertools.product((0, 1), repeat=3)]))
    d1 = max(d1, np.abs(c - f).max())
check("A1 [T]", d1 < 1e-12, "coarse Floquet fibre at random Q = union of the eight fine fibres K = (Q + 2 pi n)/2 (pre-set: < 1e-12)", f"defect {d1:.0e}")
dD = 0
for _ in range(4):
    K = rng.uniform(-np.pi, np.pi, 3); _, _, Re, Ro, _ = parts(B2, K); Dm = Re - Ro
    dD = max(dD, np.abs(Dm @ Dm - (2 / 3) * np.sum(1 - np.cos(K)) * np.eye(8)).max())
fl = [min(np.abs(np.linalg.eigvalsh(parts(B4, Qc)[2] - parts(B4, Qc)[3])).min() for Qc in CORN[n]) for n in (1, 2, 3)]
okf = all(abs(fl[n - 1] - np.sqrt(2 * n / 3)) < 1e-12 for n in (1, 2, 3))
check("A2 [T]", dD < 1e-12 and okf, "|D(K)|^2 = (2/3) sum(1 - cos K_i) on all 8 cell modes, so the zoomed kinetic D_c(Q) vanishes only at Q = 0 "
      "(the only preimage of fine K = 0), for every b; coarse X, M, R kinetic floors sqrt(2/3), sqrt(4/3), sqrt(2): ratio 1 : 1.414 : 1.732, "
      "never zero (a Wilson corner needs a zero and 1 : 2 : 3) (pre-set: 1e-12)", f"defect {dD:.0e}; floors {', '.join(f'{v:.4f}' for v in fl)}")

ZT = 1e-3
def zero_modes(H, Ls, d, near=True):
    ev, V = np.linalg.eigh(H); Z = V[:, np.abs(ev) < ZT]
    if Z.shape[1] == 0: return Z
    w = np.zeros(len(H)); w[: (Ls // 2) * d] = 1
    e2, U2 = np.linalg.eigh(Z.conj().T @ np.diag(w) @ Z); Z = Z @ U2
    return Z[:, e2 > 0.5] if near else Z[:, e2 < 0.5]
def slab(onl, A, Ls):
    S = np.eye(Ls, k=-1); return np.kron(np.eye(Ls), onl) + np.kron(S, A) + np.kron(S.T, A.conj().T)
def HCs(B, k, m, Mc, Ls):
    _, _, Re, Ro, s = parts(B, k); I = np.eye(len(Re))
    lay = (Re - Ro) + (m - 1) * (Re + Ro) / 2 - (Mc / 2) * (I - s) @ Re
    return slab(lay, ((Re + Ro) / 2 + 1j * B['EPS']) / 2, Ls)
def chirality(Hf, k, P, h=1e-5):
    if P.shape[1] != 2: return None
    v = np.zeros((3, 3))
    for j in range(3):
        q = np.zeros(3); q[j] = h; hj = P.conj().T @ (Hf(k + q) - Hf(k - q)) @ P / (2 * h)
        for i in range(3): v[i, j] = np.real(np.trace(SIG[i] @ hj)) / 2
    return int(np.sign(np.linalg.det(v)))
Ls = 12; s4 = parts(B4, np.zeros(3))[4]; sL = np.kron(np.eye(Ls), s4); res = {}; corner_hits = 0
for m in [0.5, 1.5, 2.5, 3.0, 3.5, 5.0, 7.0]:
    for n in (1, 2, 3):
        for Qc in CORN[n]: corner_hits += zero_modes(HCs(B4, Qc, m, 1.0, Ls), Ls, 64).shape[1]
    P = zero_modes(HCs(B4, np.zeros(3), m, 1.0, Ls), Ls, 64)
    sp = np.linalg.eigvalsh(P.conj().T @ sL @ P) if P.shape[1] else np.array([])
    res[m] = (int(np.sum(sp > 0)) // 2, int(np.sum(sp < 0)) // 2)
pred = {m: (int(0 < m < 2), int(1 < m < 3)) for m in res}
check("A3 [F]", corner_hits == 0 and res == pred and max(sum(v) for v in res.values()) <= 2,
      "zoomed cell slab (64-site block, Ls = 12, Mc = 1): no wall zero mode at any coarse X, M, R for m in {0.5, ..., 7}; at Q = 0 the "
      "copy counts (s+, s-) equal the fine ones (s+ iff 0 < m < 2, s- iff Mc < m < Mc + 2): never more than 2, no triplet window at any m",
      f"coarse-corner zero modes {corner_hits}; " + ", ".join(f"m={m}: {v}" for m, v in res.items()))
chs = []
for m in (0.5, 2.5):
    Hf = lambda k, m=m: HCs(B4, k, m, 1.0, Ls); H0 = Hf(np.zeros(3))
    chs.append((chirality(Hf, np.zeros(3), zero_modes(H0, Ls, 64)), chirality(Hf, np.zeros(3), zero_modes(H0, Ls, 64, near=False))))
check("A3b [F]", None not in sum(chs, ()) and chs[0][0] == -chs[1][0] and all(a == -b for a, b in chs),
      "chirality of the lone coarse-wall copy: s+ (m = 0.5) and s- (m = 2.5) opposite, far wall opposite (pre-set)",
      f"near/far s+ {chs[0][0]:+d}/{chs[0][1]:+d}, s- {chs[1][0]:+d}/{chs[1][1]:+d}")
gmin = {}
for eps in (0.3, 0.9):
    for Mc in (0, 0.5 * eps, eps, 1.5 * eps):
        g = []
        for n in (1, 2, 3):
            pre = [(Qc + 2 * np.pi * np.array(nv)) / 2 for Qc in CORN[n][:1] for nv in itertools.product((0, 1), repeat=3)]
            g.append(min(np.abs(qe(floq(B2, K, eps, 0.05, Mc))).min() for K in pre))
        gmin[(eps, Mc)] = min(g) / eps
check("A4 [F]", min(gmin.values()) > 0.05, "Floquet coarse-corner gap (fine preimages of coarse X, M, R; mu = 0.05) / eps > 0.05 (pre-set): "
      "the coarse corners are step-scale heavy for every scanned eps, Mc", ", ".join(f"({e},{c:.2f}): {v:.2f}" for (e, c), v in gmin.items()))

print("== B. the fine zone corners (folded into one coarse site): Wilson-type ladder at the copy-mass closure")
def heff(K, eps, mu, Mc):
    H = 1j * logm(floq(B2, K, eps, mu, Mc)); return (H + H.conj().T) / 2
def corner_dirac(K, eps, mu, Mc, h=1e-4):
    ev, V = np.linalg.eigh(heff(K, eps, mu, Mc)); o = np.argsort(np.abs(ev))[:4]; P = V[:, o]
    vs = []
    for j in range(3):
        q = np.zeros(3); q[j] = h
        vs.append(np.abs(np.linalg.eigvalsh(P.conj().T @ (heff(K + q, eps, mu, Mc) - heff(K - q, eps, mu, Mc)) @ P / (2 * h))))
    return np.abs(ev[o]), np.concatenate(vs)
b1 = []; okb1 = True
for eps in (0.3, 0.9):
    for mu in (0.0, 0.05):
        dl = 0.01; Mc = 2 * eps - dl; vG = corner_dirac(CORN[0][0], eps, mu, Mc)[1].mean(); row = []
        for n in range(4):
            mm, vv = corner_dirac(CORN[n][0], eps, mu, Mc); pr = abs(mu + n * (dl - mu) / 3)
            okb1 &= (np.ptp(mm) < 1e-9 and abs(mm[0] - pr) < 2e-3 and np.abs(vv / vG - 1).max() < 1e-3); row.append(f"{mm[0]:.4f}")
        b1.append(f"eps {eps} mu {mu}: v {vG:.4f}, m_n " + "/".join(row))
check("B1 [F]", okb1, "delta = 2 eps - Mc = 0.01: at each fine corner with n pi-components the 4 lowest states are an isotropic Dirac at the "
      "light speed (rel 1e-3) with |m_n| = |mu + n (delta - mu)/3| (abs 2e-3): a Wilson-type ladder, 2r = (delta - mu)/3 (pre-set)", "; ".join(b1))
dR = 0
for mu in (0.0, 0.05):
    for Mc in np.linspace(0, 2.4, 13):
        w = np.abs(qe(floq(B2, CORN[3][0], 0.3, mu, Mc))); dR = max(dR, np.abs(w - abs(0.6 - Mc)).min())
check("B2 [T]/[F]", dR < 1e-10, "|w| = |2 eps - Mc| is exactly a quasi-energy at the R corner (eps 0.3; mu 0, 0.05; Mc 0..2.4; pre-set 1e-10)", f"defect {dR:.0e}")
eps, mu = 0.3, 0.05
def crossings(eps, mu, hi):
    lowc_ = lambda n, Mc: np.abs(qe(floq(B2, CORN[n][0], eps, mu, Mc))).min(); out = {}
    for n in (1, 2, 3):
        pr = 2 * eps + mu * (3 / n - 1)
        r = minimize_scalar(lambda x: lowc_(n, x), bounds=(pr - 0.3 * mu, pr + hi * mu), method='bounded', options={'xatol': 1e-10})
        out[n] = (r.x, r.fun, pr)
    return out, lowc_
cross, lowc = crossings(eps, mu, 1.0)
gG = min(lowc(0, x) for x in np.linspace(0, 2 * eps + 4 * mu, 41))
lin = {}
for e2, m2 in ((0.9, 0.05), (0.3, 0.01)):
    cr2, _ = crossings(e2, m2, 0.3); lin[(e2, m2)] = max(abs(v[0] - v[2]) / m2 for v in cr2.values()) if all(v[1] < 1e-5 for v in cr2.values()) else 9
dev0 = max(abs(v[0] - v[2]) / mu for v in cross.values())
check("B3 [F]", all(v[1] < 1e-5 for v in cross.values()) and gG > 0.99 * mu and lin[(0.3, 0.01)] < dev0 / 3 and lin[(0.9, 0.05)] < dev0 / 3,
      "(pre-set 'within 0.1 mu of Mc_n* = 2 eps + mu (3/n - 1)' FAILED for X at (eps, mu) = (0.3, 0.05) on the first run; recorded result) "
      "every non-Gamma corner mass does cross zero (|w| < 1e-5), R exactly at 2 eps, M near 2 eps + mu/2, X near 2 eps + 2 mu with an "
      "shift of order mu^2/eps (deviation/mu falls by > 3x at (0.3, 0.01) and (0.9, 0.05)); Gamma never crosses (stays mu)",
      "; ".join(f"n={n}: Mc* {v[0]:.4f} (lin {v[2]:.4f}, |w| {v[1]:.0e})" for n, v in cross.items()) + f"; Gamma min {gG:.4f}; dev (0.3, 0.05) {dev0:.3f} mu; "
      + ", ".join(f"{k}: max dev {v:.3f} mu" for k, v in lin.items()))
# B4: turn on the coarse site (4^3 block, Q = 0)
We0, Wo0, _, _, s0 = parts(B4, np.zeros(3)); n4 = 64; Pm = np.zeros((n4, n4))
for a in B4['sites']: Pm[B4['idx'][(a[2], a[0], a[1])], B4['idx'][a]] = 1
src = [Pm @ W @ Pm.T for W in We0 + Wo0]; tgt = [We0[1], We0[2], We0[0], Wo0[1], Wo0[2], Wo0[0]]
Dg = np.zeros(n4, complex); Dg[0] = 1; todo = [0]
while todo:
    x = todo.pop()
    for A_, B_ in zip(src, tgt):
        for y in np.nonzero(np.abs(A_[x]) > 1e-12)[0]:
            if Dg[y] == 0: Dg[y] = np.conj(B_[x, y] / A_[x, y] / Dg[x]); todo.append(y)
UT = np.diag(Dg) @ Pm
Uc = floq(B4, np.zeros(3), eps, mu, 2 * eps - 0.1); comm = np.abs(UT @ Uc - Uc @ UT).max()
Tr = []
for i in range(3):
    T = np.zeros((n4, n4))
    for a in B4['sites']:
        b = list(a); b[i] = (b[i] + 2) % 4; T[B4['idx'][tuple(b)], B4['idx'][a]] = 1
    Tr.append(T)
def corner_low(c):
    P = np.eye(n4)
    for i in range(3): P = P @ (np.eye(n4) + (-1) ** c[i] * Tr[i]) / 2
    ev, V = np.linalg.eigh(P); Bs = V[:, ev > 0.5]; Ur = Bs.conj().T @ Uc @ Bs
    w, X = np.linalg.eig(Ur); o = np.argsort(np.abs(np.angle(w)))[:4]
    Qx, _ = np.linalg.qr(Bs @ X[:, o]); return Qx
tri = {}
for n in range(4):
    S = np.hstack([corner_low(tuple(int(v) for v in np.round(K / np.pi))) for K in CORN[n]]); Pr = S @ S.conj().T
    leak = np.abs(UT @ S - Pr @ UT @ S).max(); ev = np.linalg.eigvals(S.conj().T @ UT @ S)
    inv = max(min(abs(z * OM - e) for e in ev) for z in ev)
    tri[n] = (leak, inv, len(ev))
ok = comm < 1e-12 and all(v[0] < 1e-10 for v in tri.values()) and tri[1][1] < 1e-8 and tri[2][1] < 1e-8
check("B4 [T]", ok, "zoom b = 2: the turn lift commutes with the coarse Floquet operator at Q = 0; inside the coarse site the low Dirac spaces of the "
      "three X corners (12-dim) and three M corners are each turn-closed with spectrum invariant under x w (turn TRIPLETS); Gamma, R closed (pre-set)",
      f"[U,T] {comm:.0e}; leak/x-w defect " + ", ".join(f"n={n}: {v[0]:.0e}/{v[1]:.0e} (dim {v[2]})" for n, v in tri.items()))
order = {}
for lab, dl in (("3mu", 3 * mu), ("mu/3", mu / 3)):
    ms = [corner_dirac(CORN[n][0], eps, mu, 2 * eps - dl)[0][0] for n in range(4)]; order[lab] = ms
okB5 = all(np.diff(order["3mu"]) > 0) and all(np.diff(order["mu/3"]) < 0)
check("B5 [F]", okB5, "ordering: delta = 3 mu gives Gamma < X < M < R, delta = mu/3 gives R < M < X < Gamma (pre-set): the ladder is affine in n, "
      "so the lightest corner multiplet is always a singlet and a triplet is never the lightest set",
      "; ".join(f"delta={k}: " + "/".join(f"{v:.4f}" for v in ms) for k, ms in order.items()))
g10 = np.linspace(-np.pi, np.pi, 10, endpoint=False); zg = {}
for Mc in (2 * eps + mu, 2 * eps + 3 * mu):
    zg[Mc] = min(np.abs(qe(floq(B2, np.array(kk), eps, mu, Mc))).min() for kk in itertools.product(g10, repeat=3))
iso = cross[1][0] > 2 * eps + mu and cross[1][0] < 2 * eps + 3 * mu and cross[2][0] < 2 * eps + mu and cross[3][0] < 2 * eps + mu
check("B6 [F]", all(v > 1e-3 for v in zg.values()) and iso, "copy-mass interval isolating the X triplet: bulk gapped at Mc = 2 eps + mu and 2 eps + 3 mu "
      "(10^3 grid, pre-set > 1e-3) and only the X mass crosses zero between them; both ends lie OUTSIDE CL-1's gapped regime Mc < 2 eps, "
      "and the interval width is ~mu (the species mass angle)", ", ".join(f"Mc={k:.2f}: zone gap {v:.4f}" for k, v in zg.items()))
print(f"   induced ladder (forced form, supplied Mc): Wilson parameter r = (2 eps - Mc - mu)/6 per tick, r/v = {(2*eps-0.01-mu)/6/(np.sin(eps)/np.sqrt(3)):.3f}"
      f" at eps 0.3, delta 0.01, mu 0.05; inside CL-1's regime (Mc < 2 eps) no corner mass changes sign")
print("Supplied: Mc, mu, eps values, the slab kernel (Shamir layer hop, B/2 + i eps), Ls, free fields, Hamiltonian slab.")
print(f"elapsed {time.time() - T0:.1f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20:.0f} MB")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
