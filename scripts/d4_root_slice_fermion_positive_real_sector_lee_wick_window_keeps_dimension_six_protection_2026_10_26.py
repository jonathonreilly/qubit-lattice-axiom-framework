AUDIT_INPUT_PATHS = ('docs/D4_ROOT_SLICE_FERMION_POSITIVE_REAL_SECTOR_LEE_WICK_WINDOW_KEEPS_DIMENSION_SIX_PROTECTION_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Protected fermions on the D4 event lattice: which time directions admit a slice reflection, the positive real
sector (Lee-Wick window) of the W(F4) nearest-neighbour fermion along a root, its dimension-six-free light branch,
zoom suppression of the complex pair, invariant counts, and Jordan-Wigner preservation of complex slice energies.
Self-contained (numpy/scipy/sympy). Seeded. Supplied free models; exact group/discriminant facts plus float checks."""
import itertools, time
import numpy as np, scipy.linalg as sl, sympy as sp
AUDIT_TIMEOUT_SEC = 120
t0 = time.time(); rng = np.random.default_rng(20261026); NP = NF = 0
def check(name, ok, info=""):
    global NP, NF
    NP += bool(ok); NF += (not ok); print(("PASS " if ok else "FAIL ") + name + (" | " + info if info else ""))
R = np.array([v for v in itertools.product([-1, 0, 1], repeat=4) if sum(map(abs, v)) == 2], float); E4 = np.eye(4)
# ---- 1. W(F4) and its reflections
gens = []
for i in range(3):
    M = np.eye(4); M[[i, i + 1]] = M[[i + 1, i]]; gens.append(M)
M = np.eye(4); M[0, 0] = -1; gens.append(M); h = np.ones(4) / 2; gens.append(np.eye(4) - 2 * np.outer(h, h))
key = lambda A: tuple(np.round(2 * A).astype(int).ravel()); D = {key(E4): E4}; fr = [E4]
while fr:
    nf = []
    for A in fr:
        for g in gens:
            B = g @ A
            if key(B) not in D: D[key(B)] = B; nf.append(B)
    fr = nf
G = np.array(list(D.values()))
refl = [A for A in G if np.allclose(A, A.T) and np.allclose(A @ A, E4) and abs(np.trace(A) - 2) < 1e-9]
nrm = [np.linalg.eigh(A)[1][:, 0] for A in refl]
long_ = sum(1 for n in nrm if np.allclose(np.sort(np.abs(n)), [0, 0, 1 / np.sqrt(2), 1 / np.sqrt(2)]))
dirs = {"root (1,1,0,0)": [1, 1, 0, 0], "short e1": [1, 0, 0, 0], "short (1,1,1,1)": [1, 1, 1, 1], "24-cell edge (2,1,1,0)": [2, 1, 1, 0], "24-cell face (1,1,1,0)": [1, 1, 1, 0]}
has = {k: any(np.allclose(A, E4 - 2 * np.outer(np.array(v, float), v) / np.dot(v, v)) for A in G) for k, v in dirs.items()}
Mh = np.array([[1, 1, 0, 0], [1, -1, 0, 0], [0, 0, 1, 1], [0, 0, 1, -1]], float)
d4s = np.array([v for v in itertools.product([-1, 0, 1], repeat=4) if sum(map(abs, v)) == 1] + list(itertools.product([-.5, .5], repeat=4)), float)
imgs = {tuple(x) for x in (d4s @ Mh.T)}; okmap = imgs == {tuple(x) for x in R} and np.allclose(Mh @ Mh.T, 2 * E4)
check("1 [exact] |W(F4)| = 1152 has 24 reflections (12 long-root + 12 short lines); a time reflection exists only for root and short directions",
      len(G) == 1152 and len(refl) == 24 and long_ == 12 and [has[k] for k in dirs] == [True, True, True, False, False] and okmap,
      "; ".join(f"{k}: {'yes' if v else 'no'}" for k, v in has.items()) + "; D4* = F4 lattice -> D4 by M/sqrt2 (short vectors -> roots), so D4* axis = D4 root, D4* root = D4 e1")
# ---- fermion kernel and pole machinery (parent d4-fermion-positivity, generalised time vector)
s1 = np.array([[0, 1], [1, 0]]); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1, -1]); I2 = np.eye(2); Z2 = np.zeros((2, 2))
gm = np.array([np.block([[Z2, I2], [I2, Z2]])] + [np.block([[Z2, -1j * s], [1j * s, Z2]]) for s in (s1, s2, s3)])
gv = lambda r: np.einsum('m,mab->ab', r, gm)
def cD4(k, w, m, tv):
    idx = [int(round(r @ tv)) for r in R]; H = max(map(abs, idx)); C = np.zeros((2 * H + 1, 4, 4), complex); C[H] += (2 * w + m) * E4
    for r, i in zip(R, idx): C[i + H] += np.exp(1j * r @ k) * (gv(r) - w * E4) / 12
    return C
def cZ4(k, w, m):
    C = np.zeros((3, 4, 4), complex); C[1] += (4 * w + m) * E4
    for mu in (1, 2, 3): C[1] += -w * np.cos(k[mu]) * E4 + 1j * np.sin(k[mu]) * gm[mu]
    C[2] += (gm[0] - w * E4) / 2; C[0] += (-gm[0] - w * E4) / 2; return C
Dz = lambda C, z: sum(C[a] * z ** (a - (len(C) - 1) // 2) for a in range(len(C)))
def poles(C):
    A = list(C)
    while np.abs(A[-1]).max() < 1e-14: A = A[:-1]
    while np.abs(A[0]).max() < 1e-14: A = A[1:]
    d = len(A) - 1; L = np.zeros((4 * d, 4 * d), complex); Mb = np.eye(4 * d, dtype=complex)
    L[:4 * (d - 1), 4:] = np.eye(4 * (d - 1)); Mb[4 * (d - 1):, 4 * (d - 1):] = A[d]
    for a in range(d): L[4 * (d - 1):, 4 * a:4 * (a + 1)] = -A[a]
    ev = sl.eigvals(L, Mb); return ev[np.isfinite(ev) & (np.abs(ev) > 1e-12)]
def resids(C):  # G(n) = sum_j lam_j^n P_j for n >= 1
    ev = poles(C); cl = []
    for z in ev[np.abs(ev) > 1 + 1e-9]:
        if not any(abs(z - c) < 1e-6 * abs(c) for c in cl): cl.append(z)
    out = []
    for z in cl:
        rad = min([abs(z - c) for c in ev if abs(z - c) > 1e-6 * abs(z)] + [1.0]) / 3; th = 2 * np.pi * (np.arange(64) + .5) / 64
        out.append((1 / z, -sum(np.linalg.inv(Dz(C, z + rad * np.exp(1j * t))) * rad * np.exp(1j * t) for t in th) / 64 / z))
    return out
def classify(rs, Gm):  # wrong-sign fraction of the real-pole sector; conjugate-pair defect; #complex; min Re E of complex
    rv, pb, nc, mre = [], 0., 0, 9.
    for l, P in rs:
        H = P @ Gm
        if abs(l.imag) > 1e-9 * abs(l):
            nc += 1; mre = min(mre, -np.log(abs(l))); mt = [Q for lq, Q in rs if abs(lq - np.conj(l)) < 1e-7 * abs(l)]
            pb = max(pb, np.abs(mt[0] @ Gm - H.conj().T).max() if mt else 9.)
        else: rv.append(np.linalg.eigvalsh((H + H.conj().T) / 2))
    v = np.concatenate(rv) if rv else np.array([-1.]); return min(v.max(), -v.min()) / np.abs(v).max(), pb, nc, mre
def frame(tv):
    tn = np.array(tv, float) / np.linalg.norm(tv); return np.linalg.qr(np.vstack([tn, E4[:3]]).T)[0][:, 1:], np.einsum('m,mab->ab', tn, gm)
kz = [np.r_[0, rng.uniform(-np.pi, np.pi, 3)] for _ in range(4)]
zw = max(classify(resids(cZ4(k, 1., .3)), gm[0])[0] for k in kz); zn = min(classify(resids(cZ4(k, 0., .3)), gm[0])[0] for k in kz)
check("2 calibration Z^4 (time axis): Wilson r=1 real sector definite; naive r=0 indefinite (T not positive)", zw < 1e-9 and zn > .5, f"Wilson {zw:.0e}, naive {zn:.2f}")
# ---- 3. the other directions
Qe, ge = frame([1, 0, 0, 0]); ke = [Qe @ rng.uniform(-np.pi, np.pi, 3) for _ in range(20)]
we = {w: max(classify(resids(cD4(k, w, .3, np.array([1., 0, 0, 0]))), ge)[0] for k in ke) for w in (0.5, 1., 1.2, 2.)}
Qf, gf = frame([2, 1, 1, 0]); kf = [Qf @ rng.uniform(-np.pi, np.pi, 3) for _ in range(6)]
pf = min(classify(resids(cD4(k, 1., .3, np.array([2., 1, 1, 0]))), gf)[1] for k in kf)
check("3 short-direction time (e1 = D4* root): real negative-norm branches for every w; edge direction (2,1,1,0): poles not conjugate-closed (no reflection)",
      min(we.values()) > .5 and pf > 1, "e1 wrong-sign: " + " ".join(f"w={w}:{v:.2f}" for w, v in we.items()) + f"; (2,1,1,0) unpaired-pole defect {pf:.0f}")
# ---- 4. exact k=0 window edge along the root
w_, z_ = sp.symbols('w z'); r2 = sp.sqrt(2); disc = []
for s in (1, -1):
    p = sp.expand((r2 * s - w_) * z_**4 + (4 * r2 * s - 8 * w_) * z_**3 + 18 * w_ * z_**2 - (4 * r2 * s + 8 * w_) * z_ - (r2 * s + w_))
    disc.append(sp.factor(sp.discriminant(p, z_)))
wp, wm = sp.sqrt((71 + 17 * sp.sqrt(17)) / 96), sp.sqrt((71 - 17 * sp.sqrt(17)) / 96)
check("4 [exact] root time, k = 0, m = 0: both g_t sectors have discriminant 27648 (144 w^4 - 213 w^2 + 2); window edges w^2 = (71 -+ 17 sqrt17)/96",
      all(sp.simplify(d - 27648 * (144 * w_**4 - 213 * w_**2 + 2)) == 0 for d in disc) and sp.simplify((144 * w_**4 - 213 * w_**2 + 2).subs(w_, wp)) == 0,
      f"w- = {float(wm):.5f}, w+ = {float(wp):.5f}; the CL natural point w = 1 is inside")
# ---- 5. the positive real sector (Lee-Wick window) along the root
rt = np.array([1., 1, 0, 0]); Qr, gr = frame(rt); kr = [Qr @ rng.uniform(-np.pi, np.pi, 3) for _ in range(40)] + [Qr @ np.array(v) for v in ([.05, .02, -.03], [3.14, 3.14, 3.14], [3.14, 0, 0])]
tab, ok5 = [], True
for w in (0.3, 0.7, 1.0, 1.2):
    for m in (0.02, 0.3, 1.0):
        c = [classify(resids(cD4(k, w, m, rt)), gr) for k in kr]
        wr, pb, mre = max(x[0] for x in c), max(x[1] for x in c), np.sqrt(2) * min(x[3] for x in c)
        ok5 &= wr < 1e-13 and pb < 1e-11 and all(x[2] == 2 for x in c); tab.append((w, m, mre))
out = [classify(resids(cD4(Qr @ np.array([0, 1e-3, 0]), w, 0., rt)), gr)[0] for w in (0.05, 1.25)]
check("5 root time, w in (w-, w+): every real pole has one norm sign (<1e-13) and the rest is ONE complex-conjugate pair with conjugate residues (pseudo-Hermitian T)",
      ok5 and min(out) > .3, "min Re E of the pair: " + " ".join(f"(w{w},m{m}):{e:.2f}" for w, m, e in tab if m != .3) + f"; outside (w=0.05, 1.25): wrong {out[0]:.2f}, {out[1]:.2f}")
# ---- 6. light branch: speed 1 and no k^2 term in v - 1 (dimension six zero) inside the window
dd = {'axis': [1, 0, 0], 'face': [1, 1, 0], 'body': [1, 1, 1], 'gen': [.3, .5, .81]}
def El(q, w):
    z = poles(cD4(Qr @ q, w, 0., rt)); z = z[(np.abs(z) > 1 + 1e-12) & (np.abs(z.imag) < 1e-9 * np.abs(z))]; return np.sqrt(2) * np.log(np.abs(z).min())
cs = {}
for w in (0.5, 1.0, 1.2):
    for nm, n in dd.items():
        n = np.array(n, float) / np.linalg.norm(n); x = np.array([.01, .02, .03]); c = np.polyfit(x**2, [El(t * n, w) / t for t in x], 2); cs[(w, nm)] = c[::-1]
check("6 light branch inside the window: v = 1 and the k^2 coefficient of v - 1 vanishes in every direction (W(F4) protection survives in the positive sector)",
      all(abs(c[0] - 1) < 1e-6 and abs(c[1]) < 1e-5 for c in cs.values()), "max |c2| " + " ".join(f"w={w}:{max(abs(cs[(w, n)][1]) for n in dd):.0e}" for w in (0.5, 1.0, 1.2)))
# ---- 7. gap between pair and real sector (analytic projector -> exponentially local projected H) and branch ranks
gap, rk = 9., set()
for k in kr:
    rs = resids(cD4(k, 1., .02, rt)); lr = [l for l, P in rs if abs(l.imag) < 1e-9 * abs(l)]; lc = [l for l, P in rs if abs(l.imag) >= 1e-9 * abs(l)]
    gap = min(gap, min(abs(a - b) for a in lc for b in lr)); rk |= {np.linalg.matrix_rank(P, 1e-8) for l, P in rs}
check("7 w = 1: the pair never meets the real sector on sampled real k (analytic spectral projector), every branch has rank 2 (one Dirac fermion per branch)",
      gap > 1e-3 and rk == {2}, f"min |lam_pair - lam_real| = {gap:.3f}")
# ---- 8. zoom: coarse slices n -> b n; wrong-sign weight of the Hankel form sum_j lam_j^{b(n+n')} P_j g_t falls as e^{-2b dE}
rs = resids(cD4(Qr @ np.array([.05, .02, -.03]), 1., .3, rt)); fz = {}
for b in (1, 2, 4, 8):
    Hk = np.block([[sum(l ** (b * (i + j)) * P @ gr for l, P in rs) for j in range(1, 5)] for i in range(1, 5)]); Hk = -(Hk + Hk.conj().T) / 2
    e = np.linalg.eigvalsh(Hk); fz[b] = max(-e.min(), 0) / e.max()
check("8 zoom: the complex pair's indefinite weight on coarse slices decays exponentially with the rung factor b (b=8 at float floor)",
      fz[1] > fz[2] > fz[4] and fz[4] < 1e-11 and fz[8] < 1e-11, " ".join(f"b={b}:{v:.1e}" for b, v in fz.items()))
# ---- 9. invariant counts behind 'any W(F4) spinor kernel': Sym^3 V -> V and Sym^5 V -> V, quartic scalars
B4 = np.array([A for A in G if np.allclose(np.abs(A).sum(1), 1)])
def cnt(H, deg, vec):
    p = [np.trace(np.linalg.matrix_power(H, k), axis1=1, axis2=2) for k in range(1, 6)]
    sym = {3: (p[0]**3 + 3 * p[0] * p[1] + 2 * p[2]) / 6, 4: (p[0]**4 + 6 * p[0]**2 * p[1] + 3 * p[1]**2 + 8 * p[0] * p[2] + 6 * p[3]) / 24,
           5: (p[0]**5 + 10 * p[0]**3 * p[1] + 15 * p[0] * p[1]**2 + 20 * p[0]**2 * p[2] + 20 * p[1] * p[2] + 30 * p[0] * p[3] + 24 * p[4]) / 120}[deg]
    return int(round(np.mean(sym * (p[0] if vec else 1))))
cW, cB = [cnt(G, 4, 0), cnt(G, 3, 1), cnt(G, 5, 1)], [cnt(B4, 4, 0), cnt(B4, 3, 1), cnt(B4, 5, 1)]
check("9 [exact] W(F4): 1 quartic scalar, 1 cubic vector covariant (p^2 p), 2 quintic (p^4 p, grad J6); B4: 2, 2, 4. Any W(F4) Dirac kernel is p-isotropic through p^3",
      cW == [1, 1, 2] and cB == [2, 2, 4], f"W(F4) {cW}, B4 {cB}")
# ---- 10. Jordan-Wigner (exact bosonization) preserves the single-particle spectrum, complex pair included
n = 6; hs = rng.normal(size=(n, n)) * .3; hs = hs + hs.T; hs[0, 1] += .9; hs[1, 0] -= .9   # non-normal, complex pair
sx, sz, sm = np.array([[0, 1], [1, 0]]), np.diag([1., -1]), np.array([[0, 1], [0, 0.]])
op = lambda L, i: np.kron(np.kron(np.eye(2 ** i), L), np.eye(2 ** (n - i - 1)))
c = [np.linalg.multi_dot([op(sz, j) for j in range(i)] + [op(sm, i)]) if i else op(sm, 0) for i in range(n)]
Hs = sum(hs[i, j] * c[i].T @ c[j] for i in range(n) for j in range(n)); eb = np.linalg.eigvals(Hs)
e1 = np.linalg.eigvals(hs.astype(complex)); ef = np.array([sum(e1[list(S)]) for r in range(n + 1) for S in itertools.combinations(range(n), r)]); mis = max(max(np.abs(ef - x).min() for x in eb), max(np.abs(eb - x).min() for x in ef))
check("10 [exact] JW spin Hamiltonian spectrum = fermion Fock sums, complex single-particle pair kept: bosonization cannot cure a non-positive fermion",
      mis < 1e-9 and np.abs(e1.imag).max() > 1e-3, f"max mismatch {mis:.0e} over 64 levels, single-particle Im {np.abs(e1.imag).max():.2f}")
print("VERDICT: the W(F4) nearest-neighbour fermion along a root has an exactly positive real sector for w- < w < w+ (contains the dim-6-free light Dirac branch);")
print("  the only defect is one complex-conjugate (Lee-Wick) pair at Re E >= 0.8-3.5 /a (rises with w). Short and edge directions fail. Interacting fate OPEN.")
print(f"TOTAL: PASS={NP} FAIL={NF}   ({time.time() - t0:.1f} s)")
