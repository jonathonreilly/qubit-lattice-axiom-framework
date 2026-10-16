#!/usr/bin/env python3
"""Taste content of cubic cells: every spinorial cell is spin-1/2 (x) F with F a rep of S3.

The binary octahedral group 2O acts on an O-orbit of points around a cell centre
(6 face centres, 8 corners, 12 edge midpoints) by monomial matrices: the induced
representation from a character of the (cyclic) stabiliser preimage. Each is
decomposed into 2O irreps by characters. Spinorial ones contain only E1/2, E5/2
and H = E (x) E1/2, so they equal E1/2 (x) F with F = m(E1/2) A1 + m(E5/2) A2 + m(H) E,
a representation of S3 = O / V4 (the permutations of the three axes). A Dirac
pair is available on every summand F' with F' + F' inside F (U_2q (x) 1_F').
"""

from __future__ import annotations

import itertools
import sys

import numpy as np
from scipy.linalg import expm

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    'docs/CUBIC_CELL_SHAPE_SETS_THE_TASTE_CONTENT_AXIS_PERMUTATION_BOUNDED_THEOREM_NOTE_2026-10-16.md',
    '.claude/science/review-fixes/review-drain-20261016/CUBIC_TICK_SCOPE.md',
    'docs/TWO_QUBIT_SITE_UNFREEZES_THE_CUBIC_TICK_DOUBLER_FREE_DIRAC_WALK_BOUNDED_THEOREM_NOTE_2026-10-16.md',
    'docs/STAGGERED_ONE_QUBIT_BLOCKS_CARRY_A_CUBIC_COVARIANT_DIRAC_TICK_BOUNDED_THEOREM_NOTE_2026-10-16.md',
)

SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.diag([1, -1]).astype(complex)


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


def su2(axis, ang):
    a = np.array(axis, float) / np.linalg.norm(axis)
    return np.cos(ang / 2) * np.eye(2) - 1j * np.sin(ang / 2) * (a[0] * SX + a[1] * SY + a[2] * SZ)


def rot(U):
    return np.array([[0.5 * np.trace(s @ U @ t @ U.conj().T).real for t in (SX, SY, SZ)] for s in (SX, SY, SZ)])


def key(U):
    return tuple(np.round(np.concatenate([U.real.ravel(), U.imag.ravel()]) + 0.0, 6))


def binary_octahedral():
    G = [np.eye(2, dtype=complex)]
    seen = {key(G[0])}
    frontier = [G[0]]
    gens = (su2([0, 0, 1], np.pi / 2), su2([1, 0, 0], np.pi / 2))
    while frontier:
        nxt = []
        for A in frontier:
            for g in gens:
                B = A @ g
                if key(B) not in seen:
                    seen.add(key(B))
                    G.append(B)
                    nxt.append(B)
        frontier = nxt
    return G


def spin_char(G, j):
    m = np.arange(j, -j - 1, -1)
    d = len(m)
    Jp = np.zeros((d, d), complex)
    for i in range(1, d):
        Jp[i - 1, i] = np.sqrt(j * (j + 1) - m[i] * (m[i] + 1))
    Jx = (Jp + Jp.conj().T) / 2
    Jy = (Jp - Jp.conj().T) / 2j
    Jz = np.diag(m).astype(complex)
    out = []
    for U in G:
        c = np.clip(np.trace(U).real / 2, -1, 1)
        th = 2 * np.arccos(c)
        if abs(np.sin(th / 2)) < 1e-12:
            out.append(d * (1 if c > 0 else (-1) ** int(round(2 * j))))
            continue
        n = np.array([np.trace(1j * U @ s).real / (2 * np.sin(th / 2)) for s in (SX, SY, SZ)])
        out.append(np.trace(expm(-1j * th * (n[0] * Jx + n[1] * Jy + n[2] * Jz))))
    return np.array(out)


def main() -> int:
    ck = Checks()
    # Exact restriction weights + Frobenius reciprocity, no rounded floats.
    expected = {4: {1:(1,0,1),3:(0,1,1),5:(0,1,1),7:(1,0,1)},
                3: {1:(1,1,1),3:(0,0,2),5:(1,1,1)},
                2: {1:(1,1,2),3:(1,1,2)}}
    exact = {}
    for m in (4,3,2):
        shift = m if m in (4,2) else 0
        weights = ((-1,1),(-1+shift,1+shift),(-3,-1,1,3))
        exact[m] = {q:tuple(sum(w % (2*m) == q for w in ws) for ws in weights)
                    for q in range(1,2*m,2)}
    ck.check('exact cyclic restrictions give all face, corner and edge spinorial multiplicities', exact == expected)
    G = binary_octahedral()
    ck.check('binary octahedral group generated: 48 elements', len(G) == 48)
    Rs = [np.round(rot(U)).astype(int) for U in G]
    idx = {key(U): i for i, U in enumerate(G)}
    mul = lambda i, j: idx[key(G[i] @ G[j])]
    inv = lambda i: idx[key(G[i].conj().T)]
    perm_sign = lambda R: int(round(np.linalg.det(np.abs(R))))
    Bs = np.array([[1, 1], [-1, 1], [0, -2]]) @ np.diag([1 / np.sqrt(2), 1 / np.sqrt(6)])
    A1 = np.ones(48)
    A2 = np.array([perm_sign(R) for R in Rs])
    E = np.array([np.trace(Bs.T @ np.abs(R) @ Bs) for R in Rs])
    T1 = spin_char(G, 1.0)
    E12 = spin_char(G, 0.5)
    H = spin_char(G, 1.5)
    irr = {'A1': A1, 'A2': A2, 'E': E, 'T1': T1, 'T2': T1 * A2, 'E1/2': E12, 'E5/2': E12 * A2, 'H': H}
    ortho = all(abs(np.vdot(irr[a], irr[b]) / 48 - (a == b)) < 1e-9 for a in irr for b in irr)
    ck.check('eight irreducible characters, orthonormal (A1, A2, E, T1, T2, E1/2, E5/2, H); dims sum of squares = 48',
             ortho and sum(int(round(v[0].real)) ** 2 for v in irr.values()) == 48)
    ck.check('A1, A2 and E factor through S3 (trivial on the axis half-turns V4)',
             all(abs(irr[k][i] - irr[k][0]) < 1e-9 for k in ('A1', 'A2', 'E') for i in range(48)
                 if np.array_equal(np.abs(Rs[i]), np.eye(3, dtype=int))))
    ck.check('H = E (x) E1/2 and E5/2 = A2 (x) E1/2 (character identities)',
             np.allclose(H, E * E12) and np.allclose(irr['E5/2'], A2 * E12))

    def decompose(ch):
        return {k: int(round((np.vdot(v, ch) / 48).real)) for k, v in irr.items() if abs(np.vdot(v, ch) / 48) > 1e-6}

    orbits = {
        'faces(6)': [s * np.eye(3, dtype=int)[a] for a in range(3) for s in (1, -1)],
        'corners(8)': [np.array(v) for v in itertools.product((1, -1), repeat=3)],
        'edges(12)': [np.array(v) for v in {p for v0 in ((1, 1, 0), (1, -1, 0), (-1, -1, 0)) for p in itertools.permutations(v0)}],
    }
    table = {}
    for name, pts in orbits.items():
        p0 = pts[0]
        Hs = [i for i in range(48) if np.array_equal(Rs[i] @ p0, p0)]
        order = lambda i: next(k for k in range(1, 49) if np.allclose(np.linalg.matrix_power(G[i], k), np.eye(2)))
        gen = max(Hs, key=order)
        n = order(gen)
        powers = {idx[key(np.linalg.matrix_power(G[gen], k))]: k for k in range(n)}
        reps = [next(i for i in range(48) if np.array_equal(Rs[i] @ p0, p)) for p in pts]
        minus1 = idx[key(-np.eye(2))]
        rows = []
        for q in range(n):
            chi = lambda h: np.exp(2j * np.pi * q * powers[h] / n)
            ch = np.zeros(48, complex)
            for g in range(48):
                for gi in reps:
                    c = mul(mul(inv(gi), g), gi)
                    if c in powers:
                        ch[g] += chi(c)
            dec = decompose(ch)
            spinorial = abs(chi(minus1) + 1) < 1e-9
            signed = all(abs(chi(h).imag) < 1e-9 for h in Hs)
            F = {'A1': dec.get('E1/2', 0), 'A2': dec.get('E5/2', 0), 'E': dec.get('H', 0)} if spinorial else None
            rows.append((q, spinorial, signed, dec, F))
        table[name] = rows
        for q, sp_, sg, dec, F in rows:
            print(f'   {name} q={q}: {"spinorial" if sp_ else "integer"}, {"signed" if sg else "phased"}, {dec}' + (f', taste F = {F}' if sp_ else ''))
    only_spinor = all(set(dec) <= {'E1/2', 'E5/2', 'H'} for rows in table.values() for (_, sp_, _, dec, _) in rows if sp_)
    ck.check('every spinorial cell representation contains only E1/2, E5/2, H, hence equals E1/2 (x) F with F a rep of S3', only_spinor)
    faces = {tuple(sorted(F.items())) for (_, sp_, _, _, F) in table['faces(6)'] if sp_}
    ck.check('six face centres (a site\'s six neighbours): F = A1 + E or A2 + E, the axis triplet, with no repeated summand',
             faces == {(('A1', 1), ('A2', 0), ('E', 1)), (('A1', 0), ('A2', 1), ('E', 1))})
    corners_signed = [F for (_, sp_, sg, _, F) in table['corners(8)'] if sp_ and sg]
    ck.check('eight corners with signs (staggered block): F = 2E, two copies (B6 note)', corners_signed == [{'A1': 0, 'A2': 0, 'E': 2}])
    edges = [F for (_, sp_, sg, _, F) in table['edges(12)'] if sp_]
    ck.check('twelve edges (cube links), spinorial only with phases: F = A1 + A2 + 2E',
             all(F == {'A1': 1, 'A2': 1, 'E': 2} for F in edges) and len(edges) == 2 and
             all(not sg for (_, sp_, sg, _, _) in table['edges(12)'] if sp_))
    # C3 content of the copy spaces: restrict characters to the threefold rotation
    c3 = next(i for i, R in enumerate(Rs) if np.array_equal(R, np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])))
    ck.check('under the threefold axis cycle C3, A1 and A2 carry character 1 and E carries omega + omega-bar (trace -1)',
             abs(A1[c3] - 1) < 1e-9 and abs(A2[c3] - 1) < 1e-9 and abs(E[c3] + 1) < 1e-9)
    print('per_element: exact cyclic restriction multiplicities; floating character corroboration')
    print('per_site: three finite orbit types only')
    print('per_mode: checked and not executed — no momentum search in this runner')
    print('per_block: spinorial representations of prescribed 2O only')
    print('lattice_wide: checked and not executed — no electron or generation derivation')
    print(f"TOTAL: PASS={ck.passed} FAIL={ck.failed}")
    return 0 if ck.failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
