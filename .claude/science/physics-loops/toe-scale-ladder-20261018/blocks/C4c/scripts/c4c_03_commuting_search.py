"""C4c-03: numerical search for NON-diagonal U(1)-conserving Hermitian h on a NON-convex support S
whose translates (and, optionally, point-group images) all commute.  Evidence only (local
optimisation with random restarts); a positive hit would be checked exactly.

usage: python3 c4c_03_commuting_search.py <case> <restarts> <seed>
cases: seg4  : S = {0,1,2,3} e1 (smallest support with two non-vertex sites), translates only
       seg4O : same plus its images along e2, e3 (the O-orbit of a segment; all must commute)
       tee5  : S = {-e1,0,e1,2e1, e2}  (non-convex, 3D-embedded), translates only
"""
import sys, itertools
import numpy as np
from scipy.optimize import least_squares
from c4c_common import check, total


def u1_basis(n):
    confs = list(itertools.product([0, 1], repeat=n))
    ci = lambda c: int(''.join(map(str, c)), 2)
    B, diag = [], []
    for a in confs:
        for b in confs:
            if sum(a) != sum(b):
                continue
            i, j = ci(a), ci(b)
            if i == j:
                M = np.zeros((2 ** n,) * 2, complex); M[i, i] = 1; B.append(M); diag.append(True)
            elif i < j:
                M = np.zeros((2 ** n,) * 2, complex); M[i, j] = 1; M[j, i] = 1; B.append(M); diag.append(False)
                M = np.zeros((2 ** n,) * 2, complex); M[i, j] = 1j; M[j, i] = -1j; B.append(M); diag.append(False)
    return np.array(B), np.array(diag)


def embed(mat, pos, N):
    n = len(pos); rest = [k for k in range(N) if k not in pos]
    full = np.kron(mat, np.eye(2 ** (N - n))).reshape([2] * (2 * N))
    order = pos + rest
    perm = [0] * N
    for k, p in enumerate(order):
        perm[p] = k
    full = full.transpose(perm + [N + p for p in perm])
    return full.reshape(2 ** N, 2 ** N)


case = sys.argv[1]; restarts = int(sys.argv[2]); seed = int(sys.argv[3])
e = np.eye(3, dtype=int)
if case.startswith('seg4'):
    S = [tuple(k * e[0]) for k in range(4)]
elif case == 'tee5':
    S = [tuple(-e[0]), (0, 0, 0), tuple(e[0]), tuple(2 * e[0]), tuple(e[1])]
S = [tuple(int(v) for v in s) for s in S]
n = len(S)
# family members: (map site of S -> lattice site). translates of S, and for seg4O rotated copies.
maps = [lambda s: s]
if case == 'seg4O':
    P1 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])  # C3: e1->e2->e3
    maps = [lambda s: s, lambda s: tuple(P1 @ s), lambda s: tuple(P1 @ P1 @ s)]
B, isd = u1_basis(n); P = len(B)
jobs = []
for mi, m0 in enumerate(maps[:1]):          # member 0 against every overlapping other member
    base = [tuple(int(v) for v in m0(np.array(s))) for s in S]
    for mj, m1 in enumerate(maps):
        img = [tuple(int(v) for v in m1(np.array(s))) for s in S]
        for t in itertools.product(range(-4, 5), repeat=3):
            other = [tuple(np.add(s, t)) for s in img]
            if mj == 0 and (t <= (0, 0, 0)):
                continue   # t and -t give equivalent conditions for translates
            if not set(base) & set(other):
                continue
            if set(base) == set(other) and mj != 0:
                pass
            reg = sorted(set(base) | set(other)); N = len(reg)
            pa = [reg.index(s) for s in base]; pb = [reg.index(s) for s in other]
            jobs.append((np.array([embed(b, pa, N) for b in B]), np.array([embed(b, pb, N) for b in B])))
print(f"case={case} |S|={n} params={P} overlapping members={len(jobs)}", flush=True)


def res(x):
    out = []
    for A, Bt in jobs:
        h = np.tensordot(x, A, 1); g = np.tensordot(x, Bt, 1)
        c = h @ g - g @ h
        out += [c.real.ravel(), c.imag.ravel()]
    off = x[~isd]
    out.append(np.array([(off @ off - 1.0) * 10]))
    return np.concatenate(out)


def jac(x):
    cols = []
    blocks = []
    for A, Bt in jobs:
        h = np.tensordot(x, A, 1); g = np.tensordot(x, Bt, 1)
        d = np.matmul(A, g) - np.matmul(g, A) + np.matmul(h, Bt) - np.matmul(Bt, h)
        d = d.reshape(P, -1)
        blocks += [d.real.T, d.imag.T]
    row = np.zeros((1, P)); row[0, ~isd] = 20 * x[~isd]
    blocks.append(row)
    return np.vstack(blocks)


rng = np.random.default_rng(seed)
vals = []
for trial in range(restarts):
    x0 = rng.normal(size=P); x0[~isd] /= np.linalg.norm(x0[~isd])
    r = least_squares(res, x0, jac=jac, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=400)
    f = np.linalg.norm(r.fun[:-1]); vals.append(f)
    print(f"  restart {trial}: residual ||commutators|| = {f:.3e}  (||offdiag||={np.linalg.norm(r.x[~isd]):.3f})", flush=True)
mn = min(vals)
print(f"min residual over {restarts} restarts: {mn:.3e}")
check(f"{case}: no non-diagonal commuting U(1) family found (min residual > 1e-6; evidence only)",
      mn > 1e-6, f"min={mn:.3e}")
total()
