#!/usr/bin/env python3
"""Exact checks for the qubit-lattice ball capacity versus spherical entropy
bound note (2026-11-27).

Every check uses Python integers and fractions.Fraction. No floating-point
value enters a PASS decision. Irrational constants (ln 2, pi) enter only
through rational bounds that the runner itself certifies:

* ln 2 = sum_{k>=1} 1/(k 2^k), with positive terms and the tail bound
  sum_{k>K} 1/(k 2^k) <= 1/((K+1) 2^K);
* pi < 22/7 through the polynomial division behind Dalzell's integral;
* two-sided pi bounds through Machin's formula, whose Gaussian-integer form
  (5+i)^4 (239-i) = 114244 (1+i) is checked exactly, and alternating-series
  brackets for arctan(1/5) and arctan(1/239).

The general proofs are in the paired note. This runner checks the exact
rational steps of those proofs, exhaustive finite instances, a brute-force
recount of the lattice-point numbers by a second method, and controls that
fail when the statement is perturbed.

Reads: no external scientific input. One package-local integrity read: the
paired note, whose SHA-256 is printed.
"""
from __future__ import annotations

import hashlib
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/QUBIT_LATTICE_BALL_CAPACITY_EXCEEDS_SPHERICAL_ENTROPY_BOUND_BOUNDED_THEOREM_NOTE_2026-11-27.md",
)

REPO_ROOT = Path(__file__).resolve().parent.parent
PASS_COUNT = 0


def check(name: str, condition: bool) -> None:
    global PASS_COUNT
    if not condition:
        raise AssertionError(name)
    PASS_COUNT += 1
    print(f"PASS: {name}")


# ---------------------------------------------------------------------------
# Rational bounds for ln 2 and pi
# ---------------------------------------------------------------------------


def ln2_bounds(K: int) -> tuple[Q, Q]:
    """lower = sum_{k=1}^K 1/(k 2^k); upper = lower + 1/((K+1) 2^K)."""
    lower = sum((Q(1, k * 2**k) for k in range(1, K + 1)), Q(0))
    return lower, lower + Q(1, (K + 1) * 2**K)


def arctan_inv_bounds(q: int, K: int) -> tuple[Q, Q]:
    """Bracket arctan(1/q) by consecutive partial sums of the alternating
    series sum_k (-1)^k / ((2k+1) q^(2k+1)), whose terms decrease for q >= 2."""
    s = Q(0)
    partial = []
    for k in range(K + 2):
        s += Q((-1) ** k, (2 * k + 1) * q ** (2 * k + 1))
        partial.append(s)
    a, b = partial[-2], partial[-1]
    return min(a, b), max(a, b)


def pi_bounds(K: int) -> tuple[Q, Q]:
    lo5, hi5 = arctan_inv_bounds(5, K)
    lo239, hi239 = arctan_inv_bounds(239, K)
    return 16 * lo5 - 4 * hi239, 16 * hi5 - 4 * lo239


def poly_mul(p: list[int], q: list[int]) -> list[int]:
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def poly_add(p: list[int], q: list[int]) -> list[int]:
    n = max(len(p), len(q))
    return [(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n)]


def poly_integral_0_1(p: list[int]) -> Q:
    return sum((Q(c, i + 1) for i, c in enumerate(p)), Q(0))


# ---------------------------------------------------------------------------
# Lattice-point counts
# ---------------------------------------------------------------------------


def ball_count(R: int) -> int:
    """N(R) = #{x in Z^3 : x.x <= R^2}, by columns with exact isqrt."""
    n = R * R
    total = 0
    for x in range(-R, R + 1):
        m = n - x * x
        s = isqrt(m)
        for y in range(-s, s + 1):
            total += 2 * isqrt(m - y * y) + 1
    return total


def ball_count_brute(R: int) -> int:
    n = R * R
    return sum(
        1
        for x in range(-R, R + 1)
        for y in range(-R, R + 1)
        for z in range(-R, R + 1)
        if x * x + y * y + z * z <= n
    )


def boundary_count(R: int) -> int:
    """Sites of B_R with at least one nearest neighbour outside B_R."""
    n = R * R

    def col(x: int, y: int) -> int:
        m = n - x * x - y * y
        return isqrt(m) if m >= 0 else -1

    total = 0
    for x in range(-R, R + 1):
        for y in range(-R, R + 1):
            s = col(x, y)
            if s < 0:
                continue
            t = min(s - 1, col(x + 1, y), col(x - 1, y), col(x, y + 1), col(x, y - 1))
            total += (2 * s + 1) if t < 0 else 2 * (s - t)
    return total


def boundary_count_brute(R: int) -> int:
    n = R * R
    inside = lambda x, y, z: x * x + y * y + z * z <= n
    nbrs = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
    return sum(
        1
        for x in range(-R, R + 1)
        for y in range(-R, R + 1)
        for z in range(-R, R + 1)
        if inside(x, y, z) and any(not inside(x + a, y + b, z + c) for a, b, c in nbrs)
    )


def cube_side(R: int) -> int:
    """2m+1 for the largest m with 3 m^2 <= R^2."""
    return 2 * isqrt((R * R) // 3) + 1


# ---------------------------------------------------------------------------


def main() -> None:
    note = REPO_ROOT / AUDIT_INPUT_PATHS[0]
    print("Note SHA256:", hashlib.sha256(note.read_bytes()).hexdigest())
    print("Exact checks: qubit-lattice ball capacity versus the spherical entropy bound.")

    # --- Constants -------------------------------------------------------
    lo6, hi6 = ln2_bounds(6)
    check("ln 2 > 69/100: partial sum to k=6 equals 1327/1920 > 69/100", lo6 == Q(1327, 1920) and lo6 > Q(69, 100))
    check("ln 2 < 7/10 (tail bound at K=6), so a mutated constant 7/10 is rejected", hi6 < Q(7, 10))

    # Dalzell: x^4 (1-x)^4 = (1+x^2)(x^6-4x^5+5x^4-4x^2+4) - 4
    one_minus_x_4 = [1, -4, 6, -4, 1]
    lhs = poly_mul([0, 0, 0, 0, 1], one_minus_x_4)
    quotient = [4, 0, -4, 0, 5, -4, 1]
    rhs = poly_add(poly_mul([1, 0, 1], quotient), [-4])
    check("Dalzell identity x^4(1-x)^4 = (1+x^2)(x^6-4x^5+5x^4-4x^2+4) - 4", lhs == rhs)
    check("integral_0^1 of the quotient polynomial is exactly 22/7", poly_integral_0_1(quotient) == Q(22, 7))

    g = (5, 1)
    p = (1, 0)
    for _ in range(4):
        p = (p[0] * g[0] - p[1] * g[1], p[0] * g[1] + p[1] * g[0])
    machin = (p[0] * 239 + p[1], p[1] * 239 - p[0])
    check("Machin identity (5+i)^4 (239-i) = 114244 (1+i)", machin == (114244, 114244))
    pi_lo, pi_hi = pi_bounds(12)
    ln2_lo, ln2_hi = ln2_bounds(80)
    check("certified pi bracket has width < 1e-15 and sits inside (333/106, 22/7)",
          pi_hi - pi_lo < Q(1, 10**15) and Q(333, 106) < pi_lo and pi_hi < Q(22, 7))
    check("certified ln 2 bracket has width < 1e-20 and sits inside (69/100, 7/10)",
          ln2_hi - ln2_lo < Q(1, 10**20) and Q(69, 100) < ln2_lo and ln2_hi < Q(7, 10))

    # --- Lattice counts: two methods ------------------------------------
    check("hand counts N(1) = 7 and N(2) = 1+6+12+8+6 = 33", ball_count(1) == 7 and ball_count(2) == 33)
    check("column count equals brute-force count for R = 1..12",
          all(ball_count(R) == ball_count_brute(R) for R in range(1, 13)))
    check("boundary-site count equals brute-force count for R = 1..10",
          all(boundary_count(R) == boundary_count_brute(R) for R in range(1, 11)))

    RMAX = 160
    N = {R: ball_count(R) for R in range(1, RMAX + 1)}
    print("N(R) at R = 1..10:", [N[R] for R in range(1, 11)])
    print("N(R) at R = 20, 40, 80, 160:", [N[R] for R in (20, 40, 80, 160)])

    # --- Theorem 1 -------------------------------------------------------
    check("Theorem 1(i): N(R) >= (2m+1)^3, 3m^2 <= R^2, for R = 1..160",
          all(N[R] >= cube_side(R) ** 3 for R in N))
    check("Theorem 1(ii) step: (8/7)^2 * 3 < 4, so 8/7 < 2/sqrt(3)", Q(8, 7) ** 2 * 3 < 4)
    check("Theorem 1(ii): 2m+1 > R and N(R) > R^3 for R = 7..160",
          all(cube_side(R) > R and N[R] > R**3 for R in range(7, RMAX + 1)))
    check("Theorem 1(ii) needs a lower limit: 2m+1 <= R exactly at R = 1, 3, 5 within 1..160",
          [R for R in range(1, RMAX + 1) if cube_side(R) <= R] == [1, 3, 5])

    # --- Theorem 2: the rational chain ----------------------------------
    c = 6
    left = Q(69, 100) * c
    right = Q(22, 7) * Q(8, 7) ** 2
    check("Theorem 2 step: (R+1) <= (8/7) R for R >= 7", all(Q(R + 1) <= Q(8, 7) * R for R in range(7, 1000)))
    check("Theorem 2 step: (69/100)*6 = 207/50 > (22/7)(64/49) = 1408/343",
          left == Q(207, 50) and right == Q(1408, 343) and left > right)
    check("Control: the same step fails with constant 5 in place of 6",
          not (Q(69, 100) * 5 > right))

    lam2_values = [Q(1), Q(2), Q(4), Q(10), Q(100), Q(9, 4), Q(1, 3)]
    for lam2 in lam2_values:
        start = max(7, -(-(6 * lam2.numerator) // lam2.denominator))
        rng = [R for R in range(start, RMAX + 1)]
        if rng:
            ok = all(Q(69, 100) * N[R] > Q(22, 7) * lam2 * (R + 1) ** 2 for R in rng)
            check(f"Theorem 2 instances, lambda^2 = {lam2}: (69/100) N(R) > (22/7) lambda^2 (R+1)^2 "
                  f"for R = {start}..{RMAX}", ok)
        else:
            print(f"NOTE: lambda^2 = {lam2}: threshold {start} > {RMAX}, so no instance in R = 1..{RMAX}; "
                  f"spot instances at R = {start} and {start + 400} instead")
            spots = (start, start + 400)
            ok = all(Q(69, 100) * ball_count(R) > Q(22, 7) * lam2 * (R + 1) ** 2 for R in spots)
            check(f"Theorem 2 spot instances, lambda^2 = {lam2}: (69/100) N(R) > (22/7) lambda^2 (R+1)^2 "
                  f"at R = {spots[0]}, {spots[1]}", ok)

    # --- Exact minimal crossover table ----------------------------------
    print("Minimal R with N(R) ln 2 > pi lambda^2 (R+1)^2 (certified brackets):")
    for lam2 in [Q(1), Q(2), Q(4), Q(10), Q(100)]:
        Rmin = None
        for R in range(1, RMAX + 1):
            exceeds = N[R] * ln2_lo > pi_hi * lam2 * (R + 1) ** 2
            below = N[R] * ln2_hi < pi_lo * lam2 * (R + 1) ** 2
            if not (exceeds or below):
                raise AssertionError(f"undecided at lambda^2={lam2}, R={R}")
            if exceeds and Rmin is None:
                Rmin = R
        assert Rmin is not None
        after_all_exceed = all(N[R] * ln2_lo > pi_hi * lam2 * (R + 1) ** 2 for R in range(Rmin, RMAX + 1))
        thm = max(7, -(-(6 * lam2.numerator) // lam2.denominator))
        check(f"lambda^2={lam2}: minimal crossover R={Rmin}, no re-crossing up to {RMAX}, "
              f"and R_min <= Theorem 2 threshold {thm}", after_all_exceed and Rmin <= thm)

    # --- Corollary (refinement at fixed physical radius) -----------------
    # l_P = 1. Condition a <= r/7 and a^3 <= r/12 gives floor(r/a) >= max(7, 6 a^2).
    for r in [Q(10), Q(100), Q(1000)]:
        for a in [Q(1), Q(1, 2), Q(1, 10), Q(3, 2), Q(2)]:
            if a <= r / 7 and a**3 <= r / 12:
                Ra = (r / a).numerator // (r / a).denominator
                check(f"refinement condition r={r}, a={a}: floor(r/a)={Ra} >= max(7, 6a^2)",
                      Ra >= 7 and Ra >= 6 * a * a)

    # --- Corollary (orthogonal-state count) ------------------------------
    for R in (10, 20, 40):
        gap_lo = N[R] * ln2_lo - pi_hi * (R + 1) ** 2
        check(f"lambda=1, R={R}: N ln2 - pi (R+1)^2 > 0 (log of the dimension excess, nats)", gap_lo > 0)
        floor_milli = (gap_lo * 1000).numerator // (gap_lo * 1000).denominator
        print(f"  R={R}: N={N[R]}, certified lower bound of N ln2 - pi(R+1)^2, rounded down to 0.001: "
              f"{floor_milli // 1000}.{floor_milli % 1000:03d} nats")

    # --- Controls that fail when the statement is perturbed -------------
    lam2 = Q(100)
    R = 50
    check("Control: threshold (1/2) lambda^2 is false; at lambda^2=100, R=50, N ln2 < pi lambda^2 (R+1)^2",
          N[R] * ln2_hi < pi_lo * lam2 * (R + 1) ** 2)
    lam2 = Q(4)
    B = {R: boundary_count(R) for R in range(7, 61)}
    check("Control: with only boundary sites counted, lambda^2=4 never exceeds for R = 7..60",
          all(B[R] * ln2_hi < pi_lo * lam2 * (R + 1) ** 2 for R in B))
    print("Boundary-site counts at R = 10, 20, 40, 60:", [B[R] for R in (10, 20, 40, 60)])

    print(f"TOTAL PASS: {PASS_COUNT}")


if __name__ == "__main__":
    main()
