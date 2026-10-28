#!/usr/bin/env python3
"""Check c18 (session 6): finite diagnostic for Lemma A1-NA(1) (one-step non-abelian action bound), SU(2), d = 4, L = 3,
fine torus 6^4 -> coarse torus 2^4, S4' averaging (= Balaban CMP 109 (0.4) with diagonal order pairing; c17(B)).
  S_f = sum_p (1 - Re tr U_p / 2),  S_c = sum_P (1 - Re tr V'_P / 2),  ratio R(t) = S_c / S_f for U = exp(t H).
Lemma A1-NA(1) (PROOF.md) claims R <= L^{4-d} + C_L phi = 1 + C_L phi with phi = max_p ||log U_p||, for phi <= phi_0(L).
Pre-registered criteria:
  (i)  R(t_min) <= 1 + 1e-6 for every field (the abelian bound A1 at linear order, d = 4);
  (ii) every field: |R(t) - R(t_min)| / phi(t) stays bounded, and the log-log slope of |R(t) - R(t_min)| between the two
       smallest nonminimal t is >= 0.9 (the non-abelian correction vanishes at least linearly in phi);
  (iii) reported: max_t (R(t) - 1)/phi(t) (an empirical lower bound on C_L at these sizes).
Finite instances only: no uniformity in L, volume or field is tested.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
import time, itertools as it, numpy as np
AUDIT_TIMEOUT_SEC = 600
T0 = time.time(); NP = NF = 0
def check(n, ok, s=""):
    global NP, NF
    NP += bool(ok); NF += not ok; print(("PASS " if ok else "FAIL ") + n + (" | " + s if s else ""))
d = 4; Lb = 3; Tc = 2; S = Lb * Tc; E = np.eye(d, dtype=int); ORD = list(it.permutations(range(d)))
dag = lambda M: np.conj(np.swapaxes(M, -1, -2))
GEN = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], complex) / 2
def su2_exp(a):  # a[..., 3] real -> exp(i a.sigma/2)
    H = np.einsum("...a,aij->...ij", a, GEN); w, V = np.linalg.eigh(H); return V @ (np.exp(1j * w)[..., None] * dag(V))
def logu_batch(Z):
    w, V = np.linalg.eig(Z); return V @ (np.log(w)[..., None] * np.linalg.inv(V))
idx = lambda x: tuple(np.asarray(x) % S)
# precompute path link lists (geometry only)
def path_links(a, b, order):
    cur = np.array(a); out = []
    for m in order:
        while cur[m] != b[m]:
            sg = 1 if b[m] > cur[m] else -1
            out.append((idx(cur), m, 1) if sg > 0 else (idx(cur - E[m]), m, -1)); cur[m] += sg
    return out
def straight_links(y, m):
    return [(idx(np.array(y) + j * E[m]), m, 1) for j in range(Lb)]
GEOM = {}
for X in it.product(range(Tc), repeat=d):
    for m in range(d):
        cX = np.array(X) * Lb + (Lb - 1) // 2; cY = cX + Lb * E[m]; Sc = straight_links(cX, m); Zs = []
        for o in ORD:
            for off in it.product(range(Lb), repeat=d):
                y = np.array(X) * Lb + np.array(off)
                fwd = path_links(cX, y, o) + straight_links(y, m)
                back = path_links(cY, y + Lb * E[m], o)
                Zs.append((fwd, back))
        GEOM[(X, m)] = (Sc, Zs)
# vectorised products: flat matrix bank [U links, U^dag links, identity]; index of (x, m, s)
NL = d * S ** d
def lid(x, m): return int(np.ravel_multi_index((m,) + tuple(x), (d,) + (S,) * d))
def enc(links, pad):
    out = [lid(x, m) + (0 if s > 0 else NL) for (x, m, s) in links]; return out + [2 * NL] * (pad - len(out))
KEYS = list(GEOM.keys())
PF = max(len(f) for k in KEYS for (f, b) in GEOM[k][1]); PB = max(len(b) for k in KEYS for (f, b) in GEOM[k][1])
IF = np.array([enc(f, PF) for k in KEYS for (f, b) in GEOM[k][1]]); IB = np.array([enc(b, PB) for k in KEYS for (f, b) in GEOM[k][1]])
IS = np.array([enc(GEOM[k][0], Lb) for k in KEYS]); NZ = len(GEOM[KEYS[0]][1])
def bprod(bank, I):
    P = np.broadcast_to(np.eye(2, dtype=complex), (I.shape[0], 2, 2)).copy()
    for j in range(I.shape[1]): P = P @ bank[I[:, j]]
    return P
def coarse(U):
    flat = U.reshape(NL, 2, 2); bank = np.concatenate([flat, dag(flat), np.eye(2, dtype=complex)[None]], axis=0)
    Sm = bprod(bank, IS); F = bprod(bank, IF); B = bprod(bank, IB)
    Z = np.repeat(dag(Sm), NZ, axis=0) @ F @ dag(B)
    Xb = logu_batch(Z).reshape(len(KEYS), NZ, 2, 2).mean(axis=1); Xb = (Xb - dag(Xb)) / 2
    Xb = Xb - (np.trace(Xb, axis1=-2, axis2=-1) / 2)[:, None, None] * np.eye(2)
    w, Vv = np.linalg.eigh(-1j * Xb); Ex = Vv @ (np.exp(1j * w)[..., None] * dag(Vv))
    V = np.empty((d, Tc, Tc, Tc, Tc, 2, 2), complex)
    for i, (X, m) in enumerate(KEYS): V[(m,) + X] = Sm[i] @ Ex[i]
    return V
def plaq_action(U, n):
    tot = 0.0; ph = 0.0
    for mu in range(d):
        for nu in range(mu + 1, d):
            Pm = U[mu] @ np.roll(U[nu], -1, axis=mu) @ dag(np.roll(U[mu], -1, axis=nu)) @ dag(U[nu])
            tr = np.real(np.trace(Pm, axis1=-2, axis2=-1)) / 2; tot += np.sum(1 - tr)
            ph = max(ph, float(np.max(2 * np.arccos(np.clip(tr, -1, 1)) / 2)))  # ||log U_p||_op = theta/2 for SU(2)
    return tot, ph
xs = np.indices((S,) * d).transpose(1, 2, 3, 4, 0)
def field(kind, seed):
    r = np.random.default_rng(seed); a = np.zeros((d,) + (S,) * d + (3,))
    if kind == "rough":
        return r.normal(size=a.shape)
    modes = [np.array(k) for k in it.product((-1, 0, 1), repeat=d) if any(k)]
    for mu in range(d):
        for k in modes:
            ph = 2 * np.pi * (xs @ k) / S + r.uniform(0, 2 * np.pi)
            c = r.normal(size=3) if kind == "smooth-nonabelian" else np.array([0, 0, r.normal()])
            a[mu] += np.cos(ph)[..., None] * c[None, None, None, None, :]
    return a / np.abs(a).max()
TS = (1e-3, 0.02, 0.04, 0.08, 0.16)
worst = 0.0
for kind, seed in (("smooth-abelian", 1), ("smooth-nonabelian", 2), ("smooth-nonabelian", 3), ("rough", 4)):
    H = field(kind, seed); rows = []
    for t in TS:
        U = su2_exp(t * H); Sf, ph = plaq_action(U, S); V = coarse(U); Sc, _ = plaq_action(V, Tc); rows.append((t, ph, Sc / Sf))
    R0 = rows[0][2]; dev = [abs(r[2] - R0) for r in rows[1:]]; phis = [r[1] for r in rows[1:]]
    slope = np.log(dev[1] / dev[0]) / np.log(phis[1] / phis[0]) if dev[0] > 1e-13 else float('inf')
    cmax = max((r[2] - 1) / r[1] for r in rows[1:]); worst = max(worst, cmax)
    print(f"  {kind:18s} seed {seed}: " + "  ".join(f"t={t:g} phi={p:.3e} R={R:.6f}" for t, p, R in rows))
    check(f"(i) {kind} seed {seed}: R(t_min) <= 1", R0 <= 1 + 1e-6, f"R(t_min)={R0:.6f}")
    check(f"(ii) {kind} seed {seed}: |R(t)-R(t_min)| vanishes at least linearly in phi", slope >= 0.9,
          f"slope={slope:.2f}; max |R-R0|/phi={max(dv / p for dv, p in zip(dev, phis)):.3f}")
print(f"(iii) max over fields and t of (R - 1)/phi = {worst:.3f} (negative = coarse action below fine action)")
print(f"runtime {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
