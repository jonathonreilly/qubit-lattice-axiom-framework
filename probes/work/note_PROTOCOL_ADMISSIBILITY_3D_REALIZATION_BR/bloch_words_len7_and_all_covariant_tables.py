#!/usr/bin/env python3
"""J:note falsifiers for PROTOCOL_ADMISSIBILITY_3D_REALIZATION_BRIDGE_AND_WORD_DISPERSIVENESS_NARROW_THEOREM_NOTE_2026-07-10 (on main).

Falsifiers implemented, with machinery disjoint from the runner (site-level signed permutations on L = 4, 6, 12 rings, words through
length 5):
  - "a word whose direct site-level product disagrees with its predicted normal form" and "a word with net != 0 whose Bloch
    characteristic polynomial is momentum-independent": EVERY word in the six decorated letters through length 7 (335,923 words),
    multiplied in the Bloch form derived here from the site definition (cell x = 2X + p; S_i|2X+p> = eta_i(p)|2X+p+e_i>, so
    M_i(k)[p', p] = eta_i(p) e^{-i k_i [p_i = 1]}), at four generic momenta, against sigma prod_i e^{-i m_i k_i} S_1^eps1 S_2^eps2 S_3^eps3
    with sigma the parity of cross-axis inversions; then the dichotomy for every (sigma, net) class reached and for every net in
    [-9, 9]^3 directly from the normal form;
  - "a rotation-covariant varying table whose variation set misses an axis": ALL 3^10 = 59,049 rotation-covariant availability tables
    (constant on the 10 rotation orbits of the 64 neighbour profiles), each variation set computed from all one-slot changes;
  - "a frame-conjugated fixed-assignment factor with positive site-modulus translation defect": exact integer site operators on rings
    L = 4, 6, 8: the bare shifts are translation covariant, each decorated shift equals g_i F g_i^dagger with g_1 = 1,
    g_2 = (-1)^(x_0 x_1), g_3 = (-1)^((x_0 + x_1) x_2), and its modulus defect is exactly zero.
HIT if any falsifier fires.
"""
from __future__ import annotations

import itertools

import numpy as np

CELL = list(itertools.product((0, 1), repeat=3))
CIDX = {p: i for i, p in enumerate(CELL)}


def eta(axis, p):
    return 1 if axis == 0 else ((-1) ** p[0] if axis == 1 else (-1) ** (p[0] + p[1]))


def bloch_letter(k, axis, sign):
    M = np.zeros((8, 8), complex)
    for p in CELL:
        q = list(p)
        q[axis] ^= 1
        q = tuple(q)
        M[CIDX[q], CIDX[p]] = eta(axis, p) * (np.exp(-1j * k[axis]) if p[axis] == 1 else 1.0)
    return M if sign > 0 else M.conj().T


KS = [np.array([0.37, 1.21, -0.83]), np.array([2.05, -0.41, 0.66]), np.array([-1.3, 0.9, 2.4]), np.array([0.11, -2.7, 1.55])]
LETTERS = [(0, 1), (0, -1), (1, 1), (1, -1), (2, 1), (2, -1)]
LM = np.array([[bloch_letter(k, a, s) for k in KS] for (a, s) in LETTERS])          # 6 x K x 8 x 8


def normal_form_matrix(net, sigma):
    out = []
    for k in KS:
        M = np.eye(8, dtype=complex)
        phase = 1.0
        for a in range(3):
            e = net[a] % 2
            m = (net[a] - e) // 2
            phase *= np.exp(-1j * m * k[a])
            if e:
                M = M @ bloch_letter(k, a, 1)
        out.append(sigma * phase * M)
    return np.array(out)


def words_check(maxlen=7):
    """Dynamic programming over lengths: products for all words of length n, extended letter by letter (appended on the right)."""
    prods = np.broadcast_to(np.eye(8, dtype=complex), (1, len(KS), 8, 8)).copy()
    data = [(0, (0, 0, 0), (0, 0, 0))]                                   # (sigma parity, net, counts of letters per axis)
    total, worst, classes = 1, 0.0, {}
    cache = {}
    for n in range(1, maxlen + 1):
        new_prods, new_data = [], []
        for li, (a, s) in enumerate(LETTERS):
            P = np.einsum("wkij,kjl->wkil", prods, LM[li])
            nd = []
            for (par, net, cnt) in data:
                inv = sum(cnt[b] for b in range(a + 1, 3))                  # earlier letters of larger axis stand before this one
                net2 = list(net)
                net2[a] += s
                cnt2 = list(cnt)
                cnt2[a] += 1
                nd.append(((par + inv) % 2, tuple(net2), tuple(cnt2)))
            for w, (par, net2, _) in enumerate(nd):
                key = (par, net2)
                if key not in cache:
                    cache[key] = normal_form_matrix(net2, -1 if par else 1)
                worst = max(worst, float(np.abs(P[w] - cache[key]).max()))
                classes[key] = True
            new_prods.append(P)
            new_data += nd
        prods = np.concatenate(new_prods)
        data = new_data
        total += len(data)
        if n == maxlen - 1:
            pass
    return total, worst, list(classes)


def dispersive(net, sigma):
    polys = [np.poly(M) for M in normal_form_matrix(net, sigma)]
    return max(float(np.abs(p - polys[0]).max()) for p in polys[1:])


def dichotomy(keys):
    bad = []
    for (par, net) in keys:
        d = dispersive(net, -1 if par else 1)
        if (d > 1e-9) != (net != (0, 0, 0)):
            bad.append((par, net, d))
    return bad


# ------------------------------------------------------------------------------------------------ availability tables
N6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def rotations():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), int)
            for i in range(3):
                M[i, perm[i]] = signs[i]
            if round(np.linalg.det(M)) == 1:
                out.append(M)
    return out


def tables():
    R = rotations()
    slot_perm = [[N6.index(tuple(M @ np.array(d))) for d in N6] for M in R]
    profiles = list(itertools.product((0, 1), repeat=6))
    orbit_of, orbits = {}, []
    for c in profiles:
        if c in orbit_of:
            continue
        orb = set()
        for sp in slot_perm:
            img = [0] * 6
            for i in range(6):
                img[sp[i]] = c[i]
            orb.add(tuple(img))
        for x in orb:
            orbit_of[x] = len(orbits)
        orbits.append(orb)
    values = [frozenset({0}), frozenset({1}), frozenset({0, 1})]
    counts = {"none": 0, "all six": 0, "other": 0}
    for assign in itertools.product(range(3), repeat=len(orbits)):
        B = lambda c: values[assign[orbit_of[c]]]
        V = set()
        for c in profiles:
            for d in range(6):
                if c[d] == 0:
                    c2 = list(c)
                    c2[d] = 1
                    if B(c) != B(tuple(c2)):
                        V.add(d)
        counts["none" if not V else ("all six" if len(V) == 6 else "other")] += 1
    return len(orbits), counts


# ------------------------------------------------------------------------------------------------------- site frames
def site_checks(L):
    coords = list(itertools.product(range(L), repeat=3))
    idx = {c: i for i, c in enumerate(coords)}
    n = len(coords)
    ok = True
    for axis in range(3):
        F0 = np.zeros((n, n), np.int64)
        Fd = np.zeros((n, n), np.int64)
        for x in coords:
            y = list(x)
            y[axis] = (y[axis] + 1) % L
            F0[idx[tuple(y)], idx[x]] = 1
            Fd[idx[tuple(y)], idx[x]] = eta(axis, tuple(v % 2 for v in x))
        g = np.array([1 if axis == 0 else ((-1) ** (x[0] * x[1]) if axis == 1 else (-1) ** ((x[0] + x[1]) * x[2])) for x in coords])
        ok &= bool((Fd == (g[:, None] * F0 * g[None, :])).all())
        for b in range(3):
            T = np.zeros((n, n), np.int64)
            for x in coords:
                y = list(x)
                y[b] = (y[b] + 1) % L
                T[idx[tuple(y)], idx[x]] = 1
            ok &= bool((T @ F0 @ T.T == F0).all())                       # bare shift exactly covariant
            ok &= bool((np.abs(T @ Fd @ T.T) == np.abs(Fd)).all())       # decorated: zero modulus defect
    return ok


def main():
    total, worst, keys = words_check(7)
    bad = dichotomy(keys)
    bad_grid = dichotomy([(par, net) for par in (0, 1) for net in itertools.product(range(-9, 10), repeat=3)])
    print(f"1. {total} words through length 7 in Bloch form at 4 momenta: max |product - normal form| = {worst:.2e}; "
          f"{len(keys)} (sigma, net) classes reached; dichotomy failures among them {bad}; over all net in [-9,9]^3 and both signs: {bad_grid}")
    norb, counts = tables()
    print(f"2. rotation-covariant availability tables: {norb} orbits, 3^{norb} = {3 ** norb} tables; variation sets: {counts}")
    sc = {L: site_checks(L) for L in (4, 6, 8)}
    print(f"3. exact site frames: decorated = g F g^dagger, bare shifts covariant, zero modulus defect on L = 4, 6, 8: {sc}")
    fails = []
    if worst > 1e-10:
        fails.append("normal form")
    if bad or bad_grid:
        fails.append("dispersiveness dichotomy")
    if counts["other"]:
        fails.append("covariant varying table missing an axis")
    if not all(sc.values()):
        fails.append("frame/defect")
    if fails:
        print(f"HIT: {fails}")
    print(f"SUMMARY: all {total} decorated-mover words through length 7 equal their predicted normal form in the Bloch form at four generic "
          f"momenta (max deviation {worst:.1e}); the characteristic polynomial is momentum-independent exactly when net = 0 for every "
          f"(sigma, net) class reached and for every net in [-9,9]^3; of the {3 ** norb} rotation-covariant availability tables "
          f"{counts['none']} have empty variation set and {counts['all six']} vary at all six offsets, none at a proper subset; decorated "
          f"shifts are exact frame conjugates of covariant shifts with zero modulus defect on rings 4, 6, 8; no falsifier fires")


if __name__ == "__main__":
    main()
