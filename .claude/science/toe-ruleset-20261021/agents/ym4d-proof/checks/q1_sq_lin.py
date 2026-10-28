"""q1: linear deviation square function (SQ-lin) of SQ.md, and its 1D multilevel Bessel lemmas.
Criteria: checks/q1_criteria.md (written before this script). Output: stdout (kept under 6000 chars)."""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import sys, time, itertools, resource
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh, LinearOperator

AUDIT_TIMEOUT_SEC = 1800
t0 = time.time()
RES = {}


def T(n, u):
    u = np.asarray(u)
    out = np.minimum(u + 1, 2 * n - 1 - u)
    out[(u < 0) | (u > 2 * n - 2)] = 0
    return out


# ---------------- Part A: 1D frames ----------------
def frame_rows(fam, L, J):
    h = (L - 1) // 2
    N0 = 2 * L ** J
    rows, cols, vals = [], [], []
    r = 0
    for j in range(J):
        n = L ** j
        Nj = N0 // n
        if fam == "box":
            for X in range(Nj - 1):
                idx = np.arange(n * X, n * (X + 2))
                v = np.r_[-np.ones(n), np.ones(n)] / np.sqrt(n)
                rows += [r] * len(idx); cols += list(idx); vals += list(v); r += 1
        elif fam == "tri":
            npos = Nj - 1
            for X in range(npos - 1):
                u = np.arange(n * X, n * X + 3 * n - 1)
                v = (T(n, u - n * (X + 1)) - T(n, u - n * X)) / n ** 1.5
                rows += [r] * len(u); cols += list(u); vals += list(v); r += 1
        elif fam == "edge":
            npos = Nj - 1
            Nj1 = Nj // L
            pos = list(range(h)) + list(range(L * (Nj1 - 1) + h, L * Nj1 - 1))
            for s in pos:
                u = np.arange(n * s, n * s + 2 * n - 1)
                v = T(n, u - n * s) / n ** 1.5
                rows += [r] * len(u); cols += list(u); vals += list(v); r += 1
    ncol = N0 if fam == "box" else N0 - 1
    Phi = sp.csr_matrix((vals, (rows, cols)), shape=(r, ncol))
    return Phi


def lam_max(Phi):
    n = Phi.shape[1]
    if n <= 2500:  # [crash fix after the first official run: ARPACK non-convergence] dense for small sizes
        G = (Phi.T @ Phi).toarray()
        return float(np.linalg.eigvalsh(G)[-1])
    op = LinearOperator((n, n), matvec=lambda x: Phi.T @ (Phi @ x), dtype=float)
    w = eigsh(op, k=1, which="LA", tol=1e-10, ncv=96, return_eigenvectors=False, maxiter=200000)
    return float(w[0])


def bounds(L):
    h = (L - 1) // 2
    bM = 4 + 8 / (np.sqrt(L) - 1)
    bA = 10 + 6 / (np.sqrt(L) - 1) + 14 / (L ** 1.5 - 1)
    bE = min(h, 3) + (h * (h + 1) / 2 + h) / (L ** 1.5 - 1)
    return {"box": bM, "tri": bA, "edge": 2 * bE}


A1 = True; A2 = True
print("== Part A: 1D multilevel Bessel constants (largest frame eigenvalue) ==")
for L, Js in ((3, range(1, 10)), (5, range(1, 6))):
    bd = bounds(L)
    for fam in ("box", "tri", "edge"):
        lams = {}
        for J in Js:
            lams[J] = lam_max(frame_rows(fam, L, J))
            if lams[J] > bd[fam]:
                A1 = False
        if L == 3 and not (lams[9] <= 1.05 * lams[6] + 1e-6):
            A2 = False
        print(f"L={L} {fam:4s} bound {bd[fam]:6.3f} | " + " ".join(f"{lams[J]:.4f}" for J in Js))
print(f"A1 (all <= proven bounds): {'PASS' if A1 else 'FAIL'};  A2 (lam(9) <= 1.05 lam(6), L=3): {'PASS' if A2 else 'FAIL'}")

# ---------------- Part B: 4D cone boxes ----------------
L = 3; h = 1
SHAPE = (2, 2, 1, 1)
COMPS = list(itertools.combinations(range(4), 2))


def Ncount(k, j, a):
    return SHAPE[a] * L ** (k - j)


def mat_A(Nc, Nf):  # in-plane, plaquette positions: rows Nc-1, cols Nf-1
    M = np.zeros((Nc - 1, Nf - 1))
    for X in range(Nc - 1):
        s = np.arange(Nf - 1)
        M[X] = T(L, s - L * X) / L
    return M


def mat_M(Nc, Nf):
    M = np.zeros((Nc, Nf))
    for X in range(Nc):
        M[X, L * X:L * X + L] = 1.0 / L
    return M


def mat_J0(Nc, Nf):
    M = np.zeros((Nf - 1, Nc - 1))
    for X in range(Nc - 1):
        M[L * X + h:L * X + h + L, X] = 1.0 / L
    return M


def mat_J1(Nc, Nf):
    M = np.zeros((Nf, Nc))
    for x in range(Nf):
        if x < h:
            M[x, 0] = 1.0
        elif x > L * (Nc - 1) + h:
            M[x, Nc - 1] = 1.0
        else:
            X0 = (x - h) // L
            lam = (x - h - L * X0) / L
            if X0 >= Nc - 1:
                M[x, Nc - 1] = 1.0
            else:
                M[x, X0] += 1 - lam; M[x, X0 + 1] += lam
    return M


def tens(mats, F):
    for a, Mx in enumerate(mats):
        F = np.moveaxis(np.tensordot(Mx, F, axes=([1], [a])), 0, a)
    return F


def build(k):
    """per component, per level j (0..k-1): Q maps (j -> j+1) and I maps (j+1 -> j)."""
    out = {}
    for (al, be) in COMPS:
        Qs, Is = [], []
        for j in range(k):
            qm, im = [], []
            for a in range(4):
                Nf, Nc = Ncount(k, j, a), Ncount(k, j + 1, a)
                if a in (al, be):
                    qm.append(mat_A(Nc, Nf)); im.append(mat_J0(Nc, Nf))
                else:
                    qm.append(mat_M(Nc, Nf)); im.append(mat_J1(Nc, Nf))
            Qs.append(qm); Is.append(im)
        out[(al, be)] = (Qs, Is)
    return out


def shape_plaq(k, j, comp):
    return tuple(Ncount(k, j, a) - (1 if a in comp else 0) for a in range(4))


def shape_link(k, j, mu):
    return tuple(Ncount(k, j, a) - (1 if a == mu else 0) for a in range(4))


def curl(Bl, comp):
    al, be = comp
    Ba, Bb = Bl[al], Bl[be]
    sa = [slice(None)] * 4; sb = [slice(None)] * 4
    t1 = np.take(Ba, range(Ba.shape[be] - 1), axis=be) - np.take(Ba, range(1, Ba.shape[be]), axis=be)
    t2 = np.take(Bb, range(1, Bb.shape[al]), axis=al) - np.take(Bb, range(Bb.shape[al] - 1), axis=al)
    return t1 + t2


def chain(k, ops, F0, rs):
    """F0: dict comp->array; rs: list over j of link dicts at level j+1 (or None). Returns D list, F list per comp."""
    Ds = {}; Fs = {}
    for comp in COMPS:
        Qs, Is = ops[comp]
        F = F0[comp]; Fl = [F]; Dl = []
        for j in range(k - 1):
            Fn = tens(Qs[j], F)
            if rs is not None:
                Fn = Fn - curl(rs[j], comp)
            Dl.append(F - tens(Is[j], Fn))
            F = Fn; Fl.append(F)
        Ds[comp] = Dl; Fs[comp] = Fl
    return Ds, Fs


def nrm2(x):
    return float(np.sum(x * x))


B1 = True; B2 = True; B3 = True
summary = {}
print("== Part B: 4D cone boxes (L=3) ==")
for k in (2, 3):
    ops = build(k)
    # B3 identities
    if k == 2:
        rng = np.random.default_rng(0)
        B0 = {mu: rng.standard_normal(shape_link(k, 0, mu)) for mu in range(4)}
        Qstr = {}
        for mu in range(4):
            mats = []
            for a in range(4):
                Nf, Nc = Ncount(k, 0, a), Ncount(k, 1, a)
                mats.append(mat_A(Nc, Nf) if a == mu else mat_M(Nc, Nf))
            Qstr[mu] = tens(mats, B0[mu])
        errb = 0.0
        for comp in COMPS:
            lhs = tens(ops[comp][0][0], curl(B0, comp)); rhs = curl(Qstr, comp)
            errb = max(errb, np.max(np.abs(lhs - rhs)) / np.max(np.abs(rhs)))
    erra = 0.0; errc = 0.0
    for comp in COMPS:
        for j in range(k - 1):
            c = np.ones(shape_plaq(k, j, comp))
            q = tens(ops[comp][0][j], c)
            erra = max(erra, np.max(np.abs(q - L * L)) / (L * L))
            p = tens(ops[comp][1][j], q)
            sl = [slice(None)] * 4
            for a in comp:
                sl[a] = slice(h, c.shape[a] - h)
            errc = max(errc, np.max(np.abs(p[tuple(sl)] - 1.0)))
    ok3 = erra < 1e-12 and errc < 1e-12 and (k != 2 or errb < 1e-10)
    B3 = B3 and ok3
    print(f"k={k} B3: const err {erra:.1e}, interior P-repro err {errc:.1e}" + (f", dQstr err {errb:.1e}" if k == 2 else ""))
    def fams():
        for seed in (1, 2):
            rng = np.random.default_rng(seed)
            yield ("rand", seed, {c: rng.standard_normal(shape_plaq(k, 0, c)) for c in COMPS}, None)
        for seed in (3, 4, 5, 6):
            rng = np.random.default_rng(seed)
            B0 = {mu: rng.standard_normal(shape_link(k, 0, mu)) for mu in range(4)}
            F0 = {c: curl(B0, c) for c in COMPS}
            del B0
            rs = None
            if seed >= 5:
                rs = [{mu: rng.standard_normal(shape_link(k, j + 1, mu)) for mu in range(4)} for j in range(k - 1)]
            yield ("exact" if seed < 5 else "res", seed, F0, rs)
        B0 = {}
        for mu in range(4):
            sh = shape_link(k, 0, mu); nu = (mu + 1) % 4
            x = np.arange(sh[nu]) + 0.5
            prof = np.cos(np.pi * x / Ncount(k, 0, nu))
            shp = [1] * 4; shp[nu] = sh[nu]
            B0[mu] = np.broadcast_to(prof.reshape(shp), sh).copy()
        yield ("smooth", 0, {c: curl(B0, c) for c in COMPS}, None)
    for (name, seed, F0, rs) in fams():
        Ds, Fs = chain(k, ops, F0, rs)
        num = sum(nrm2(d) for c in COMPS for d in Ds[c])
        den = sum(nrm2(F0[c]) for c in COMPS)
        rden = 0.0 if rs is None else sum(nrm2(r[mu]) for r in rs for mu in range(4))
        RD = num / (den + rden)
        RF = sum(nrm2(Fs[c][j]) for c in COMPS for j in range(k - 1)) / den
        if RD > 34200:
            B1 = False
        summary[(k, name, seed)] = (RD, RF)
    # adversarial per component
    advs = []
    for comp in COMPS:
        Qs, Is = ops[comp]
        sh0 = shape_plaq(k, 0, comp); n0 = int(np.prod(sh0))
        QT = [[m.T for m in q] for q in Qs]; IT = [[m.T for m in q] for q in Is]

        def mv(x):
            F = x.reshape(sh0); Fl = [F]
            for j in range(k - 1):
                Fl.append(tens(Qs[j], Fl[-1]))
            out = np.zeros(sh0)
            for j in range(k - 1):
                D = Fl[j] - tens(Is[j], Fl[j + 1])
                # adjoint of D_j = (1 - I_j Q_j) Q_{j-1}..Q_0
                y = D - tens(QT[j], tens(IT[j], D))
                for i in range(j - 1, -1, -1):
                    y = tens(QT[i], y)
                out += y
            return out.ravel()
        op = LinearOperator((n0, n0), matvec=mv, dtype=float)
        lam = float(eigsh(op, k=1, which="LA", tol=1e-6, return_eigenvectors=False, maxiter=5000)[0])
        advs.append(lam)
        if lam > 11400:
            B1 = False
    summary[(k, "adv", 0)] = (max(advs), min(advs))
    print(f"k={k} B-adv eigenvalues per component: " + " ".join(f"{a:.4f}" for a in advs))

print("family  seed |  R_D(k=2)  R_D(k=3) |  R_F(k=2)  R_F(k=3)")
for (name, seed) in [("rand", 1), ("rand", 2), ("exact", 3), ("exact", 4), ("res", 5), ("res", 6), ("smooth", 0)]:
    a, b = summary[(2, name, seed)], summary[(3, name, seed)]
    print(f"{name:6s} {seed:4d} | {a[0]:9.4f} {b[0]:9.4f} | {a[1]:9.4f} {b[1]:9.4f}")
s2, s3 = summary[(2, "smooth", 0)], summary[(3, "smooth", 0)]
B2 = (s3[1] / s2[1] >= 1.4) and (s3[0] <= 1.5 * s2[0] + 0.05)
print(f"B2 smooth: R_F ratio {s3[1] / s2[1]:.3f} (>=1.4), R_D {s2[0]:.5f} -> {s3[0]:.5f}")
print(f"B1: {'PASS' if B1 else 'FAIL'}  B2: {'PASS' if B2 else 'FAIL'}  B3: {'PASS' if B3 else 'FAIL'}")
ok = A1 and A2 and B1 and B2 and B3
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6
print(f"OVERALL: {'PASS' if ok else 'FAIL'}   (wall {time.time() - t0:.1f} s, peak RSS {rss:.0f} MB)")
