"""2D (x,y) degree-2 identity: enumerate unknowns, assemble sparse system, test consistency."""
import sys, time, itertools
import numpy as np
import scipy.sparse as sps
from fractions import Fraction as F
from model2 import *

C1_TEMPLATE = None


def c1_template(k=K):
    t = []
    for (di, dj, cf) in ((0, 1, -1), (0, 0, 2), (0, -1, -1)):
        t.append((XX, di, dj, k * cf))
    for (di, dj, cf) in ((1, 0, -1), (0, 0, 2), (-1, 0, -1)):
        t.append((YY, di, dj, k * cf))
    for (di, dj, cf) in ((1, 0, -1), (-1, 0, -1), (0, 1, -1), (0, -1, -1), (0, 0, 4)):
        t.append((ZZ, di, dj, k * cf))
    for (di, dj, cf) in ((0, 0, 1), (1, 0, -1), (0, 1, -1), (1, 1, 1)):
        t.append((XY, di, dj, 2 * k * cf))
    return t


def slots(R):
    hs = []
    for c in SITE:
        for i in range(R + 1):
            for j in range(R + 1):
                hs.append((c, pos(c, i, j)))
    for i in range(R):
        for j in range(R):
            hs.append((XY, pos(XY, i, j)))
    return hs


def enum_V2(R):
    S = slots(R)
    Ls = [(2 * i, 2 * j) for i in range(R + 1) for j in range(R + 1)]
    res = set()
    for (a, b) in itertools.combinations_with_replacement(S, 2):
        for lp in Ls:
            mono = tuple(sorted([('N', 0, lp), ('h', a[0], a[1]), ('h', b[0], b[1])]))
            res.add(canon(mono))
    return sorted(res)


def enum_T3(R):
    S = slots(R)
    Ls = [(2 * i, 2 * j) for i in range(R + 1) for j in range(R + 1)]
    res = set()
    for (a, b) in itertools.combinations_with_replacement(S, 2):
        for hh in S:
            for lp in Ls:
                mono = tuple(sorted([('N', 0, lp), ('P', a[0], a[1]), ('P', b[0], b[1]), ('h', hh[0], hh[1])]))
                res.add(canon(mono))
    return sorted(res)


def bbox_ok(points, R):
    xs = [p[0] for p in points]; ys = [p[1] for p in points]
    return max(xs) - min(xs) <= 2 * R and max(ys) - min(ys) <= 2 * R


def all_positions(R, comps=(XX, YY, ZZ, XY)):
    out = []
    rng = range(-R - 1, R + 2)
    for c in comps:
        for i in rng:
            for j in rng:
                out.append((c, pos(c, i, j)))
    return out


def enum_G2(R):
    """xi_j(bond from (0,0)) * P_c(p) h_d(q)"""
    res = []
    APos = all_positions(R)
    for dirn, ep in (('x', (2, 0)), ('y', (0, 2))):
        for (c, p) in APos:
            for (d, q) in APos:
                if bbox_ok([(0, 0), ep, p, q], R):
                    res.append((dirn, c, p, d, q))
    return res


def bond_monos(dirn, extra):
    """xi0_j(bond) * extra-tuple as functional"""
    xx, yy = xi0_xy()
    xi = xx if dirn == 'x' else yy
    out = {}
    for m, c in xi.items():
        add(out, m + tuple(extra), c)
    return out


def enum_xi1(R):
    res = []
    Ls = [(2 * i, 2 * j) for i in range(-R - 1, R + 2) for j in range(-R - 1, R + 2)]
    APos = all_positions(R)
    for dirn, ep in (('x', (2, 0)), ('y', (0, 2))):
        for a, b in itertools.combinations(Ls, 2):
            for (e, q) in APos:
                if bbox_ok([(0, 0), ep, a, b, q], R):
                    res.append((dirn, a, b, e, q))
    return res


def enum_chi(R):
    res = []
    Ls = [(2 * i, 2 * j) for i in range(-R - 1, R + 2) for j in range(-R - 1, R + 2)]
    APos = all_positions(R)
    for a, b in itertools.combinations(Ls, 2):
        for (e, q) in APos:
            if bbox_ok([(0, 0), a, b, q], R):
                res.append((a, b, e, q))
    return res


def V2_of(mono, L):
    return {tuple(sorted((L if v[0] == 'N' else v[0], v[1], v[2]) for v in mono)): F(1)}


def col_V2(mono, alpha=ALPHA):
    return fadd(bracket(T2('N', alpha), V2_of(mono, 'M')), bracket(V2_of(mono, 'N'), T2('M', alpha)))


def col_T3(mono, k=K):
    return fadd(bracket(C1('N', k), V2_of(mono, 'M')), bracket(V2_of(mono, 'N'), C1('M', k)))


def col_G2(u, k=K, alpha=ALPHA):
    dirn, c, p, d, q = u
    return bond_monos(dirn, [('P', c, p), ('h', d, q)])


def xi1_raw(u):
    dirn, a, b, e, q = u
    out = {}
    raw_add(out, [('N', 0, a), ('M', 0, b), ('h', e, q)], F(1))
    raw_add(out, [('N', 0, b), ('M', 0, a), ('h', e, q)], F(-1))
    return out


def col_xi1(u):
    dirn = u[0]
    m = xi1_raw(u)
    return G1_of_xi(m, {}) if dirn == 'x' else G1_of_xi({}, m)


def chi_raw(u):
    a, b, e, q = u
    out = {}
    raw_add(out, [('N', 0, a), ('M', 0, b), ('P', e, q)], F(1))
    raw_add(out, [('N', 0, b), ('M', 0, a), ('P', e, q)], F(-1))
    return out


def col_chi(u, k=K):
    out = {}
    tmpl = c1_template(k)
    for m, cf in chi_raw(u).items():
        for (c, di, dj, tc) in tmpl:
            add(out, shift(m, (2 * di, 2 * dj)) + (hv(c, 0, 0),), tc * cf)
    return out


def build(R, mode='full', use=('V2', 'T3', 'G2', 'xi1', 'chi'), verbose=True):
    t0 = time.time()
    cols = []
    if 'V2' in use:
        for m in enum_V2(R):
            cols.append((('V2', m), col_V2(m)))
    if 'T3' in use:
        for m in enum_T3(R):
            cols.append((('T3', m), col_T3(m)))
    if 'G2' in use:
        for u in enum_G2(R):
            cols.append((('G2', u), fscale(col_G2(u), F(-1))))
    if 'xi1' in use:
        for u in enum_xi1(R):
            cols.append((('xi1', u), fscale(col_xi1(u), F(-1))))
    if 'chi' in use:
        for u in enum_chi(R):
            cols.append((('chi', u), fscale(col_chi(u), F(-1))))
    if mode == 'uniformM':
        cols = [(lab, restrict_uniform_M(d)) for lab, d in cols]
    if verbose:
        print("columns built:", len(cols), "in", round(time.time() - t0, 1), "s", {f: sum(1 for l, _ in cols if l[0] == f) for f in ('V2', 'T3', 'G2', 'xi1', 'chi')})
    rows = {}
    entries = []
    def rid(key):
        if key not in rows:
            rows[key] = len(rows)
        return rows[key]
    for j, (lab, d) in enumerate(cols):
        for mono, c in d.items():
            entries.append((rid(('I', mono)), j, c))
    b = {}
    if 'V2' in use:
        for j, (lab, d) in enumerate(cols):
            if lab[0] == 'V2':
                u = substitute_uniform(V2_of(lab[1], 'N'), 'N')
                for mono, c in u.items():
                    entries.append((rid(('R', mono)), j, c))
        for mono, c in R2_2D().items():
            b[rid(('R', mono))] = K * c
    return cols, rows, entries, b


def to_sparse(entries, b, nr, nc):
    I = np.array([e[0] for e in entries]); J = np.array([e[1] for e in entries]); V = np.array([float(e[2]) for e in entries])
    A = sps.coo_matrix((V, (I, J)), shape=(nr, nc)).tocsr()
    bb = np.zeros(nr)
    for i, c in b.items():
        bb[i] = float(c)
    return A, bb


def consistency(entries, b, nr, nc):
    """Float least squares via dense QR-based lstsq on the column-space (uses normal equations with eigh for large sizes)."""
    A, bb = to_sparse(entries, b, nr, nc)
    from scipy.sparse.linalg import lsqr
    sol = lsqr(A, bb, atol=1e-14, btol=1e-14, iter_lim=200000, conlim=1e14)
    x = sol[0]
    res = np.linalg.norm(A @ x - bb)
    return res, sol[1], sol[2], np.linalg.norm(bb)


if __name__ == '__main__':
    R = int(sys.argv[1]); use = tuple(sys.argv[2].split(',')) if len(sys.argv) > 2 else ('V2', 'T3', 'G2', 'xi1', 'chi')
    cols, rows, entries, b = build(R, 'full', use)
    print("rows", len(rows), "cols", len(cols), "nnz", len(entries))
    print("lsqr residual, istop, iters, |b|:", consistency(entries, b, len(rows), len(cols)))
