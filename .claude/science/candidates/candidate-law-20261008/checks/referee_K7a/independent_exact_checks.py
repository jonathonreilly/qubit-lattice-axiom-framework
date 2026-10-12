"""Independent exact checks for the K7a referee report.

This deliberately does not import the submitted runners.  It uses a monomial
orbit construction over the signed-permutation group and exact integer/rational
linear algebra for the load-bearing 9/4/1 count.
"""

from collections import defaultdict
from itertools import combinations_with_replacement, permutations, product
from math import gcd

import sympy as sp


HPAIRS = tuple(combinations_with_replacement(range(4), 2))
HINDEX = {p: i for i, p in enumerate(HPAIRS)}
HMON = tuple(combinations_with_replacement(range(10), 2))
SMON = tuple(combinations_with_replacement(range(4), 2))
MON = tuple((hm, sm) for hm in HMON for sm in SMON)
MINDEX = {m: i for i, m in enumerate(MON)}
GROUP = tuple((p, sg) for p in permutations(range(4))
              for sg in product((1, -1), repeat=4))


def transform_h(a, p, sg):
    i, j = HPAIRS[a]
    return HINDEX[tuple(sorted((p[i], p[j])))], sg[i] * sg[j]


def transform_mon(m, p, sg):
    (a, b), (i, j) = m
    aa, sa = transform_h(a, p, sg)
    bb, sb = transform_h(b, p, sg)
    return (tuple(sorted((aa, bb))), tuple(sorted((p[i], p[j])))), sa * sb * sg[i] * sg[j]


def primitive(v):
    g = 0
    for x in v.values():
        g = gcd(g, abs(x))
    out = {k: x // g for k, x in v.items() if x}
    if out[min(out)] < 0:
        out = {k: -x for k, x in out.items()}
    return out


def invariant_orbits():
    unseen = set(range(len(MON)))
    basis = []
    while unseen:
        seed = min(unseen)
        acc = defaultdict(int)
        orbit = set()
        for p, sg in GROUP:
            mt, sign = transform_mon(MON[seed], p, sg)
            k = MINDEX[mt]
            orbit.add(k)
            acc[k] += sign
        unseen.difference_update(orbit)
        acc = {k: v for k, v in acc.items() if v}
        if acc:
            basis.append(primitive(acc))
    return basis


def sparse_rank(columns, ncols):
    row_names = sorted({r for col in columns for r in col})
    ridx = {r: i for i, r in enumerate(row_names)}
    entries = {}
    for j, col in enumerate(columns):
        for r, value in col.items():
            if value:
                entries[(ridx[r], j)] = sp.Integer(value)
    matrix = sp.MutableSparseMatrix(len(row_names), ncols, entries)
    return matrix.rank(), matrix


def dh_terms(a):
    """Terms in delta h_ij = s_i xi_j + s_j xi_i."""
    i, j = HPAIRS[a]
    out = defaultdict(int)
    out[(i, j)] += 1
    out[(j, i)] += 1
    return out


def gauge_variation_column(inv):
    """Exact coefficients of delta Q, with targets (h, xi, s,s,s)."""
    out = defaultdict(int)
    for midx, weight in inv.items():
        (a, b), (i, j) = MON[midx]
        for (ss, xi), c in dh_terms(a).items():
            out[(b, xi, tuple(sorted((ss, i, j))))] += weight * c
        for (ss, xi), c in dh_terms(b).items():
            out[(a, xi, tuple(sorted((ss, i, j))))] += weight * c
    return {k: v for k, v in out.items() if v}


def generator_expansions(p, q):
    """Infinitesimal rotation A_pq=-1, A_qp=+1 on h and s."""
    A = [[0] * 4 for _ in range(4)]
    A[p][q] = -1
    A[q][p] = 1
    ds = []
    for i in range(4):
        d = defaultdict(int)
        for k in range(4):
            d[k] += A[i][k]
        ds.append({k: v for k, v in d.items() if v})
    dh = []
    for i, j in HPAIRS:
        d = defaultdict(int)
        for k in range(4):
            d[HINDEX[tuple(sorted((k, j)))]] += A[i][k]
            d[HINDEX[tuple(sorted((i, k)))]] += A[j][k]
        dh.append({k: v for k, v in d.items() if v})
    return dh, ds


def rotation_column(inv, p, q):
    dh, ds = generator_expansions(p, q)
    out = defaultdict(int)
    for midx, weight in inv.items():
        (a, b), (i, j) = MON[midx]
        for aa, c in dh[a].items():
            out[MINDEX[(tuple(sorted((aa, b))), (i, j))]] += weight * c
        for bb, c in dh[b].items():
            out[MINDEX[(tuple(sorted((a, bb))), (i, j))]] += weight * c
        for ii, c in ds[i].items():
            out[MINDEX[((a, b), tuple(sorted((ii, j))))]] += weight * c
        for jj, c in ds[j].items():
            out[MINDEX[((a, b), tuple(sorted((i, jj))))]] += weight * c
    return {k: v for k, v in out.items() if v}


def exact_symbol_checks():
    # Orthonormal symmetric-tensor coordinates, independently rebuilt.
    q = sp.symbols("q0:10", real=True)
    H = sp.zeros(4)
    for c, (i, j) in enumerate(HPAIRS):
        H[i, j] = H[j, i] = q[c] if i == j else q[c] / sp.sqrt(2)
    s = sp.Matrix([1, 0, 0, 0])
    tr = sp.trace(H)
    form = sp.Rational(1, 4) * ((H.T * H).trace() - 2 * (H * s).dot(H * s)
                                + 2 * (s.dot(H * s)) * tr - tr**2)
    K = sp.hessian(sp.expand(form), q)
    spectrum = K.eigenvals()

    # Gauge-fixed inverse at general nonzero s^2.
    t = sp.Matrix([1 if i == j else 0 for i, j in HPAIRS])
    A = sp.eye(10) - sp.Rational(1, 2) * t * t.T
    assert sp.simplify(A * A - sp.eye(10)) == sp.zeros(10)
    # Rebuild the general symbol for the exact gauge and ADM identities.
    ss = sp.Matrix(sp.symbols("s0:4", real=True))
    ss2 = ss.dot(ss)
    hs = H * ss
    qform = sp.Rational(1, 4) * (ss2 * (H.T * H).trace() - 2 * hs.dot(hs)
                                      + 2 * ss.dot(H * ss) * tr - ss2 * tr**2)
    Kg = sp.hessian(sp.expand(qform), q)
    D = sp.zeros(10, 4)
    for c, (i, j) in enumerate(HPAIRS):
        if i == j:
            D[c, i] = 2 * ss[i]
        else:
            D[c, j] = sp.sqrt(2) * ss[i]
            D[c, i] = sp.sqrt(2) * ss[j]
    gauge_ok = (Kg * D).applyfunc(sp.expand) == sp.zeros(10, 4)

    spatial_pairs = ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2))
    spatial = [HINDEX[x] for x in spatial_pairs]
    c44 = HINDEX[(3, 3)]
    c4i = [HINDEX[(i, 3)] for i in range(3)]
    kt = Kg.subs({ss[0]: 0, ss[1]: 0, ss[2]: 0, ss[3]: 1}).extract(spatial, spatial)
    kt_inverse_spectrum = kt.inv().eigenvals()
    s3sq = sum(ss[i] ** 2 for i in range(3))
    r = []
    for i, j in spatial_pairs:
        r.append(s3sq - ss[i] ** 2 if i == j else -sp.sqrt(2) * ss[i] * ss[j])
    lapse_ok = all(sp.expand(Kg[c44, spatial[j]].subs(ss[3], 0) + sp.Rational(1, 2) * r[j]) == 0
                   for j in range(6))
    # In q_{i4}=sqrt(2) h_{i4} coordinates the shift row is -s4/sqrt(2)
    # times s_j(h_ij-delta_ij tr h).  In h_{i4} coordinates it is exactly -s4 times it.
    shift_ok = True
    for i, row in enumerate(c4i):
        expected = []
        for a, b in spatial_pairs:
            E = sp.zeros(3)
            E[a, b] = E[b, a] = 1 if a == b else 1 / sp.sqrt(2)
            expected.append(sum(ss[j] * (E[i, j] - (1 if i == j else 0) * sp.trace(E))
                                for j in range(3)))
        shift_ok &= all(sp.expand(Kg[row, spatial[j]] + ss[3] * expected[j] / sp.sqrt(2)) == 0
                        for j in range(6))
    return spectrum, gauge_ok, kt_inverse_spectrum, lapse_ok, shift_ok


def parity_sign_check():
    """Exact parity-cell cocycle check for all signed permutations."""
    def eta_bit(mu, x):
        return sum(x[:mu]) % 2

    failures = []
    for p, sg in GROUP:
        invp = [0] * 4
        for a in range(4):
            invp[p[a]] = a
        edge = {}
        for y in product((0, 1), repeat=4):
            x = tuple(y[p[a]] for a in range(4))  # signs disappear modulo 2
            for nu in range(4):
                mu = invp[nu]
                edge[(y, nu)] = ((sg[mu] == -1) + eta_bit(mu, x) + eta_bit(nu, y)) % 2
        f = {(0, 0, 0, 0): 0}
        stack = [(0, 0, 0, 0)]
        ok = True
        while stack:
            y = stack.pop()
            for nu in range(4):
                z = list(y)
                z[nu] ^= 1
                z = tuple(z)
                value = f[y] ^ edge[(y, nu)]
                if z in f and f[z] != value:
                    ok = False
                elif z not in f:
                    f[z] = value
                    stack.append(z)
        if not ok or len(f) != 16:
            failures.append((p, sg))
    return failures


def main():
    basis = invariant_orbits()
    gauge_cols = [gauge_variation_column(v) for v in basis]
    gauge_rank, _ = sparse_rank(gauge_cols, len(basis))

    # Stack all six infinitesimal rotation equations by tagging their rows.
    rot_cols = [defaultdict(int) for _ in basis]
    for plane, (p, q) in enumerate(combinations_with_replacement(range(4), 2)):
        if p == q:
            continue
        for j, inv in enumerate(basis):
            for row, val in rotation_column(inv, p, q).items():
                rot_cols[j][(plane, row)] += val
    rot_rank, _ = sparse_rank(rot_cols, len(basis))

    print(f"exact monomial-orbit count W(B4): {len(basis)}")
    print(f"exact infinitesimal-rotation rank: {rot_rank}; O(4) nullity: {len(basis) - rot_rank}")
    print(f"exact gauge-variation rank: {gauge_rank}; gauge-invariant nullity: {len(basis) - gauge_rank}")
    spectrum, gauge_ok, kinv_spec, lapse_ok, shift_ok = exact_symbol_checks()
    print(f"exact spectrum at s=(1,0,0,0): {spectrum}")
    print(f"exact K(s)D(s)=0: {gauge_ok}")
    print(f"exact inverse temporal-block spectrum: {kinv_spec}; lapse: {lapse_ok}; shift(q basis): {shift_ok}")
    failures = parity_sign_check()
    print(f"exact staggered-fermion parity cocycle: {len(GROUP)-len(failures)}/384; failures: {len(failures)}")


if __name__ == "__main__":
    main()
