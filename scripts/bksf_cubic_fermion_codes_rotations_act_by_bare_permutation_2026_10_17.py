#!/usr/bin/env python3
"""Rotation action on translation-invariant BKSF fermion codes on the cubic lattice, with signs.

Companion of bksf_cubic_fermion_codes_rotation_orbits_2026_10_17.py, which classified the 60 codes
<B_v, S_p> (one ordering of the six edge directions at every vertex) and their stabilizers in the
proper cubic group O. Here the plaquette generators carry signs: S_p(c) is the Hermitian product of
the four edge operators around a plaquette normal to axis c, times (-1)^{s_c}, one sign per plaquette
orientation (translation-invariant sign sectors s = (s_x, s_y, s_z)).

The runner checks, exactly on the L = 4 torus (Paulis with phases, P = i^k X^x Z^z):
- every sign sector of every code is a valid stabilizer group (-1 is not in it);
- the hopping charge sees flux 0 through every plaquette in sector (0,0,0) and flux pi in (1,1,1):
  the hop product A(v,b) A(v+b,a) A(v+a,b) A(v,a) around a plaquette equals the signed S_p in sector
  (0,0,0) and minus it in sector (1,1,1);
- for every code and every rotation R in its stabilizer, the bare qubit permutation induced by R
  maps every signed generator of the sectors (0,0,0) and (1,1,1) to an element of the same signed
  group (no sign correction is needed), so R acts as a pure permutation U_R with U_R^n = 1;
- control (the test can fail): in every mixed sector some code has a stabilizing rotation whose bare
  permutation does not preserve the signed group (a sign correction is needed);
- pair test: for each (code, C2) pair with an ordering whose plaquette span P_R preserves (72 of 108),
  the state with fermions at x and Rx (path of that ordering's edge operators) has P_R-eigenvalue
  lambda = +1 relative to the vacuum, in both sectors, for every tested off-axis x; with exchange sign -1
  this is eta_f(C2, C2) = -1 (the bare permutation acts spinorially); control: lambda = +1 for the
  bosonic charge of the untwisted toric code.
"""

from __future__ import annotations

import itertools
import os
import sys
from collections import Counter, defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bksf_cubic_fermion_codes_rotation_orbits_2026_10_17 as bk  # noqa: E402
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1  # noqa: E402


_PS = {}


def plaq_span(o):
    """Hash of the unsigned span of the plaquette generators of ordering o on the L = 4 torus."""
    if o not in _PS:
        _PS[o] = bk.span_hash(bk.torus_rows(bk.gens(o)[1:], 4))
    return _PS[o]

AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = (
    'docs/BKSF_CUBIC_FERMION_CODES_BARE_PERMUTATION_ROTATIONS_ACT_SPINORIALLY_ON_THE_FERMION_BOUNDED_THEOREM_NOTE_2026-10-17.md',
)

L = 4
N = 3 * L ** 3
E = bk.E


def idx(p, a):
    return 3 * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + a


def from_op(op):
    """Hermitian Pauli dict ((p, a) -> 1, 2, 3 for X, Y, Z) to [x, z, k] with P = i^k X^x Z^z."""
    x = np.zeros(N, np.uint8)
    z = np.zeros(N, np.uint8)
    k = 0
    for (p, a), lab in op.items():
        q = idx(p, a)
        if lab in (1, 2):
            x[q] ^= 1
        if lab in (2, 3):
            z[q] ^= 1
        if lab == 2:
            k += 1
    return [x, z, k % 4]


def one():
    return [np.zeros(N, np.uint8), np.zeros(N, np.uint8), 0]


def mulp(P, Q):
    s = int(P[1].astype(int) @ Q[0].astype(int)) % 2
    return [P[0] ^ Q[0], P[1] ^ Q[1], (P[2] + Q[2] + 2 * s) % 4]


def gens(order, signs):
    G, lab = [], []
    for v in itertools.product(range(L), repeat=3):
        G.append(from_op(bk.B(v)))
        lab.append(('B', v, None))
        for c in range(3):
            a, b = [t for t in range(3) if t != c]
            va = tuple(v[i] + E[a][i] for i in range(3))
            vb = tuple(v[i] + E[b][i] for i in range(3))
            P = one()
            for e in (bk.A(v, a, order), bk.A(va, b, order), bk.A(vb, a, order), bk.A(v, b, order)):
                P = mulp(P, from_op(e))
            if (P[2] - int(P[0].astype(int) @ P[1].astype(int))) % 2:
                P[2] = (P[2] + 1) % 4   # Hermitian choice of phase
            P[2] = (P[2] + 2 * signs[c]) % 4
            G.append(P)
            lab.append(('S', v, c))
    return G, lab


def valid(G):
    _, null = c1.f2_rank_and_null(np.array([np.concatenate([g[0], g[1]]) for g in G]))
    for c in null:
        R = one()
        for i in np.nonzero(c)[0]:
            R = mulp(R, G[i])
        if R[2] % 4:
            return False
    return True


def solve_multi(M, T):
    A = np.concatenate([M, T], axis=1).astype(np.uint8) % 2
    m, nv = M.shape
    piv, r = [], 0
    for c in range(nv):
        p = next((i for i in range(r, m) if A[i, c]), None)
        if p is None:
            continue
        A[[r, p]] = A[[p, r]]
        rows = np.nonzero(A[:, c])[0]
        rows = rows[rows != r]
        A[rows] ^= A[r]
        piv.append(c)
        r += 1
        if r == m:
            break
    ok = ~A[r:, nv:].any(axis=0)
    W = np.zeros((nv, T.shape[1]), np.uint8)
    for i, c in enumerate(piv):
        W[c] = A[i, nv:]
    return W, ok


def perm_of(M):
    perm = np.zeros(N, int)
    for v in itertools.product(range(L), repeat=3):
        w = tuple(int(x) for x in M @ np.array(v))
        for a in range(3):
            d = M @ np.array(E[a])
            b = int(np.nonzero(d)[0][0])
            p = w if d[b] == 1 else tuple(w[i] - (1 if i == b else 0) for i in range(3))
            perm[idx(v, a)] = idx(p, b)
    return perm


def apply_perm(P, perm):
    x = np.zeros(N, np.uint8)
    z = np.zeros(N, np.uint8)
    x[perm] = P[0]
    z[perm] = P[1]
    return [x, z, P[2]]


def sign_corrections(G, perm):
    """Number of signed generators whose bare-permuted image is minus an element of the signed group."""
    Mg = np.array([np.concatenate([g[0], g[1]]) for g in G]).T
    imgs = [apply_perm(g, perm) for g in G]
    W, ok = solve_multi(Mg, np.array([np.concatenate([im[0], im[1]]) for im in imgs]).T)
    assert ok.all(), 'rotated generator outside the group'
    bad = 0
    for j, im in enumerate(imgs):
        R = one()
        for i in np.nonzero(W[:, j])[0]:
            R = mulp(R, G[i])
        bad += int(R[2] != im[2])
    return bad


def dag(P):
    return [P[0], P[1], (-P[2] + 2 * int(P[0].astype(int) @ P[1].astype(int))) % 4]


def phase_in_group(G, P):
    """i^f with P = i^f * (element of the signed group generated by G), or None if P is not in the group."""
    Mg = np.array([np.concatenate([g[0], g[1]]) for g in G]).T
    W, ok = solve_multi(Mg, np.concatenate([P[0], P[1]])[:, None])
    if not ok[0]:
        return None
    R = one()
    for i in np.nonzero(W[:, 0])[0]:
        R = mulp(R, G[i])
    return (P[2] - R[2]) % 4


def path(x, y):
    """Axis-by-axis lattice path from x to y as a list of edges (base vertex, axis)."""
    out, cur = [], list(x)
    for a in range(3):
        while cur[a] != y[a]:
            if y[a] > cur[a]:
                out.append((tuple(cur), a))
                cur[a] += 1
            else:
                cur[a] -= 1
                out.append((tuple(cur), a))
    return out


def pair_eigenvalue(order, G, M, x, twisted=True):
    """Eigenvalue lambda of the bare permutation P_R on S|vac>, relative to the vacuum, where S is the product of
    edge operators along a path from x to Rx: P_R S|vac> = S (S^dag S^R) P_R|vac>, and S^dag S^R lies in
    +-(signed group); lambda is that sign."""
    Rx = tuple(int(c) for c in M @ np.array(x))
    S = one()
    for (v, a) in path(x, Rx):
        S = mulp(S, from_op(bk.A(v, a, order, twisted)))
    f = phase_in_group(G, mulp(dag(S), apply_perm(S, perm_of(M))))
    return None if f is None else (1 if f == 0 else (-1 if f == 2 else 'imaginary'))


def plaquette_flux(order, G, lab):
    """Phase i^f with hop product around the plaquette at v = (1,1,1) equal to i^f times the signed S_p."""
    v = (1, 1, 1)
    S = {l[2]: g for g, l in zip(G, lab) if l[0] == 'S' and l[1] == v}
    out = []
    for c in range(3):
        a, b = [t for t in range(3) if t != c]
        va = tuple(v[i] + E[a][i] for i in range(3))
        vb = tuple(v[i] + E[b][i] for i in range(3))
        P = one()
        for e in (bk.A(v, b, order), bk.A(vb, a, order), bk.A(va, b, order), bk.A(v, a, order)):
            P = mulp(P, from_op(e))
        assert (P[0] == S[c][0]).all() and (P[1] == S[c][1]).all()
        out.append((P[2] - S[c][2]) % 4)
    return tuple(out)


def main() -> int:
    ck = c1.Checks()
    orders = list(itertools.permutations(range(6)))
    H = {o: bk.span_hash(bk.torus_rows(bk.gens(o), 4)) for o in orders}
    classes = defaultdict(list)
    for o in orders:
        classes[H[o]].append(o)
    ck.check('60 codes (as in the orbit note)', len(classes) == 60)

    sectors = list(itertools.product((0, 1), repeat=3))
    all_valid, flux, preserved, mixed_broken = True, Counter(), Counter(), Counter()
    for h, ords in classes.items():
        o = ords[0]
        stab = [M for M in c1.O if H[bk.rot_order(M, o)] == h]
        for s in sectors:
            G, lab = gens(o, s)
            all_valid &= valid(G)
            if s in ((0, 0, 0), (1, 1, 1)):
                flux[(s, plaquette_flux(o, G, lab))] += 1
                for M in stab:
                    preserved[(24 // len(stab), s, bk.kind(M), sign_corrections(G, perm_of(M)) == 0)] += 1
            else:
                mixed_broken[s] += any(sign_corrections(G, perm_of(M)) > 0 for M in stab)
    ck.check('all 8 translation-invariant sign sectors of all 60 codes are valid (-1 not in the signed group, L = 4)', all_valid)
    print('plaquette flux (sector, i-exponent per orientation): count', dict(flux))
    ck.check('the hopping charge sees flux 0 on every plaquette in sector (0,0,0) and flux pi in sector (1,1,1), all 60 codes',
             flux == Counter({((0, 0, 0), (0, 0, 0)): 60, ((1, 1, 1), (2, 2, 2)): 60}))
    for k in sorted(preserved):
        print('  (orbit size, sector, rotation type, bare permutation preserves signs):', k, preserved[k])
    ck.check('in sectors (0,0,0) and (1,1,1), every stabilizing rotation of every code acts as a bare qubit permutation (no sign correction)',
             all(k[3] for k in preserved) and sum(preserved.values()) == 2 * (12 * 6 + 12 * 4 + 36 * 2))
    print('mixed sectors: number of codes with a stabilizing rotation that needs a sign correction', dict(mixed_broken))
    ck.check('control: in each of the 6 mixed sectors, some code has a stabilizing rotation that needs a sign correction',
             len(mixed_broken) == 6 and all(v > 0 for v in mixed_broken.values()))


    # Pair test: fermions at x and Rx (x off the axis) for every (code, C2) pair that has an ordering o in its
    # class whose plaquette span is preserved by P_R (so the hops of o are mapped to hops of the same type).
    xs = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, -1, 0)]
    lam, covered, uncovered = Counter(), 0, 0
    for h, ords in classes.items():
        stab = [M for M in c1.O if H[bk.rot_order(M, ords[0])] == h]
        for M in stab:
            if bk.kind(M) not in ('C2edge', 'C2axis'):
                continue
            o = next((o for o in ords if plaq_span(o) == plaq_span(bk.rot_order(M, o))), None)
            if o is None:
                uncovered += 1
                continue
            covered += 1
            for s_ in ((0, 0, 0), (1, 1, 1)):
                G, lab = gens(o, s_)
                fl = 'flux0' if plaquette_flux(o, G, lab) == (0, 0, 0) else 'fluxpi'
                for x in xs:
                    if tuple(int(c) for c in M @ np.array(x)) != x:
                        lam[(fl, bk.kind(M), pair_eigenvalue(o, G, M, x))] += 1
    print('pair test: covered (code, C2) pairs', covered, 'not covered', uncovered)
    print('pair eigenvalues (sector, rotation, lambda): count', dict(lam))
    ck.check('pair test: for all 72 covered (code, C2) pairs, in both sectors and for every tested x, the swapped fermion pair has P_R-eigenvalue lambda = +1, so eta_f(C2, C2) = theta_f * lambda = -1',
             covered == 72 and uncovered == 36 and set(k[2] for k in lam) == {1})
    # control: untwisted toric code (A_e = X_e, boson): lambda = +1, eta = +1
    tor = []
    for v in itertools.product(range(L), repeat=3):
        tor.append(from_op(bk.B(v)))
        for c in range(3):
            tor.append(from_op(bk.plaq(v, c, orders[0], twisted=False)))
    ctl = Counter(pair_eigenvalue(orders[0], tor, M, x, twisted=False) for M in c1.O if bk.kind(M) == 'C2edge' for x in xs
                  if tuple(int(c) for c in M @ np.array(x)) != x)
    print('control (toric code boson) pair eigenvalues:', dict(ctl))
    ck.check('control: in the untwisted toric code (bosonic charge) the swapped pair has lambda = +1 for every edge C2', ctl == Counter({1: sum(ctl.values())}))

    print('per_element: all 60 codes, all 8 translation-invariant sign sectors, every stabilizing rotation')
    print('per_site: one qubit per edge; exact Pauli algebra with phases on the L = 4 torus')
    print('per_mode: not applicable')
    print('per_block: not applicable')
    print('lattice_wide: L = 4 torus (translation-invariant generators; rotations about a vertex)')
    print(f"TOTAL: PASS={ck.passed} FAIL={ck.failed}")
    return 0 if ck.failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
