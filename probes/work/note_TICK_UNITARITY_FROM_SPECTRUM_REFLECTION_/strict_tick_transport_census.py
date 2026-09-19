#!/usr/bin/env python3
"""J:note falsifier for TICK_UNITARITY_FROM_SPECTRUM_REFLECTION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-06-10 (on main).

Falsifier implemented (the note's third): "a retained-surface derivation that the realized strict tick FAILS the tick-level transport
of both retained identities (would empty the C-reading on the realized carrier and re-open bare P2)".

The note's C-reading: the realized tick carries a tick-level transport Theta T Theta^-1 = T^-1 of either identity, (a) the unitary
sublattice parity eps (eps H eps = -H) or (b) the antiunitary commuting representative, which the note's runner implements as
Theta = eps o K (Part E3/E4); the runner checks both only on the exponential tick e^{-iH}, which is not radius 1 (its Part G1). The
cited CPT note also declares P o K (its Theta_H = C P T_H) and the unitary inversion P (P H P = -H).

The realized strict tick of the chain is site-licensed (radius 1 in sites, the dichotomy note's P1 reading) and dispersive (reduced P4).
This script enumerates EVERY such unitary tick in an exact finite class and tests the four transports literally in position space:
  - period m = 2 (the dichotomy's periodicity), each column (on-site a, right hop b, left hop c) from the alphabet of Gaussian dyadics
    {0, unimodular +-1 +-i, (+-1 +-i)/2, +-1/2, +-i/2} with |a|^2+|b|^2+|c|^2 = 1 (252 columns, 63504 candidate ticks);
  - periods m = 3, 4 (beyond the note's sizes) with unimodular-or-zero entries (12 columns per site);
  - ring of N = 12 sites (at least 5 cells for m = 2, so ring unitarity equals line unitarity for these Laurent degrees); exact
    arithmetic (all entries are dyadic Gaussian rationals, exact in binary floating point); dispersive = the Bloch characteristic
    polynomial depends on z, tested exactly at 2m+2 dyadic points.
Proof of the pattern (checked literally below): eps U eps = U^dag makes eps U a Hermitian unitary radius-1 matrix R with R^2 = I; the
(n+2, n) entry of R^2 is R[n+2,n+1] R[n+1,n] = 0, so no two consecutive bonds carry hopping: the bonds form a matching and U is
block-diagonal on dimers, i.e. flat. For eps o K the same argument runs with the symmetric unitary eps conj(U). Hence neither
transport exists on any dispersive radius-1 unitary tick, at any periodicity.
"""
from __future__ import annotations

import itertools

import numpy as np

N = 12
UNIMOD = [2, -2, 2j, -2j]          # entries of 2U with |U| = 1
HALF = [1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j]  # |U| = 1/sqrt2
QUART = [1, -1, 1j, -1j]           # |U| = 1/2


def columns(full):
    vals = [0] + UNIMOD + (HALF + QUART if full else [])
    n2 = lambda x: complex(x).real ** 2 + complex(x).imag ** 2   # exact for these small integers (abs() would round)
    return [c for c in itertools.product(vals, repeat=3) if n2(c[0]) + n2(c[1]) + n2(c[2]) == 4]


def ring(cols, m):
    V = np.zeros((N, N), dtype=complex)
    for n in range(N):
        a, b, c = cols[n % m]
        V[n, n] += a
        V[(n + 1) % N, n] += b
        V[(n - 1) % N, n] += c
    return V


def perm_sign(p):
    s, p = 1, list(p)
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]
            p[i], p[j] = p[j], p[i]
            s = -s
    return s


PERMS = {k: [(p, perm_sign(p)) for p in itertools.permutations(range(k))] for k in range(1, 5)}


def det(M):
    k = len(M)
    if k == 0:
        return 1
    return sum(s * np.prod([M[i][p[i]] for i in range(k)]) for p, s in PERMS[k])


def bloch(cols, m, z):
    B = [[0j] * m for _ in range(m)]
    for j, (a, b, c) in enumerate(cols):
        B[j][j] += a
        B[(j + 1) % m][j] += b * (z if j == m - 1 else 1)
        B[(j - 1) % m][j] += c * (1 / z if j == 0 else 1)
    return B


def charpoly(B):
    m = len(B)
    return tuple(sum(det([[B[i][j] for j in S] for i in S]) for S in itertools.combinations(range(m), k)) for k in range(1, m + 1))


ZS = [1, -1, 1j, -1j, 2, -2, 2j, -2j, 4, -4]


def dispersive(cols, m):
    ref = charpoly(bloch(cols, m, 1))
    return any(charpoly(bloch(cols, m, z)) != ref for z in ZS[1: 2 * m + 2])


EPS = np.diag([(-1.0) ** n for n in range(N)])
PINV = np.zeros((N, N))
for n in range(N):
    PINV[(-n) % N, n] = 1


def transports(V):
    Vd = V.conj().T
    return {"eps": np.array_equal(EPS @ V @ EPS, Vd), "eps K": np.array_equal(EPS @ V.conj() @ EPS, Vd),
            "P": np.array_equal(PINV @ V @ PINV, Vd), "P K": np.array_equal(PINV @ V.conj() @ PINV, Vd)}


def dimerized(V):
    on = [V[(n + 1) % N, n] != 0 or V[n, (n + 1) % N] != 0 for n in range(N)]
    return not any(on[n] and on[(n + 1) % N] for n in range(N))


def census(m, full):
    cols = columns(full)
    out = {"candidates": 0, "unitary": 0, "dispersive": 0, "dispersive non-monomial": 0,
           "dispersive with": {"eps": 0, "eps K": 0, "P": 0, "P K": 0}, "flat with eps or eps K": 0,
           "eps/eps K transporters not dimerized": 0, "shift phases with P K": set(), "shift phases with P": set()}
    four_I = 4 * np.eye(N)
    for combo in itertools.product(cols, repeat=m):
        out["candidates"] += 1
        V = ring(combo, m)
        if not np.array_equal(V.conj().T @ V, four_I):
            continue
        out["unitary"] += 1
        t = transports(V)
        disp = dispersive(combo, m)
        if (t["eps"] or t["eps K"]) and not dimerized(V):
            out["eps/eps K transporters not dimerized"] += 1
        if disp:
            out["dispersive"] += 1
            if any(sum(1 for x in c if x != 0) > 1 for c in combo):
                out["dispersive non-monomial"] += 1
            for k in t:
                out["dispersive with"][k] += t[k]
            if m == 2:
                ph = tuple(x / 2 for c in combo for x in c if x != 0)
                if t["P K"]:
                    out["shift phases with P K"].add(ph)
                if t["P"]:
                    out["shift phases with P"].add(ph)
        elif t["eps"] or t["eps K"]:
            out["flat with eps or eps K"] += 1
    return out


def main():
    # the note's H-level instance on the same ring, exact: massless hopping H = i D
    D = np.zeros((N, N))
    for n in range(N):
        D[n, (n + 1) % N] += 0.5
        D[(n + 1) % N, n] -= 0.5
    H = 1j * D
    hl = {"eps H eps = -H": np.array_equal(EPS @ H @ EPS, -H), "P H P = -H": np.array_equal(PINV @ H @ PINV, -H),
          "conj(H) = -H": np.array_equal(H.conj(), -H)}
    print(f"0. H-level identities of the cited CPT note on the N = {N} ring (exact): {hl}; they give all four transports on e^(-iH), "
          f"which is not radius 1 (the note's runner Part G1)")
    results = {}
    for m, full in ((2, True), (3, False), (4, False)):
        r = census(m, full)
        results[m] = r
        extra = ""
        if m == 2:
            extra = (f"; dispersive (q, r) phase pairs with P K: {sorted(r['shift phases with P K'], key=str)}; with P: "
                     f"{sorted(r['shift phases with P'], key=str)}")
        print(f"{m - 1}. period m = {m} ({'252-column dyadic alphabet' if full else 'unimodular-or-zero entries'}), ring N = {N}: candidates "
              f"{r['candidates']}, unitary {r['unitary']}, dispersive {r['dispersive']} (non-monomial among them "
              f"{r['dispersive non-monomial']}); dispersive ticks carrying each tick-level transport {r['dispersive with']}; flat ticks "
              f"carrying eps or eps K {r['flat with eps or eps K']}; eps/eps K transporters that are not dimerized "
              f"{r['eps/eps K transporters not dimerized']}{extra}")
    no_eps = all(r["dispersive"] > 0 and r["dispersive with"]["eps"] == 0 and r["dispersive with"]["eps K"] == 0 for r in results.values())
    proof_ok = all(r["eps/eps K transporters not dimerized"] == 0 for r in results.values())
    pk = {m: (r["dispersive with"]["P K"], r["dispersive with"]["P"], r["dispersive"]) for m, r in results.items()}
    if no_eps and proof_ok:
        print(f"HIT: falsifier 3 fires for the pair the note reads and its runner implements (eps; Theta = eps o K): no dispersive "
              f"radius-1 unitary tick carries either tick-level transport at periods 2, 3, 4 (dispersive ticks "
              f"{[r['dispersive'] for r in results.values()]}, transporting 0 and 0), every eps- or eps o K-transporting tick is dimerized "
              f"(flat), and by the theorem an invertible contraction carrying them is unitary, hence flat too; only inversion-based "
              f"representatives transport on dispersive strict ticks: (P o K, P, of dispersive) = {pk}")
    print(f"SUMMARY: on the realized strict-tick class (radius-1, unitary, dispersive) the note's C-reading via eps or eps o K is empty at "
          f"every enumerated periodicity (m = 2: {results[2]['dispersive']} dispersive ticks, all monomial site shifts; m = 3, 4 likewise); "
          f"the transports survive only as P o K (the CPT note's Theta_H) or P, under a phase condition on the shift: counts "
          f"(P o K, P, dispersive) = {pk}; the theorem's own forward and converse directions are untouched")


if __name__ == "__main__":
    main()
