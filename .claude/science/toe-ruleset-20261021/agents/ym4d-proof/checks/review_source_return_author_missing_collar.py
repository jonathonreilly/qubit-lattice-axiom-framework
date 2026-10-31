#!/usr/bin/env python3
"""Bounded exact checks for SOURCE_LOCAL_RETURN_ASTRA; not an RG proof.

Only Python integer/Fraction arithmetic is used. Independent calculations:
Gaussian elimination vs local-compression Neumann products; permutation
determinants vs inverse traces; full SU(2) link transport vs tree gauge;
antiderivative endpoints vs oriented swept-face integrals.
"""
from fractions import Fraction as F
from itertools import product, permutations
import json


def zero(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


def eye(n):
    a = zero(n)
    for i in range(n):
        a[i][i] = F(1)
    return a


def add(a, b, scale=F(1)):
    return [[x + scale*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def mul(a, b):
    c = zero(len(a), len(b[0]))
    for i, ar in enumerate(a):
        for k, x in enumerate(ar):
            if x:
                for j, y in enumerate(b[k]):
                    if y:
                        c[i][j] += x*y
    return c


def inverse(a):
    n = len(a)
    c = [a[i][:] + eye(n)[i] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if c[i][j])
        c[j], c[pivot] = c[pivot], c[j]
        d = c[j][j]
        c[j] = [x/d for x in c[j]]
        for i in range(n):
            if i != j and c[i][j]:
                f = c[i][j]
                c[i] = [x-f*y for x, y in zip(c[i], c[j])]
    return [r[n:] for r in c]


def norm(a):
    row = max((sum(map(abs, r)) for r in a), default=F(0))
    col = max((sum(abs(a[i][j]) for i in range(len(a)))
               for j in range(len(a[0]))), default=F(0))
    return row, col


def det_permutation(a):
    n = len(a)
    total = F(0)
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        term = F((-1)**inversions)
        for i, j in enumerate(perm):
            term *= a[i][j]
        total += term
    return total


def atom_norm(atoms, n, weight):
    row, col, inc = [F(0)]*n, [F(0)]*n, [F(0)]*n
    for support, a in atoms:
        w = weight**len(support)
        total = F(0)
        for i in range(n):
            for j in range(n):
                val = w*abs(a[i][j])
                row[i] += val
                col[j] += val
                total += val
        for v in support:
            inc[v] += total
    return max(row), max(col), max(inc)


def connected(s, n):
    if not s:
        return False
    seen = {next(iter(s))}
    while True:
        new = seen | {y for x in seen for y in ((x-1) % n, (x+1) % n) if y in s}
        if new == seen:
            return seen == set(s)
        seen = new


def local_atoms(k, boxes, radius):
    n = len(k)
    ps, rs = [], []
    for box in boxes:
        omega = {((x+j) % n) for x in box for j in range(-radius, radius+1)}
        support = omega
        inds = sorted(omega)
        inv = inverse([[k[i][j] for j in inds] for i in inds])
        p = zero(n)
        for ii, i in enumerate(inds):
            for j in box:
                p[i][j] = inv[ii][inds.index(j)]
        r = mul(k, p)
        for i in range(n):
            for j in range(n):
                r[i][j] = -r[i][j] if i not in omega else F(0)
        ps.append((frozenset(support), p))
        rs.append((frozenset(support), r))
    return ps, rs


gates = {}
data = {}
n = 12
k = zero(n)
for i in range(n):
    k[i][i] = F(4) + F(i+1, 100)
    k[i][(i-1) % n] = k[i][(i+1) % n] = F(-1)
boxes = [list(range(i, i+3)) for i in range(0, n, 3)]
ps, rs = local_atoms(k, boxes, 2)
p = zero(n)
r = zero(n)
for _, a in ps:
    p = add(p, a)
for _, a in rs:
    r = add(r, a)
gates['compression_parametrix_identity'] = mul(k, p) == add(eye(n), r, F(-1))
g = inverse(k)
gates['direct_inverse_identity'] = mul(k, g) == eye(n)
sn, term = zero(n), p
for order in range(4):
    sn = add(sn, term)
    term = mul(term, r)
r4 = eye(n)
for _ in range(4):
    r4 = mul(r4, r)
gates['exact_neumann_remainder'] = add(g, sn, F(-1)) == mul(g, r4)
qrow, qcol = norm(r)
prow, pcol = norm(p)
error = max(norm(add(g, sn, F(-1))))
q = max(qrow, qcol)
gates['unweighted_geometric_bound'] = q < 1 and error <= max(prow, pcol)*q**4/(1-q)
weight = F(101, 100)
mp_row, mp_col, bp = atom_norm(ps, n, weight)
mr_row, mr_col, br = atom_norm(rs, n, weight)
mp, mr = max(mp_row, mp_col), max(mr_row, mr_col)
walks = ps[:]
all_atoms = ps[:]
for length in range(1, 4):
    new = []
    for s1, a in walks:
        for s2, b in rs:
            c = mul(a, b)
            if any(any(row) for row in c):
                assert s1 & s2
                new.append((s1 | s2, c))
    walks = new
    all_atoms.extend(walks)
amrow, amcol, ab = atom_norm(all_atoms, n, weight)
major_m = mp*sum(mr**j for j in range(4))
major_b = bp*sum(mr**j for j in range(4)) + mp*br*sum(j*mr**(j-1) for j in range(1, 4))
gates['weighted_rows_and_columns'] = mr < 1 and max(amrow, amcol) <= major_m
gates['marked_support_incidence'] = ab <= major_b
gates['connected_walk_supports'] = all(connected(s, n) for s, _ in all_atoms)
gates['matrix_endpoints_in_support'] = all(i in s and j in s
    for s, a in all_atoms for i in range(n) for j in range(n) if a[i][j])
outside = next(v for v in range(n) if v not in ps[0][0])
kremote = [row[:] for row in k]
kremote[outside][outside] += F(1, 7)
pr, rr = local_atoms(kremote, boxes, 2)
gates['original_source_outside_collar_invisible'] = ps[0] == pr[0] and rs[0] == rr[0]
klocal = [row[:] for row in k]
klocal[0][0] += F(1, 7)
pl, _ = local_atoms(klocal, boxes, 2)
gates['original_source_inside_compression_detected'] = ps[0][1] != pl[0][1]
star = zero(4)
for i in range(1, 4):
    star[i][0] = F(1, 4)
gates['row_only_control_detected'] = norm(star) == (F(1, 4), F(3, 4))
data['parametrix'] = dict(size=n, cutoff_order=3, atoms_through_order_3=len(all_atoms),
    row_q=str(qrow), column_q=str(qcol), weighted_q=str(mr), error=str(error),
    incidence=str(ab), incidence_bound=str(major_b), remote_source=outside)

# Full determinant: independent permutation sum and Gaussian-elimination inverse.
kd = zero(5)
for i in range(5):
    kd[i][i] = F(4) + F(i+1, 10)
    kd[i][(i-1) % 5] = kd[i][(i+1) % 5] = F(-1)
minor = [[kd[i][j] for j in range(1, 5)] for i in range(1, 5)]
det = det_permutation(kd)
ddet = det_permutation(minor)
via_perm = -ddet/(2*det)
via_trace = -inverse(kd)[0][0]/2
gates['determinant_derivative_independent_paths'] = via_perm == via_trace
gates['omitted_determinant_control_detected'] = via_perm != 0
data['minus_half_logdet_derivative'] = str(via_perm)

# Exact SU(2), as unit quaternions. This checks actual noncommuting link data.
one = (F(1), F(0), F(0), F(0))


def qm(a, b):
    w, x, y, z = a
    v, r, s, t = b
    return (w*v-x*r-y*s-z*t, w*r+x*v+y*t-z*s,
            w*s-x*t+y*v+z*r, w*t+x*s-y*r+z*v)


def qi(a):
    return (a[0], -a[1], -a[2], -a[3])


sites = list(product(range(3), repeat=4))


def step(x, mu, amount=1):
    y = list(x)
    y[mu] = (y[mu]+amount) % 3
    return tuple(y)


links = {}
for idx, x in enumerate(sites):
    for mu in range(4):
        s = F(1, 5+(idx+mu) % 5)
        qv = [F(0)]*4
        qv[0] = (1-s*s)/(1+s*s)
        qv[1+(idx+mu) % 3] = 2*s/(1+s*s)
        links[x, mu] = tuple(qv)
root = (0, 0, 0, 0)
gauge = {root: one}
tree = []
for x in sorted(sites, key=lambda x: (sum(x), x)):
    if x == root:
        continue
    mu = max(i for i in range(4) if x[i])
    parent = list(x)
    parent[mu] -= 1
    parent = tuple(parent)
    edge = (parent, mu)
    tree.append(edge)
    gauge[x] = qm(gauge[parent], links[edge])
transformed = {(x, mu): qm(qm(gauge[x], links[x, mu]), qi(gauge[step(x, mu)]))
               for x in sites for mu in range(4)}
gates['su2_all_links_unit'] = all(sum(v*v for v in qv) == 1 for qv in links.values())
gates['su2_tree_edges_are_identity'] = all(transformed[e] == one for e in tree)


def plaquette(u, x, mu, nu):
    return qm(qm(qm(u[x, mu], u[step(x, mu), nu]),
                 qi(u[step(x, nu), mu])), qi(u[x, nu]))


gates['su2_all_plaquette_traces_invariant'] = all(
    plaquette(links, x, mu, nu)[0] == plaquette(transformed, x, mu, nu)[0]
    for x in sites for mu in range(4) for nu in range(mu+1, 4))


def transport(u, x, ordering):
    value = one
    here = root
    for mu in ordering:
        for _ in range(x[mu]):
            value = qm(value, u[here, mu])
            here = step(here, mu)
    assert here == x
    return value


contours_checked = 0
contours_ok = True
for ordering in [tuple(range(4)), tuple(reversed(range(4)))]:
    for x in sites:
        for mu in range(4):
            values = []
            for u in [links, transformed]:
                tx = transport(u, x, ordering)
                value, here = one, x
                for _ in range(3):
                    value = qm(value, u[here, mu])
                    here = step(here, mu)
                values.append(qm(qm(tx, value), qi(tx)))
            contours_ok &= values[0] == values[1]
            contours_checked += 1
gates['su2_anchored_contours_invariant'] = contours_ok
corrupt = dict(transformed)
free_edge = next(e for e in corrupt if e not in set(tree))
corrupt[free_edge] = qm((F(3, 5), F(4, 5), F(0), F(0)), corrupt[free_edge])
gates['su2_wrong_link_control_detected'] = any(
    plaquette(links, x, mu, nu)[0] != plaquette(corrupt, x, mu, nu)[0]
    for x in sites for mu in range(4) for nu in range(mu+1, 4))
data['su2'] = dict(dimension=4, side=3, sites=len(sites), links=len(links),
    tree_edges=len(tree), free_links=len(links)-len(tree), plaquettes=81*6,
    anchored_contours=contours_checked,
    scope='Exact gauge/contour identities; no nonlinear Hessian or Haar integration computed.')

# Contour sides in one dimension, f(a)=1+z*a+a^2.
pwidth, shift, zsource = F(2), F(1, 3), F(2, 5)


def primitive(x):
    return x+zsource*x*x/2+x*x*x/3


reference = primitive(pwidth)-primitive(-pwidth)
moving = primitive(shift+pwidth)-primitive(shift-pwidth)
# Integrate each oriented face directly as a polynomial in the homotopy time.
def face_integral(base):
    return shift*(1+zsource*base+base*base) + shift*shift*(zsource+2*base)/2 + shift**3/3


side = face_integral(pwidth)-face_integral(-pwidth)
gates['moving_cut_side_identity'] = moving-reference == side
gates['discarded_side_control_detected'] = side != 0
history_left, history_right = F(-1, 2), F(3, 2)
history_integral = max(F(0), history_right-max(history_left, F(0)))
without_history_integral = history_right-history_left
gates['retained_history_control_detected'] = history_integral != without_history_integral
data['cutoff'] = dict(reference=str(reference), moving=str(moving), side=str(side),
    retained_history_integral=str(history_integral),
    discarded_history_integral=str(without_history_integral),
    scope='Polynomial holomorphic-form identity; no uniform normalized Gaussian-face estimate.')

result = {'arithmetic': 'exact Fraction only', 'gates': gates,
          'all_passed': all(gates.values()), 'data': data,
          'limitations': ['Finite calculations do not establish the general proofs.',
              'No higher-level operator, nontrivial history return, or continuum limit is computed.',
              'The scalar parametrix example checks algebra, not a Yang-Mills measure.',
              'The SU(2) example checks exact nonabelian gauge/contour identities, not a gauge Jacobian by quadrature.']}
print(json.dumps(result, indent=2, sort_keys=True))
assert result['all_passed']
