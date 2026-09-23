#!/usr/bin/env python3
"""Uniform ice seen by layer units: the flux sectors of the layer transfer
matrix cost free energy close to quadratic in the flux and inverse in the
cross-section, with one stiffness across cross-sections.

Open PR 8740 formed the uniform ice measure (3 of each vertex's 6 links
occupied) on infinite prisms layer by layer: the transfer matrix T[v, w]
between vertical-link layers conserves the staggered vertical flux
S(v) = sum of (-1)^(x+y) (2 v - 1) (it flips sign at every layer), and long
prisms select zero flux.  Here the flux sectors are compared across three
cross-sections, 2 x 2, 2 x 4 and 2 x 6 (areas A = 4, 8, 12).  With lambda_S
the largest eigenvalue modulus in the sector |S|, the free energy of flux S
per layer is f(S) = -ln(lambda_S / lambda_0).
  * The counts are checked: trace T^2 = 9600 on 2 x 2 (the landed torus),
    and the tori 2 x 2 x 4 and 2 x 2 x 6 are counted two ways.
  * Every cross-section conserves |S|, and zero flux has the largest
    eigenvalue.
  * f(S) A / S^2 lies between 0.28 and 0.41 over every flux sector of all
    three cross-sections; for the smallest flux, |S| = 2, it takes the
    values 0.2808, 0.3073 and 0.3121 at A = 4, 8, 12, with shrinking steps;
    at each A it rises slowly with the flux.
So the flux sectors cost close to c S^2 / A per layer with one c near 0.31,
with corrections growing with the flux density: the Gaussian flux stiffness
of a Coulomb phase, seen by layer units.  The landed cubic-ice note
computes the Coulomb correlations of the same measure.  No constant is
compared with any outside value.

Next-steps campaign after the TOE derivation campaign by underdetermination
witnesses.

Declared objects
  * a x b transverse tori (a = 2, b = 2, 4, 6) times the integers; the
    uniform ice measure; the layer transfer matrix of open PR 8740, built
    from exact integer counts of in-plane configurations with prescribed
    degrees;
  * eigenvalues of each flux sector's block in floating point, checked
    against exact integer traces;
  * the in-plane configurations are enumerated in chunks of 2^18.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys

import numpy as np

RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


def transfer(a, b, chunk=1 << 18):
    V = [(x, y) for x in range(a) for y in range(b)]
    idx = {v: i for i, v in enumerate(V)}
    links = []
    for x, y in V:
        links.append((idx[(x, y)], idx[((x + 1) % a, y)]))
        links.append((idx[(x, y)], idx[(x, (y + 1) % b)]))
    E, n = len(links), len(V)
    P = np.array([5 ** i for i in range(n)], dtype=np.int64)
    counts = {}
    for start in range(0, 1 << E, chunk):
        cfg = (np.arange(start, min(start + chunk, 1 << E), dtype=np.int64)[:, None] >> np.arange(E, dtype=np.int64)) & 1
        deg = np.zeros((cfg.shape[0], n), dtype=np.int64)
        for j, (p, q) in enumerate(links):
            deg[:, p] += cfg[:, j]
            deg[:, q] += cfg[:, j]
        u, c = np.unique(deg @ P, return_counts=True)
        for k, m in zip(u.tolist(), c.tolist()):
            counts[k] = counts.get(k, 0) + m
    N = 1 << n
    bits = ((np.arange(N)[:, None] >> np.arange(n)) & 1).astype(np.int64)
    T = np.zeros((N, N), dtype=np.int64)
    for v in range(N):
        need = 3 - bits[v][None, :] - bits
        ok = (need >= 0).all(axis=1) & (need <= 4).all(axis=1)
        keys = np.clip(need, 0, 4) @ P
        T[v] = [counts.get(int(k), 0) if o else 0 for k, o in zip(keys, ok)]
    eps = np.array([(-1) ** (x + y) for x, y in V])
    flux = (2 * bits - 1) @ eps
    return T, flux


def trace_power(T, H):
    P = np.array(T, dtype=object)
    M = P.copy()
    for _ in range(H - 1):
        M = M.dot(P)
    return int(sum(M[i, i] for i in range(M.shape[0])))


CROSS = {(2, 2): None, (2, 4): None, (2, 6): None}
for ab in CROSS:
    CROSS[ab] = transfer(*ab)

print("A. the counts")
T22, T24, T26 = CROSS[(2, 2)][0], CROSS[(2, 4)][0], CROSS[(2, 6)][0]
tr22 = {H: trace_power(T22, H) for H in (2, 4, 6)}
tr24 = trace_power(T24, 2)
t26 = T26.astype(object)
tr26 = int(sum((t26[i, :] * t26[:, i]).sum() for i in range(t26.shape[0])))
check("trace T^2 = 9600 on 2 x 2, and the tori 2 x 2 x 4 and 2 x 2 x 6 agree with transfers along another axis",
      tr22[2] == 9600 and tr22[4] == tr24 and tr22[6] == tr26,
      f"2 x 2 x 4: {tr22[4]}; 2 x 2 x 6: {tr22[6]}")

print("B. flux sectors")
spec, sector_ok = {}, True
for ab, (T, flux) in CROSS.items():
    N = T.shape[0]
    nz = np.nonzero(T)
    sector_ok = sector_ok and bool(np.all(flux[nz[1]] == -flux[nz[0]]))
    spec[ab] = {}
    for S in sorted(set(np.abs(flux).tolist())):
        idx = np.where(np.abs(flux) == S)[0]
        ev = np.linalg.eigvalsh(T[np.ix_(idx, idx)].astype(float))
        spec[ab][S] = float(np.max(np.abs(ev)))
    sector_ok = sector_ok and all(spec[ab][S] < spec[ab][0] for S in spec[ab] if S)
check("every cross-section conserves the size of the flux, and zero flux carries the largest eigenvalue",
      sector_ok,
      "; ".join(f"{a} x {b}: lambda_0 = {spec[(a, b)][0]:.4f}, sectors |S| = 0.." + str(max(spec[(a, b)])) for a, b in spec))

print("C. the flux stiffness")
coef = {ab: {S: -np.log(spec[ab][S] / spec[ab][0]) * ab[0] * ab[1] / S ** 2 for S in spec[ab] if S} for ab in spec}
allc = [c for ab in coef for c in coef[ab].values()]
small = [coef[ab][2] for ab in ((2, 2), (2, 4), (2, 6))]
rising = all(all(coef[ab][S1] <= coef[ab][S2] + 1e-12 for S1, S2 in zip(sorted(coef[ab]), sorted(coef[ab])[1:])) for ab in coef)
check("f(S) A / S^2 stays between 0.28 and 0.41 over every flux sector, and at the smallest flux it settles near 0.31",
      min(allc) > 0.28 and max(allc) < 0.41 and small[0] < small[1] < small[2]
      and (small[2] - small[1]) < (small[1] - small[0]) / 4 and abs(small[2] - 0.3121) < 1e-3 and rising,
      "smallest flux, A = 4, 8, 12: " + ", ".join(f"{c:.4f}" for c in small)
      + "; by flux on 2 x 6: " + ", ".join(f"|S| = {S}: {c:.4f}" for S, c in sorted(coef[(2, 6)].items()))
      + "; at each A the coefficient rises with the flux")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
