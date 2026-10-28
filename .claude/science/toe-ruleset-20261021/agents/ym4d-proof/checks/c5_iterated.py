#!/usr/bin/env python3
"""Check for Lemma L1e and Corollary L3s' (PROOF.md, session 2): ITERATED Balaban-type log-averaging, SU(2).
Fine lattice of spacing eps = L^-k (unit blocks of side 1), periodic, T unit blocks per side, d = 2, 3, 4.
V^(k) = U; V^(j) = A(V^(j+1)) (one log-averaging step of S4 on the resolution-(j+1) lattice).
S_b = fine straight transporter between the fine roots of the two level-j blocks of b.
  delta_j := max_b ||V^(j)_b - S_b|| / s_j^2   (s_j = L^-j),  F := max fine ||1 - U_p|| / eps^2.
L1e claims (proved in PROOF.md):
  (R) recursion  delta_j <= rho delta_{j+1} + c C_A F,  rho = (1 + c (d+2)) / L,  C_A = (d-1)/2,  c = 4 arcsin(1/4),
      valid whenever every averaged Z_y obeys ||Z_y - 1|| <= 1/2 (domain, also checked);
  (C) coarse curvature  ||1 - V^(j)_p|| / s_j^2 <= F + 4 delta_j;
  (P) scalar transports, Option I (fine composite path) theta_I <= d(d-1)F/4;
      Option II (stage transports by V^(j)) theta_II <= theta_I + d (L-1)/2 sum_j delta_j L^-2j.
(R) is proven for every L; the k-uniform bound needs rho < 1 (L >= 9 in d = 4; L >= 7 in d = 2).
Cases with rho >= 1 are finite diagnostics only (the recursion inequality is still a theorem there).
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
import time, itertools as it, numpy as np
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0
cLOG = 4 * np.arcsin(0.25)
def check(n, ok, s=""):
    global NP, NF
    NP += bool(ok); NF += not ok; print(("PASS " if ok else "FAIL ") + n + (" | " + s if s else ""))
dag = lambda M: np.conj(np.swapaxes(M, -1, -2))
SIG = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], complex) / 2
def hexp(a):  # exp(i a.sigma/2), batched a (...,3)
    ph = np.linalg.norm(a, axis=-1) / 2; n = a / np.maximum(2 * ph, 1e-300)[..., None]
    return np.cos(ph)[..., None, None] * np.eye(2) + 1j * np.sin(ph)[..., None, None] * np.einsum("...a,aij->...ij", 2 * n, SIG)
def ulog(W):  # principal log of SU(2), batched (anti-Hermitian)
    a0 = np.clip(np.real(np.trace(W, axis1=-2, axis2=-1)) / 2, -1, 1); th = np.arccos(a0)
    f = np.where(th > 1e-12, th / np.maximum(np.sin(th), 1e-300), 1.0)
    return f[..., None, None] * (W - dag(W)) / 2
def aexp(X):  # exp of traceless anti-Hermitian 2x2, batched
    ph = np.sqrt(np.maximum(-np.real(np.trace(X @ X, axis1=-2, axis2=-1)) / 2, 0))
    f = np.where(ph > 1e-12, np.sin(ph) / np.maximum(ph, 1e-300), 1.0)
    return np.cos(ph)[..., None, None] * np.eye(2) + f[..., None, None] * X
nrm = lambda M: np.linalg.norm(M, 2, axis=(-2, -1))
def dist1(W):  # ||1 - W|| for SU(2) = 2 sin(theta/2)
    a0 = np.clip(np.real(np.trace(W, axis1=-2, axis2=-1)) / 2, -1, 1); return 2 * np.sin(np.arccos(a0) / 2)
class Grid:
    def __init__(s, d, S): s.d, s.S = d, S; s.X = np.array(list(it.product(range(S), repeat=d)))
    def fl(s, Y): return np.ravel_multi_index(tuple((np.asarray(Y) % s.S).T), (s.S,) * s.d)
def walk(g, U, start, steps):  # product of transporters along a step list from each start (batched)
    P = np.broadcast_to(np.eye(2, dtype=complex), (len(start), 2, 2)).copy(); cur = start.copy(); E = np.eye(g.d, dtype=int)
    for m, sg in steps:
        if sg > 0: P = P @ U[m][g.fl(cur)]
        else: P = P @ dag(U[m][g.fl(cur - E[m])])
        cur = cur + sg * E[m]
    return P
def axial_steps(o, r0, unit=1):
    st = []
    for m in range(len(o)):
        k = o[m] - r0; st += [(m, 1 if k > 0 else -1)] * (abs(k) * unit)
    return st
def avg_step(g, U, b):
    """One log-averaging step with block side b (odd); returns coarse grid, coarse links, max ||Z-1||."""
    d = g.d; r0 = (b - 1) // 2; gc = Grid(d, g.S // b); E = np.eye(d, dtype=int); c = gc.X * b + r0
    Vc = []; zmax = 0.0
    for mu in range(d):
        nbr = gc.fl(gc.X + E[mu]); Tc = walk(g, U, c, [(mu, 1)] * b); acc = np.zeros_like(Tc)
        for o in it.product(range(b), repeat=d):
            o = np.array(o); P = walk(g, U, c, axial_steps(o, r0))
            Mid = walk(g, U, c + (o - r0), [(mu, 1)] * b)
            T = P @ Mid @ dag(P[nbr]); Z = dag(Tc) @ T; zmax = max(zmax, dist1(Z).max()); acc += ulog(Z)
        Vc.append(Tc @ aexp(acc / b ** d))
    return gc, np.array(Vc), zmax
def plaq_max(g, U):
    E = np.eye(g.d, dtype=int); out = 0.0
    for mu in range(g.d):
        for nu in range(mu + 1, g.d):
            P = U[mu] @ U[nu][g.fl(g.X + E[mu])] @ dag(U[mu][g.fl(g.X + E[nu])]) @ dag(U[nu]); out = max(out, dist1(P).max())
    return out
def field(g, eps, T, amp, rough, seed):
    r = np.random.default_rng(seed); x = g.X * eps; d = g.d; U = []
    K = r.integers(-1, 2, size=(3, d)); K[np.all(K == 0, 1)] = 1; C = r.normal(size=(3, d, 3)); ph = r.uniform(0, 6.3, (3, d, 3))
    for m in range(d):
        xm = x + .5 * eps * np.eye(d)[m]
        a = sum(C[j, m][None] * np.cos(2 * np.pi * (xm @ K[j])[:, None] / T + ph[j, m][None]) for j in range(3))
        U.append(hexp(amp * eps * a + rough * eps ** 2 * r.normal(size=(len(g.X), 3))))
    return np.array(U)
def run(d, L, k, T, amp, rough, seed, scalar=True):
    S = T * L ** k; eps = L ** -k; g0 = Grid(d, S); U = field(g0, eps, T, amp, rough, seed)
    F = plaq_max(g0, U) / eps ** 2
    grids, V, zm = [g0], [U], []
    for j in range(k):  # build V^(k-1), ..., V^(0)
        gc, Vc, z = avg_step(grids[-1], V[-1], L); grids.append(gc); V.append(Vc); zm.append(z)
    grids, V = grids[::-1], V[::-1]  # index by resolution j = 0..k
    E = np.eye(d, dtype=int); delta, Fj = [], []
    for j in range(k + 1):
        bt = L ** (k - j); R = (bt - 1) // 2; gj = grids[j]; dj = 0.0
        for mu in range(d):
            Sb = walk(g0, U, gj.X * bt + R, [(mu, 1)] * bt); dj = max(dj, nrm(V[j][mu] - Sb).max())
        delta.append(dj / (L ** -j) ** 2); Fj.append(plaq_max(gj, V[j]) / (L ** -j) ** 2)
    out = dict(F=F, delta=delta, Fj=Fj, zmax=max(zm))
    if scalar:  # theta_I, theta_II over all fine y in all unit blocks
        n = L ** k; corner = grids[0].X * n; R0 = (n - 1) // 2; thI = thII = 0.0; h = (L - 1) // 2
        for o in it.product(range(n), repeat=d):
            o = np.array(o); Pd = walk(g0, U, corner + R0, axial_steps(o, R0))
            dig = [(o // L ** (k - i)) % L for i in range(1, k + 1)]
            WI = np.broadcast_to(np.eye(2, dtype=complex), Pd.shape).copy(); WII = WI.copy(); pos = corner + R0
            for i in range(1, k + 1):
                stp = dig[i - 1] - h; unit = L ** (k - i)
                WI = WI @ walk(g0, U, pos, axial_steps(stp, 0, unit))
                Ri = (L ** (k - i) - 1) // 2; posi = (pos - Ri) // unit
                WII = WII @ walk(grids[i], V[i], posi, axial_steps(stp, 0, 1)); pos = pos + stp * unit
            thI = max(thI, nrm(WI - Pd).max()); thII = max(thII, nrm(WII - Pd).max())
        out.update(thI=thI, thII=thII)
    return out
CA = lambda d: (d - 1) / 2
cases = [(2, 9, 2, 2, 0.06, 0.03, 1), (2, 7, 2, 2, 0.12, 0.0, 2), (3, 5, 2, 2, 0.05, 0.03, 3), (3, 3, 3, 2, 0.05, 0.02, 4),
         (4, 3, 2, 2, 0.05, 0.0, 5), (4, 3, 2, 2, 0.04, 0.03, 6), (4, 3, 2, 2, 0.6, 0.3, 7)]  # last: large field, diagnostic
for (d, L, k, T, amp, rough, seed) in cases:
    t0 = time.time(); o = run(d, L, k, T, amp, rough, seed, scalar=(d < 4 or seed == 5) and seed != 7)
    F, de = o["F"], o["delta"]; rho = (1 + cLOG * (d + 2)) / L; tag = f"d={d} L={L} k={k}"
    dom = o["zmax"] <= 0.5
    rec = all(de[j] <= rho * de[j + 1] + cLOG * CA(d) * F + 1e-12 for j in range(k))
    if not dom:
        print(f"DIAG {tag} large field, outside the domain ||Z-1||<=1/2 of L1e (no claim): recursion {'holds' if rec else 'fails'} | F={F:.3f}, max||Z-1||={o['zmax']:.3f}, delta_j/F=" + ",".join(f"{x / F:.3f}" for x in de)); continue
    check(f"{tag} (R) domain max||Z-1||<=1/2 and recursion delta_j <= rho delta_(j+1) + c C_A F (rho={rho:.2f}{'' if rho < 1 else ', >=1: k-uniformity not covered'})",
          dom and rec, f"F={F:.3f}, max||Z-1||={o['zmax']:.3f}, delta_j/F (j=0..k)=" + ",".join(f"{x / F:.3f}" for x in de))
    curv = all(o["Fj"][j] <= F + 4 * de[j] + 1e-12 for j in range(k + 1))
    check(f"{tag} (C) coarse curvature F_j <= F + 4 delta_j", curv, "F_j/F=" + ",".join(f"{x / F:.3f}" for x in o["Fj"]))
    if "thI" in o:
        bI = d * (d - 1) * F / 4; bII = bI + d * (L - 1) / 2 * sum(de[j] * L ** (-2 * j) for j in range(1, k + 1))
        check(f"{tag} (P) scalar iterated transports: theta_I <= d(d-1)F/4, theta_II <= theta_I-bound + stage sum",
              o["thI"] <= bI and o["thII"] <= bII, f"theta_I/F={o['thI'] / F:.3f} (bound {d * (d - 1) / 4:.2f}), theta_II/F={o['thII'] / F:.3f} (bound {bII / F:.2f}), {time.time() - t0:.0f}s")
print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
