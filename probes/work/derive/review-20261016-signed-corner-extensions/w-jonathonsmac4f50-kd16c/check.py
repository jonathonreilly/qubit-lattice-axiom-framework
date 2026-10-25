#!/usr/bin/env python3
"""Signed corner actions of the 2x2x2 block: exhaustive classification of the central
extensions realised, with exact representatives and induced characters for the
GL(2,3) class (the spinorial class that is NOT the prescribed binary octahedral lift).

Setting (supplied, not axioms): 8 corners of a block, the 24 proper cubic rotations act
about the block centre by permuting corners; a lift is a signed permutation matrix
D(R) = diag(s) P(R) (or P(R) diag(s)).  Everything below is exact integer / Fraction /
sympy arithmetic; no floating point is used for any finite claim.

Run:  python3 check.py          (checks only)
      python3 check.py --tables (also print the detailed tables used in ATTEMPT.md)
"""
import itertools
import sys
from collections import Counter, defaultdict
from fractions import Fraction

import numpy as np
import sympy as sp

TABLES = '--tables' in sys.argv
PASS = FAIL = 0


def check(name, ok):
    global PASS, FAIL
    if ok:
        PASS += 1
        print('PASS ' + name)
    else:
        FAIL += 1
        print('FAIL ' + name)


def table(*lines):
    if TABLES:
        for l in lines:
            print('  | ' + str(l))


# ---------------------------------------------------------------- rotations and corners
def rotations():
    out = []
    for p in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            R = [[0] * 3 for _ in range(3)]
            for i in range(3):
                R[i][p[i]] = sg[i]
            R = tuple(map(tuple, R))
            if int(round(np.linalg.det(np.array(R)))) == 1:
                out.append(R)
    return out


ROTS = rotations()
RIDX = {R: i for i, R in enumerate(ROTS)}


def rmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)) for i in range(3))


RID = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
CORNERS = list(itertools.product((0, 1), repeat=3))


def cidx(v):
    return 4 * v[0] + 2 * v[1] + v[2]


def permR(R):
    img = []
    for v in CORNERS:
        w = [sum(R[i][j] * (2 * v[j] - 1) for j in range(3)) for i in range(3)]
        img.append(cidx(tuple((x + 1) // 2 for x in w)))
    return tuple(img)


RZ = ((0, -1, 0), (1, 0, 0), (0, 0, 1))      # quarter turn about z (sources' RZ)
RX = ((1, 0, 0), (0, 0, -1), (0, 1, 0))      # quarter turn about x (sources' RX)
C3 = ((0, 0, 1), (1, 0, 0), (0, 1, 0))       # threefold about (1,1,1) (independent check's B_t)

# signed permutation: tuple x of length 8, e_i -> sign(x_i) e_{|x_i|-1}
ID = tuple(range(1, 9))


def smul(A, B):          # (A B) e_i = A (B e_i)
    return tuple((A[abs(x) - 1] if x > 0 else -A[abs(x) - 1]) for x in B)


def sinv(A):
    out = [0] * 8
    for i, x in enumerate(A):
        out[abs(x) - 1] = (i + 1) if x > 0 else -(i + 1)
    return tuple(out)


def sneg(A):
    return tuple(-x for x in A)


def sperm(A):
    return tuple(abs(x) - 1 for x in A)


def strace(A):
    return sum((1 if x > 0 else -1) for i, x in enumerate(A) if abs(x) - 1 == i)


def spow(A, n):
    h = ID
    for _ in range(n):
        h = smul(h, A)
    return h


def sorder(A):
    h, n = A, 1
    while h != ID:
        h = smul(h, A)
        n += 1
    return n


def smat(A):
    M = np.zeros((8, 8), dtype=int)
    for i, x in enumerate(A):
        M[abs(x) - 1, i] = 1 if x > 0 else -1
    return M


def D_target(R, s):      # D = diag(s) P : sign attached to the TARGET corner (blockrep.py)
    P = permR(R)
    return tuple((P[i] + 1) * s[P[i]] for i in range(8))


def D_source(R, s):      # D = P diag(s) : sign attached to the SOURCE corner (independent check)
    P = permR(R)
    return tuple((P[i] + 1) * s[i] for i in range(8))


def gen(gens, cap=49):
    G = {ID}
    fr = [ID]
    while fr:
        nx = []
        for A in fr:
            for g in gens:
                B = smul(A, g)
                if B not in G:
                    G.add(B)
                    nx.append(B)
                    if len(G) >= cap:
                        return None
        fr = nx
    return G


SIGNS = list(itertools.product((1, -1), repeat=8))
PERMKEY = {permR(R): R for R in ROTS}
AXIS_C2 = [R for R in ROTS if sum(R[i][i] for i in range(3)) == -1 and all(abs(R[i][i]) == 1 for i in range(3))]
EDGE_C2 = [R for R in ROTS if sum(R[i][i] for i in range(3)) == -1 and any(R[i][i] == 0 for i in range(3))]
RIDENT_PERM = permR(RID)


def lifts_by_rotation(G):
    d = defaultdict(list)
    for g in G:
        d[PERMKEY[sperm(g)]].append(g)
    return d


def invariants(G):
    """(a, e): does a lift of an axis C2 / an edge C2 square to -I ?  None if not constant."""
    d = lifts_by_rotation(G)
    sq = lambda R: {spow(g, 2) for g in d[R]}
    a = set()
    e = set()
    for R in AXIS_C2:
        a |= sq(R)
    for R in EDGE_C2:
        e |= sq(R)
    if len(a) != 1 or len(e) != 1:
        return None
    return (1 if sneg(ID) in a else 0, 1 if sneg(ID) in e else 0)


NAMES = {(0, 0): 'S4 x C2', (0, 1): 'A4 x| C4', (1, 0): 'GL(2,3)', (1, 1): '2O (binary octahedral)'}


def enumerate_groups(Df, ra, rb):
    """all 2^16 raw sign choices; return counts and the set of generated groups of order 24/48."""
    cnt = Counter()
    groups = {}
    for sa in SIGNS:
        a = Df(ra, sa)
        for sb in SIGNS:
            b = Df(rb, sb)
            G = gen([a, b])
            if G is None:
                cnt['big'] += 1
            else:
                cnt[len(G)] += 1
                groups.setdefault(frozenset(G), (sa, sb))
    return cnt, groups


# ---------------------------------------------------------------- linear algebra over F2
def f2_rank(rows):
    basis = {}
    r = 0
    for v in rows:
        while v:
            h = v.bit_length() - 1
            if h in basis:
                v ^= basis[h]
            else:
                basis[h] = v
                r += 1
                break
    return r


def main():
    # ------------------------------------------------------------ S0 setting
    closed = all(rmul(A, B) in RIDX for A in ROTS for B in ROTS)
    hom = all(permR(rmul(A, B)) == tuple(permR(A)[permR(B)[i]] for i in range(8)) for A in ROTS for B in ROTS)
    orbit0 = {permR(R)[0] for R in ROTS}
    stab0 = [R for R in ROTS if permR(R)[0] == 0]
    faithful = len({permR(R) for R in ROTS}) == 24
    check('S0 24 proper cubic rotations form a group, act on the 8 block corners as a faithful homomorphism, '
          'transitively, corner stabiliser of order 3 (C3 about a body diagonal)',
          len(ROTS) == 24 and closed and hom and faithful and len(orbit0) == 8 and len(stab0) == 3)

    # ------------------------------------------------------------ S1 exhaustive enumeration
    cntT, grT = enumerate_groups(D_target, RZ, RX)
    cntS, grS = enumerate_groups(D_source, RZ, RX)
    check('S1a exhaustive: all 65536 raw pairs of corner-sign vectors (sign on target, sources\' (RZ,RX) generators) '
          'generate a group of order 24 (128 pairs), 48 (896 pairs) or more than 48 (64512 pairs); no other order occurs; '
          f'counts {dict(cntT)}',
          cntT == Counter({24: 128, 48: 896, 'big': 64512}))
    check('S1b same exhaustive count with the sign attached to the source corner (independent check\'s convention): '
          f'{dict(cntS)}, and the set of generated groups of order 24/48 is IDENTICAL as a set of subgroups of the signed-permutation group '
          f'({len(grT)} subgroups)',
          cntS == cntT and set(grT) == set(grS))
    cntC, grC = enumerate_groups(D_target, RZ, C3)
    check('S1c same with the generator pair (quarter turn RZ, threefold C3(111)) used by the independent check: '
          f'{dict(cntC)}; the set of generated groups of order 24/48 equals the (RZ,RX) set -> the classification does not depend on '
          'the generator pair or on the target/source sign convention',
          cntC == cntT and set(grC) == set(grT))
    g24 = [G for G in grT if len(G) == 24]
    g48 = [G for G in grT if len(G) == 48]
    kern_ok = all(len([g for g in G if sperm(g) == RIDENT_PERM]) == len(G) // 24 and
                  {g for g in G if sperm(g) == RIDENT_PERM} <= {ID, sneg(ID)} for G in grT)
    check(f'S1d every generated group of order <= 48 has diagonal kernel K = G cap (diagonal signs) of order |G|/24, K inside {{+I,-I}}: '
          f'{len(g24)} groups with K = 1 and {len(g48)} groups with K = {{+-I}} (central extensions of O by Z2); '
          'a group of order > 48 has |K| >= 4, i.e. a non-scalar diagonal sign matrix acting as the identity rotation',
          kern_ok and len(g24) == 128 and len(g48) == 256 and all(sneg(ID) in G for G in g48))

    # ------------------------------------------------------------ S2 classes
    inv48 = {G: invariants(G) for G in g48}
    fib = Counter(inv48.values())
    check('S2a the invariant (a,e) = (does an axis-C2 lift square to -I, does an edge-C2 lift square to -I) is constant on '
          'every axis/edge class of every one of the 256 groups, and takes all four values (0,0),(0,1),(1,0),(1,1) exactly 64 times each: '
          f'{dict(fib)}',
          None not in fib and set(fib) == {(0, 0), (0, 1), (1, 0), (1, 1)} and all(v == 64 for v in fib.values()))
    gauges = [tuple(g) for g in SIGNS]

    def conj(G, g):
        gd = tuple((i + 1) * g[i] for i in range(8))   # diag(g): e_i -> g_i e_i ; self-inverse
        return frozenset(smul(smul(gd, x), gd) for x in G)

    orbit_ok = True
    stab_sizes = {}
    orbit_sizes = {}
    for cls in sorted(fib):
        members = {G for G in g48 if inv48[G] == cls}
        G0 = next(iter(members))
        orb = {conj(G0, g) for g in gauges}
        orbit_sizes[cls] = len(orb)
        stab_sizes[cls] = sum(1 for g in gauges if conj(G0, g) == G0)
        orbit_ok &= (orb == members)
    check('S2b each (a,e) fibre is ONE orbit under the 256 diagonal sign conjugations: orbit sizes '
          f'{orbit_sizes} = 256 / stabiliser sizes {stab_sizes} (the stabiliser is {{+-I, +-diag(v_eps)}}, v_eps = the eps-twisted sign vector); '
          'hence exactly four diagonal-sign gauge classes of projective signed corner actions',
          orbit_ok and all(v == 64 for v in orbit_sizes.values()) and all(v == 4 for v in stab_sizes.values()))
    G24orb = {conj(g24[0], g) for g in gauges}
    split_ok = (G24orb == set(g24)) and all(inv48[frozenset(set(G) | {sneg(x) for x in G})] == (0, 0) for G in g24)
    check('S2c the 128 honest (K = 1) lifts form one conjugation orbit (the permutation representation P(O) up to diagonal sign gauge), '
          'and each, enlarged by -I, lies in the class (0,0); so there are 5 classes of generated matrix groups '
          '(O; S4xC2; A4x|C4; GL(2,3); 2O) but 4 classes of projective actions',
          split_ok)

    # element-order histograms and names
    hist = {}
    for cls in sorted(fib):
        G = next(G for G in g48 if inv48[G] == cls)
        hist[cls] = dict(sorted(Counter(sorder(g) for g in G).items()))
    table(*[f'{cls} {NAMES[cls]} element orders {h}' for cls, h in hist.items()])
    only_inv_2O = [c for c, h in hist.items() if h.get(2) == 1]
    check('S2d element-order histograms of the four classes are pairwise different; (1,1) is the only one with a single involution '
          '(-I): the binary octahedral group 2O; (1,0) has 13 involutions and 12 elements of order 8: ' + str(hist),
          len({tuple(h.items()) for h in hist.values()}) == 4 and only_inv_2O == [(1, 1)] and hist[(1, 0)] == {1: 1, 2: 13, 3: 8, 4: 6, 6: 8, 8: 12})

    s4 = list(itertools.permutations(range(4)))
    def pord(p):
        q, n = p, 1
        while q != tuple(range(4)):
            q = tuple(p[i] for i in q)
            n += 1
        return n
    s4c2 = Counter(max(pord(p), 1) if z == 0 else (pord(p) if pord(p) % 2 == 0 else 2 * pord(p)) for p in s4 for z in (0, 1))
    check('S2f the class (0,0) has the element-order histogram of S4 x C2 computed independently from permutations of 4 points '
          f'({dict(sorted(s4c2.items()))}); the class (1,0) is shown to be GL(2,3) by explicit isomorphism (S4b); (0,1) is identified only by its (a,e) '
          'data and order histogram (the Majorana note calls this extension A4 x| Z4; not re-derived here)',
          dict(sorted(s4c2.items())) == hist[(0, 0)])

    # runner key (trace data) merges classes
    def trace_key(G):
        return (len(G), len(G) == 48 and any(sorder(g) == 8 for g in G), tuple(sorted(strace(g) for g in G)))
    keys = {}
    for G in g24[:1] + [next(G for G in g48 if inv48[G] == c) for c in sorted(fib)]:
        keys.setdefault(trace_key(G), []).append(inv48.get(G, 'O'))
    check('S2e the source runner\'s key (group order, spinorial flag, sorted traces) gives exactly 3 keys: it merges (0,0) with (0,1) '
          'and (1,0) with (1,1), and its docstring\'s "five classes, two spinorial" counts generated group types; '
          f'keys -> {list(keys.values())}',
          len(keys) == 3 and sorted(map(sorted, [[str(x) for x in v] for v in keys.values()])) ==
          sorted(map(sorted, [['O'], ['(0, 0)', '(0, 1)'], ['(1, 0)', '(1, 1)']])))

    first = None
    for sz_ in SIGNS:                       # the source runner's loop order: sz outer, sx inner, +1 before -1
        a_ = D_target(RZ, sz_)
        for sx_ in SIGNS:
            G_ = gen([a_, D_target(RX, sx_)])
            if G_ is not None and len(G_) == 48 and sorder(a_) == 8:
                first = (sz_, sx_, invariants(G_))
                break
        if first:
            break
    check('S2g the only spinorial representative the source runner keeps (classes.setdefault on its trace key, first hit in its loop order) is '
          f's_Z = {first[0]}, s_X = {first[1]}, which lies in the class {first[2]} = 2O; the GL(2,3) class (1,0) is never separately tested by that runner '
          '(its trace key coincides with the 2O key)',
          first is not None and first[2] == (1, 1))

    # ------------------------------------------------------------ S3 cohomology
    idx = {R: i for i, R in enumerate(sorted(ROTS, key=lambda R: (R != RID, R)))}   # identity -> 0
    elems = sorted(ROTS, key=lambda R: (R != RID, R))
    mul = [[idx[rmul(elems[i], elems[j])] for j in range(24)] for i in range(24)]
    nv = 23 * 23

    def var(x, y):
        return (x - 1) * 23 + (y - 1)

    eqs = []
    for x in range(24):
        for y in range(24):
            for z in range(24):
                v = 0
                for (p, q) in ((y, z), (mul[x][y], z), (x, mul[y][z]), (x, y)):
                    if p != 0 and q != 0:
                        v ^= 1 << var(p, q)
                if v:
                    eqs.append(v)
    rank_z = f2_rank(eqs)
    dimZ = nv - rank_z
    bnd = []
    for k in range(1, 24):
        v = 0
        for x in range(1, 24):
            for y in range(1, 24):
                if ((x == k) + (y == k) + (mul[x][y] == k)) % 2:
                    v |= 1 << var(x, y)
        bnd.append(v)
    rank_b = f2_rank(bnd)
    check(f'S3a H^2(O, F2) computed by F2 linear algebra on normalised cochains of the 24 rotations: dim Z^2 = {dimZ}, dim B^2 = {rank_b}, '
          f'dim H^2 = {dimZ - rank_b} (so exactly 4 central extensions of O by Z2 up to equivalence)',
          dimZ == 24 and rank_b == 22 and dimZ - rank_b == 2)

    def cocycle_vec(G):
        sect = {}
        for g in G:
            if g[0] > 0:
                sect[PERMKEY[sperm(g)]] = g
        assert len(sect) == 24
        bits = 0
        ok_cocycle_form = True
        for x in range(1, 24):
            for y in range(1, 24):
                prod = smul(sect[elems[x]], sect[elems[y]])
                tgt = sect[elems[mul[x][y]]]
                if prod == tgt:
                    pass
                elif prod == sneg(tgt):
                    bits |= 1 << var(x, y)
                else:
                    ok_cocycle_form = False
        return bits, ok_cocycle_form

    reps = {c: next(G for G in g48 if inv48[G] == c) for c in sorted(fib)}
    omega = {}
    form_ok = True
    for c, G in reps.items():
        omega[c], f_ok = cocycle_vec(G)
        form_ok &= f_ok
    is_cocycle = all(all(bin(e & omega[c]).count('1') % 2 == 0 for e in eqs) for c in omega)
    in_B = {c: f2_rank(bnd + [omega[c]]) == rank_b for c in omega}
    check('S3b the four section-cocycles omega_c(R,R\') = D(R)D(R\')D(RR\')^-1 in {+-1} (section: lift with positive image of e_0) '
          'satisfy the cocycle identity exactly; only the class (0,0) is a coboundary: ' + str(in_B),
          form_ok and is_cocycle and [c for c, v in in_B.items() if v] == [(0, 0)])
    sums_ok = True
    for c1 in omega:
        for c2 in omega:
            c3 = ((c1[0] + c2[0]) % 2, (c1[1] + c2[1]) % 2)
            diff = omega[c1] ^ omega[c2] ^ omega[c3]
            sums_ok &= f2_rank(bnd + [diff]) == rank_b
    check('S3c the map (a,e) -> [omega] in H^2(O,F2) is a group isomorphism Z2^2 -> H^2 (omega_c1 + omega_c2 + omega_{c1+c2} is a coboundary '
          'for all 16 pairs; the four classes are pairwise distinct): the signed corner actions realise EVERY central extension of O by Z2',
          sums_ok and all((f2_rank(bnd + [omega[c1] ^ omega[c2]]) == rank_b) == (c1 == c2) for c1 in omega for c2 in omega))

    # sign character eps of O = S4 (parity on the 4 body diagonals)
    diags = [frozenset({cidx(v), cidx(tuple(1 - x for x in v))}) for v in CORNERS if v[0] == 0]

    def eps(R):
        P = permR(R)
        perm = [diags.index(frozenset(P[i] for i in d)) for d in diags]
        inv = sum(1 for i in range(4) for j in range(i + 1, 4) if perm[i] > perm[j])
        return inv % 2

    eps_hom = all(eps(rmul(A, B)) == (eps(A) + eps(B)) % 2 for A in ROTS for B in ROTS)
    eps_vec = 0
    for x in range(1, 24):
        for y in range(1, 24):
            if eps(elems[x]) * eps(elems[y]):
                eps_vec |= 1 << var(x, y)
    rel_ok = all(f2_rank(bnd + [omega[(a, e)] ^ omega[(a, 1 - e)] ^ eps_vec]) == rank_b for a in (0, 1) for e in (0, 1))
    check('S3d eps = sign character of O = S4 (parity on the 4 body diagonals) is a homomorphism, odd exactly on quarter turns and edge half-turns; '
          'the cup square eps U eps is a nontrivial class and omega_(a,e) + omega_(a,1-e) = eps U eps up to coboundary (i.e. multiplying odd lifts '
          'by i flips the edge-C2 invariant e and fixes a): 2O <-> GL(2,3), S4xC2 <-> A4x|C4',
          eps_hom and sum(eps(R) for R in ROTS) == 12 and f2_rank(bnd + [eps_vec]) == rank_b + 1 and rel_ok)

    # Schur class (phase-gauge invariant): commutator of lifts of two commuting axis half-turns
    kap = {}
    for c, G in reps.items():
        L = lifts_by_rotation(G)
        rx, ry = rmul(RZ, RZ), rmul(RX, RX)
        A, B = L[rx][0], L[ry][0]
        com = smul(smul(A, B), sinv(smul(B, A)))
        kap[c] = 1 if com == ID else -1
    check('S3e Schur invariant kappa = commutator of lifts of two perpendicular axis half-turns is +-I independent of scalar twists and of the choice of lifts: '
          f'kappa = {kap}: kappa = -1 exactly when a = 1, so up to per-rotation phases there are only two projective classes '
          '(H^2(S4,U(1)) = Z2): integer {(0,0),(0,1)} and spinorial {(1,0),(1,1)}',
          all(kap[c] == (-1 if c[0] else 1) for c in kap))

    # ------------------------------------------------------------ S4 the GL(2,3) class
    GLc = (1, 0)
    # canonical representative: first pair in itertools sign order (+1 before -1) that generates a GL(2,3)-class group
    sa = sb = None
    for A_ in SIGNS:
        for B_ in SIGNS:
            G_ = gen([D_target(RZ, A_), D_target(RX, B_)])
            if G_ is not None and len(G_) == 48 and invariants(G_) == GLc:
                sa, sb = A_, B_
                break
        if sa:
            break
    a = D_target(RZ, sa)
    b = D_target(RX, sb)
    G = gen([a, b])
    table(f'GL(2,3) representative: s_Z = {sa}, s_X = {sb}  (D = diag(s) P(R), sign on target corner; corner index 4v0+2v1+v2)',
          'D(RZ) as signed permutation e_i -> sign*e_j (1-based, + / -): ' + str(a),
          'D(RX) as signed permutation: ' + str(b))
    rel = {'a^4': spow(a, 4) == sneg(ID), 'b^4': spow(b, 4) == sneg(ID), 'a^8': spow(a, 8) == ID,
           '(ab)^3 = +-I?': smul(smul(a, b), smul(smul(a, b), smul(a, b))) in (ID, sneg(ID)),
           'a^2 b^2 order': sorder(smul(spow(a, 2), spow(b, 2)))}
    table('relations ' + str(rel), 'order of a, b, ab: ' + str((sorder(a), sorder(b), sorder(smul(a, b)))))
    check('S4a GL(2,3)-class representative (first pair in sign order generating the class (1,0)): D(RZ)^4 = D(RX)^4 = -I, order 8 each; '
          'the generated group has 48 elements, contains -I as its only central involution, with orders ' + str(hist[GLc]),
          len(G) == 48 and spow(a, 4) == sneg(ID) and spow(b, 4) == sneg(ID) and sorder(a) == 8 and sorder(b) == 8 and invariants(G) == GLc)

    # explicit isomorphism with GL(2, F3)
    GL3 = [(p, q, r, s) for p, q, r, s in itertools.product(range(3), repeat=4) if (p * s - q * r) % 3]
    mm = lambda X, Y: ((X[0] * Y[0] + X[1] * Y[2]) % 3, (X[0] * Y[1] + X[1] * Y[3]) % 3,
                       (X[2] * Y[0] + X[3] * Y[2]) % 3, (X[2] * Y[1] + X[3] * Y[3]) % 3)
    iso_found = None
    for A_ in GL3:
        for B_ in GL3:
            phi = {ID: (1, 0, 0, 1)}
            fr = [ID]
            ok = True
            while fr and ok:
                nx = []
                for g in fr:
                    for gg, MM in ((a, A_), (b, B_)):
                        h = smul(g, gg)
                        M = mm(phi[g], MM)
                        if h in phi:
                            if phi[h] != M:
                                ok = False
                                break
                        else:
                            phi[h] = M
                            nx.append(h)
                    if not ok:
                        break
                fr = nx
            if ok and len(phi) == 48 and len(set(phi.values())) == 48:
                iso_found = (A_, B_)
                break
        if iso_found:
            break
    check(f'S4b explicit isomorphism of the generated group with GL(2,F3) (words in D(RZ), D(RX) -> matrices; D(RZ) -> {iso_found[0] if iso_found else None}, '
          f'D(RX) -> {iso_found[1] if iso_found else None} mod 3): well defined, bijective onto all 48 invertible 2x2 matrices over F3, so the class (1,0) is GL(2,3)',
          iso_found is not None)

    # conjugacy classes and induced character
    Gl = sorted(G)
    ginv = {g: sinv(g) for g in Gl}
    seen = set()
    ccls = []
    for g in Gl:
        if g in seen:
            continue
        cl = {smul(smul(h, g), ginv[h]) for h in Gl}
        seen |= cl
        ccls.append(sorted(cl))
    chi = lambda g: strace(g)
    rows = []
    for cl in ccls:
        g = cl[0]
        rows.append((len(cl), sorder(g), chi(g)))
    rows.sort(key=lambda r: (r[1], r[2]))
    ip = sum(Fraction(len(cl) * chi(cl[0]) ** 2) for cl in ccls) / 48
    table('conjugacy classes (size, element order, chi_rho = trace of the 8x8 signed matrix): ' + str(rows),
          f'<chi,chi> = {ip}')
    supp_ok = all((chi(g) == 0) for g in Gl if sorder(g) not in (1, 2, 3, 6) or (sorder(g) == 2 and g != sneg(ID)))
    check(f'S4c GL(2,3)-class induced character chi_rho (trace of the 8x8 matrices) has 8 conjugacy classes {rows}; support only on {{+-I}} and the order-3/6 elements '
          f'(values +-8, +2, -2); <chi,chi> = {ip}',
          len(ccls) == 8 and ip == 4 and supp_ok and sorted(rows) == sorted([(1, 1, 8), (1, 2, -8), (8, 3, 2), (8, 6, -2), (12, 2, 0), (6, 4, 0), (6, 8, 0), (6, 8, 0)]))

    # stabiliser, Frobenius
    H = [g for g in Gl if abs(g[0]) == 1]
    chiH = {h: (1 if h[0] > 0 else -1) for h in H}
    hom_ok = all(chiH[smul(h1, h2)] == chiH[h1] * chiH[h2] for h1 in H for h2 in H)
    gen6 = [h for h in H if sorder(h) == 6]
    cyc = len(H) == 6 and bool(gen6) and {spow(gen6[0], k) for k in range(6)} == set(H)
    trans = {}
    for g in Gl:
        v = abs(g[0]) - 1
        if g[0] > 0 and v not in trans:
            trans[v] = g
    frob_ok = len(trans) == 8
    for g in Gl:
        tot = 0
        for v in range(8):
            h = smul(smul(ginv[trans[v]], g), trans[v])      # t_v^-1 g t_v
            if abs(h[0]) == 1:                                  # inside the stabiliser of corner 0
                tot += chiH[h]
        frob_ok &= (tot == chi(g))
    check('S4d stabiliser H of corner e_0 in the GL(2,3)-class group is cyclic of order 6 (preimage of the corner C3), the entry chi(h) of D(h) on e_0 is a homomorphism '
          'H -> {+-1} with chi(-I) = -1 and chi(generator) = -1 (the real odd C6 character; it is the unique real character of C6 with chi(-I) = -1); '
          'Frobenius induction formula over the 8 coset representatives reproduces tr D(g) for all 48 elements: rho = Ind_H^G chi',
          hom_ok and cyc and chiH[gen6[0]] == -1 and chiH[sneg(ID)] == -1 and frob_ok)

    # exact commutant
    def commutant_data(gens):
        n = 8
        unknown = [(i, j) for i in range(n) for j in range(n)]
        rowsL = []
        for g in gens:
            M = smat(g)
            for k in range(n):
                for l in range(n):
                    row = [0] * (n * n)
                    for i in range(n):
                        if M[i, l]:
                            row[k * n + i] += int(M[i, l])        # X[k,i] M[i,l]
                    for j in range(n):
                        if M[k, j]:
                            row[j * n + l] -= int(M[k, j])        # M[k,j] X[j,l]
                    if any(row):
                        rowsL.append(row)
        A = sp.Matrix(rowsL)
        ns = A.nullspace()
        basis = [sp.Matrix(n, n, list(v)) for v in ns]
        d = len(basis)
        cs = sp.symbols('c0:%d' % d)
        X = sp.zeros(n, n)
        for c_, m_ in zip(cs, basis):
            X += c_ * m_
        eqz = []
        for m_ in basis:
            eqz += list(X * m_ - m_ * X)
        Az = sp.Matrix([[sp.diff(e_, c_) for c_ in cs] for e_ in eqz])
        return d, len(Az.nullspace())

    cd = commutant_data([a, b])
    V_ch = [(sz_, o_, c_ // 2) for (sz_, o_, c_) in rows]
    ipV = sum(Fraction(sz_ * (c_ // 2) ** 2) for (sz_, o_, c_) in rows) / 48
    check(f'S4e exact (rational) commutant of the 8-dim GL(2,3)-class representation: dimension {cd[0]}, centre dimension {cd[1]}; '
          f'a 4-dim semisimple algebra with 1-dim centre is M_2(C), so rho = V (x) C^2 with V irreducible of dimension 4 '
          f'(character chi_V = chi_rho / 2 = {V_ch}, <chi_V,chi_V> = {ipV}): two copies of the faithful 4-dim irrep of GL(2,3)',
          cd == (4, 1) and ipV == 1)

    allcd = {}
    for c, GG in reps.items():
        A_ = next(iter(sorted(GG)))
        # generators: lifts of RZ and RX in GG
        L = lifts_by_rotation(GG)
        allcd[c] = commutant_data([L[RZ][0], L[RX][0]])
    check('S4f exact commutant (dim, centre dim) of the signed 8-dim representation for all four classes: ' + str(allcd) +
          ' -> the integer classes (0,0),(0,1) are multiplicity-free sums of four irreps (commutative commutant C^4), the spinorial classes (1,0),(1,1) '
          'are 2 x (one 4-dim irrep); 2O: V = H = spin 3/2',
          allcd == {(0, 0): (4, 4), (0, 1): (4, 4), (1, 0): (4, 1), (1, 1): (4, 1)})

    adch = {}
    for c, GG in reps.items():
        L = lifts_by_rotation(GG)
        adch[c] = tuple(strace(L[R][0]) ** 2 for R in elems)
    check('S4g conjugation (adjoint) character |tr D(R)|^2 on the 24 rotations is the same for all four classes (it equals the square of the corner-permutation character), '
          'so every covariance statement that only involves D W D^dagger sees the same O-representation on M_8 in all four classes',
          len(set(adch.values())) == 1)

    # phase-gauge equivalence 2O <-> GL(2,3)
    G2 = reps[(1, 1)]
    # first pair for 2O
    pr2 = None
    for A_ in SIGNS:
        for B_ in SIGNS:
            G_ = gen([D_target(RZ, A_), D_target(RX, B_)])
            if G_ is not None and len(G_) == 48 and invariants(G_) == (1, 1):
                pr2 = (A_, B_)
                break
        if pr2:
            break
    a2, b2 = D_target(RZ, pr2[0]), D_target(RX, pr2[1])
    # try gauge g in {1,i,-1,-i}^8 with g0 = 1 and unit scalars lam in {1,i,-1,-i}
    A2c, B2c, Agc, Bgc = [smat(x).astype(complex) for x in (a2, b2, a, b)]
    found = []
    for gv in itertools.product([1, 1j, -1, -1j], repeat=7):
        gg = np.array((1,) + gv)
        Gm, Gi = np.diag(gg), np.diag(gg.conj())
        lam = []
        ok = True
        for DG, D2 in ((Agc, A2c), (Bgc, B2c)):
            M = Gm @ DG @ Gi
            k = tuple(np.argwhere(np.abs(D2) > 0.5)[0])
            l_ = M[k] / D2[k]
            if not np.array_equal(M, l_ * D2):    # all entries are exact small Gaussian integers
                ok = False
                break
            lam.append(l_)
        if ok:
            found.append((gg, lam))
    gg, lam = found[0]
    table('2O representative signs: ' + str(pr2), 'diagonal phase gauge g = ' + str(list(gg)) + ' scalars lambda = ' + str(lam))
    check(f'S4h phase-gauge equivalence: there are {len(found)} diagonal gauges g in {{1,i,-1,-i}}^8 (g_0 = 1) with g D_GL(R) g^dagger = lambda(R) D_2O(R) for both generators, '
          f'lambda = {[complex(x) for x in lam]} (odd rotations get a factor +-i); [real sign gauges cannot do this: S2a/S2b]. Hence the two spinorial classes are equivalent as PROJECTIVE (conjugation) '
          'actions, not as central extensions (a,e differ in e)',
          len(found) >= 1 and all(abs(abs(l_) - 1) < 1e-12 and abs(l_ ** 2 + 1) < 1e-12 for l_ in lam))
    # integer pair
    int_pr = []
    for c in ((0, 0), (0, 1)):
        for A_ in SIGNS:
            for B_ in SIGNS:
                G_ = gen([D_target(RZ, A_), D_target(RX, B_)])
                if G_ is not None and len(G_) == 48 and invariants(G_) == c:
                    int_pr.append((A_, B_))
                    break
            else:
                continue
            break
    (p0, p1) = int_pr
    P0 = [smat(D_target(RZ, p0[0])).astype(complex), smat(D_target(RX, p0[1])).astype(complex)]
    P1 = [smat(D_target(RZ, p1[0])).astype(complex), smat(D_target(RX, p1[1])).astype(complex)]
    found_int = 0
    for gv in itertools.product([1, 1j, -1, -1j], repeat=7):
        gg_ = np.array((1,) + gv)
        Gm, Gi = np.diag(gg_), np.diag(gg_.conj())
        ok = True
        for X, Y in zip(P1, P0):
            M = Gm @ X @ Gi
            k = tuple(np.argwhere(np.abs(Y) > 0.5)[0])
            if not np.array_equal(M, (M[k] / Y[k]) * Y):
                ok = False
                break
        found_int += ok
    cross = 0
    for gv in itertools.product([1, 1j, -1, -1j], repeat=7):
        gg_ = np.array((1,) + gv)
        Gm, Gi = np.diag(gg_), np.diag(gg_.conj())
        ok = True
        for X, Y in zip(P0, [A2c, B2c]):
            M = Gm @ X @ Gi
            k = tuple(np.argwhere(np.abs(Y) > 0.5)[0])
            if not np.array_equal(M, (M[k] / Y[k]) * Y):
                ok = False
                break
        cross += ok
    check(f'S4i the integer pair (0,0)~(0,1) is also phase-gauge equivalent ({found_int} gauges), while the integer class (0,1) and the spinorial class (1,1) '
          f'have {cross} equivalences inside the same gauge family (kappa differs, S3e: none can exist for any U(1) gauge)',
          found_int >= 1 and cross == 0)

    # consequence: covariant families
    hops = []
    for v in CORNERS:
        for d in itertools.product((-1, 0, 1), repeat=3):
            x = tuple(v[i] + d[i] for i in range(3))
            hops.append((tuple(xx // 2 for xx in x), tuple(xx % 2 for xx in x), v))
    hidx = {h: i for i, h in enumerate(hops)}

    def rv(R, u):
        w = [sum(R[i][j] * (2 * u[j] - 1) for j in range(3)) for i in range(3)]
        return tuple((x + 1) // 2 for x in w)

    def hop_act(R, h):
        t, vp, v = h
        return (tuple(sum(R[i][j] * t[j] for j in range(3)) for i in range(3)), rv(R, vp), rv(R, v))

    inv_closed = all(hop_act(R, h) in hidx for R in (RZ, RX) for h in hops)

    def family_dim(gens):
        """gens: list of (R, D) ; covariance A_{R t}[Rv',Rv] = D[Rv',v'] D[Rv,v] A_t[v',v] (real signs)"""
        rowsL = []
        for R, Dg in gens:
            M = smat(Dg)
            for h in hops:
                h2 = hop_act(R, h)
                sgn = M[cidx(h2[1]), cidx(h[1])] * M[cidx(h2[2]), cidx(h[2])]
                row = [0] * len(hops)
                row[hidx[h2]] += 1
                row[hidx[h]] -= int(sgn)
                rowsL.append(row)
        return len(hops) - sp.Matrix(rowsL).rank()

    fam = {}
    for c, GG in reps.items():
        L = lifts_by_rotation(GG)
        fam[c] = family_dim([(RZ, L[RZ][0]), (RX, L[RX][0])])
    fixed_psi = True
    for c, GG in reps.items():
        L = lifts_by_rotation(GG)
        for R in ROTS:
            for g in L[R]:
                M = smat(g)
                for h in hops:
                    if hop_act(R, h) == h:
                        fixed_psi &= (M[cidx(h[1]), cidx(h[1])] * M[cidx(h[2]), cidx(h[2])] == 1)
    check(f'S4j nearest-site covariant family (hop of at most one site per axis: 8 x 27 = 216 coefficients, rotation-invariant stencil = {inv_closed}): exact dimension of the '
          f'solution space of A_Rt = D A_t D^T for both generators is {fam}: 11 in ALL four signed classes. Reason: every hop fixed by a rotation has sign product +1 '
          f'({fixed_psi}) so the dimension is the number of O-orbits on the 216 hops, independent of the extension class. '
          'Any eleven-dimensional nearest-site family reported for a spinorial block is therefore consistent with the exact count; the number does not distinguish the extension classes.',
          inv_closed and fixed_psi and set(fam.values()) == {11})

    # ------------------------------------------------------------ S5 phased induced characters
    # exact arithmetic in Z[w], w^2 = -1 - w : (p,q) = p + q w ;  |p+qw|^2 = p^2 - p q + q^2
    def phased_ip(GG, j):
        Gs = sorted(GG)
        Hs = [g for g in Gs if abs(g[0]) == 1]
        c0 = next(h for h in Hs if sorder(h) == 3)
        kidx = {ID: 0, c0: 1, smul(c0, c0): 2}
        T = {}
        for g in Gs:
            if g[0] > 0:
                T.setdefault(abs(g[0]) - 1, g)
        wpow = [(1, 0), (0, 1), (-1, -1)]          # w^k = p + q w
        tot = Fraction(0)
        for g in Gs:
            p_ = q_ = 0
            for v in range(8):
                h = smul(smul(sinv(T[v]), g), T[v])
                if abs(h[0]) == 1:                      # t_v^-1 g t_v lies in the stabiliser of corner 0
                    s_ = 1 if spow(h, 3) == ID else -1
                    c_ = h if s_ == 1 else sneg(h)
                    base = wpow[(j * kidx[c_]) % 3]
                    p_ += s_ * base[0]
                    q_ += s_ * base[1]
            tot += p_ * p_ - p_ * q_ + q_ * q_
        return tot / 48

    pht = {c: [phased_ip(reps[c], j) for j in range(3)] for c in reps}
    check('S5 phased monomial corner actions (complex character of C6 with chi(-I) = -1, chi(c3) = w^j, j = 0,1,2): exact <chi,chi> of the induced 8-dim character, '
          f'per class [j=0 (signed), j=1, j=2]: {pht}; j = 0 reproduces the signed case (4), and j = +-1 gives 3 in every class (3 = 1+1+1: three inequivalent constituents; for 2O this is the source table E1/2 + E5/2 + H); the decomposition of the phased cases for the other classes is not worked out here',
          all(pht[c][0] == 4 for c in pht) and all(pht[c][1] == pht[c][2] for c in pht) and pht[(1, 1)][1] == 3)

    # ------------------------------------------------------------ S6 transfer of covariance
    def family_vectors(gens, d_):
        rowsL = []
        for R, Dg in gens:
            M = smat(Dg)
            for h in hops:
                h2 = hop_act(R, h)
                sgn = M[cidx(h2[1]), cidx(h[1])] * M[cidx(h2[2]), cidx(h[2])]
                row = [0] * len(hops)
                row[hidx[h2]] += 1
                row[hidx[h]] -= int(sgn)
                rowsL.append(row)
        return sp.Matrix(rowsL).nullspace()

    L2 = lifts_by_rotation(reps[(1, 1)])
    LG = lifts_by_rotation(reps[(1, 0)])
    gensG = [(RZ, LG[RZ][0]), (RX, LG[RX][0])]
    # use the representative pairs from S4 / 2O above (the gauge g was found for them)
    gens2 = [(RZ, a2), (RX, b2)]
    gensGL = [(RZ, a), (RX, b)]
    basis2 = family_vectors(gens2, 0)
    tr_ok = True
    for vec in basis2:
        # A_t[v',v] = vec[hidx[(t,v',v)]]; conjugate: A'_t = g^dagger A_t g  -> entries multiplied by conj(g_{v'}) g_v
        newvec = [vec[hidx[h]] * np.conj(gg[cidx(h[1])]) * gg[cidx(h[2])] for h in hops]
        for R, Dg in gensGL:
            M = smat(Dg)
            for h in hops:
                h2 = hop_act(R, h)
                sgn = M[cidx(h2[1]), cidx(h[1])] * M[cidx(h2[2]), cidx(h[2])]
                tr_ok &= bool(newvec[hidx[h2]] == sgn * newvec[hidx[h]])
    check('S6 exact transfer: every covariant nearest-site coefficient array of the 2O-class (11 independent ones) is mapped by A_t -> g^dagger A_t g (diagonal, so hop positions and ranges '
          'are unchanged, unitarity is preserved) to a covariant array of the GL(2,3)-class; any covariant unitary block walk of the 2O class (e.g. the sources\' T (U_2q (x) 1_E) T^dagger) '
          'gives one of the GL(2,3) class with the same spectrum',
          tr_ok and len(basis2) == 11)

    # ------------------------------------------------------------ verdict
    if FAIL == 0:
        print('HIT: exhaustive exact classification of signed 2x2x2-corner actions: the 65536 sign choices realise exactly the four central extensions of O by Z2 '
              '(S4xC2, A4x|C4, GL(2,3), 2O) once each up to diagonal sign gauge, the GL(2,3) class has exact representatives, induced character '
              '(+-8, +2, -2, 0) and rho = 2 x (4-dim irrep), and it is phase-gauge equivalent (odd rotations times +-i) but not extension-equivalent to the prescribed 2O lift')
    print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
    print('SUMMARY: all 65536 signed corner lifts are enumerated exactly: they realise each of the four central extensions of the cube rotation group by Z2 once '
          'up to diagonal sign gauge, the second spinorial one (GL(2,3)) is classified with exact representatives and character, and it relates to 2O only by an i-twist of odd rotations.')
    return 0 if FAIL == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
