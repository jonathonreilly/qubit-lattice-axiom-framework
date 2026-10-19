"""Independent numerical tests of Lemma V / Cor C / Prop S4 (no use of the author's code).
Magnon basis: |1> = magnon (sigma^z = +1 on |1> here; conventions irrelevant to diagonality)."""
import itertools, numpy as np, scipy.optimize as so, scipy.linalg as sl
from rv_common import check, total
rng = np.random.default_rng(2026)
def embed(h, pos, n):
    k = len(pos); T = h.reshape([2]*(2*k))
    rest = [i for i in range(n) if i not in pos]
    full = np.tensordot(T, np.eye(2**len(rest)).reshape([2]*(2*len(rest))), axes=0) if rest else T
    # current axes: out(pos), in(pos), out(rest), in(rest)
    order_out = list(pos) + rest
    perm = [order_out.index(i) for i in range(n)]
    nk, nr = k, len(rest)
    axes = [ (perm[i] if perm[i] < nk else 2*nk + (perm[i]-nk)) for i in range(n)]
    axes += [ (nk + perm[i] if perm[i] < nk else 2*nk + nr + (perm[i]-nk)) for i in range(n)]
    return np.transpose(full, axes).reshape(2**n, 2**n)
def charge(k): return np.array([bin(i).count("1") for i in range(2**k)])
def u1_basis(k, diag_only=False, offdiag_only=False, u1=True):
    q = charge(k); B = []
    for i in range(2**k):
        for j in range(i, 2**k):
            if u1 and q[i] != q[j]: continue
            if i == j:
                if offdiag_only: continue
                E = np.zeros((2**k,)*2, complex); E[i, i] = 1; B.append(E)
            else:
                if diag_only: continue
                E = np.zeros((2**k,)*2, complex); E[i, j] = E[j, i] = 1; B.append(E)
                E = np.zeros((2**k,)*2, complex); E[i, j] = 1j; E[j, i] = -1j; B.append(E)
    return B
def regions(S, ts):
    out = []
    for t in ts:
        sites = sorted(set(S) | {tuple(np.add(p, t)) for p in S})
        idx = {p: i for i, p in enumerate(sites)}
        out.append(([idx[p] for p in S], [idx[tuple(np.add(p, t))] for p in S], len(sites)))
    return out
def diffs(S): return sorted({tuple(np.subtract(a, b)) for a in S for b in S if a != b})
def comm_norm(h, regs):
    return sum(np.linalg.norm(embed(h, p0, n) @ embed(h, p1, n) - embed(h, p1, n) @ embed(h, p0, n))**2 for p0, p1, n in regs)
# (A) commutants by nullspace
sp_ = np.array([[0, 1], [0, 0]]); sm = sp_.T; sz = np.diag([1, -1])
def commutant_dim(ops):
    M = np.vstack([np.kron(o, np.eye(2)) - np.kron(np.eye(2), o.T) for o in ops]); return 4 - np.linalg.matrix_rank(M)
check("(A) dim comm(sz)=2, comm(s+)=2, comm(s+,s-)=1", (commutant_dim([sz]), commutant_dim([sp_]), commutant_dim([sp_, sm])) == (2, 2, 1))
# (B) local operator span of a random U(1) operator is charge graded
k = 3; h = sum(rng.normal() * E for E in u1_basis(k))
T = h.reshape(2, 4, 2, 4).transpose(0, 2, 1, 3).reshape(4, 16)   # rows: site-0 operator entries
U, s, Vh = np.linalg.svd(T); V0 = U[:, s > 1e-10]                 # span{P_i} at site 0 (vectorised)
P = V0 @ V0.conj().T
graded = all(np.linalg.norm(P @ (v * m) - v * m) < 1e-9 for v in V0.T for m in [np.array([1, 0, 0, 1]), np.array([0, 1, 0, 0]), np.array([0, 0, 1, 0])])
check("(B) single-site Schmidt span of a U(1) operator is closed under charge projection", graded)
# (C) random U(1) 2-site and 3-site unitaries: generic ones do not commute with translates; diagonal ones do
def rand_u1_unitary(k, diag=False):
    H = sum(rng.normal() * E for E in u1_basis(k, diag_only=diag)); return sl.expm(1j * H)
for S, name in [([(0,0,0),(1,0,0)], "bond e1"), ([(0,0,0),(1,1,0)], "bond face"), ([(0,0,0),(1,0,0),(2,0,0)], "collinear triple"),
                ([(0,0,0),(1,0,0),(0,1,0)], "L-triple"), ([(0,0,0),(1,0,0),(1,1,1)], "skew triple")]:
    regs = regions(S, diffs(S)); k = len(S)
    gen = [comm_norm(rand_u1_unitary(k), regs) for _ in range(200)]
    dg = [comm_norm(rand_u1_unitary(k, True), regs) for _ in range(50)]
    check(f"(C) {name}: 200 random U(1) gates all fail translate-commutation, diagonal ones commute", min(gen) > 1e-6 and max(dg) < 1e-20, f"min generic={min(gen):.3g}")
# (D) minimisation: residual = sum_t [h,h_t] entries, h = D + X, constraint ||X|| = 1 on the off-diagonal (hop) part.
# Levenberg-Marquardt over (D, X) jointly; min of ||residual||^2 reported (0 iff a commuting non-diagonal family exists).
def make_res(S, u1=True):
    k = len(S); regs = regions(S, diffs(S))
    Db = u1_basis(k, diag_only=True); Xb = u1_basis(k, offdiag_only=True, u1=u1)
    def res(z):
        d, x = z[:len(Db)], z[len(Db):]
        h = sum(c * E for c, E in zip(d, Db)) + sum(c * E for c, E in zip(x, Xb)); out = []
        for p0, p1, n in regs:
            H0, H1 = embed(h, p0, n), embed(h, p1, n); C = (H0 @ H1 - H1 @ H0).ravel(); out += [C.real, C.imag]
        out.append(np.array([10.0 * (x @ x - 1.0)])); return np.concatenate(out)
    return res, len(Db) + len(Xb), len(Db)
def minimise(S, u1=True, restarts=4):
    res, m, nd = make_res(S, u1); best = np.inf
    for _ in range(restarts):
        z0 = rng.normal(size=m); z0[nd:] /= np.linalg.norm(z0[nd:])
        r = so.least_squares(res, z0, method="lm", xtol=1e-14, ftol=1e-14, max_nfev=4000)
        best = min(best, float(np.sum(r.fun**2)))
    return best
mc = minimise([(0,0,0),(1,0,0),(2,0,0)], u1=False, restarts=4)
check("(D0) positive control: without U(1), collinear triple admits a non-diagonal commuting family (ZXZ-type), min G ~ 0", mc < 1e-8, f"{mc:.2e}")
for S, name in [([(0,0,0),(1,0,0)], "bond"), ([(0,0,0),(1,0,0),(2,0,0)], "collinear triple"), ([(0,0,0),(1,0,0),(0,1,0)], "L-triple")]:
    m = minimise(S, restarts=4 if len(S) < 4 else 3)
    check(f"(D) {name}: U(1) Hermitian h with unit hop part never has commuting translates (min G bounded away from 0)", m > 1e-3, f"min G = {m:.4f}")
# (E) sanity of 'unforced' reality: 3x3-square-type gate with ZXZ-like non-U(1) structure exists (not U(1)); skipped
print('(4-segment full-ansatz test is in rv1b_seg4_full_ansatz.py)')
total()
