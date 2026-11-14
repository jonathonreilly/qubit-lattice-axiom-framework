#!/usr/bin/env python3
"""Check for E8.1-E8.3 (PROOF.md, session 3): fine-scale local large-field bounds for the Wilson action.
(A) Chessboard estimate (E8.1(i)), EXACT instance: 2D U(1) Wilson on even tori 4x4 and 6x4 (cells = plaquettes). For U(1)
    on a torus the plaquette angles are uniform on {sum phi_p = 0 mod 2pi} under Haar links, so every probability below is
    an exact Fourier sum. Test mu(all cells in R bad) <= qbar^|R| for many R, with qbar = mu(all bad)^(1/|Lambda|).
(B) SU(2) Haar ball: h_2(delta) = Haar{||U-1|| <= delta} >= (8/(3 pi^3)) delta^3 (exact integral).
(C) Second-order lemma: f(U*) - f(U* e^X) <= N (d-1) ||X||^2 for f = Re tr(U W), U* the maximiser, ||W|| <= 2(d-1).
(D) Conditional lower bound (E8.3) for SU(2): P_W(||U - R|| >= t) >= h_2(delta) exp(-beta (d-1) x^2),
    x = 2 arcsin((t + 3 delta)/2), law of U ~ exp((beta/2) Re tr(U W)) dHaar, random W, R; quadrature on SU(2).
(E) Ribbon count (E8.2): ||Z^s_y - 1|| <= A_L max_{p in slab} ||1 - U_p||, A_L = (d-1) L (L-1)/2, all 24 orders, L = 3.
(F) INFO: the AF-window exponents of E8.3's corollary.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
import time, itertools as it, numpy as np
from scipy.special import iv
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0; rng = np.random.default_rng(10)
def check(n, ok, s=""):
    global NP, NF
    NP += bool(ok); NF += not ok; print(("PASS " if ok else "FAIL ") + n + (" | " + s if s else ""))
# (A) exact 2D U(1)
ph = np.linspace(-np.pi, np.pi, 40001)[:-1] + np.pi / 40000; dph = 2 * np.pi / 40000
def coef(beta, mask, nmax):  # c_n = (1/2pi) int_mask e^{beta cos} e^{i n phi}
    w = np.exp(beta * (np.cos(ph) - 1)) * mask
    return np.array([np.sum(w * np.cos(n * ph)) * dph / (2 * np.pi) for n in range(-nmax, nmax + 1)])
def prob(beta, bad_set, P, eta, nmax=80):
    big = np.abs(1 - np.exp(1j * ph)) >= eta; cb = coef(beta, big, nmax); ca = coef(beta, np.ones_like(ph), nmax)
    k = len(bad_set); num = np.sum(cb ** k * ca ** (P - k)); den = np.sum(ca ** P); return num / den
worst = 0; cnt = 0
for (S1, S2) in ((4, 4), (6, 4)):
    P = S1 * S2
    for beta in (0.5, 2.0, 6.0):
        for eta in (0.3, 1.0, 1.6):
            qbar = prob(beta, range(P), P, eta) ** (1 / P)
            for k in (1, 2, 3, 5, P // 2):
                pk = prob(beta, range(k), P, eta); worst = max(worst, pk / qbar ** k); cnt += 1
check(f"A chessboard, exact 2D U(1): mu(R all bad) <= qbar^|R| ({cnt} cases, tori 4x4, 6x4)", worst <= 1 + 1e-9, f"max ratio {worst:.4f}")
print("INFO (A): in 2D U(1) the plaquettes are exchangeable, so mu(R bad) depends only on |R|; the test is the inequality, not geometry.")
# (B) SU(2) Haar ball; class angle theta in [0, pi], eigenvalues e^{+-i theta}, density (2/pi) sin^2, ||U-1|| = 2 sin(theta/2)
ok = True; rr = []
for dl in (0.01, 0.1, 0.3, 0.5, 1.0):
    tm = 2 * np.arcsin(dl / 2); h = (tm - np.sin(tm) * np.cos(tm)) / np.pi; rr.append(h / (8 / (3 * np.pi ** 3) * dl ** 3)); ok &= h >= 8 / (3 * np.pi ** 3) * dl ** 3
check("B SU(2) Haar ball h_2(delta) >= (8/(3 pi^3)) delta^3", ok, "ratios " + ", ".join(f"{v:.2f}" for v in rr))
# SU(2) as unit quaternions; matrix form
def q2m(q):
    a, b, c, e = q[..., 0], q[..., 1], q[..., 2], q[..., 3]
    return np.stack([np.stack([a + 1j * b, c + 1j * e], -1), np.stack([-c + 1j * e, a - 1j * b], -1)], -2)
def haar(n): q = rng.normal(size=(n, 4)); return q2m(q / np.linalg.norm(q, axis=1, keepdims=True))
d = 4
def staple():
    return sum(haar(1)[0] for _ in range(2 * (d - 1)))
def maximiser(W):  # argmax Re tr(U W) over SU(2): W = sum of SU(2) is a real multiple of SU(2): W = r V, U* = V^dag
    r = np.sqrt(abs(np.linalg.det(W))); return np.conj(W.T) / r if r > 1e-12 else np.eye(2)
# (C)
worstC = 0
for _ in range(300):
    W = staple(); Us = maximiser(W); f0 = np.real(np.trace(Us @ W))
    a = rng.normal(size=3) * rng.uniform(0, 1.5); X = 1j * (a[0] * np.array([[1, 0], [0, -1]]) + a[1] * np.array([[0, 1], [1, 0]]) + a[2] * np.array([[0, -1j], [1j, 0]]))
    w, V = np.linalg.eigh(-1j * X); eX = V @ np.diag(np.exp(1j * w)) @ np.conj(V.T); nX = np.max(np.abs(w))
    worstC = max(worstC, (f0 - np.real(np.trace(Us @ eX @ W))) / (2 * (d - 1) * nX ** 2))
check("C second-order lemma f(U*) - f(U* e^X) <= N (d-1) ||X||^2 (SU(2), 300 random W, X)", worstC <= 1 + 1e-12, f"max ratio {worstC:.3f}")
# (D) quadrature: Haar sample of size 400k (MC with fixed seed; statistical error printed)
Us = haar(400000)
worstD = 0; lines = []; untest = []
for beta in (1.0, 4.0, 10.0):
    for t in (0.25, 0.5, 1.0):
        for _ in range(4):
            W = staple(); R = haar(1)[0]
            lw = (beta / 2) * np.real(np.einsum("nij,ji->n", Us, W)); w = np.exp(lw - lw.max())
            ev = np.linalg.norm(Us - R, ord=2, axis=(1, 2)) >= t; p = np.sum(w * ev) / np.sum(w)
            ess = np.sum(w * ev) ** 2 / max(np.sum((w * ev) ** 2), 1e-300)  # effective sample count in the event
            if ess < 200: untest.append((beta, t)); continue
            dl = min(0.5, (2 - t) / 3) * 0.5; x = 2 * np.arcsin((t + 3 * dl) / 2); tm = 2 * np.arcsin(dl / 2)
            lb = (tm - np.sin(tm) * np.cos(tm)) / np.pi * np.exp(-beta * (d - 1) * x ** 2)
            worstD = max(worstD, lb / max(p, 1e-300))
        lines.append(f"b{beta:g}t{t:g}:p={p:.1e},lb={lb:.1e}")
check("D conditional lower bound P_W(||U-R|| >= t) >= h_2(delta) e^{-beta (d-1) x^2} (SU(2), random W, R; MC 4e5)", worstD <= 1.0,
      f"max lb/p {worstD:.2e}; untestable (MC effective count < 200): {len(untest)}; " + " ".join(lines[::2]))
# (E) ribbon count, L = 3, d = 4, fine torus side 6, SU(2) near-identity field
Lb = 3; S = 6; E = np.eye(d, dtype=int); ORD = list(it.permutations(range(d)))
G = 0.06 * rng.normal(size=(d, S, S, S, S, 3)); qn = np.concatenate([np.cos(np.linalg.norm(G, axis=-1, keepdims=True)),
     np.sin(np.linalg.norm(G, axis=-1, keepdims=True)) * G / np.linalg.norm(G, axis=-1, keepdims=True)], -1); U = q2m(qn)
dag = lambda M: np.conj(np.swapaxes(M, -1, -2)); idx = lambda x: tuple(np.asarray(x) % S)
def step(x, m, sg): return U[m][idx(x)] if sg > 0 else dag(U[m][idx(np.asarray(x) - E[m])])
def path(a, b, order):
    P = np.eye(2, dtype=complex); cur = np.array(a)
    for m in order:
        while cur[m] != b[m]:
            sg = 1 if b[m] > cur[m] else -1; P = P @ step(cur, m, sg); cur[m] += sg
    return P
def straight(y, m):
    P = np.eye(2, dtype=complex); cur = np.array(y)
    for _ in range(Lb): P = P @ step(cur, m, 1); cur[m] += 1
    return P
X = np.array([0, 1, 0, 1]); m = 2; cX = X * Lb + 1; cY = cX + Lb * E[m]; Sc = straight(cX, m); zmax = 0
for o in ORD:
    for off in it.product(range(Lb), repeat=d):
        y = X * Lb + np.array(off); Z = dag(Sc) @ path(cX, y, o) @ straight(y, m) @ dag(path(cY, y + Lb * E[m], o)); zmax = max(zmax, np.linalg.norm(Z - np.eye(2), 2))
pmax = 0
for off in it.product(*[range(Lb * 2) if k == m else range(Lb) for k in range(d)]):
    x = X * Lb + np.array(off)
    for a_ in range(d):
        for b_ in range(a_ + 1, d):
            Pp = step(x, a_, 1) @ step(x + E[a_], b_, 1) @ dag(step(x + E[b_], a_, 1)) @ dag(step(x, b_, 1)); pmax = max(pmax, np.linalg.norm(np.eye(2) - Pp, 2))
AL = (d - 1) * Lb * (Lb - 1) / 2
check(f"E ribbon count: max_(s,y) ||Z - 1|| <= A_L max_slab ||1 - U_p||, A_L = {AL:g}", zmax <= AL * pmax, f"{zmax:.3f} <= {AL:g} x {pmax:.3f} = {AL * pmax:.3f}")
# (F) AF-window exponents: failures dense iff 3 x^2 lambda_AF < 4 ln L, lambda_AF = 4 N b0 ln L, b0 = 11N/(48 pi^2)
for N in (2, 3, 4, 6, 10):
    tauN = min(1, 2 * np.sin(np.pi / N)); out = []
    for name, t in (("t=1", 1.0), ("t=tau_N/2", tauN / 2)):
        x = 2 * np.arcsin(t / 2); out.append(f"{name}: 3 x^2 * 4 N b0 = {3 * x ** 2 * 4 * N * 11 * N / (48 * np.pi ** 2):.2f} ({'dense' if 3 * x ** 2 * 4 * N * 11 * N / (48 * np.pi ** 2) < 4 else 'undecided'})")
    print(f"INFO (F) SU({N}): " + "; ".join(out) + " vs 4")
print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
