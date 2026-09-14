#!/usr/bin/env python3
"""Possibility-covariance witness: the soldering fork in the possibility domain.

Target: the symmetry group under which the nearest-neighbour admissibility rule
must be covariant on the possibility side, and the rules each reading permits.

Domain: seven Bloch vectors -- the centre p (index 0) and the six neighbour
slots q_1..q_6 in directions +x,-x,+y,-y,+z,-z (indices 1..6).  A neighbourhood
stratum is the subset of slots that carry a record; unrecorded slots supply no
vector.  Three readings of the one-site presentation:

  U   unsoldered SO(3): Aut(M_2(C)) acts on every Bloch vector by one global
      internal rotation, independently of the proper cubic rotation permuting
      slots.  The covariance group is the direct product.
  U3  unsoldered O(3): U together with the internal inversion p -> -p.
  S   soldered: the three Cl(3,0) generators are the lattice axes, so only the
      diagonal subgroup acts -- the cubic rotation moves slots and vectors alike.

All arithmetic is exact (Fractions).  Dimension counts are Molien-Weyl sums over
the cubic stabiliser with the SO(3) Haar average taken as a Laurent residue;
degrees <= 3 are recomputed independently as the nullity of the stacked
so(3)-derivation and cubic-fixed conditions.
"""
import time
from fractions import Fraction as Fr
from itertools import product
from math import factorial as fact

T0 = time.time()
PASS = 0
FAIL = 0
FAILED = []


def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        FAILED.append(name)
    print((' ok ' if cond else ' FAIL ') + name)


# ---------------------------------------------------------------- group
DIRS = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]


def matmul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1]) - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))


def cubic_group():
    out = []
    for perm in [(0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)]:
        for signs in product([1,-1], repeat=3):
            m = tuple(tuple(signs[i] if perm[i] == j else 0 for j in range(3)) for i in range(3))
            if det3(m) == 1:
                out.append(m)
    return out


G = cubic_group()
ID = ((1,0,0),(0,1,0),(0,0,1))


def apply(m, v):
    return tuple(sum(m[i][j]*v[j] for j in range(3)) for i in range(3))


def slot_perm(m):
    return tuple(DIRS.index(apply(m, d)) for d in DIRS)


def mpow(m, k):
    r = ID
    for _ in range(k):
        r = matmul(r, m)
    return r


def stabilizer(slots):
    return [g for g in G if set(slot_perm(g)[j] for j in slots) == set(slots)]


def strata():
    seen = set(); out = []
    for mask in range(64):
        S = frozenset(j for j in range(6) if mask >> j & 1)
        if S in seen:
            continue
        orb = set()
        for g in G:
            sp = slot_perm(g)
            orb.add(frozenset(sp[j] for j in S))
        seen |= orb
        out.append((tuple(sorted(S)), len(orb), 24 // len(orb)))
    out.sort(key=lambda x: (len(x[0]), -x[2]))
    return out


def bary(S):
    return tuple(sum(DIRS[i][a] for i in S) for a in range(3))


# ------------------------------------------------- Molien-Weyl dimensions
def lmul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i+j] = out.get(i+j, 0) + x*y
    return {k: v for k, v in out.items() if v != 0}


def ladd(a, b, c=1):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + c*v
    return {k: v for k, v in out.items() if v != 0}


def lscale(a, c):
    return {k: v*c for k, v in a.items() if v*c != 0}


def so3_integral(f):
    """Haar average over SO(3) of a class function written in z = e^{i theta}:
    the multiplicity of the trivial character in sum_n a_n chi_n."""
    return f.get(0, Fr(0)) - f.get(1, Fr(0))


def sym_counts(power_traces, D):
    h = [{0: Fr(1)}]
    for d in range(1, D+1):
        acc = {}
        for k in range(1, d+1):
            acc = ladd(acc, lmul(power_traces[k-1], h[d-k]))
        h.append(lscale(acc, Fr(1, d)))
    return h


def molien(slots, reading, D, include_p=True, out='triv', subgroup=None):
    """Dimension of covariant rule terms of each degree 0..D in the supplied Bloch
    vectors.  out: 'triv' scalar rule terms, 'vec' internal-vector-valued output,
    'lat' lattice-vector-valued scalar, 'veclat' lattice-to-internal frame map."""
    slots = tuple(slots)
    H = subgroup if subgroup is not None else stabilizer(slots)
    total = [Fr(0)]*(D+1)
    vecdeg = 1 if out in ('vec', 'veclat') else 0
    for g in H:
        trg = g[0][0] + g[1][1] + g[2][2]
        pts = []
        for k in range(1, D+1):
            gk = mpow(g, k); sp = slot_perm(gk)
            nfix = (1 if include_p else 0) + sum(1 for j in slots if sp[j] == j)
            if reading in ('U', 'U3'):
                pts.append(lscale({k: Fr(1), 0: Fr(1), -k: Fr(1)}, Fr(nfix)))
            else:
                trk = gk[0][0] + gk[1][1] + gk[2][2]
                pts.append({0: Fr(trk*nfix)})
        h = sym_counts(pts, D)
        for d in range(D+1):
            f = h[d]
            if out in ('vec', 'veclat'):
                f = lmul(f, {1: Fr(1), 0: Fr(1), -1: Fr(1)}) if reading in ('U', 'U3') else lscale(f, Fr(trg))
            if out in ('lat', 'veclat'):
                f = lscale(f, Fr(trg))
            total[d] += so3_integral(f) if reading in ('U', 'U3') else f.get(0, Fr(0))
    dims = [t/len(H) for t in total]
    if reading == 'U3':
        dims = [dm if (d + vecdeg) % 2 == 0 else Fr(0) for d, dm in enumerate(dims)]
    for dm in dims:
        assert dm.denominator == 1 and dm >= 0, (slots, reading, out, dims)
    return [int(dm) for dm in dims]


# --------------------------------------------- sparse polynomials, 21 vars
NV = 21


def var(j, a):
    return 3*j + a


def monomial(idx_list):
    e = [0]*NV
    for i in idx_list:
        e[i] += 1
    return tuple(e)


def poly_add(f, g, c=1):
    out = dict(f)
    for m, v in g.items():
        out[m] = out.get(m, 0) + c*v
    return {m: v for m, v in out.items() if v != 0}


def dot(j, k):
    return {monomial([var(j, a), var(k, a)]): Fr(1) for a in range(3)}


EPSD = {(0,1,2):1,(1,2,0):1,(2,0,1):1,(0,2,1):-1,(2,1,0):-1,(1,0,2):-1}


def eps(a, b, c):
    return EPSD.get((a, b, c), 0)


def triple(j, k, l):
    out = {}
    for (a, b, c), s in EPSD.items():
        m = monomial([var(j, a), var(k, b), var(l, c)])
        out[m] = out.get(m, 0) + s
    return {m: Fr(c) for m, c in out.items() if c != 0}


def act_unsoldered(g, f):
    """slot permutation only; the internal frame is untouched."""
    sp = slot_perm(g)
    out = {}
    for m, c in f.items():
        e = [0]*NV
        for j in range(7):
            jj = 0 if j == 0 else sp[j-1] + 1
            for a in range(3):
                e[var(jj, a)] = m[var(j, a)]
        out[tuple(e)] = out.get(tuple(e), 0) + c
    return out


def act_soldered(g, f):
    """diagonal action: slot permutation together with the signed coordinate permutation."""
    sp = slot_perm(g)
    out = {}
    for m, c in f.items():
        e = [0]*NV
        sign = 1
        for j in range(7):
            jj = 0 if j == 0 else sp[j-1] + 1
            for a in range(3):
                k = m[var(j, a)]
                if k == 0:
                    continue
                b = next(bb for bb in range(3) if g[bb][a] != 0)
                if g[b][a] < 0 and k % 2 == 1:
                    sign = -sign
                e[var(jj, b)] += k
        out[tuple(e)] = out.get(tuple(e), 0) + sign*c
    return {m: v for m, v in out.items() if v != 0}


def deriv(a, f):
    """the a-th so(3) generator acting on polynomials in the Bloch coordinates."""
    out = {}
    for m, c in f.items():
        for k in range(7):
            for cc in range(3):
                e = m[var(k, cc)]
                if e == 0:
                    continue
                for b in range(3):
                    s = eps(a, b, cc)
                    if s == 0:
                        continue
                    mm = list(m); mm[var(k, cc)] -= 1; mm[var(k, b)] += 1
                    mm = tuple(mm)
                    out[mm] = out.get(mm, 0) + s*e*c
    return {m: v for m, v in out.items() if v != 0}


def rank(rows):
    piv = {}
    r = 0
    for f in rows:
        f = dict(f)
        while f:
            m = max(f)
            if m in piv:
                pf = piv[m]
                c = f[m]/pf[m]
                f = poly_add(f, pf, -c)
            else:
                piv[m] = f
                r += 1
                break
    return r


# ------------------------- independent recomputation (no character sums)
def monos(vi, d):
    from itertools import combinations_with_replacement as cwr
    return sorted({monomial(c) for c in cwr(vi, d)})


def multideg(m, vecs):
    return tuple(sum(m[var(j, a)] for a in range(3)) for j in vecs)


def nullspace(rows, ncols):
    m = [r[:] for r in rows]
    piv = []
    r = 0
    for c in range(ncols):
        p = None
        for i in range(r, len(m)):
            if m[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        m[r], m[p] = m[p], m[r]
        iv = Fr(1)/m[r][c]
        m[r] = [x*iv for x in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [a - f*b for a, b in zip(m[i], m[r])]
        piv.append(c)
        r += 1
        if r == len(m):
            break
    ps = set(piv)
    out = []
    for fc in [c for c in range(ncols) if c not in ps]:
        v = [Fr(0)]*ncols
        v[fc] = Fr(1)
        for i, c in enumerate(piv):
            v[c] = -m[i][fc]
        out.append(v)
    return out


def so3_basis(vecs, d, nout):
    """Basis of the so(3)-invariant (nout=0) or equivariant (nout=1) degree-d
    polynomials in the given vectors, found blockwise by multidegree as the
    kernel of the three derivations -- no character sum anywhere."""
    vi = [var(j, a) for j in vecs for a in range(3)]
    ms = monos(vi, d)
    blk = {}
    for m in ms:
        blk.setdefault(multideg(m, vecs), []).append(m)
    out = []
    for _, bms in sorted(blk.items()):
        pos = {m: i for i, m in enumerate(bms)}
        n = len(bms)
        nc = n*(3 if nout else 1)
        rows = {}
        for i, m in enumerate(bms):
            for a in range(3):
                dm = deriv(a, {m: Fr(1)})
                for b in range(3 if nout else 1):
                    col = b*n + i
                    for mm, c in dm.items():
                        rows.setdefault((a, b, mm), {})[col] = \
                            rows.setdefault((a, b, mm), {}).get(col, Fr(0)) + c
                    if nout:
                        for cc in range(3):
                            s = eps(b, a, cc)
                            if s:
                                k = (a, b, m)
                                rows.setdefault(k, {})[cc*n + i] = \
                                    rows.setdefault(k, {}).get(cc*n + i, Fr(0)) - s
        dense = [[r.get(j, Fr(0)) for j in range(nc)] for r in rows.values()]
        for v in nullspace(dense, nc):
            if nout:
                out.append([{bms[i]: v[b*n + i] for i in range(n) if v[b*n + i] != 0}
                            for b in range(3)])
            else:
                out.append({bms[i]: v[i] for i in range(n) if v[i] != 0})
    return out


def rank_triples(trs):
    return rank([{(b, m): c for b, f in enumerate(t) for m, c in f.items()} for t in trs])


def indep_dim(slots, reading, d, nout, include_p=True):
    """Dimension of the covariant degree-d rule terms, recomputed as the rank of
    the Reynolds image over the cubic stabiliser (soldered: on signed-monomial
    orbit representatives; unsoldered: on the so(3) kernel basis)."""
    vecs = ([0] if include_p else []) + [j+1 for j in slots]
    H = stabilizer(tuple(slots))
    if reading == 'S':
        vi = [var(j, a) for j in vecs for a in range(3)]
        ms = monos(vi, d)
        seen = set()
        rows = []
        for m in ms:
            for b0 in range(3 if nout else 1):
                if (b0, m) in seen:
                    continue
                orb = set()
                acc = [{} for _ in range(3)] if nout else {}
                for g in H:
                    im = act_soldered(g, {m: Fr(1)})
                    (mm, cc), = im.items()
                    if nout:
                        b1 = next(bb for bb in range(3) if g[bb][b0] != 0)
                        orb.add((b1, mm))
                        acc[b1] = poly_add(acc[b1], {mm: cc*g[b1][b0]})
                    else:
                        orb.add((0, mm))
                        acc = poly_add(acc, im)
                seen |= orb
                if nout:
                    if any(acc):
                        rows.append(acc)
                elif acc:
                    rows.append(acc)
        return rank_triples(rows) if nout else rank(rows)
    bas = so3_basis(vecs, d, nout)
    rows = []
    for f in bas:
        if nout:
            acc = [{} for _ in range(3)]
            for g in H:
                for b in range(3):
                    acc[b] = poly_add(acc[b], act_unsoldered(g, f[b]))
            if any(acc):
                rows.append(acc)
        else:
            acc = {}
            for g in H:
                acc = poly_add(acc, act_unsoldered(g, f))
            if acc:
                rows.append(acc)
    return rank_triples(rows) if nout else rank(rows)


def fixdim(Hj):
    """Dimension of the common fixed space of Hj acting on the lattice R^3."""
    rows = [[Fr(g[a][b] - (1 if a == b else 0)) for b in range(3)]
            for g in Hj for a in range(3)]
    return len(nullspace(rows, 3)) if rows else 3


def lin_pred(slots):
    """Frobenius count of soldered linear invariants: one contribution per
    stabiliser orbit of the occupied vectors, from the fixed space of that
    orbit's point stabiliser. No Molien series and no polynomial algebra."""
    H = stabilizer(tuple(slots))
    seen, tot = set(), 0
    for j in [0] + [k+1 for k in slots]:
        if j in seen:
            continue
        img = (lambda g, i=j: 0 if i == 0 else slot_perm(g)[i-1] + 1)
        seen |= {img(g) for g in H}
        tot += fixdim([g for g in H if img(g) == j])
    return tot


# ========================= 1. domain, group, strata =========================
print('1. domain, lattice group, recorded-slot strata')
check('cubic group has order 24', len(G) == 24)
check('every element is a proper rotation', all(det3(g) == 1 for g in G))
check('all group elements distinct', len({tuple(map(tuple, g)) for g in G}) == 24)
check('closed under multiplication',
      all(tuple(map(tuple, matmul(a, b))) in {tuple(map(tuple, g)) for g in G}
          for a in G for b in G))
check('slot action is faithful',
      len({slot_perm(g) for g in G}) == 24)
check('slot action permutes the six lattice directions',
      all(sorted(slot_perm(g)) == list(range(6)) for g in G))
check('antipodal slots stay antipodal',
      all(slot_perm(g)[j ^ 1] == (slot_perm(g)[j] ^ 1) for g in G for j in range(6)))
ST = strata()
check('recorded-slot subsets fall into 10 orbits', len(ST) == 10)
check('orbit sizes sum to 64', sum(sz for _, sz, _ in ST) == 64)
check('orbit size times stabiliser order is 24',
      all(sz * st == 24 for _, sz, st in ST))
check('orbit representatives are the expected ten',
      [S for S, _, _ in ST] == [(), (0,), (0, 1), (0, 2), (0, 2, 4), (0, 1, 2),
                                (0, 1, 2, 3), (0, 1, 2, 4), (0, 1, 2, 3, 4),
                                (0, 1, 2, 3, 4, 5)])
DNZ = [S for S, _, _ in ST if any(x != 0 for x in bary(S))]
check('barycentre is nonzero on exactly six strata',
      DNZ == [(0,), (0, 2), (0, 2, 4), (0, 1, 2), (0, 1, 2, 4), (0, 1, 2, 3, 4)])
check('barycentre vanishes on the antipodally closed strata',
      all(bary(S) == (Fr(0), Fr(0), Fr(0))
          for S in [(), (0, 1), (0, 1, 2, 3), (0, 1, 2, 3, 4, 5)]))


# ================== 2. how many covariant rule terms exist ==================
print('2. dimension of the covariant rule space, by reading')
check('single Bloch vector, unsoldered: one invariant per even degree',
      molien((), 'U', 10) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
check('single Bloch vector, soldered: cubic harmonics appear from degree 4',
      molien((), 'S', 10) == [1, 0, 1, 0, 2, 0, 3, 0, 4, 1, 5])
check('centre plus one recorded neighbour, unsoldered',
      molien((0,), 'U', 6) == [1, 0, 3, 0, 6, 0, 10])
check('centre plus one recorded neighbour, soldered',
      molien((0,), 'S', 6) == [1, 2, 7, 12, 36, 60, 124])
FULL = (0, 1, 2, 3, 4, 5)
check('full neighbourhood, unsoldered SO(3)',
      molien(FULL, 'U', 6) == [1, 0, 5, 1, 34, 27, 230])
check('full neighbourhood, unsoldered O(3): odd degrees vanish',
      molien(FULL, 'U3', 6) == [1, 0, 5, 0, 34, 0, 230])
check('full neighbourhood, soldered',
      molien(FULL, 'S', 6) == [1, 1, 15, 69, 475, 2171, 9753])
check('soldering strictly enlarges the rule space at every positive degree',
      all(s > u for s, u in zip(molien(FULL, 'S', 6)[1:], molien(FULL, 'U', 6)[1:])))
check('no covariant rule term is linear in the vectors, unsoldered',
      all(molien(S, 'U', 3)[1] == 0 for S, _, _ in ST))
check('soldered linear terms match an independent Frobenius orbit count',
      all(molien(S, 'S', 1)[1] == lin_pred(S) for S, _, _ in ST))
check('soldered, one linear term where the barycentre vanishes, more where not',
      all((molien(S, 'S', 1)[1] >= 2) if S in DNZ else
          (molien(S, 'S', 1)[1] == (1 if S else 0)) for S, _, _ in ST))
check('independent route reproduces the unsoldered full-window counts',
      [indep_dim(FULL, 'U', d, 0) for d in (1, 2, 3)] == [0, 5, 1])
check('independent route reproduces the soldered full-window counts',
      [indep_dim(FULL, 'S', d, 0) for d in (1, 2, 3)] == [1, 15, 69])


# ============ 3. the same tables, stratum by stratum, both routes ===========
print('3. per-stratum tables and the independent recomputation')
TRIV = {S: (molien(S, 'U', 3), molien(S, 'U3', 3), molien(S, 'S', 3))
        for S, _, _ in ST}
VEC = {S: (molien(S, 'U', 3, out='vec'), molien(S, 'U3', 3, out='vec'),
           molien(S, 'S', 3, out='vec')) for S, _, _ in ST}
VL = {S: (molien(S, 'U', 3, out='veclat'), molien(S, 'S', 3, out='veclat'))
      for S, _, _ in ST}
check('scalar table, unsoldered SO(3)',
      [TRIV[S][0] for S, _, _ in ST] ==
      [[1, 0, 1, 0], [1, 0, 3, 0], [1, 0, 4, 0], [1, 0, 4, 0], [1, 0, 4, 2],
       [1, 0, 7, 1], [1, 0, 5, 0], [1, 0, 9, 4], [1, 0, 8, 4], [1, 0, 5, 1]])
check('scalar table, unsoldered O(3): every odd degree is empty',
      all(TRIV[S][1] == [TRIV[S][0][0], 0, TRIV[S][0][2], 0] for S, _, _ in ST))
check('scalar table, soldered',
      [TRIV[S][2] for S, _, _ in ST] ==
      [[1, 0, 1, 0], [1, 2, 7, 12], [1, 1, 10, 16], [1, 4, 25, 80],
       [1, 4, 26, 124], [1, 5, 43, 175], [1, 1, 21, 75], [1, 7, 64, 336],
       [1, 5, 46, 280], [1, 1, 15, 69]])
check('Bloch-valued table, unsoldered SO(3)',
      [VEC[S][0] for S, _, _ in ST] ==
      [[0, 1, 0, 1], [0, 2, 1, 6], [0, 2, 1, 10], [0, 2, 1, 10], [0, 2, 2, 14],
       [0, 3, 3, 24], [0, 2, 1, 16], [0, 3, 4, 39], [0, 3, 4, 37], [0, 2, 1, 17]])
check('Bloch-valued table, soldered',
      [VEC[S][2] for S, _, _ in ST] ==
      [[0, 1, 0, 2], [1, 6, 15, 44], [0, 5, 14, 67], [1, 14, 65, 250],
       [1, 12, 78, 364], [1, 19, 113, 553], [0, 7, 39, 265], [1, 23, 176, 1024],
       [1, 15, 126, 860], [0, 4, 25, 229]])
check('soldering identifies the lattice and internal vector representations',
      all(molien(S, 'S', 3, out='lat') == VEC[S][2] for S, _, _ in ST))
check('it does not identify them unsoldered',
      any(molien(S, 'U', 3, out='lat') != VEC[S][0] for S, _, _ in ST))
check('no occupancy-only Bloch response, unsoldered SO(3)',
      all(VEC[S][0][0] == 0 for S, _, _ in ST))
check('no occupancy-only Bloch response, unsoldered O(3)',
      all(VEC[S][1][0] == 0 for S, _, _ in ST))
check('one occupancy-only Bloch response soldered, exactly where d is nonzero',
      [S for S, _, _ in ST if VEC[S][2][0] == 1] == DNZ)
check('and none where the barycentre vanishes',
      all(VEC[S][2][0] == 0 for S, _, _ in ST if S not in DNZ))
check('no occupancy-only lattice-frame response, unsoldered',
      all(VL[S][0][0] == 0 for S, _, _ in ST))
check('a lattice-frame response appears at first order on every occupied stratum',
      all(VL[S][0][1] >= 1 for S, _, _ in ST if S))
check('soldered, the empty neighbourhood already carries a frame response',
      VL[()][1][0] == 1)
BAD = [(S, r, n) for S, _, _ in ST for r in ('U', 'S') for n in (0, 1)
       if [molien(S, r, 3, out=('triv' if n == 0 else 'vec'))[d] for d in (1, 2, 3)]
       != [indep_dim(S, r, d, n) for d in (1, 2, 3)]]
check('character sums and derivation kernels agree on all 120 dimensions',
      BAD == [])


def lscale_poly(f, c):
    """Scale every coefficient of a polynomial by the rational c."""
    return {m: v*c for m, v in f.items() if v*c}


def poly_sum(fs):
    """Sum a list of polynomials."""
    out = {}
    for f in fs:
        out = poly_add(out, f)
    return out


# ================= 4. explicit rule terms on each side of the fork ==========
print('4. explicit covariant rule terms and the frame a record registers')
S1 = {}
for i in range(6):
    for a in range(3):
        if DIRS[i][a]:
            S1 = poly_add(S1, {monomial([var(i+1, a)]): Fr(DIRS[i][a])})
check('the axis-weighted sum has one term per lattice axis direction',
      len(S1) == 6)
check('it is invariant under the soldered action',
      all(act_soldered(g, S1) == S1 for g in G))
check('it is not invariant under the unsoldered lattice action',
      any(act_unsoldered(g, S1) != S1 for g in G))
check('internal so(3) does not annihilate it',
      any(deriv(a, S1) for a in range(3)))
T = {}
for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            c = det3([DIRS[i], DIRS[j], DIRS[k]])
            if c:
                T = poly_add(T, lscale_poly(triple(i+1, j+1, k+1), Fr(c)))
check('the handed lattice term has 48 monomials', len(T) == 48)
check('it is annihilated by internal so(3)', not any(deriv(a, T) for a in range(3)))
check('it is invariant under the unsoldered lattice action',
      all(act_unsoldered(g, T) == T for g in G))
check('it is the unique unsoldered cubic invariant of degree three',
      molien(FULL, 'U', 3)[3] == 1)
check('and it is handed: no such invariant survives adding the inversion',
      molien(FULL, 'U3', 3)[3] == 0)
D2 = [dot(0, 0), poly_sum([dot(i, i) for i in range(1, 7)]),
      poly_sum([dot(0, i) for i in range(1, 7)]),
      poly_sum([dot(2*t+1, 2*t+2) for t in range(3)]),
      poly_sum([dot(i, j) for i in range(1, 7) for j in range(i+1, 7)
                if (i-1) ^ 1 != (j-1)])]
check('five explicit quadratic terms are unsoldered invariants',
      all(not any(deriv(a, f) for a in range(3)) and
          all(act_unsoldered(g, f) == f for g in G) for f in D2))
check('they are linearly independent', rank(D2) == 5)
check('and they span the whole quadratic unsoldered space',
      molien(FULL, 'U', 2)[2] == 5)
RZ = [[Fr(3, 5), Fr(-4, 5), Fr(0)], [Fr(4, 5), Fr(3, 5), Fr(0)],
      [Fr(0), Fr(0), Fr(1)]]
def tp(m):
    return tuple(tuple(m[b][a] for b in range(3)) for a in range(3))


check('the test internal rotation is a proper rotation',
      det3(RZ) == 1 and matmul(RZ, tp(RZ)) == ID)
QCFG = [[Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(1), Fr(0)], [Fr(0), Fr(0), Fr(1)],
        [Fr(1, 2), Fr(1, 2), Fr(0)], [Fr(0), Fr(1, 3), Fr(-2, 3)],
        [Fr(-1, 5), Fr(0), Fr(4, 5)]]


def frame(qs):
    return [[sum(Fr(DIRS[i][a])*qs[i][b] for i in range(6)) for b in range(3)]
            for a in range(3)]


def moved(qs, g, R):
    sp = slot_perm(g)
    out = [None]*6
    for i in range(6):
        out[sp[i]] = [sum(R[b][c]*qs[i][c] for c in range(3)) for b in range(3)]
    return out


check('the recorded frame transforms as a lattice-by-internal bimodule',
      all(tuple(map(tuple, frame(moved(QCFG, g, R)))) ==
          matmul(matmul(g, frame(QCFG)), tp(R))
          for g in G for R in (RZ, ID)))
check('the recorded frame is generically invertible',
      det3(frame(QCFG)) != 0)
check('so a record can register an identification the law does not supply',
      det3(frame(QCFG)) != 0 and molien(FULL, 'U', 1)[1] == 0)


# ================= 5. the empty-neighbourhood law on the Bloch sphere ======
print('5. the law at a site with no recorded neighbour')
SPH = {}
for rd in ('U', 'U3', 'S'):
    ser = molien((), rd, 10)
    SPH[rd] = [ser[d] - (ser[d-2] if d >= 2 else 0) for d in range(11)]
check('unsoldered, the sphere has no invariant past the constant to degree ten',
      SPH['U'] == [1] + [0]*10 and SPH['U3'] == SPH['U'])
check('soldered, a second invariant appears on the sphere at degree four',
      SPH['S'] == [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1])
check('neither reading has a linear or a non-constant quadratic sphere invariant',
      all(SPH[r][1] == 0 and SPH[r][2] == 0 for r in SPH))


def dfac(n):
    r = 1
    while n > 1:
        r, n = r*n, n-2
    return r


def haar(e):
    """Exact average of the monomial p^e over the rotation-invariant law on S^2."""
    if any(x % 2 for x in e):
        return Fr(0)
    a, b, c = (x//2 for x in e)
    return Fr(dfac(2*a-1)*dfac(2*b-1)*dfac(2*c-1), dfac(2*(a+b+c)+1))


AX = [tuple(s if i == a else 0 for i in range(3)) for a in range(3) for s in (1, -1)]


def sixax(e, R=None):
    pts = AX if R is None else [apply(R, v) for v in AX]
    return sum(Fr(1, 6)*v[0]**e[0]*v[1]**e[1]*v[2]**e[2] for v in pts)


PW = [(0, 0, 2), (0, 0, 4), (0, 0, 6)]
check('rotation-invariant even axial moments are 1/3, 1/5, 1/7',
      [haar(e) for e in PW] == [Fr(1, 3), Fr(1, 5), Fr(1, 7)])
check('and they match the one-dimensional projection integral',
      all(haar((0, 0, 2*c)) == Fr(1, 2*c+1) for c in range(1, 6)))
check('the rotation-invariant law normalises on the sphere at every order',
      all(sum(Fr(fact(n), fact(a)*fact(b)*fact(n-a-b))
              * haar((2*a, 2*b, 2*(n-a-b)))
              for a in range(n+1) for b in range(n+1-a)) == 1
          for n in range(1, 6)))
check('every odd moment of the rotation-invariant law vanishes',
      all(haar(e) == 0 for e in [(1, 0, 0), (0, 0, 1), (2, 1, 0), (1, 1, 1)]))
check('the six-axis law is invariant under the lattice rotations',
      all(sorted(apply(g, v) for v in AX) == sorted(AX) for g in G))
check('the six-axis law is not invariant under an internal rotation',
      sixax((0, 0, 4), RZ) + sixax((0, 4, 0), RZ) + sixax((4, 0, 0), RZ) != 1)
check('its even axial moments are all 1/3, unlike 1/3, 1/5, 1/7',
      [sixax(e) for e in PW] == [Fr(1, 3)]*3)
check('and it gives no weight to a mixed even monomial',
      sixax((2, 2, 0)) == 0 and haar((2, 2, 0)) == Fr(1, 15))
check('both laws give the fair antipodal coin along a lattice axis',
      Fr(1, 2)*(1 + haar((0, 0, 1))) == Fr(1, 2)
      and Fr(1, 2)*(1 + sixax((0, 0, 1))) == Fr(1, 2))
Q4H = sum(haar(tuple(4 if i == j else 0 for i in range(3))) for j in range(3))
Q4S = sum(sixax(tuple(4 if i == j else 0 for i in range(3))) for j in range(3))
check('the two laws separate first at the quartic axis sum, 3/5 against 1',
      Q4H == Fr(3, 5) and Q4S == 1)


# ================= 6. the witness pair =====================================
print('6. two rules that satisfy the axioms and differ on a recorded menu')
RX = ((1, 0, 0), (0, 0, -1), (0, 1, 0))
EZ = (Fr(0), Fr(0), Fr(1))
MU = (Fr(2, 3), Fr(2, 3), Fr(1, 3))
SUB = [tuple(r) for k in range(7) for r in
       [[i for i in range(6) if (msk >> i) & 1] for msk in range(64)]
       if len(r) == k]


def dA(rec, qs):
    """Model A: the barycentre of the lattice directions of the recorded slots."""
    if not rec:
        return (Fr(0),)*3
    return tuple(Fr(sum(DIRS[i][a] for i in rec), len(rec)) for a in range(3))


def dB(rec, qs):
    """Model B: the barycentre of the recorded neighbours' own Bloch vectors."""
    if not rec:
        return (Fr(0),)*3
    return tuple(sum(qs[i][a] for i in rec)/len(rec) for a in range(3))


def menu(model, rec, qs, m):
    """Antipodal menu along m under the barycentre selector [I + d.sigma/3]/2."""
    d = model(rec, qs)
    t = sum(d[a]*m[a] for a in range(3))/3
    return (Fr(1, 2)*(1+t), Fr(1, 2)*(1-t))


def act_sold(rec, qs, m, g):
    sp = slot_perm(g)
    nq = [None]*6
    for i in range(6):
        nq[sp[i]] = apply(g, qs[i])
    return tuple(sorted(sp[i] for i in rec)), nq, apply(g, m)


def act_slots(rec, qs, m, g):
    sp = slot_perm(g)
    nq = [None]*6
    for i in range(6):
        nq[sp[i]] = qs[i]
    return tuple(sorted(sp[i] for i in rec)), nq, m


def act_int(rec, qs, m, R):
    return rec, [apply(R, q) for q in qs], apply(R, m)


TQ = [(Fr(0),)*3 for _ in range(6)]
TQ[4] = (Fr(1), Fr(0), Fr(0))
check('the two models disagree on one recorded neighbour, 2/3 against 1/2',
      menu(dA, (4,), TQ, EZ) == (Fr(2, 3), Fr(1, 3))
      and menu(dB, (4,), TQ, EZ) == (Fr(1, 2), Fr(1, 2)))
check('and they agree on the empty neighbourhood, the fair coin',
      menu(dA, (), TQ, EZ) == menu(dB, (), TQ, EZ) == (Fr(1, 2), Fr(1, 2)))
check('every menu either model returns is a state on both readings',
      all(0 <= pr <= 1 and sum(menu(md, r, QCFG, mm)) == 1
          for md in (dA, dB) for r in SUB for mm in (EZ, MU)
          for pr in menu(md, r, QCFG, mm)))
check('model A is covariant under the soldered action, whole group and strata',
      all(menu(dA, *act_sold(r, QCFG, mm, g)) == menu(dA, r, QCFG, mm)
          for g in G for r in SUB for mm in (EZ, MU)))
check('that test is not vacuous: the soldered action moves the menu it returns',
      any(menu(dA, act_sold(r, QCFG, mm, g)[0], QCFG, mm) != menu(dA, r, QCFG, mm)
          for g in G for r in SUB for mm in (EZ, MU)))
check('model A is not covariant when the cubic rotation moves slots alone',
      any(menu(dA, *act_slots(r, QCFG, mm, g)) != menu(dA, r, QCFG, mm)
          for g in G for r in SUB for mm in (EZ, MU)))
check('the internal test rotation is proper and moves the menu direction',
      det3(RX) == 1 and matmul(RX, tp(RX)) == ID and apply(RX, EZ) != EZ)
check('model A is not covariant under an independent internal rotation',
      menu(dA, *act_int((4,), TQ, EZ, RX)) != menu(dA, (4,), TQ, EZ)
      and menu(dA, *act_int((4,), TQ, EZ, RX)) == (Fr(1, 2), Fr(1, 2)))
check('model B is covariant under independent internal rotations',
      all(menu(dB, *act_int(r, QCFG, mm, R)) == menu(dB, r, QCFG, mm)
          for R in (RX, RZ) for r in SUB for mm in (EZ, MU)))
check('model B is covariant under the cubic rotation acting on slots alone',
      all(menu(dB, *act_slots(r, QCFG, mm, g)) == menu(dB, r, QCFG, mm)
          for g in G for r in SUB for mm in (EZ, MU)))
check('model B is covariant under the soldered action as well',
      all(menu(dB, *act_sold(r, QCFG, mm, g)) == menu(dB, r, QCFG, mm)
          for g in G for r in SUB for mm in (EZ, MU)))
check('so the pair is separated by the soldering, not by the lattice symmetry',
      menu(dA, (4,), TQ, EZ) != menu(dB, (4,), TQ, EZ)
      and all(menu(dB, *act_slots(r, QCFG, EZ, g)) == menu(dB, r, QCFG, EZ)
              for g in G for r in SUB))


# ================= 7. can the parity roles and link orientation be law? =====
print('7. roles, translations, and where oriented link data can come from')
SITES = [v for v in product(range(2), repeat=3)]


def shift(v, t):
    return tuple((v[a] + t[a]) % 2 for a in range(3))


def orbits(points, group, act):
    seen, n = set(), 0
    for x in points:
        if x in seen:
            continue
        seen |= {act(x, t) for t in group}
        n += 1
    return n


PAR = {v: sum(v) % 2 for v in SITES}
ROLE = {v: v for v in SITES}
KEEP_PAR = [t for t in SITES if all(PAR[shift(v, t)] == PAR[v] for v in SITES)]
KEEP_ROLE = [t for t in SITES if all(ROLE[shift(v, t)] == ROLE[v] for v in SITES)]
check('translations act transitively on the sites of the parity cell',
      orbits(SITES, SITES, shift) == 1)
check('so a translation-covariant function of one site is constant',
      orbits(SITES, SITES, shift) == 1)
check('the staggered labelling keeps an index-two subgroup of translations',
      len(KEEP_PAR) == 4 and len(SITES)//len(KEEP_PAR) == 2)
check('translation-invariant functions of the parity class are the constants',
      orbits([0, 1], SITES, lambda c, t: (c + sum(t)) % 2) == 1)
check('the four-role labelling keeps the identity translation alone',
      KEEP_ROLE == [(0, 0, 0)] and len(SITES)//len(KEEP_ROLE) == 8)
NN = [d for d in DIRS]
NNN = [tuple(u[a] + w[a] for a in range(3)) for i, u in enumerate(DIRS)
       for w in DIRS[i+1:] if any(u[a] + w[a] for a in range(3))]
check('a nearest-neighbour step has parity weight one and flips the class',
      all(sum(abs(c) for c in d) == 1 for d in NN)
      and all(PAR[shift((0, 0, 0), tuple(c % 2 for c in d))] == 1 for d in NN))
check('a next-nearest step has parity weight two and preserves the class',
      len(NNN) == 12 and all(sum(abs(c) for c in d) == 2 for d in NNN)
      and all(PAR[shift((0, 0, 0), tuple(c % 2 for c in d))] == 0 for d in NNN))
check('so the roles separate sites the six-neighbour window identifies',
      len(KEEP_ROLE) < len(KEEP_PAR))
check('translation-invariant functions of an ordered site pair span eight',
      orbits([(u, w) for u in SITES for w in SITES], SITES,
             lambda x, t: (shift(x[0], t), shift(x[1], t))) == 8)


def inv3(m):
    dt = det3(m)
    cof = [[m[(b+1) % 3][(a+1) % 3]*m[(b+2) % 3][(a+2) % 3]
            - m[(b+1) % 3][(a+2) % 3]*m[(b+2) % 3][(a+1) % 3]
            for b in range(3)] for a in range(3)]
    return tuple(tuple(Fr(cof[a][b], 1)/dt for b in range(3)) for a in range(3))


M0 = frame(QCFG)
check('the registered frame inverts exactly', matmul(M0, inv3(M0)) == ID)
check('through it a lattice direction reads as an internal vector, unsoldered',
      all(apply(inv3(frame(moved(QCFG, g, R))), apply(g, n))
          == apply(R, apply(inv3(M0), n))
          for g in G for R in (ID, RZ, RX) for n in (DIRS[0], DIRS[4])))
check('and that reading is not available from the law alone',
      molien(FULL, 'U', 0, out='veclat')[0] == 0
      and molien(FULL, 'S', 0, out='veclat')[0] == 1)


# ================= summary ==================================================
for line in FAILED:
    print('FAIL: ' + line)
print('TOTAL: PASS=%d FAIL=%d' % (PASS, FAIL))
print('elapsed %.1f s' % (time.time() - T0))
