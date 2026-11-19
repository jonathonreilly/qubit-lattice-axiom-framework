#!/usr/bin/env python3
"""family-labels: what in the ADOPTED rules can label the three families on the family-class tick?
Candidates: (a) CL-1's even-cube copy mass on N_f = 3 copies; (b) copy depths along the slab's layer direction
(split-fermion reading); (c) copies on different zoom rungs; (d) family-dependent record cadence.
Supplied model: FREEZE (W_F = (-2,1,1)) as the family-class tick, rebuilt exactly as in t-breaking-tick-lowenergy
(twist-local-single seed and draw order); the coupled-layer slab of floquet-pi-slab (F, F^+ alternating, label gates,
g = 0.5, Ls = 7); CL-1's copy mass exp(i (M/4)(1 - s) R_e) before and after the tick; zoom-3 labels (2pi/3) j (1,1,1);
3x3 mass matrices seeded. Labels: [T] exact, [F] finite diagnostic, [S] estimate. Verdict per criteria_pre_run.txt:
PASS lines record that the computation came out as stated, including the predicted failures of the candidates."""
import os, time, itertools as it, resource
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import numpy as np
from scipy.linalg import expm, null_space, schur

rng = np.random.default_rng(20261023)
T0 = time.time(); NP = [0, 0]
def check(tag, ok, msg, det=""):
    ok = bool(ok); NP[0 if ok else 1] += 1
    print(f"{'PASS' if ok else 'FAIL'}: {tag} {msg}" + (f"  [{det}]" if det else ""))
w = np.exp(2j * np.pi / 3); I8 = np.eye(8)
# ------------------------------------------------ FREEZE rebuild (twist-local-single, same seed and draw order)
def nullsp(rows): return null_space(np.vstack(rows), rcond=1e-9)
def cm(o): return np.kron(o, I8) - np.kron(I8, o.T)
def axang(R):
    ev, vv = np.linalg.eig(R); n = np.real(vv[:, np.argmin(abs(ev - 1))])
    th = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1)); K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
    return (n if np.allclose(expm(th * K), R) else -n), th
C3d = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0.0]])
CELL = list(it.product([0, 1], repeat=3)); A = np.array(CELL); IDX = {a: 4 * a[0] + 2 * a[1] + a[2] for a in CELL}
def eta_s(i, a): return [1, (-1) ** a[0], (-1) ** (a[0] + a[1])][i]
def Wl(i, k, odd):
    M = np.zeros((8, 8), complex)
    for a in CELL:
        if a[i] == (1 if odd else 0):
            b = list(a); b[i] = 1 - a[i]; b = tuple(b); ph = np.exp(2j * k[i]) if odd else 1
            M[IDX[b], IDX[a]] = eta_s(i, a) * ph; M[IDX[a], IDX[b]] = eta_s(i, a) * np.conj(ph)
    return M
Re = sum(Wl(i, np.zeros(3), 0) for i in range(3)) / np.sqrt(3)
def U1(k, eps=0.3): return expm(1j * eps * sum(Wl(i, k, 1) for i in range(3)) / np.sqrt(3)) @ expm(-1j * eps * Re)
hh = 1e-6; Av = []
for i in range(3):
    d = np.zeros(3); d[i] = hh; Av.append(1j * (U1(d) - U1(-d)) / (2 * hh))
Ah = [a / np.sqrt(np.trace(a @ a).real / 8) for a in Av]
S = [-0.25j * (Ah[(i + 1) % 3] @ Ah[(i + 2) % 3] - Ah[(i + 2) % 3] @ Ah[(i + 1) % 3]) for i in range(3)]
chi = 1j * Ah[0] @ Ah[1] @ Ah[2]
kt = [rng.uniform(-1, 1, 3) for _ in range(2)]
P = np.zeros((8, 8))
for a in CELL:
    b = tuple(np.rint(C3d @ (np.array(a) - .5) + .5).astype(int)); P[IDX[b], IDX[a]] = 1
for sgn in it.product([1, -1], repeat=8):
    T3 = np.diag(sgn) @ P
    if all(np.allclose(T3 @ U1(k) @ T3.T, U1(C3d @ k)) for k in kt): break
nl, th = axang(C3d)
tt = expm(-1j * th * sum(nl[i] * S[i] for i in range(3))).conj().T @ T3
if not np.allclose(np.linalg.matrix_power(tt, 3), I8, atol=1e-6): tt = -tt
PL = (I8 + chi) / 2; PR = I8 - PL; sig = [2 * s for s in S]
tau3 = (tt - tt.conj().T) / (1j * np.sqrt(3)); tau3 = (tau3 + tau3.conj().T) / 2
Pw = (I8 + tau3) / 2; Pb = I8 - Pw
Cb = nullsp([cm(o) for o in sig + [chi]]); Yr = (Cb @ rng.normal(size=Cb.shape[1])).reshape(8, 8)
tp = np.zeros((8, 8), complex)
for Pq in (PL, PR):
    Zb = Pq @ Pw @ Yr @ Pb @ Pq; tp += Zb / np.sqrt(np.trace(Zb @ Zb.conj().T).real / 2)
tau1 = tp + tp.conj().T; tau2 = -1j * (tp - tp.conj().T); gam = [tau3 @ s for s in sig]
def Uc(K):
    c, s = np.cos(K), np.sin(K); H = (np.sqrt(2) / 3) * (c[0] + np.conj(w) * c[1] + w * c[2])
    return c.sum() / 3 * I8 + 1j * (H * tp + np.conj(H) * tp.conj().T + sum(s[i] * gam[i] for i in range(3)) / np.sqrt(3))
Cm = nullsp([cm(o) for o in sig + [tau1, tau2, tau3]])
for j in range(Cm.shape[1]):
    e = Cm[:, j].reshape(8, 8); a = (e - chi @ e @ chi) / 2
    if np.linalg.norm(a) > 1e-6: Ex = a + a.conj().T; break
Ex = Ex / np.sqrt(np.trace(Ex @ Ex).real / 8); Y = Pw + Pb @ Ex
Pp = (I8 + chi @ tau3) / 2; Pm = I8 - Pp
def UF(K): return Pp @ (Y @ Uc(K) @ Y.conj().T) + Pm @ (1j * tau3)
Pq1, Pq2 = Pp @ (I8 + tau3) / 2, Pp @ (I8 - tau3) / 2            # node labels: tau3 = +1 -> q 1, tau3 = -1 -> q 2 (A1)
from scipy.linalg import logm
ROTS = []
for p in it.permutations(range(3)):
    for sg in it.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i in range(3): R[p[i], i] = sg[i]
        if np.linalg.det(R) > 0: ROTS.append(R)
isT = lambda R: abs(np.trace(R)) < 1e-9 or np.allclose(R, np.diag(np.diag(R)))     # the 12 tetrahedral rotations
kr = [rng.uniform(-np.pi, np.pi, 3) for _ in range(4)]
uni = max(np.linalg.norm(UF(K) @ UF(K).conj().T - I8) for K in kr)
check("A0 [T]", uni < 1e-12 and np.linalg.norm(UF(np.zeros(3)) @ Pp - Pp) < 1e-12, "FREEZE rebuilt: unitary, light Pi+ at quasi-energy 0 at K = 0", f"unitarity {uni:.0e}")
# ================================================================ (a) copy mass
print("== (a) CL-1's even-cube copy mass on the family-class tick and on N_f = 3 copies")
We = [Wl(i, np.zeros(3), 0) for i in range(3)]                       # even cube's undressed unit hops
s = 1j * We[0] @ We[1] @ We[2] @ Re                                   # copy sign
def CM(M): return expm(1j * (M / 4) * (I8 - s) @ Re)
def UM(K, M): C = CM(M); return C @ UF(K) @ C
ph = np.sort(np.angle(np.linalg.eigvals(UM(np.zeros(3), 0.2))))
check("A1 [T]", np.abs(s @ s - I8).max() < 1e-12 and np.abs(s @ Re - Re @ s).max() < 1e-12 and np.abs(s @ tau3 - tau3 @ s).max() < 1e-12
      and abs(np.trace(s @ Pq1).real + 2) < 1e-12 and abs(np.trace(s @ Pq2).real - 2) < 1e-12,
      "copy sign s: s^2 = 1, commutes with R_e and tau3; on Pi+ the q 1 pair has s = -1, the q 2 pair s = +1; the copy mass "
      "moves only the q 1 (mirror-copy) pair off 0", f"node phases at M = 0.2: {np.round(ph, 3)}")
Fu, _ = np.linalg.qr(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))
K0 = rng.uniform(-np.pi, np.pi, 3); Ub = np.kron(UM(K0, 0.2), np.eye(3)); Xf = np.kron(I8, Fu)
cm3 = np.abs(Ub @ Xf - Xf @ Ub).max()
check("A2 [T]", cm3 < 1e-13, "the copy mass is built from one cube's hops, so on N_f copies it is (cell op) x 1_F: it commutes "
      "with every U(3) family rotation; it gives every copy the same mass M and labels nothing", f"|[U_M x 1, 1 x u]| = {cm3:.0e}")
Ks = [rng.uniform(-np.pi, np.pi, 3) for _ in range(12)]
def tr_anti(U, R, Kset=Ks):
    """time-reversing antiunitary T x R: V conj(U(K)) = U(-R K)^+ V over Kset; return invertible V or None."""
    rows = [np.kron(I8, U(-R @ K).conj().T) - np.kron(U(K).conj().T, I8) for K in Kset]
    N = null_space(np.vstack(rows), rcond=1e-9)
    if N.shape[1] == 0: return None
    V = (N @ (rng.normal(size=N.shape[1]) + 1j * rng.normal(size=N.shape[1]))).reshape(8, 8, order='F')
    sv = np.linalg.svd(V, compute_uv=False)
    return V if sv[-1] / sv[0] > 1e-6 else None
def keptset(U): return [R for R in ROTS if tr_anti(U, R) is not None]
KS = {M: keptset(lambda K, M=M: UM(K, M)) for M in (0.0, 0.05, 0.2)}
Hr = (lambda X: X + X.conj().T)(rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8)))
Kctl = keptset(lambda K: expm(0.3j * Hr) @ UF(K))
nt = lambda L: sorted(int(not isT(R)) for R in L)
check("A3 [F]", all(len(L) == 12 and nt(L) == [1] * 12 for L in KS.values()) and len(Kctl) == 0,
      "kept time-reversing antiunitaries T x R with the copy mass on: exactly the 12 non-tetrahedral R (6 C4, 6 C2'), "
      "the same as without it; T alone stays broken. Control: a random cell gate breaks all 24 (the search can fail)",
      f"counts M = 0, 0.05, 0.2: {[len(L) for L in KS.values()]}; random-gate control: {len(Kctl)}")
C2p = np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1.]])                # C2' about (1,-1,0)
Kf = [rng.uniform(-np.pi, np.pi, 3) for _ in range(20)]
V = tr_anti(lambda K: UM(K, 0.2), C2p); u_, _, vh_ = np.linalg.svd(V); V = u_ @ vh_
err = max(np.abs(V @ UM(K, 0.2).conj() @ V.conj().T - UM(-C2p @ K, 0.2).conj().T).max() for K in Kf)
chiral = np.abs(V @ tau3.conj() @ V.conj().T - tau3).max()
check("A4 [F]", err < 1e-10 and chiral < 1e-10, "T x C2'(1,-1,0) with the copy mass: unitary V intertwines 20 fresh momenta "
      "and keeps tau3 (turn label) - the copy mass's kept element set CONTAINS T x C2', not only T x C4", f"err {err:.0e}, tau3 {chiral:.0e}")
def img(R, j):
    k = np.mod(-R @ ((2 * np.pi / 3) * j * np.ones(3)), 2 * np.pi)
    for jj in range(3):
        if np.allclose(k, np.mod((2 * np.pi / 3) * jj * np.ones(3), 2 * np.pi), atol=1e-9): return jj
    return None
fix = [R for R in KS[0.2] if [img(R, j) for j in range(3)] == [0, 1, 2]]
off = [R for R in KS[0.2] if any(img(R, j) is None for j in range(3))]
check("A5 [T]", len(fix) == 3 and len(off) == 9 and all(abs(axang(R)[0] @ np.ones(3)) < 1e-9 for R in fix),
      "family action of the kept elements: the 3 axis-reversing T x C2' fix every zoom-3 label (X diagonal), the other 9 "
      "(T x C4, T x C2'(110)-type) take the labels off the family set; on stacked copies every one acts with X = 1",
      f"fixing {len(fix)}, off-set {len(off)}")
def jarlskog(Mu, Md):
    _, Uu = np.linalg.eigh(Mu @ Mu.conj().T); _, Ud = np.linalg.eigh(Md @ Md.conj().T); Vc = Uu.conj().T @ Ud
    return np.imag(Vc[0, 0] * Vc[1, 1] * np.conj(Vc[0, 1]) * np.conj(Vc[1, 0]))
def cg(): return rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
jx = 0.0
for _ in range(300):
    d1, d2 = np.diag(np.exp(1j * rng.uniform(0, 6.3, 3))), np.diag(np.exp(1j * rng.uniform(0, 6.3, 3)))
    Mu, Md = d1 @ rng.normal(size=(3, 3)), d1 @ rng.normal(size=(3, 3)) @ d2          # X diagonal: real up to rephasing
    jx = max(jx, abs(jarlskog(Mu, Md)))
check("A6 [T]", jx < 1e-14, "so the generalized-CP lemma still applies with the copy mass on: any mass sector respecting a "
      "kept element that fixes the families (X = 1 or diagonal) is real up to rephasing and has J = 0 - the 'not checked' item "
      "of cp-source-new-tick closes NEGATIVE: the copy mass neither labels families nor removes the family-fixing antiunitary",
      f"max|J| over 300 = {jx:.0e}")
# ================================================================ (b) depths along the slab's layer direction
print("== (b) copy depths along the slab's layer direction (split-fermion reading)")
Pq1, Pq2 = Pp @ (I8 + tau3) / 2, Pp @ (I8 - tau3) / 2
def slab(K, Ls=7, g=0.5):
    F = UF(K); U0 = np.zeros((8 * Ls, 8 * Ls), complex); HA = np.zeros_like(U0); HB = np.zeros_like(U0)
    for l in range(Ls): U0[8 * l:8 * l + 8, 8 * l:8 * l + 8] = F if l % 2 == 0 else F.conj().T
    for l in range(Ls - 1):
        H = HA if l % 2 == 0 else HB; Pq = Pq1 if l % 2 == 0 else Pq2
        H[8 * l:8 * l + 8, 8 * l + 8:8 * l + 16] += Pq; H[8 * l + 8:8 * l + 16, 8 * l:8 * l + 8] += Pq
    return expm(-1j * g * HB) @ expm(-1j * g * HA) @ U0
dirn = np.array([0.3, -0.5, 0.81]); dirn /= np.linalg.norm(dirn)
def nearwall(kap, Ls=7):
    e, v = np.linalg.eig(slab(kap * dirn, Ls)); best = None
    for j in np.where(np.abs(np.angle(e)) < 0.3)[0]:
        x = v[:, j] / np.linalg.norm(v[:, j]); wl = np.array([np.linalg.norm(x[8 * l:8 * l + 8]) ** 2 for l in range(Ls)])
        if best is None or wl[0] > best[0]: best = wl
    return best
Sb = slab(K0); cmb = np.abs(np.kron(Sb, np.eye(3)) @ np.kron(np.eye(56), Fu) - np.kron(np.eye(56), Fu) @ np.kron(Sb, np.eye(3))).max()
check("B1 [T]", cmb < 1e-13, "the adopted slab is family-blind: N_f copies stacked on it have identical layer profiles (slab x 1_F "
      "commutes with U(3)); a family-dependent depth needs a family-dependent termination or label-gate pattern, i.e. CHOSEN",
      f"|[slab x 1, 1 x u]| = {cmb:.0e}")
w0 = nearwall(0.0); wk = {k: nearwall(k) for k in (0.02, 0.04, 0.08)}
ex1 = np.log(wk[0.08][1] / wk[0.02][1]) / np.log(4); ex2 = np.log(wk[0.08][2] / wk[0.02][2]) / np.log(4)
check("B2 [F]", w0[0] > 1 - 1e-12 and w0[1:].max() < 1e-25 and abs(ex1 - 4) < 0.05 and abs(ex2 - 8) < 0.1,
      "the near-wall light Weyl at the node is EXACTLY single-layer (zero width); off the node its weight on layer n grows as "
      "|K|^(4n), i.e. amplitude ~ (c K^2)^n, c ~ 0.23: a displaced copy has ZERO overlap with a wall channel at K = 0, so depth "
      "gives no exponential mass hierarchy, only momentum-suppressed (higher-dimension) couplings",
      f"K=0 weights {w0[0]:.12f}, max rest {w0[1:].max():.0e}; exponents layer1 {ex1:.3f}, layer2 {ex2:.3f}; amp1/K^2 at 0.08 {np.sqrt(wk[0.08][1]) / 0.08 ** 2:.3f}")
rk = []
for n in (1, 2, 3):
    A_ = rng.normal(size=(3, n)) + 1j * rng.normal(size=(3, n)); B_ = rng.normal(size=(3, n)) + 1j * rng.normal(size=(3, n))
    Y = A_ @ np.diag(rng.normal(size=n)) @ B_.T; rk.append(int(np.linalg.matrix_rank(Y, tol=1e-10)))
check("B3 [T]", rk == [1, 2, 3], "a Higgs-type channel on one layer gives Y_ij = phi_i(z_H) chi_j(z_H): rank 1 (one massive family); "
      "a channel spread over n layers gives rank <= n, so three masses need a channel over >= 3 layers, i.e. no suppression",
      f"ranks for 1, 2, 3 layers: {rk}")
mtop_a = 173.0 / 1.22e19                                               # K a at the top mass, a = l_P  [S]
supp = 0.23 * mtop_a ** 2
check("B4 [S]", supp < 1e-30, "estimate: even reading the off-node tail at K a = m_t a / hbar c as a mass suppression gives a factor "
      "~0.23 (K a)^2 per layer, ~5e-35 at a = l_P, against measured m_e/m_t = 3e-6 and m_u/m_t = 1.3e-5: depth hierarchies on the "
      "adopted slab are all-or-nothing (excluded), not exponential", f"per-layer factor {supp:.1e}")
# ================================================================ (c) zoom ladder
print("== (c) copies on different zoom rungs")
ov = []
for a, b in [(0, 1), (0, 2), (1, 2), (1, 3)]:
    nb = 2 ** b; vb = np.ones(nb ** 3) / nb ** 1.5
    va = np.zeros((nb, nb, nb)); na = 2 ** a; va[:na, :na, :na] = 1; va = va.ravel() / np.linalg.norm(va)
    ov.append(abs(va @ vb - 2 ** (-1.5 * (b - a))))
jr = max(abs(jarlskog(np.array([[2 ** (-1.5 * abs(i - j - o)) * c for j, c in enumerate(rng.uniform(.5, 2, 3))] for i in range(3)]),
                      np.array([[2 ** (-1.5 * abs(i - 2 * j)) * c for j, c in enumerate(rng.uniform(.5, 2, 3))] for i in range(3)])))
         for o in range(3) for _ in range(50))
check("C1 [T]", max(ov) < 1e-12 and jr < 1e-14, "nested block-uniform readings overlap by exactly 2^(-3|a-b|/2) (hierarchy base "
      "fixed, exponents = rung numbers); CL-1 puts matter on the finest role block, so rung labels are CHOSEN; real positive overlaps "
      "times real O(1) coefficients give J = 0, so the phase is supplied too (flavour-rule: >= 2 ranges with range-non-linear phases)",
      f"overlap err {max(ov):.0e}; max|J| real rung ladders {jr:.0e}")
# ================================================================ (d) records
print("== (d) family-dependent record cadence")
def liou(H, Ps, gs):
    n = H.shape[0]; I = np.eye(n); L = -1j * (np.kron(I, H) - np.kron(H.T, I))
    for P, gm in zip(Ps, gs): L += gm * (np.kron(P.conj(), P) - 0.5 * np.kron(I, P @ P) - 0.5 * np.kron((P @ P).T, I))
    return L
Q, _ = np.linalg.qr(cg()); Ps = [np.outer(Q[:, f], Q[:, f].conj()) for f in range(3)]; gs = [0.1, 0.37, 1.3]
im1 = np.abs(np.linalg.eigvals(liou(0.8 * np.eye(3), Ps, gs)).imag).max()
check("D1 [T]", im1 < 1e-12, "records as a family-dependent dephasing (rates 0.1, 0.37, 1.3 in a random family basis) on the family-blind "
      "generator m 1: every Liouvillian eigenvalue is real, so no oscillation frequency, no mass splitting, no mixing phase; records "
      "only remove coherence, and under CL-2 they never condition the odds at all", f"max |Im lambda| = {im1:.0e}")
print("VERDICT: (a) copy mass: label NOT given (U(3) intact), kept T x C2' fixes families -> J = 0. (b) depth: CHOSEN; node "
      "profile single-layer -> all-or-nothing, no hierarchy. (c) rungs: CHOSEN (matter on finest block); base 2^(-3/2) fixed, "
      "exponents chosen, J = 0 without supplied phases. (d) records: no splitting. No adopted rule labels the families.")
print(f"runtime {time.time() - T0:.1f} s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20:.0f} MB")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
