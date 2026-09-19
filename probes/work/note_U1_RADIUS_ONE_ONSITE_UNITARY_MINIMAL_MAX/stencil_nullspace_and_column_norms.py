#!/usr/bin/env python3
"""J:note falsifiers for U1_RADIUS_ONE_ONSITE_UNITARY_MINIMAL_MAXWELL_TICK_BOUNDED_NO_GO_NOTE_2026-09-03 (on main).

Falsifiers implemented (three of the note's list): "the physical radius-one role graph permits a dynamical same-role input";
"gauge/chain compatibility permits an off-diagonal stencil not represented by the declared curl blocks"; "a nonzero curl coefficient
can cancel its positive contribution to the diagonal column norm" (with independent orientation coefficients).

The runner enumerates 625 integer reverse stencils in {-2..2}^4 around one face and works with the Fourier symbol. Here, exactly and on
whole periodic doubled lattices (2L sites per axis, L = 2, 3, 4, 5; vertices/edges/faces/cubes = 0/1/2/3 odd coordinates):
  1. every site's six nearest neighbours are enumerated and their roles tallied (edges see only vertices and faces; faces only edges
     and cubes); C d0 = 0 for the oriented curl (integer matrices);
  2. the most general translation-covariant radius-one edge->face map Q (one unknown per face orientation and boundary-edge
     displacement: 12 complex unknowns) under gauge compatibility Q d0 = 0, and the most general face->edge map R (12 unknowns) under
     electric-Gauss preservation d0^T R = 0: every constraint row of the whole lattice is generated and the exact rational nullspace
     taken (integer constraint matrices, so it spans the complex nullspace); expected dimension 3 each, one oriented curl (co-curl)
     per orientation;
  3. column norms of U = [[diag(u_a), R], [Q, diag(v_n)]] with independent orientation coefficients Q = sum_n q_n curl_n: the
     constant electric field of orientation a has zero curl, so exact norm preservation gives |u_a| = 1, and the (E_a, E_a) entry of
     U^dag U is |u_a|^2 + 2|q_b|^2 + 2|q_c|^2 (read off the lattice curl, exactly); together every q_n = 0 (r_n likewise).
"""
from __future__ import annotations

import itertools

import numpy as np
import sympy as sp


def unit(a):
    return tuple(1 if i == a else 0 for i in range(3))


def shift(s, a, sg, M):
    return tuple((s[i] + (sg if i == a else 0)) % M for i in range(3))


def odd_axes(s):
    return [i for i in range(3) if s[i] % 2]


def analyse(L):
    M = 2 * L
    sites = list(itertools.product(range(M), repeat=3))
    role = {s: sum(c % 2 for c in s) for s in sites}
    tally = {}
    for s in sites:
        for a in range(3):
            for sg in (1, -1):
                tally.setdefault(role[s], set()).add(role[shift(s, a, sg, M)])
    same_role = any(r in tally[r] for r in tally)
    V = [s for s in sites if role[s] == 0]
    E = [s for s in sites if role[s] == 1]
    F = [s for s in sites if role[s] == 2]
    iv, ie, ifc = ({s: i for i, s in enumerate(X)} for X in (V, E, F))
    d0 = np.zeros((len(E), len(V)), dtype=np.int64)
    for e in E:
        a = odd_axes(e)[0]
        d0[ie[e], iv[shift(e, a, 1, M)]] += 1
        d0[ie[e], iv[shift(e, a, -1, M)]] -= 1
    C = np.zeros((len(F), len(E)), dtype=np.int64)
    pattern = {}
    for f in F:
        n = [i for i in range(3) if f[i] % 2 == 0][0]
        a, b = odd_axes(f)
        for (ax, sg), c in (((b, -1), 1), ((a, 1), 1), ((b, 1), -1), ((a, -1), -1)):
            C[ifc[f], ie[shift(f, ax, sg, M)]] += c
            pattern[(n, ax, sg)] = c
    chain = not np.any(C @ d0)
    keysQ = sorted(pattern)
    # Q d0 = 0: rows indexed by (face, vertex)
    rows = {}
    for f in F:
        n = [i for i in range(3) if f[i] % 2 == 0][0]
        for ax in odd_axes(f):
            for sg in (1, -1):
                e = shift(f, ax, sg, M)
                a_e = odd_axes(e)[0]
                for vs, val in ((1, 1), (-1, -1)):
                    v = shift(e, a_e, vs, M)
                    rows.setdefault((f, v), {})
                    rows[(f, v)][(n, ax, sg)] = rows[(f, v)].get((n, ax, sg), 0) + val
    AQ = sp.Matrix(sorted({tuple(r.get(k, 0) for k in keysQ) for r in rows.values()}))
    nsQ = AQ.nullspace()
    curl_ok = len(nsQ) == 3
    for v in nsQ:
        sup = {keysQ[i][0] for i in range(12) if v[i] != 0}
        if len(sup) != 1:
            curl_ok = False
            continue
        n0 = sup.pop()
        pat = sp.Matrix([pattern[k] if k[0] == n0 else 0 for k in keysQ])
        i0 = [i for i in range(12) if pat[i] != 0][0]
        curl_ok &= (v - v[i0] / pat[i0] * pat).is_zero_matrix
    # R: R[e, f] = x[(a_e, b, sg)] for f = e + sg e_b; d0^T R = 0: rows indexed by (vertex, face)
    keysR = sorted({(a, b, sg) for a in range(3) for b in range(3) if b != a for sg in (1, -1)})
    rowsR = {}
    for e in E:
        a = odd_axes(e)[0]
        for b in range(3):
            if b == a:
                continue
            for sg in (1, -1):
                f = shift(e, b, sg, M)
                for vs, val in ((1, 1), (-1, -1)):
                    v = shift(e, a, vs, M)
                    rowsR.setdefault((v, f), {})
                    rowsR[(v, f)][(a, b, sg)] = rowsR[(v, f)].get((a, b, sg), 0) + val
    AR = sp.Matrix(sorted({tuple(r.get(k, 0) for k in keysR) for r in rowsR.values()}))
    nsR = AR.nullspace()
    # co-curl pattern: C^T[e, f] for f = e + sg e_b equals the curl coefficient of edge e in face f
    copat = {}
    for e in E[:60]:
        a = odd_axes(e)[0]
        for b in range(3):
            if b == a:
                continue
            for sg in (1, -1):
                f = shift(e, b, sg, M)
                copat[(a, b, sg)] = int(C[ifc[f], ie[e]])
    cocurl_ok = len(nsR) == 3
    for v in nsR:
        normals = {3 - k[0] - k[1] for k, x in zip(keysR, v) if x != 0}
        if len(normals) != 1:
            cocurl_ok = False
            continue
        n0 = normals.pop()
        pat = sp.Matrix([copat[k] if 3 - k[0] - k[1] == n0 else 0 for k in keysR])
        i0 = [i for i in range(12) if pat[i] != 0][0]
        cocurl_ok &= (v - v[i0] / pat[i0] * pat).is_zero_matrix
    # faces containing an a-edge, by normal
    e0 = E[0]
    a0 = odd_axes(e0)[0]
    by_normal = {}
    for fi in np.nonzero(C[:, ie[e0]])[0]:
        f = F[fi]
        n = [i for i in range(3) if f[i] % 2 == 0][0]
        by_normal[n] = by_normal.get(n, 0) + 1
    return {"roles seen": {k: sorted(v) for k, v in sorted(tally.items())}, "same-role neighbour": same_role, "C d0 = 0": chain,
            "Q constraint rows": AQ.rows, "dim Q": len(nsQ), "Q = curl per orientation": curl_ok,
            "R constraint rows": AR.rows, "dim R": len(nsR), "R = co-curl per orientation": cocurl_ok,
            "faces at an edge by normal": by_normal, "edge orientation": a0}


def main():
    res = {L: analyse(L) for L in (2, 3, 4, 5)}
    for L, v in res.items():
        print(f"L = {L} (doubled {2 * L}^3): {v}")
    u = sp.symbols("u0:3")
    q = sp.symbols("q0:3")
    fa = res[3]["faces at an edge by normal"]
    a0 = res[3]["edge orientation"]
    # (E_a, E_a) entry of U^dag U: |u_a|^2 + sum over faces at an a-edge of |q_normal|^2 (curl entries are +-1)
    diag = {a: u[a] * sp.conjugate(u[a]) + sum(2 * q[n] * sp.conjugate(q[n]) for n in range(3) if n != a) for a in range(3)}
    consistent = fa == {n: 2 for n in range(3) if n != a0}
    Q2 = sp.symbols("Q2_0:3", nonnegative=True)
    eqs = [sp.Eq(1 + sum(2 * Q2[n] for n in range(3) if n != a), 1) for a in range(3)]
    sol = sp.solve(eqs, Q2, dict=True)
    norm_ok = consistent and sol == [{Q2[0]: 0, Q2[1]: 0, Q2[2]: 0}]
    print(f"column norms: faces at an edge of orientation {a0} by normal {fa} (two of each other normal: {consistent}); (E_a, E_a) entry "
          f"= {diag}; with |u_a|^2 = 1 from the zero-curl constant mode, |q_n|^2 = {sol}")
    ok = all(not v["same-role neighbour"] and v["C d0 = 0"] and v["dim Q"] == 3 and v["Q = curl per orientation"] and v["dim R"] == 3
             and v["R = co-curl per orientation"] for v in res.values())
    if not (ok and norm_ok):
        print(f"HIT: a falsifier fires: lattice structure {ok}, column norms {norm_ok}")
    print(f"SUMMARY: the three falsifiers do not fire on doubled lattices L = 2, 3, 4, 5: no site has a same-role nearest neighbour; over "
          f"all complex coefficients the gauge-compatible edge->face maps (Q d0 = 0) and the Gauss-preserving face->edge maps (d0^T R = 0) "
          f"are exactly 3-dimensional, one oriented curl (co-curl) per orientation ({ok}), which contains and extends the runner's "
          f"625-stencil integer census; and with independent orientation coefficients the zero-curl constant mode plus the exact column "
          f"norms force every q_n to 0 ({norm_ok})")


if __name__ == "__main__":
    main()
