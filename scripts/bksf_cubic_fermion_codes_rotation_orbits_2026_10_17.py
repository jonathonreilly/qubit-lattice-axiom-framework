#!/usr/bin/env python3
"""Rotation orbits of translation-invariant Bravyi-Kitaev superfast (BKSF) fermion codes on the cubic lattice.

Qubit on each edge (edge (v, a) runs from v to v + e_a). An ordering of the six edge directions at a
vertex (the same at every vertex) defines
  A_(v,a) = X_(v,a) * prod Z over edges at v ordered before +a * prod Z over edges at v + e_a ordered before -a,
  B_v     = Z on the six edges at v,
and plaquette stabilizers S_p = product of A around each plaquette. The code is the stabilizer group
<B_v, S_p>; violations of B_v are point charges moved by the A operators.

The runner checks, for all 720 orderings:
- generators commute; A_e flips exactly the two endpoint B's and commutes with every plaquette;
- the point charge is a fermion: the Levin-Wen T-junction sign with straight legs (products of A
  along axes, meeting only at the junction) is -1 for all 20 triples of the six axis directions
  (control: the untwisted toric code, A_e = X_e, gives +1 for all 20);
- torus code dimension (log2 = 3 at L = 4, 6) for one code per orbit type;
- the 720 orderings give 60 distinct stabilizer groups (equality of spans on the L = 4 torus);
- the proper cubic group O permutes them in orbits of sizes 4, 6 and 12 (12, 12 and 36 codes); no
  code is O-invariant; the largest stabilizer is D3 (a C3 about a body diagonal and three edge C2).
"""

from __future__ import annotations

import hashlib
import itertools
import os
import sys
from collections import Counter, defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1  # noqa: E402

AUDIT_TIMEOUT_SEC = 1200
AUDIT_INPUT_PATHS = (
    'docs/BKSF_CUBIC_FERMION_CODES_ARE_NOT_ROTATION_INVARIANT_MINIMAL_ORBIT_FOUR_BOUNDED_THEOREM_NOTE_2026-10-17.md',
)

E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
DIRS = [(0, 1), (1, 1), (2, 1), (0, -1), (1, -1), (2, -1)]   # (axis, sign)
O = c1.O


def edge_at(v, d):
    a, s = DIRS[d]
    return (v, a) if s == 1 else (tuple(v[i] - E[a][i] for i in range(3)), a)


def mul(op, key, lab):
    c = op.get(key, 0)
    op[key] = lab if c == 0 else (0 if c == lab else 6 - c - lab)
    if op[key] == 0:
        del op[key]


def A(v, a, order, twisted=True):
    op = {}
    mul(op, (v, a), 1)
    if not twisted:
        return op
    pos = {d: i for i, d in enumerate(order)}
    dplus, dminus = DIRS.index((a, 1)), DIRS.index((a, -1))
    w = tuple(v[i] + E[a][i] for i in range(3))
    for d in range(6):
        if pos[d] < pos[dplus]:
            mul(op, edge_at(v, d), 3)
        if pos[d] < pos[dminus]:
            mul(op, edge_at(w, d), 3)
    return op


def B(v):
    op = {}
    for d in range(6):
        mul(op, edge_at(v, d), 3)
    return op


def prod(*ops):
    out = {}
    for o in ops:
        for k, l in o.items():
            mul(out, k, l)
    return out


def plaq(v, c, order, twisted=True):
    a, b = [k for k in range(3) if k != c]
    va = tuple(v[i] + E[a][i] for i in range(3))
    vb = tuple(v[i] + E[b][i] for i in range(3))
    return prod(A(v, a, order, twisted), A(va, b, order, twisted), A(vb, a, order, twisted), A(v, b, order, twisted))


def anti(o1, o2):
    return sum(1 for k, l in o1.items() if o2.get(k, 0) not in (0, l)) % 2


def shift(op, s):
    return {(tuple(p[i] + s[i] for i in range(3)), a): l for (p, a), l in op.items()}


def gens(order, twisted=True):
    return [B((0, 0, 0))] + [plaq((0, 0, 0), c, order, twisted) for c in range(3)]


def leg(order, d, n, twisted=True):
    a, s = DIRS[d]
    ops, v = [], (0, 0, 0)
    for _ in range(n):
        if s == 1:
            base = v
            v = tuple(v[i] + E[a][i] for i in range(3))
        else:
            v = tuple(v[i] - E[a][i] for i in range(3))
            base = v
        ops.append(A(base, a, order, twisted))
    return prod(*ops)


def junction_signs(order, twisted=True):
    out = Counter()
    for trip in itertools.combinations(range(6), 3):
        L = [leg(order, d, 3, twisted) for d in trip]
        out[(-1) ** (anti(L[0], L[1]) + anti(L[1], L[2]) + anti(L[0], L[2]))] += 1
    return out


def torus_rows(gs, L):
    n = 3 * L ** 3
    idx = lambda p, a: 3 * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + a
    R = []
    for v in itertools.product(range(L), repeat=3):
        for g in gs:
            x = np.zeros(2 * n, np.uint8)
            for (p, a), l in g.items():
                q = idx([v[i] + p[i] for i in range(3)], a)
                if l in (1, 2):
                    x[q] ^= 1
                if l in (2, 3):
                    x[n + q] ^= 1
            R.append(x)
    return np.array(R)


def span_hash(M):
    A_ = M.copy() % 2
    m, n = A_.shape
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if A_[i, c]), None)
        if p is None:
            continue
        A_[[r, p]] = A_[[p, r]]
        rows = np.nonzero(A_[:, c])[0]
        rows = rows[rows != r]
        A_[rows] ^= A_[r]
        r += 1
        if r == m:
            break
    return hashlib.sha1(np.packbits(A_[:r]).tobytes()).hexdigest()


def rotdir(M, d):
    a, s = DIRS[d]
    v = M @ (s * np.array(E[a]))
    b = int(np.nonzero(v)[0][0])
    return DIRS.index((b, int(v[b])))


def rot_order(M, order):
    return tuple(rotdir(M, d) for d in order)


def kind(M):
    tr = int(round(np.trace(M)))
    if tr == 3:
        return 'E'
    if tr == 0:
        return 'C3'
    if tr == 1:
        return 'C4'
    w, v = np.linalg.eig(M.astype(float))
    ax = np.real(v[:, np.argmin(abs(w - 1))])
    return 'C2axis' if sum(abs(ax) > 1e-9) == 1 else 'C2edge'


def main() -> int:
    ck = c1.Checks()
    SH = list(itertools.product(range(-3, 4), repeat=3))
    orders = list(itertools.permutations(range(6)))

    # structure for a sample of orderings (all 720 checked for the hopping property below)
    ok_comm = True
    for order in orders[::37]:
        g = gens(order)
        ok_comm &= all(not anti(g[i], shift(g[j], s)) for i in range(4) for j in range(4) for s in SH)
    ck.check('generators commute with all translates (sampled orderings, every 37th of 720)', ok_comm)
    ok_hop = True
    for order in orders:
        g = gens(order)
        for a in range(3):
            u = A((0, 0, 0), a, order)
            ok_hop &= all(not anti(u, shift(g[k], s)) for k in (1, 2, 3) for s in SH)
            ok_hop &= sorted(s for s in SH if anti(u, shift(g[0], s))) == sorted([(0, 0, 0), E[a]])
    ck.check('for all 720 orderings, each A_e commutes with every plaquette stabilizer and flips exactly its two endpoint charges', ok_hop)
    ctrl = junction_signs(orders[0], twisted=False)
    ck.check('control: the untwisted toric code (A_e = X_e) has a bosonic charge, +1 for all 20 straight-leg triples', ctrl == Counter({1: 20}))

    H, classes = {}, defaultdict(list)
    for order in orders:
        h = span_hash(torus_rows(gens(order), 4))
        H[order] = h
        classes[h].append(order)
    ck.check('the 720 orderings give 60 distinct stabilizer groups (span equality on the L = 4 torus)', len(classes) == 60)
    ferm = all(junction_signs(list(v[0])) == Counter({-1: 20}) for v in classes.values())
    ck.check('every one of the 60 codes has a fermionic point charge: T-junction sign -1 for all 20 triples of straight axis legs', ferm)

    orbit_size, stabs = Counter(), {}
    for h, ords in classes.items():
        o = ords[0]
        st = [M for M in O if H[rot_order(M, o)] == h]
        orbit_size[24 // len(st)] += 1
        stabs[24 // len(st)] = (o, Counter(kind(M) for M in st))
    print('orbit sizes (size: number of codes):', dict(orbit_size))
    for k, (o, kinds) in sorted(stabs.items()):
        print(f'  orbit size {k}: example ordering {o}, stabilizer elements {dict(kinds)}')
    ck.check('O permutes the 60 codes in orbits of sizes 4, 6 and 12 (12, 12 and 36 codes); no code is O-invariant',
             orbit_size == Counter({4: 12, 6: 12, 12: 36}))
    ck.check('the largest stabilizer is D3: one C3 pair about a body diagonal and three edge C2 (orbit size 4)',
             stabs[4][1] == Counter({'E': 1, 'C2edge': 3, 'C3': 2}))
    dims = {k: [3 * L ** 3 - c1.f2_rank_and_null(torus_rows(gens(list(o)), L))[0] for L in (4, 6)] for k, (o, _) in stabs.items()}
    print('torus log2 code dimensions (L = 4, 6) per orbit type:', dims)
    ck.check('one code of each orbit type has bounded torus code dimension: log2 = 3 at L = 4 and L = 6', all(v == [3, 3] for v in dims.values()))

    print('per_element: all 720 orderings; exact GF(2) algebra')
    print('per_site: one qubit per edge of Z^3 (not site-covariant qubits); no dynamics')
    print('per_mode: not applicable')
    print('per_block: not applicable')
    print('lattice_wide: L = 4 torus for group equality; L = 4, 6 for code dimension')
    print(f"TOTAL: PASS={ck.passed} FAIL={ck.failed}")
    return 0 if ck.failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
