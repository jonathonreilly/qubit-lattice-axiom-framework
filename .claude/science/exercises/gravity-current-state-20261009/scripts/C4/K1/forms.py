"""K1 step 1: W(B4)-invariant quadratic forms in a symmetric tensor h_{mu nu} on Z^4.
O(q^0): mass forms; O(q^2): two-derivative forms. Gauge map delta h = s xi + xi s (linearized diffeo).
Pure numpy (float64, SVD ranks with gaps reported). Usage: python forms.py
"""
import numpy as np, itertools
np.set_printoptions(precision=4, suppress=True, linewidth=150)
rng = np.random.default_rng(1)
D = 4
pairs = [(m, n) for m in range(D) for n in range(m, D)]          # 10 components
def sym(v):
    h = np.zeros((D, D))
    for k, (m, n) in enumerate(pairs):
        h[m, n] = h[n, m] = v[k]
    return h
def unsym(h):
    return np.array([h[m, n] for (m, n) in pairs])
# W(B4): signed permutation matrices (384)
G = []
for perm in itertools.permutations(range(D)):
    for sg in itertools.product((1, -1), repeat=D):
        R = np.zeros((D, D))
        for i, j in enumerate(perm):
            R[i, j] = sg[i]
        G.append(R)
assert len(G) == 384
# action of R on h-components (10x10) : h -> R h R^T
def rep10(R):
    M = np.zeros((10, 10))
    for k in range(10):
        e = np.zeros(10); e[k] = 1
        M[:, k] = unsym(R @ sym(e) @ R.T)
    return M
G10 = [rep10(R) for R in G]
def rank(M, tol=1e-9):
    s = np.linalg.svd(M, compute_uv=False)
    r = int(np.sum(s > tol * max(1, s[0])))
    gap = (s[r - 1], s[r] if r < len(s) else 0.0)
    return r, gap
# ---- mass forms: symmetric 10x10 matrices invariant under G10 ----
def reynolds_mass(Mq):
    return sum(g.T @ Mq @ g for g in G10) / len(G10)
basis55 = []
for i in range(10):
    for j in range(i, 10):
        E = np.zeros((10, 10)); E[i, j] = E[j, i] = 1; basis55.append(E)
P = np.array([reynolds_mass(E).ravel() for E in basis55])
rm, gm = rank(P)
print(f"[mass] dim of W(B4)-invariant mass forms = {rm}  (sv gap {gm[0]:.2e} / {gm[1]:.2e})")
def massform(f):
    M = np.zeros((10, 10))
    for i in range(10):
        for j in range(10):
            ei = np.zeros(10); ei[i] = 1; ej = np.zeros(10); ej[j] = 1
            M[i, j] = 0.25 * (f(sym(ei + ej)) - f(sym(ei - ej)))
    return M
M1 = massform(lambda h: np.sum(np.diag(h) ** 2))
M2 = massform(lambda h: np.sum(h ** 2) - np.sum(np.diag(h) ** 2))
M3 = massform(lambda h: np.trace(h) ** 2)
Mnamed = np.array([M.ravel() for M in (M1, M2, M3)])
print("[mass] named M1=sum h_mm^2, M2=sum_{m!=n} h_mn^2, M3=(tr h)^2: rank", rank(Mnamed)[0],
      " in invariant span:", rank(np.vstack([P, Mnamed]))[0] == rm)
# TT restriction of mass forms (random q, TT basis)
def TTbasis(q):
    # symmetric h with q.h = 0, tr h = 0 : solve linear constraints
    C = []
    for nu in range(D):
        row = np.zeros(10)
        for k, (m, n) in enumerate(pairs):
            if m == n:
                if m == nu: row[k] += q[m]
            else:
                if n == nu: row[k] += q[m]
                if m == nu: row[k] += q[n]
        C.append(row)
    tr = np.zeros(10)
    for k, (m, n) in enumerate(pairs):
        if m == n: tr[k] = 1
    C.append(tr)
    C = np.array(C)
    _, s, Vt = np.linalg.svd(C)
    return Vt[np.sum(s > 1e-12):]          # 5 x 10
def restricted_rank(forms_of_q, nq=6):
    rows = []
    for f in forms_of_q:
        r = []
        for t in range(nq):
            q = rng.normal(size=D) if t > 1 else (np.array([1., 0, 0, 0]) if t == 0 else np.array([1., 1, 1, 1]))
            B = TTbasis(q)
            r.append((B @ f(q) @ B.T).ravel())
        rows.append(np.concatenate(r))
    return rank(np.array(rows))[0]
rng = np.random.default_rng(7)
print("[mass] rank of mass forms restricted to TT modes:", restricted_rank([lambda q, M=M: M for M in (M1, M2, M3)]))
# gauge variation of mass forms: M(h, s xi + xi s) for random s, xi
def gauge_img_mass(M):
    out = []
    for t in range(5):
        s = rng.normal(size=D); xi = rng.normal(size=D); h = rng.normal(size=10)
        dh = unsym(np.outer(s, xi) + np.outer(xi, s))
        out.append(h @ M @ dh)
    return np.array(out)
Gm = np.array([gauge_img_mass(M) for M in (M1, M2, M3)])
print("[mass] gauge map rank on mass forms:", rank(Gm.T)[0], "(3 => no mass combination is gauge invariant)")
# ---- two-derivative forms: K[A,B,a,b] h_A h_B s_a s_b ----
# represent as quadratic form in h whose entries are quadratic forms in s: tensor T (10,10,4,4) sym in (A,B),(a,b)
def rep_kin(T, R):
    g = rep10(R)
    return np.einsum('Ai,Bj,ak,bl,ABab->ijkl', g, g, R, R, T, optimize=True)
def reynolds_kin(T):
    return sum(rep_kin(T, R) for R in G) / 384
# basis of sym tensors
idx = []
for A in range(10):
    for B in range(A, 10):
        for a in range(4):
            for b in range(a, 4):
                idx.append((A, B, a, b))
def Ebasis(A, B, a, b):
    T = np.zeros((10, 10, 4, 4))
    for (x, y) in {(A, B), (B, A)}:
        for (u, v) in {(a, b), (b, a)}:
            T[x, y, u, v] = 1
    return T
# Reynolds via random projections (fast): project 40 random tensors, rank of image
imgs = []
for t in range(25):
    T = sum(rng.normal() * Ebasis(*rng.choice(10, 2), *rng.choice(4, 2)) for _ in range(60))
    imgs.append(reynolds_kin(T).ravel())
rk, gk = rank(np.array(imgs))
print(f"[kin] dim of W(B4)-invariant two-derivative forms = {rk}  (sv gap {gk[0]:.2e} / {gk[1]:.2e})")
def kinform(f):
    """f(h, s) quadratic in h and in s -> tensor"""
    T = np.zeros((10, 10, 4, 4))
    E10 = np.eye(10); E4 = np.eye(4)
    for A in range(10):
        for B in range(10):
            for a in range(4):
                for b in range(4):
                    hp = sym(E10[A] + E10[B]); hm = sym(E10[A] - E10[B])
                    sp = E4[a] + E4[b]; sm = E4[a] - E4[b]
                    T[A, B, a, b] = 0.0625 * (f(hp, sp) - f(hp, sm) - f(hm, sp) + f(hm, sm))
    return T
names = ["F1", "F2", "F3", "F4", "A1", "A2", "A3", "A4", "A6"]
fdefs = {
    "F1": lambda h, s: (s @ s) * np.sum(h * h),
    "F2": lambda h, s: (h @ s) @ (h @ s),
    "F3": lambda h, s: (s @ h @ s) * np.trace(h),
    "F4": lambda h, s: (s @ s) * np.trace(h) ** 2,
    "A1": lambda h, s: np.sum(s ** 2 * np.diag(h) ** 2),
    "A2": lambda h, s: np.sum(s ** 2 * np.sum(h ** 2, axis=1)),
    "A3": lambda h, s: np.sum(s ** 2 * np.diag(h)) * np.trace(h),
    "A4": lambda h, s: np.sum(s * np.diag(h) * (h @ s)),
    "A6": lambda h, s: sum(s[m] ** 2 * h[n, n] ** 2 for m in range(4) for n in range(4) if m != n),
}
KT = {n: kinform(fdefs[n]) for n in names}
Kmat = np.array([KT[n].ravel() for n in names])
print("[kin] named 9 forms: rank", rank(Kmat)[0], "; invariant:",
      max(np.abs(reynolds_kin(KT[n]) - KT[n]).max() for n in names) < 1e-12,
      "; span = invariant space:", rank(np.vstack([np.array(imgs), Kmat]))[0] == rk)
# O(4)-invariant subspace: invariance under random rotations
def o4_violation_matrix():
    rows = []
    for t in range(3):
        A = rng.normal(size=(4, 4)); Q, _ = np.linalg.qr(A)
        rows.append(np.array([(rep_kin(KT[n], Q) - KT[n]).ravel() for n in names]))
    return np.hstack(rows)          # 9 x big
V = o4_violation_matrix()
_, s, Vt = np.linalg.svd(V)
ro = 9 - int(np.sum(s > 1e-9 * s[0]))
print(f"[kin] O(4)-invariant subspace dim = {ro}")
# gauge map: K(h, s xi + xi s; s) -> cubic in s ; evaluate at random (h, xi, s)
def gauge_img(T, samples):
    out = []
    for (h, xi, s) in samples:
        dh = unsym(np.outer(s, xi) + np.outer(xi, s))
        out.append(np.einsum('A,B,a,b,ABab->', h, dh, s, s, T, optimize=True))
    return np.array(out)
samples = [(rng.normal(size=10), rng.normal(size=4), rng.normal(size=4)) for _ in range(200)]
Gk = np.array([gauge_img(KT[n], samples) for n in names]).T     # 200 x 9
rg, gg = rank(Gk)
_, s, Vt = np.linalg.svd(Gk)
null = Vt[-1] / Vt[-1][0]
print(f"[kin] gauge map rank = {rg} (gap {gg[0]:.2e}/{gg[1]:.2e}); gauge-invariant forms = {9 - rg}")
print("[kin] null vector (coeffs of F1..F4,A1,A2,A3,A4,A6) normalised to F1:", null)
# split ranks: images of O(4) block (F1..F4) and anisotropic block (A*)
print("[kin] gauge-image rank: O(4) block", rank(Gk[:, :4])[0], ", anisotropic block", rank(Gk[:, 4:])[0])
# TT restriction
ttr = restricted_rank([lambda q, n=n: np.einsum('ABab,a,b->AB', KT[n], q, q) for n in names], nq=8)
ttr_o4 = restricted_rank([lambda q, n=n: np.einsum('ABab,a,b->AB', KT[n], q, q) for n in names[:4]], nq=8)
print(f"[kin] TT-restricted rank: all 9 -> {ttr}; O(4) block -> {ttr_o4}")
# full count summary of non-gauge-invariant structures
print(f"[count] W(B4) quadratic forms: masses {rm} (TT-visible {restricted_rank([lambda q, M=M: M for M in (M1, M2, M3)])}),"
      f" two-derivative {rk} (O(4) {ro}, gauge-invariant {9 - rg});"
      f" non-gauge-invariant: {rm} mass + {rg} kinetic = {rm + rg}; of the kinetic: {ro - (9 - rg)} O(4) + {9 - ro} anisotropic")
np.savez("forms_data.npz", M=np.array([M1, M2, M3]), K=np.array([KT[n] for n in names]))
