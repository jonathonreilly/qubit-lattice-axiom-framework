#!/usr/bin/env python3
"""Parity-grading escape dichotomy (signed-gravity, no-pin route).

Companion runner for
docs/SIGNED_GRAVITY_PARITY_GRADING_ESCAPE_DICHOTOMY_NARROW_THEOREM_NOTE_2026-06-11.md

Verifies:

  [P1] parity-flipping-only operators have eta_delta = 0 on ANY
       geometry: even torus AND open defect box, uniform and random
       complex couplings; same-parity blocks vanish identically;
       {Gamma_5, H} = 0 exactly.
  [P2] on-site uniform mass: eta_delta != 0 but ORIENTATION-EVEN
       (reflection + conjugation leaves eta invariant), at two masses.
  [P3] the registered log-generator form of a strictly-local transfer
       contains same-parity (distance-2) couplings (the BCH
       tails); single-factor control has ZERO same-parity content;
       robust at a second coupling set.
  [F]  a second-difference (Wilson-type) term breaks the parity
       anticommutation and the mirror pairing — the (P1) hypothesis is
       load-bearing.

Deterministic, numpy + scipy, runtime seconds.
Exit code 0 iff TOTAL: PASS=n FAIL=0.
"""

from __future__ import annotations

import sys

import numpy as np
from scipy.linalg import expm, logm

PASS = 0
FAIL = 0
DELTA = 1e-8


def check(tag: str, label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        s = "PASS"
    else:
        FAIL += 1
        s = "FAIL"
    print(f"  [{s}] [{tag}] {label}" + (f"  ({detail})" if detail else ""))


def section(title: str) -> None:
    print()
    print("-" * 76)
    print(title)
    print("-" * 76)


def eta_of(H: np.ndarray, delta: float = DELTA) -> int:
    lam = np.linalg.eigvalsh(H)
    return int(np.sum(lam > delta) - np.sum(lam < -delta))


# ---------------------------------------------------------------------------
# geometries and NN operators
# ---------------------------------------------------------------------------

def torus_sites_bonds(L):
    sites = [(x, y) for x in range(L) for y in range(L)]
    bonds = []
    for x in range(L):
        for y in range(L):
            bonds.append(((x, y), ((x + 1) % L, y)))
            bonds.append(((x, y), (x, (y + 1) % L)))
    return sites, bonds


def defect_box_sites_bonds():
    """Open 5x4 box with the interior site (2,2) removed.
    Symmetric under x -> 4 - x (the defect is on the mirror axis)."""
    sites = [(x, y) for x in range(5) for y in range(4) if (x, y) != (2, 2)]
    bonds = []
    for (x, y) in sites:
        if (x + 1, y) in sites and x + 1 < 5:
            bonds.append(((x, y), (x + 1, y)))
        if (x, y + 1) in sites and y + 1 < 4:
            bonds.append(((x, y), (x, y + 1)))
    return sites, bonds


def nn_H(sites, bonds, seed=None):
    rng = np.random.default_rng(seed)
    N = len(sites)
    idx = {s: i for i, s in enumerate(sites)}
    H = np.zeros((N, N), dtype=complex)
    for (a, b) in bonds:
        t = (rng.standard_normal() + 1j * rng.standard_normal()) \
            if seed is not None else 0.5j
        H[idx[a], idx[b]] += t
        H[idx[b], idx[a]] += np.conj(t)
    return H, idx


def parity_vec(sites):
    return np.array([(s[0] + s[1]) % 2 for s in sites])


def main() -> int:
    print("=" * 76)
    print("PARITY-GRADING ESCAPE DICHOTOMY (signed-gravity, no-pin route)")
    print("(P1) parity-flipping-only => eta = 0 on ANY geometry;")
    print("(P2) on-site mass is orientation-even; (P3) the registered")
    print("log-generator contains the forbidden-class couplings")
    print("=" * 76)

    # =======================================================================
    section("[P1] general parity obstruction: torus AND open defect box")
    # =======================================================================
    for label_g, (sites, bonds) in (("even 6x6 torus", torus_sites_bonds(6)),
                                    ("open 5x4 defect box",
                                     defect_box_sites_bonds())):
        for seed, lab in ((None, "uniform"), (11, "random cplx seed 11")):
            H, idx = nn_H(sites, bonds, seed)
            par = parity_vec(sites)
            blk = max(np.abs(H[np.ix_(par == 0, par == 0)]).max(),
                      np.abs(H[np.ix_(par == 1, par == 1)]).max())
            G5 = np.diag([(-1.0) ** p for p in par])
            anti = np.abs(G5 @ H @ G5 + H).max()
            check("P1", f"{label_g}, {lab}: same-parity blocks = 0, "
                        f"{{Gamma_5, H}} = 0, eta = 0",
                  blk < 1e-14 and anti < 1e-14 and eta_of(H) == 0,
                  f"blocks = {blk:.1e}, anti = {anti:.1e}, "
                  f"eta = {eta_of(H):+d}")

    # =======================================================================
    section("[P2] on-site mass: nonzero eta but ORIENTATION-EVEN")
    # =======================================================================
    sites, bonds = defect_box_sites_bonds()
    H0, idx = nn_H(sites, bonds, seed=11)
    N = len(sites)
    refl = np.zeros((N, N))
    for s in sites:
        refl[idx[(4 - s[0], s[1])], idx[s]] = 1.0
    for m in (0.7, 0.3):
        Hm = H0 + m * np.eye(N)
        Hm_rev = refl @ H0.conj() @ refl.T + m * np.eye(N)  # reflect + conj
        e, er = eta_of(Hm), eta_of(Hm_rev)
        check("P2", f"m = {m}: eta != 0 but orientation-reversed eta is "
                    f"IDENTICAL (orientation-even; cannot source the "
                    f"[+1,-1] pair)",
              e != 0 and er == e, f"eta = {e:+d}, reversed = {er:+d}")

    # =======================================================================
    section("[P3] the registered log-generator contains same-parity "
            "couplings")
    # =======================================================================
    I2 = np.eye(2)
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    Z = np.diag([1.0, -1.0]).astype(complex)
    PAULI = {"I": I2, "X": X, "Y": Y, "Z": Z}

    def kron3(a, b, c):
        return np.kron(np.kron(a, b), c)

    def same_parity_content(Hmat):
        """Max |coeff| over Pauli strings with support on BOTH end sites
        (distance 2 = same parity on the 3-site chain)."""
        best = 0.0
        for a in "IXYZ":
            for b in "IXYZ":
                for c in "IXYZ":
                    if a == "I" or c == "I":
                        continue
                    P = kron3(PAULI[a], PAULI[b], PAULI[c])
                    best = max(best, abs(np.trace(P.conj().T @ Hmat)) / 8.0)
        return best

    def log_generator(A, B):
        T = expm(-A / 2) @ expm(-B) @ expm(-A / 2)
        Hl = -logm(T)
        return 0.5 * (Hl + Hl.conj().T)

    A1 = 0.9 * kron3(X, X, I2) + 0.4 * kron3(Z, I2, I2)
    B1 = 0.7 * kron3(I2, Z, Z) + 0.3 * kron3(I2, I2, X)
    c1 = same_parity_content(log_generator(A1, B1))
    check("P3", "witness transfer: -log T has same-parity "
                "(distance-2) coupling > 0.04 (the BCH tails ARE the "
                "forbidden-class structure)",
          c1 > 0.04, f"max same-parity coeff = {c1:.4f}")
    A2 = 0.6 * kron3(Y, X, I2) + 0.5 * kron3(X, I2, I2)
    B2 = 0.8 * kron3(I2, Z, X) + 0.2 * kron3(I2, I2, Z)   # Z_1 vs X_1: non-commuting
    c2 = same_parity_content(log_generator(A2, B2))
    check("P3", "second (non-commuting) coupling set: same-parity content "
                "persists (not a fine-tuned accident)",
          c2 > 0.01, f"max same-parity coeff = {c2:.4f}")
    # commuting control: if A and B commute on the shared site, the BCH
    # tails vanish and log T = A + B exactly -- zero same-parity content.
    A3 = 0.6 * kron3(Y, X, I2)
    B3 = 0.8 * kron3(I2, X, Z)                              # X_1 vs X_1: commuting
    c3 = same_parity_content(log_generator(A3, B3))
    check("P3", "commuting control: [A, B] = 0 gives log T = A + B exactly "
                "and ZERO same-parity content (the tails come from "
                "non-commutativity, as the BCH structure says)",
          c3 < 1e-10, f"same-parity coeff = {c3:.1e}")
    # single-factor control: -log e^{-A} = A exactly, no distance-2 content
    Tsingle = expm(-A1)
    Hl_single = -logm(Tsingle)
    Hl_single = 0.5 * (Hl_single + Hl_single.conj().T)
    c0 = same_parity_content(Hl_single)
    back = np.abs(Hl_single - A1).max()
    check("P3", "single-factor control: -log e^{-A} = A exactly, ZERO "
                "same-parity content (the escape is generated by "
                "non-commuting composition only)",
          back < 1e-10 and c0 < 1e-10,
          f"resid = {back:.1e}, same-parity = {c0:.1e}")

    # =======================================================================
    section("[F] the (P1) hypothesis is load-bearing")
    # =======================================================================
    # add a Wilson-type second difference along x on the torus:
    # same-parity couplings (distance 2) + on-site compensation.
    sites, bonds = torus_sites_bonds(6)
    H, idx = nn_H(sites, bonds, seed=11)
    W = np.zeros_like(H)
    r = 0.8
    for (x, y) in sites:
        i = idx[(x, y)]
        j = idx[((x + 2) % 6, y)]
        W[i, j] += -r / 2
        W[j, i] += -r / 2
        W[i, i] += r
    Hw = H + W
    par = parity_vec(sites)
    G5 = np.diag([(-1.0) ** p for p in par])
    anti_w = np.abs(G5 @ Hw @ G5 + Hw).max()
    lam = np.sort(np.linalg.eigvalsh(Hw))
    # mirror pairing <=> lambda_(i) = -lambda_(n-1-i) for all i
    mirror_resid = float(np.abs(lam + lam[::-1]).max())
    lam0 = np.sort(np.linalg.eigvalsh(H))
    mirror_resid0 = float(np.abs(lam0 + lam0[::-1]).max())
    check("F", "second-difference (Wilson-type) term breaks "
               "{Gamma_5, H} = 0 by a nonzero margin",
          anti_w > 0.5, f"max|anti| = {anti_w:.3f}")
    check("F", "control: the bare NN operator IS mirror-paired "
               "(residual = 0), and the second-difference term lifts the "
               "pairing (residual > 0) -- the (P1) hypothesis is "
               "load-bearing; sufficiency = the sister realization note",
          mirror_resid0 < 1e-10 and mirror_resid > 0.1,
          f"mirror residual: NN = {mirror_resid0:.1e} -> "
          f"+Wilson = {mirror_resid:.3f}")

    print()
    print("=" * 76)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 76)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
