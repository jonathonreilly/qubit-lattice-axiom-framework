#!/usr/bin/env python3
"""Check for Lemma L1a-L1d (PROOF.md): Balaban-type log-averaging of SU(N) links over L^4 blocks (L = 3, d = 4).
  T_y = P_X(c_X -> y) U(y -> y + L e_mu) P_Y(c_Y -> y + L e_mu)^dag   (axial tree paths, straight middle leg)
  U'(X, X + e_mu) = T_{c_X} exp( L^-4 sum_y log(T_{c_X}^-1 T_y) )
Checks: (a) gauge covariance with arbitrary fine gauge transforms; (b) U' in SU(N); (c) pure gauge -> pure gauge;
(d) linearisation = abelian average of line integrals, error O(t^2); (e) field-strength bound carried to the coarse lattice
(ratio of physical F, smooth fields). Finite checks of statements proven in PROOF.md (a-d) or measured (e).
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
import time, itertools as it, numpy as np
from scipy.linalg import logm, expm
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0; rng = np.random.default_rng(98); d = 4; Lb = 3
def check(n, ok, s=""):
    global NP, NF
    NP += bool(ok); NF += not ok; print(("PASS " if ok else "FAIL ") + n + (" | " + s if s else ""))
dag = lambda M: np.conj(np.swapaxes(M, -1, -2))
def gens(N):
    G = []
    for i in range(N):
        for j in range(i + 1, N):
            A = np.zeros((N, N), complex); A[i, j] = A[j, i] = .5; G.append(A)
            B = np.zeros((N, N), complex); B[i, j] = -.5j; B[j, i] = .5j; G.append(B)
    for k in range(1, N):
        D = np.zeros((N, N), complex); D[:k, :k] = np.eye(k); D[k, k] = -k; G.append(D / np.sqrt(2 * k * (k + 1)))
    return np.array(G)
def hexp(Hm):  # exp(i H) for batched hermitian H
    w, V = np.linalg.eigh(Hm); return V @ (np.exp(1j * w)[..., None] * dag(V))
class Lat:
    def __init__(s, N, Tc=3):
        s.N = N; s.S = Lb * Tc; s.V = s.S ** d; s.eps = 1 / Lb; s.G = gens(N)
        s.X = np.array(list(it.product(range(s.S), repeat=d))); s.fl = lambda Y: np.ravel_multi_index(tuple((np.asarray(Y) % s.S).T), (s.S,) * d)
        s.nb = np.array([s.fl(s.X + np.eye(d, dtype=int)[m]) for m in range(d)])
    def links(s, amp, rough=0.0, seed=1):
        r = np.random.default_rng(seed); x = s.X * s.eps; ng = len(s.G); U = []
        K = r.integers(-1, 2, size=(3, d)); K[np.all(K == 0, 1)] = 1; C = r.normal(size=(3, d, ng)); ph = r.uniform(0, 6.3, (3, d, ng))
        for m in range(d):
            xm = x + .5 * s.eps * np.eye(d)[m]; a = sum(C[j, m][None] * np.cos(2 * np.pi * (xm @ K[j])[:, None] / (s.S * s.eps) + ph[j, m][None]) for j in range(3))
            a = amp * s.eps * a + rough * r.normal(size=(s.V, ng)); U.append(hexp(np.einsum("va,aij->vij", a, s.G)))
        return np.array(U), None
    def step(s, U, x, m, sign):  # transporter for one step from x in direction sign*e_m
        return U[m][s.fl(x)] if sign > 0 else dag(U[m][s.fl(x - np.eye(d, dtype=int)[m])])
    def path(s, U, a, b):  # complete axial path a -> b (dirs 0..3), product of transporters
        P = np.eye(s.N, dtype=complex); cur = np.array(a)
        for m in range(d):
            while cur[m] != b[m]:
                sg = 1 if b[m] > cur[m] else -1; P = P @ s.step(U, cur, m, sg); cur[m] += sg
        return P
    def Ts(s, U, X, m):
        cX = np.array(X) * Lb + 1; cY = cX + Lb * np.eye(d, dtype=int)[m]; out = []
        for off in it.product(range(Lb), repeat=d):
            y = np.array(X) * Lb + np.array(off); P1 = s.path(U, cX, y); Mid = np.eye(s.N, dtype=complex); cur = y.copy()
            for _ in range(Lb): Mid = Mid @ s.step(U, cur, m, 1); cur[m] += 1
            out.append(P1 @ Mid @ dag(s.path(U, cY, cur)))
        return out
    def avg(s, U, X, m, lin=False):
        T = s.Ts(U, X, m); T0_ = T[[tuple(o) for o in it.product(range(Lb), repeat=d)].index((1,) * d)]
        Lg = sum(logm(dag(T0_) @ t) for t in T) / Lb ** d
        return T0_ @ expm(Lg)
def plaq1(M): return np.linalg.norm(np.eye(M.shape[0]) - M, 2)
for N in (2, 3):
    l = Lat(N); U, _ = l.links(0.6); X = (0, 1, 2, 0); m = 1
    Up = l.avg(U, X, m)
    g = hexp(np.einsum("va,aij->vij", rng.normal(size=(l.V, len(l.G))), l.G))
    Ug = np.array([g @ U[k] @ dag(g[l.nb[k]]) for k in range(d)]); Upg = l.avg(Ug, X, m)
    cX = l.fl(np.array(X) * Lb + 1); cY = l.fl(np.array(X) * Lb + 1 + Lb * np.eye(d, dtype=int)[m])
    cov = np.linalg.norm(Upg - g[cX] @ Up @ dag(g[cY]))
    check(f"a SU({N}) gauge covariance U'[gUg^-1] = g(c_X) U' g(c_Y)^dag (random g on all fine sites)", cov < 1e-10, f"err {cov:.1e}")
    check(f"b SU({N}) U' unitary with det 1", np.linalg.norm(Up @ dag(Up) - np.eye(N)) < 1e-10 and abs(np.linalg.det(Up) - 1) < 1e-10,
          f"|UU^+-1| {np.linalg.norm(Up @ dag(Up) - np.eye(N)):.1e}, |det-1| {abs(np.linalg.det(Up) - 1):.1e}")
    Upure = np.array([g @ dag(g[l.nb[k]]) for k in range(d)]); pp = np.linalg.norm(l.avg(Upure, X, m) - g[cX] @ dag(g[cY]))
    check(f"c SU({N}) pure gauge U_b = g_x g_y^-1 averages to g(c_X) g(c_Y)^-1", pp < 1e-10, f"err {pp:.1e}")
    # (f) reflection covariance through a block-boundary plane: x0 -> (S-1) - x0 (coarse X0 -> Tc-1-X0)
    S = l.S; refl = lambda Y: np.concatenate([[(S - 1 - Y[0]) % S], Y[1:]])
    Xs = l.X; thX = Xs.copy(); thX[:, 0] = (S - 1 - Xs[:, 0]) % S
    th0 = Xs.copy(); th0[:, 0] = (S - 2 - Xs[:, 0]) % S
    Ur = np.array([dag(U[0][l.fl(th0)])] + [U[k][l.fl(thX)] for k in range(1, d)])
    Tc = S // Lb; Xr = np.array(X)
    v1 = l.avg(Ur, tuple(Xr), 1); w1 = l.avg(U, tuple([(Tc - 1 - Xr[0]) % Tc] + list(Xr[1:])), 1)
    v0 = l.avg(Ur, tuple(Xr), 0); w0 = l.avg(U, tuple([(Tc - 2 - Xr[0]) % Tc] + list(Xr[1:])), 0)
    e1, e0 = np.linalg.norm(v1 - w1), np.linalg.norm(v0 - dag(w0))
    check(f"f SU({N}) reflection covariance: V[thetaU] = theta(V[U]) (unreflected dir exact; reflected dir = inverse, exact)", max(e1, e0) < 1e-10,
          f"err {e1:.1e}, {e0:.1e}")
    errs = []
    for t in (0.04, 0.02, 0.01):
        Ut, _ = l.links(t / l.eps, seed=5)  # links = exp(i t a_b)
        Ta = l.Ts(Ut, X, m); lin = sum(-1j * logm(tt) for tt in Ta) / Lb ** d  # abelianised average of path log ~ sum of A along path
        full = -1j * logm(l.avg(Ut, X, m)); errs.append(np.linalg.norm(full - lin) / np.linalg.norm(lin))
    rat = errs[0] / errs[1], errs[1] / errs[2]
    check(f"d SU({N}) linearisation: log U' = average of path logs + O(t^2): relative error -> 0 at least linearly (halving ratio >= 1.6; observed ~4 = second-order agreement)",
          all(r >= 1.6 for r in rat), "rel err " + ", ".join(f"{e:.2e}" for e in errs))
    Fs, Fc = [], []
    for amp in (0.3, 0.6):
        U, _ = l.links(amp, seed=11); fine = 0.0
        for mu in range(d):
            for nu in range(mu + 1, d):
                P = U[mu] @ U[nu][l.nb[mu]] @ dag(U[mu][l.nb[nu]]) @ dag(U[nu]); fine = max(fine, max(plaq1(p) for p in P))
        Fs.append(fine / l.eps ** 2)
        Xc = (0, 0, 0, 0); mu, nu = 0, 1; e = np.eye(d, dtype=int)
        c1 = l.avg(U, Xc, mu); c2 = l.avg(U, tuple(np.array(Xc) + e[mu]), nu); c3 = l.avg(U, tuple(np.array(Xc) + e[nu]), mu); c4 = l.avg(U, Xc, nu)
        Fc.append(plaq1(c1 @ c2 @ dag(c3) @ dag(c4)) / 1.0 ** 2)
    check(f"e SU({N}) one coarse plaquette, physical units: F_coarse <= 1.5 F_fine,max (smooth fields)", all(c <= 1.5 * f for c, f in zip(Fc, Fs)),
          "F_fine,max / F_coarse(one plaquette): " + ", ".join(f"{f:.3f}/{c:.3f}" for f, c in zip(Fs, Fc)))
print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
