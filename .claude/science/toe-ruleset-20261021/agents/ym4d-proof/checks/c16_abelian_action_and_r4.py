#!/usr/bin/env python3
"""Check c16 (PROOF.md, session 5).
(R4) REVIEW_S4 fix 1: the E8*-sup domain. The central element e^{2 pi i/13} 1 of SU(13) has ||Z - 1|| = 2 sin(pi/13) < 1/2
     but its principal log has trace 2 pi i (not traceless). With ||Z - 1|| <= tau_N/2 (tau_N = min(1, 2 sin(pi/N))) the
     principal log is traceless (random and extremal tests, N = 2..40).
(B)  1 - N^-1 Re tr U = ||1 - U||_HS^2 / (2N) >= ||1 - U||_op^2 / (2N) on random SU(N) (used in Lemma A2, Gaussian E8**).
(A1) Lemma A1 (abelian, linear): for real link fields A and the S4' averaging linearised (A' = avg_{sigma,y} A(T^sigma_y)),
     (i)  dA'(P) = avg_{y in B(X)} flux(A; L x L straight square at y in the plane of P)  (exact identity), and
     (ii) the operator M: F = dA -> Phi = dA' satisfies ||M||_op^2 <= L^(4-d), so sum_P Phi_P^2 <= L^(4-d) sum_p F_p^2.
     In d = 4 the constant is 1: the coarse action never exceeds the fine action (contrast E8*-ob: sup grows like L^2).
     Tested d = 2, 3, 4 with L = 3 (one step), and d = 2 two steps. Checks test instances, not uniformity.
Pre-registered criteria are the PASS lines below.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
import time, itertools as it, math, numpy as np
from scipy.linalg import expm, logm
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0; rng = np.random.default_rng(16)
def check(n, ok, s=""):
    global NP, NF
    NP += bool(ok); NF += not ok; print(("PASS " if ok else "FAIL ") + n + (" | " + s if s else ""))

def plog(Z):  # principal log via eigendecomposition (Z normal)
    w, V = np.linalg.eig(Z); return V @ np.diag(np.log(w)) @ np.linalg.inv(V)

def rand_su(N, s):  # exp of random traceless anti-Hermitian of norm ~ s
    H = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N)); H = (H + H.conj().T) / 2
    H -= np.trace(H) / N * np.eye(N); H *= s / np.linalg.norm(H, 2); return expm(1j * H)

# (R4)
N = 13; Z = np.exp(2j * np.pi / 13) * np.eye(N)
nz = np.linalg.norm(Z - np.eye(N), 2); tr = np.trace(plog(Z))
check("R4a N=13 centre: ||Z-1|| < 1/2 and tr log Z = 2 pi i", nz < 0.5 and abs(tr - 2j * np.pi) < 1e-9,
      f"||Z-1||={nz:.4f}, tr log={tr.imag:.4f}i")
worst = 0.0; viol = 0
for N in range(2, 41):
    tau = min(1.0, 2 * math.sin(math.pi / N))
    for _ in range(20):
        U = rand_su(N, 1.0); w = np.linalg.eigvals(U - np.eye(N)); nrm = np.max(np.abs(w))
        U = expm(logm(U) * (tau / 2 / max(nrm, 1e-12)) * rng.uniform(0.2, 1.0))  # shrink so ||U-1|| <= tau/2
        if np.linalg.norm(U - np.eye(N), 2) > tau / 2 + 1e-12: continue
        worst = max(worst, abs(np.trace(plog(U))))
    for j in range(1, N):  # extremal central-type elements diag(e^{i th}) with ||Z-1|| = tau/2 exactly
        th = 2 * math.asin(tau / 4); ph = np.array([th] * j + [-th * j / (N - j)] * (N - j))
        Z = np.diag(np.exp(1j * ph))
        if np.linalg.norm(Z - np.eye(N), 2) <= tau / 2 + 1e-12: worst = max(worst, abs(np.trace(plog(Z))))
        cz = np.exp(2j * np.pi * j / N) * np.eye(N)
        if np.linalg.norm(cz - np.eye(N), 2) <= tau / 2 + 1e-12: viol += 1
check("R4b ||Z-1|| <= tau_N/2 => principal log traceless (N=2..40)", worst < 1e-8, f"max |tr log| = {worst:.1e}")
check("R4c no nontrivial centre element within tau_N/2 (N=2..40)", viol == 0, f"violations={viol}")

# (B)
worstB = 1e9
for N in (2, 3, 4, 5, 8):
    for s in (0.1, 1.0, 3.0):
        for _ in range(30):
            U = rand_su(N, s); lhs = 1 - np.trace(U).real / N
            hs = np.linalg.norm(np.eye(N) - U) ** 2 / (2 * N); op = np.linalg.norm(np.eye(N) - U, 2) ** 2 / (2 * N)
            worstB = min(worstB, lhs - op) if abs(lhs - hs) < 1e-10 else -1
check("B 1 - Re tr U/N = ||1-U||_HS^2/2N >= ||1-U||_op^2/2N", worstB >= -1e-12, f"min(lhs - op) = {worstB:.2e}")

# (A1) abelian averaging. A[mu] has shape (n,)*d ; A[mu][x] is the link x -> x + e_mu.
def axial(c, y, order, n):  # list of (direction, start point, sign) from c to y moving coordinates in 'order'
    steps = []; p = list(c)
    for nu in order:
        while p[nu] != y[nu]:
            if y[nu] > p[nu]: steps.append((nu, tuple(p), 1)); p[nu] += 1
            else: p[nu] -= 1; steps.append((nu, tuple(p), -1))
    return steps

def lineint(A, steps, n):
    return sum(sg * A[nu][tuple(q % n for q in pt)] for nu, pt, sg in steps)

def average(A, d, L, n):  # one S4' step, linearised: returns coarse A' on side n // L
    nc = n // L; Ap = np.zeros((d,) + (nc,) * d); h = (L - 1) // 2
    orders = list(it.permutations(range(d)))
    offs = list(it.product(range(-h, h + 1), repeat=d))
    for X in it.product(range(nc), repeat=d):
        c = np.array(X) * L + h
        for mu in range(d):
            cY = c.copy(); cY[mu] += L; tot = 0.0
            for o in orders:
                for off in offs:
                    y = c + np.array(off); yL = y.copy(); yL[mu] += L
                    st = axial(c, y, o, n) + [(mu, tuple(y[:mu]) + (y[mu] + t,) + tuple(y[mu + 1:]), 1) for t in range(L)]
                    back = axial(cY, yL, o, n); st += [(nu, pt, -sg) for nu, pt, sg in back]
                    tot += lineint(A, st, n)
            Ap[mu][X] = tot / (len(orders) * len(offs))
    return Ap

def curl(A, d, n):  # F[(mu,nu)] plaquette field
    return {(m, v): A[m] + np.roll(A[v], -1, axis=m) - np.roll(A[m], -1, axis=v) - A[v]
            for m in range(d) for v in range(m + 1, d)}

def square_flux_avg(F, d, L, n):  # avg over y in B(X) of flux through the L x L square at y in plane (m,v)
    nc = n // L; h = (L - 1) // 2; out = {}
    for (m, v), f in F.items():
        S = np.zeros_like(f)  # S[y] = sum of f over the L x L square with lower corner y
        for a in range(L):
            for b in range(L): S += np.roll(np.roll(f, -a, axis=m), -b, axis=v)
        G = np.zeros((nc,) * d)
        for X in it.product(range(nc), repeat=d):
            sl = tuple(slice(x * L, x * L + L) for x in X); G[X] = S[sl].mean()
        out[(m, v)] = G
    return out

L = 3
for d, nc in ((2, 4), (3, 2), (4, 2)):
    n = nc * L; A = rng.normal(size=(d,) + (n,) * d); t = time.time()
    Ap = average(A, d, L, n); Fp = curl(Ap, d, nc); F = curl(A, d, n); Sq = square_flux_avg(F, d, L, n)
    err = max(np.max(np.abs(Fp[k] - Sq[k])) for k in Fp)
    check(f"A1(i) d={d}: dA'(P) = avg_y flux(square_y)", err < 1e-10, f"max err {err:.1e}, {time.time()-t:.1f}s")
    # operator norm of M: F -> Phi (blocks per plane are independent): build M for one plane explicitly
    m, v = 0, 1; npl = n ** d; rows = []
    for X in it.product(range(nc), repeat=d):
        r = np.zeros((n,) * d)
        for y in it.product(*[range(x * L, x * L + L) for x in X]):
            for a in range(L):
                for b in range(L):
                    q = list(y); q[m] = (q[m] + a) % n; q[v] = (q[v] + b) % n; r[tuple(q)] += 1
        rows.append(r.ravel() / L ** d)
    Mm = np.array(rows); nm = np.linalg.eigvalsh(Mm @ Mm.T).max()
    ratio = sum((Fp[k] ** 2).sum() for k in Fp) / sum((F[k] ** 2).sum() for k in F)
    check(f"A1(ii) d={d}: ||M||^2 <= L^(4-d) = {L**(4-d)}", nm <= L ** (4 - d) * (1 + 1e-12),
          f"||M||^2 = {nm:.6f}; random-field ratio {ratio:.4f}")
# two steps, d = 2
d, n = 2, 18; A = rng.normal(size=(d, n, n)); A1 = average(A, d, L, n); A2 = average(A1, d, L, n // L)
r1 = sum((curl(A1, d, 6)[k] ** 2).sum() for k in [(0, 1)]) / (curl(A, d, n)[(0, 1)] ** 2).sum()
r2 = (curl(A2, d, 2)[(0, 1)] ** 2).sum() / (curl(A1, d, 6)[(0, 1)] ** 2).sum()
check("A1(iii) d=2 two steps: each step ratio <= L^2", r1 <= 9 and r2 <= 9, f"ratios {r1:.4f}, {r2:.4f}")
print(f"elapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
