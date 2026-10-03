"""t6: many-body (1- and 2-excitation sectors) checks on a 4x4x4 torus, plain partial swaps
G = exp(-i th SWAP) (normalized so |00>,|11> -> 1; one-excitation block e^{i th}(c - i s sigma_x)).
Layers applied as sparse matrices; operator identities tested on random vectors."""
import numpy as np, itertools
import scipy.sparse as sp

L = 4
pi = np.pi
th = 0.6
rng = np.random.default_rng(7)

def sid(x, y, z):
    return (x % L) + L * (y % L) + L * L * (z % L)
coords = [(x, y, z) for z in range(L) for y in range(L) for x in range(L)]

def bonds(axis, par):
    out = []
    for (x, y, z) in coords:
        s = [x, y, z]
        if s[axis] % 2 == par:
            t = list(s); t[axis] += 1
            out.append((sid(*s), sid(*t)))
    return out

def sector(n):
    basis = list(itertools.combinations(range(L ** 3), n))
    return basis, {b: i for i, b in enumerate(basis)}

def layer_matrix(axis, par, n, signed=False):
    basis, index = sector(n)
    c, s = np.cos(th), np.sin(th)
    partner = {}
    for (a, b) in bonds(axis, par):
        e = 1.0
        if signed:
            x, y, z = coords[a]
            e = 1.0 if axis == 0 else ((-1.0) ** x if axis == 1 else (-1.0) ** (x + y))
        partner[a] = (b, e); partner[b] = (a, e)
    rows, cols, vals = [], [], []
    for j, conf in enumerate(basis):
        occ = set(conf)
        # each particle: if its partner is occupied -> bond |11>, phase 1; else mix
        opts = []
        for p in conf:
            q, e = partner[p]
            if q in occ:
                opts.append([(p, 1.0)])
            else:
                opts.append([(p, np.exp(1j * th) * c), (q, np.exp(1j * th) * (-1j) * e * s)])
        for choice in itertools.product(*opts):
            new = tuple(sorted(site for site, _ in choice))
            if len(set(new)) < n:
                continue
            amp = np.prod([a for _, a in choice])
            rows.append(index[new]); cols.append(j); vals.append(amp)
    M = sp.csr_matrix((vals, (rows, cols)), shape=(len(basis), len(basis)))
    return M

def perm_matrix(f, n):
    basis, index = sector(n)
    rows = [index[tuple(sorted(f(p) for p in conf))] for conf in basis]
    return sp.csr_matrix((np.ones(len(basis)), (rows, list(range(len(basis))))), shape=(len(basis),) * 2)

def rot_site(M, shift=(0, 0, 0)):
    # rotation about the cube centre (1/2,1/2,1/2), then a translation
    c = np.array([0.5, 0.5, 0.5])
    def f(i):
        v = np.array(coords[i], float)
        w = np.rint(M @ (v - c) + c).astype(int) + np.array(shift)
        return sid(*w)
    return f

C3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])          # x->y->z->x
C4z = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])

for n in (1, 2):
    Lm = {(a, p): layer_matrix(a, p, n) for a in range(3) for p in (0, 1)}
    dim = Lm[(0, 0)].shape[0]
    V = rng.normal(size=(dim, 4)) + 1j * rng.normal(size=(dim, 4))
    def apply(seq, v):              # seq: list of (axis,par), first acts first
        for k in seq:
            v = Lm[k] @ v
        return v
    X = [(0, 0), (0, 1)]; Y = [(1, 0), (1, 1)]; Z = [(2, 0), (2, 1)]
    U = X + Y + Z
    nrm = np.linalg.norm(V)
    comm = np.linalg.norm(apply(X + Y, V) - apply(Y + X, V)) / nrm
    # unitarity / norm preservation
    unit = abs(np.linalg.norm(apply(U, V)) - nrm) / nrm
    # C3 about the cube centre: P U P^-1 == X^-1-conjugate?  P U P^-1 = (images) ; compare with cyclic shift
    P3 = perm_matrix(rot_site(C3), n)
    lhs = P3 @ apply(U, P3.T @ V)
    rhs_shift = apply(Y + Z + X, V)                  # cyclic shift by one axis block
    c3 = np.linalg.norm(lhs - rhs_shift) / nrm
    # C4z about the cube centre
    P4 = perm_matrix(rot_site(C4z), n)
    lhs4 = P4 @ apply(U, P4.T @ V)
    flat = [k for k in U]
    shifts = [flat[r:] + flat[:r] for r in range(6)]
    c4 = min(np.linalg.norm(lhs4 - apply(sh, V)) / nrm for sh in shifts)
    # antiunitary relation: C4 image == Y-block-conjugate of T111 U^T T111^-1, with U^T = reversed layer order
    T111 = perm_matrix(lambda i: sid(*(np.array(coords[i]) + 1)), n)
    rev = list(reversed(flat))
    def UT_trans(v):     # T111 U^T T111^-1 v
        return T111 @ apply(rev, T111.T @ v)
    # C4z maps U = X,Y,Z (x first) to the word Y,X,Z ; check it against all schedule shifts of T U^T T^-1
    best = np.inf
    for r in range(6):
        pre = flat[:r]                       # conjugate by the first r layers of U's word image
        # V_r (T U^T T^-1) V_r^-1 with V_r = product of the last r layers of the word Y,X,Z, try both
        for word in (Y + X + Z,):
            Vr = word[len(word) - r:] if r else []
            def VrInv(v, Vr=Vr):
                for k in reversed(Vr):
                    v = Lm[k].conj().T @ v
                return v
            out = apply(Vr, UT_trans(VrInv(V)))
            best = min(best, np.linalg.norm(lhs4 - out) / nrm)
    # record-level odds: |<b|U|a>|^2 vs |<b|P U P^-1|a>|^2 for basis inputs a
    dodds = 0.0
    for j in rng.choice(dim, size=min(dim, 40), replace=False):
        e = np.zeros((dim, 1), complex); e[j] = 1
        o1 = np.abs(apply(U, e)) ** 2
        o2 = np.abs(P4 @ apply(U, P4.T @ e)) ** 2
        dodds = max(dodds, np.abs(o1 - o2).max())
    print(f"n={n} (dim {dim}): |[X,Y]|={comm:.2e}  norm defect={unit:.1e}  C3 vs schedule shift={c3:.1e}  "
          f"C4 vs best schedule shift={c4:.2e}  C4 vs shifted T111 U^T T111^-1 = {best:.1e}  "
          f"max |odds(U) - odds(C4 U C4^-1)| from basis inputs = {dodds:.3f}")
