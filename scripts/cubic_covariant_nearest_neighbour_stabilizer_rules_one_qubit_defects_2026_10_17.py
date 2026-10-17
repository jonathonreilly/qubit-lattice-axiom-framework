#!/usr/bin/env python3
"""Cubic-covariant nearest-neighbour Pauli stabilizer rules on one qubit per site of Z^3.

A rule is a set of signed Pauli strings on the star of the origin (the site and its six
neighbours), closed under the proper cubic group O acting on positions and, on Pauli
labels, by one of the four soldering-menu actions (trivial, sign twist, axis, full).
Translates of the rule generate a stabilizer group, which must be abelian and must not
contain -1. The runner:

1. enumerates every single O-orbit (4^7 - 1 strings) and keeps the sign-consistent,
   self-commuting ones;
2. finds all maximal mutually commuting sets of such orbits;
3. shows that under the axis and full actions the only rule is the Chamon octahedron
   X(+-x) Y(+-y) Z(+-z), and that under the trivial and sign actions every rule is either
   single-label (one Pauli label throughout) or a single cluster-type orbit;
4. for the Chamon rule computes the excitation (charge) module R / I over
   R = F2[x, y, z] (Laurent), shows I is the intersection of four primes (curves along
   the four body diagonals), hence every nonzero charge has mobility rank at most two and a single
   defect is immobile;
5. checks code dimension and sign consistency on L^3 tori.
Exact throughout: finite enumeration, and Groebner bases over GF(2), which is the field
of the Pauli binary symplectic representation.
"""

from __future__ import annotations

import itertools
import sys

import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    'docs/ONE_QUBIT_CUBIC_COVARIANT_NEAREST_NEIGHBOUR_STABILIZER_RULES_HAVE_NO_THREE_DIMENSIONALLY_MOBILE_DEFECT_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, ok: bool) -> None:
        if ok:
            self.passed += 1
            print(f"PASS {name}")
        else:
            self.failed += 1
            print(f"FAIL {name}")


# ---------------------------------------------------------------- group and actions
O = []
for p in itertools.permutations(range(3)):
    for s in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3):
            M[p[i], i] = s[i]
        if round(np.linalg.det(M)) == 1:
            O.append(M)
STAR = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
SIDX = {p: i for i, p in enumerate(STAR)}
LAB = 'IXYZ'
ACTIONS = ('trivial', 'sign', 'axis', 'full')


def perm_sign(M):
    return int(round(np.linalg.det(np.abs(M))))


def Q(M, action):
    if action == 'trivial':
        return np.eye(3, dtype=int)
    if action == 'sign':
        s = perm_sign(M)
        return np.diag([1, s, s])
    if action == 'axis':
        return perm_sign(M) * np.abs(M)
    return M


def act(M, Qm, string):
    out, sg = [0] * 7, 1
    for i, a in enumerate(string):
        if a == 0:
            continue
        pos = tuple(int(x) for x in M @ np.array(STAR[i]))
        col = Qm[:, a - 1]
        b = int(np.nonzero(col)[0][0])
        out[SIDX[pos]] = b + 1
        sg *= int(col[b])
    return tuple(out), sg


def orbit(string, action):
    orb = {}
    for M in O:
        st, sg = act(M, Q(M, action), string)
        if st in orb and orb[st] != sg:
            return None
        orb[st] = sg
    return orb


def placed(string, shift):
    return {tuple(np.add(STAR[i], shift)): a for i, a in enumerate(string) if a}


def anticommute(P1, P2):
    return sum(1 for site, a in P1.items() if P2.get(site, 0) not in (0, a)) % 2 == 1


SHIFTS = [s for s in itertools.product(range(-2, 3), repeat=3) if sum(map(abs, s)) <= 4]


def families_commute(A, B):
    for s1 in A:
        P1 = placed(s1, (0, 0, 0))
        for s2 in B:
            for sh in SHIFTS:
                if anticommute(P1, placed(s2, sh)):
                    return False
    return True


def single_orbits(action):
    seen, good = set(), []
    for string in itertools.product(range(4), repeat=7):
        if not any(string) or string in seen:
            continue
        orb = orbit(string, action)
        for M in O:
            seen.add(act(M, Q(M, action), string)[0])
        if orb is not None and families_commute(list(orb), list(orb)):
            good.append(orb)
    return good


def maximal_cliques(n, adj):
    out = []

    def bk(R, P, X):
        if not P and not X:
            out.append(R)
            return
        u = max(P | X, key=lambda w: len(adj[w] & P))
        for v in list(P - adj[u]):
            bk(R | {v}, P & adj[v], X & adj[v])
            P = P - {v}
            X = X | {v}

    bk(set(), set(range(n)), set())
    return out


def labels(orb):
    return {a for st in orb for a in st if a}


def is_cluster_type(orb):
    st = next(iter(orb))
    if st[0] == 0 or len(orb) != 1:
        return False
    nb = set(st[1:])
    return len(nb) == 1 and 0 not in nb and st[0] not in nb


# ---------------------------------------------------------------- F2 linear algebra
def f2_rank_and_null(M):
    """Row-reduce a 0/1 matrix over GF(2); return rank and a basis of the left null space."""
    A = (np.array(M, dtype=np.uint8) % 2).copy()
    m, n = A.shape
    T = np.eye(m, dtype=np.uint8)
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if A[i, c]), None)
        if piv is None:
            continue
        A[[r, piv]] = A[[piv, r]]
        T[[r, piv]] = T[[piv, r]]
        for i in range(m):
            if i != r and A[i, c]:
                A[i] ^= A[r]
                T[i] ^= T[r]
        r += 1
        if r == m:
            break
    return r, T[r:]


MULT = {(1, 2): (3, 1), (2, 1): (3, 3), (2, 3): (1, 1), (3, 2): (1, 3), (3, 1): (2, 1), (1, 3): (2, 3)}


def chamon_torus(L):
    n = L ** 3
    idx = lambda p: ((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)
    rows, labs = [], []
    for v in itertools.product(range(L), repeat=3):
        lab = {}
        for a in range(3):
            for s in (1, -1):
                p = list(v)
                p[a] += s
                lab[idx(p)] = a + 1
        x = np.zeros(2 * n, np.uint8)
        for i, P in lab.items():
            if P in (1, 2):
                x[i] = 1
            if P in (2, 3):
                x[n + i] = 1
        rows.append(x)
        labs.append(lab)
    r, N = f2_rank_and_null(np.array(rows))
    bad = 0
    for c in N:
        cur, phase = {}, 0
        for k in np.nonzero(c)[0]:
            for i, P in labs[k].items():
                q = cur.get(i)
                if q is None:
                    cur[i] = P
                elif q == P:
                    del cur[i]
                else:
                    cur[i], ph = MULT[(q, P)]
                    phase += ph
        if cur or phase % 4:
            bad += 1
    return n, r, len(N), bad


def main() -> int:
    ck = Checks()
    x, y, z = sp.symbols('x y z')

    # ---------------- 1-3: classification
    orbs = {a: single_orbits(a) for a in ACTIONS}
    for a in ACTIONS:
        print(f'{a}: {len(orbs[a])} sign-consistent self-commuting single orbits')
    chamon = (0, 1, 1, 2, 2, 3, 3)
    for a in ('axis', 'full'):
        ck.check(f'{a} action: the only single-orbit rule is the Chamon octahedron X(+-x) Y(+-y) Z(+-z), with identity at the centre',
                 len(orbs[a]) == 1 and set(orbs[a][0]) == {chamon} and orbs[a][0][chamon] == 1)
    ck.check('O-invariant Paulis at the centre under the axis or full action: only the identity (so no rule pins a site through its own label)',
             all(any(act(M, Q(M, a), (lab, 0, 0, 0, 0, 0, 0))[0][0] != lab for M in O) for a in ('axis', 'full') for lab in (1, 2, 3)))
    for a in ('trivial', 'sign'):
        G = orbs[a]
        adj = {i: set() for i in range(len(G))}
        for i, j in itertools.combinations(range(len(G)), 2):
            if families_commute(list(G[i]), list(G[j])):
                adj[i].add(j)
                adj[j].add(i)
        cl = maximal_cliques(len(G), adj)
        kinds = []
        for c in cl:
            labset = set().union(*[labels(G[i]) for i in c])
            if len(labset) == 1:
                kinds.append('single-label')
            elif len(c) == 1 and is_cluster_type(G[next(iter(c))]):
                kinds.append('cluster')
            else:
                kinds.append('other')
        print(f'{a}: {len(G)} orbits, {len(cl)} maximal commuting sets: {sorted(kinds)}')
        ck.check(f'{a} action: every maximal commuting set of orbits is single-label or one cluster-type orbit',
                 'other' not in kinds)
        # any rule is a subset of a maximal set; a subset of a single-label set is single-label
        ck.check(f'{a} action: every orbit containing two different labels is a cluster-type singleton (centre P, six neighbours Q != P)',
                 all(is_cluster_type(o) for o in G if len(labels(o)) > 1))
        # cluster-type: a single-site Pauli Q at the centre flips exactly one generator (the one centred there)
        ok = True
        for o in G:
            if len(labels(o)) > 1:
                st = next(iter(o))
                q = st[1]
                hits = [sh for sh in SHIFTS if anticommute({(0, 0, 0): q}, placed(st, sh))]
                ok &= hits == [(0, 0, 0)]
        ck.check(f'{a} action: in every cluster-type rule each single defect is created by one single-site Pauli (no topological charge)', ok)

    # single-label rules: excitations are created and moved by operators of one other label,
    # which mutually commute, so every hopping-operator commutator (Levin-Wen T-junction) is +1.
    paulis = (np.array([[0, 1], [1, 0]], dtype=complex),
              np.array([[0, -1j], [1j, 0]], dtype=complex),
              np.diag([1, -1]).astype(complex))
    identity = np.eye(2, dtype=complex)
    fixed_label_ok = True
    for pauli in paulis:
        operators = []
        for support in itertools.product((0, 1), repeat=3):
            op = np.array([[1]], dtype=complex)
            for occupied in support:
                op = np.kron(op, pauli if occupied else identity)
            operators.append(op)
        fixed_label_ok &= all(np.array_equal(A @ B, B @ A)
                              for A, B in itertools.product(operators, repeat=2))
        fixed_label_ok &= all(np.array_equal(A @ B @ C, C @ B @ A)
                              for A, B, C in itertools.product(operators, repeat=3))
    # A deliberately mixed-label pair must fail the same commutation predicate.
    mixed_label_control = not np.array_equal(paulis[0] @ paulis[2],
                                             paulis[2] @ paulis[0])
    ck.check('exact three-site fixed-label hopping algebra and noncommuting control; '
             'arbitrary-support exchange inference is analytic',
             fixed_label_ok and mixed_label_control)

    # ---------------- 4: Chamon charge module
    # syndrome of X_0 and Z_0 at the origin: generators at -p for star positions p where the
    # generator has a label anticommuting with X (resp. Z).
    def syndrome(lab):
        terms = []
        for i, a in enumerate(chamon):
            if a and a != lab:
                p = STAR[i]
                terms.append(x ** (-p[0]) * y ** (-p[1]) * z ** (-p[2]))
        return sp.expand(sum(terms))

    sX, sZ = syndrome(1), syndrome(3)
    ck.check('Chamon syndromes: X -> y + 1/y + z + 1/z, Z -> x + 1/x + y + 1/y (over GF(2))',
             sp.expand(sX - (y + 1 / y + z + 1 / z)) == 0 and sp.expand(sZ - (x + 1 / x + y + 1 / y)) == 0)
    g1 = sp.expand((y + z) * (1 + y * z))
    g2 = sp.expand((x + y) * (1 + x * y))
    g3 = sp.expand((x + z) * (1 + x * z))
    ck.check('y z sX = (y + z)(1 + y z), x y sZ = (x + y)(1 + x y), x z (sX + sZ) = (x + z)(1 + x z) over GF(2)',
             sp.Poly(sp.expand(y * z * sX) - g1, x, y, z, modulus=2).is_zero
             and sp.Poly(sp.expand(x * y * sZ) - g2, x, y, z, modulus=2).is_zero
             and sp.Poly(sp.expand(x * y * z * (sX + sZ)) - y * g3, x, y, z, modulus=2).is_zero)
    gens = [x, y, z]
    GI = sp.groebner([g1, g2, g3], *gens, modulus=2, order='grevlex')
    primes = [[y * z + 1, x + y], [y * z + 1, x + z], [x * z + 1, y + z], [y + z, x + z]]
    t = sp.Symbol('t')

    def intersect(A, B):
        GB = sp.groebner([t * a for a in A] + [(1 + t) * b for b in B], t, *gens, modulus=2, order='lex')
        return [g for g in GB.exprs if not g.has(t)]

    J = primes[0]
    for P in primes[1:]:
        J = intersect(J, P)
    GJ = sp.groebner(J, *gens, modulus=2, order='grevlex')
    ck.check('the Chamon charge ideal I = (g1, g2, g3) equals the intersection of the four primes '
             '(yz+1, x+y), (yz+1, x+z), (xz+1, y+z), (y+z, x+z): curves along the four body diagonals',
             set(GI.exprs) == set(GJ.exprs))
    # each component is prime: modulo (y+z, x+z) the ring is F2[z]; modulo the others it is
    # F2[s, 1/s] (one variable eliminated linearly, one relation s s' = 1). None contains x, y
    # or z, so each extends to a prime of the Laurent ring, and I = their intersection is
    # Laurent-saturated.
    ck.check('no component contains x, y or z (each is a prime of the Laurent ring; I is saturated)',
             all(sp.groebner(P, *gens, modulus=2, order='grevlex').reduce(v)[1] != 0 for P in primes for v in gens))
    # I is the intersection of four height-2 primes, none of them the maximal ideal at (1,1,1);
    # so (I : f) = I for f = x+1, y+1, z+1, i.e. no nonzero charge class is fixed by all
    # three unit translations; the note separately proves the arbitrary-stride rank bound.
    def colon_is_trivial(f):
        lhs = sp.groebner(intersect(GI.exprs, [f]), *gens, modulus=2, order='grevlex')
        rhs = sp.groebner([sp.expand(gg * f) for gg in GI.exprs], *gens, modulus=2, order='grevlex')
        return set(lhs.exprs) == set(rhs.exprs)   # I cap (f) = f I  iff  I : f = I

    ck.check('(I : x+1) = (I : y+1) = (I : z+1) = I: unit-axis colon checks only',
             all(colon_is_trivial(f) for f in (x + 1, y + 1, z + 1)))

    def mono(tv):
        return x ** tv[0] * y ** tv[1] * z ** tv[2]

    def shift_poly(tv):   # x^t + 1 times x^2 y^2 z^2, a polynomial for t in {-2..2}^3
        return sp.expand(mono([a + 2 for a in tv]) + mono((2, 2, 2)))

    box = [tv for tv in itertools.product(range(-2, 3), repeat=3) if any(tv)]
    ck.check('a single defect (the class of 1) cannot be translated by any nonzero t in {-2..2}^3 (fracton)',
             all(GI.reduce(shift_poly(tv))[1] != 0 for tv in box))
    # a charge supported on the curve P1 = (yz+1, x+y), i.e. (s, s, 1/s): h in P2 cap P3 cap P4, h not in I
    K = primes[1]
    for P in primes[2:]:
        K = intersect(K, P)
    h = next(k for k in sp.groebner(K, *gens, modulus=2, order='grevlex').exprs if GI.reduce(k)[1] != 0)
    ok = all(GI.reduce(sp.expand(h * g))[1] == 0 for g in primes[0])
    ck.check('a charge class h supported on the curve (s, s, 1/s) exists: h P1 lies in I and h is not in I', ok)
    moved = [tv for tv in box if GI.reduce(sp.expand(h * shift_poly(tv)))[1] == 0]
    ck.check('that charge moves by t exactly when t is orthogonal to (1, 1, -1): a planon in (1,1,-1) planes',
             set(moved) == {tv for tv in box if tv[0] + tv[1] - tv[2] == 0})

    # ---------------- 5: tori
    for L in (4, 6):
        n, r, nrel, bad = chamon_torus(L)
        print(f'torus L={L}: qubits {n}, rank {r}, log2 code dimension {n - r}, relations {nrel}, inconsistent relations {bad}')
        ck.check(f'L={L} torus: log2 code dimension = 4L (grows with L, type-I fracton signature) and no generator product equals -1 or +-i',
                 n - r == 4 * L and bad == 0)

    print('per_element: exhaustive single-orbit enumeration and exact GF(2) Groebner bases')
    print('per_site: one qubit per site; no dynamics or tick is supplied')
    print('per_mode: not applicable')
    print('per_block: not applicable')
    print('lattice_wide: charge module over the Laurent ring (infinite lattice); tori L = 4, 6 only for code dimension')
    print(f"TOTAL: PASS={ck.passed} FAIL={ck.failed}")
    return 0 if ck.failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
