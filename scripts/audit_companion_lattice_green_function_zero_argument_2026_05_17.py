#!/usr/bin/env python3
"""Audit-companion runner for the narrow source note
`LATTICE_GREEN_FUNCTION_ZERO_ARGUMENT_NARROW_THEOREM_NOTE_2026-05-17.md`.

The parent narrow note's load-bearing content is the closed-arithmetic
readout of the cubic-lattice scalar Laplacian Green function at zero
separation on `Z^3` with periodic boundary conditions, at four sample
sizes `L in {8, 16, 32, 64}`:

    G_lat(0; L) := (1 / L^3) * sum_{n != 0} 1 / [hat{k}(n_x)^2 + hat{k}(n_y)^2 + hat{k}(n_z)^2]
    hat{k}(m)   := 2 sin(pi m / L)

This runner verifies:

  (T1) Four sample readouts at 1e-9 absolute precision.
  (T2) Strict monotone-in-L ordering across the four sample sizes.
  (T3) L=64 readout sits below the literature BKM constant 0.2527 with
       gap < 0.005.
  (T4) Cubic-symmetry invariance under coordinate permutations at L=8.
  (C1) Positivity at every sample size; positivity of every summand at L=8.
  Zero-mode bookkeeping: L=8 sum has exactly L^3 - 1 = 511 terms.
  Counterfactual probe: replacing the lattice-momentum kernel
       hat{k}(m) = 2 sin(pi m / L) by the naive momentum k(m) = 2 pi m / L
       gives a strictly different numerical value at L = 8 (confirms
       lattice-momentum kernel is load-bearing for the readout).

Companion role: not a new claim row, not a status promotion. Provides
audit-friendly numerical evidence that the parent narrow note's closed
arithmetic readout reproduces at machine precision, that cubic symmetry
holds for the kernel choice, and that the kernel choice itself is
load-bearing. The four readouts and the BKM literature value `0.2527`
are quoted (not derived) from the parent broad note
`MONOPOLE_DERIVED_NOTE.md`; the narrow theorem isolates only the closed
arithmetic readout.
"""

from __future__ import annotations

import math
import sys


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
    else:
        FAIL += 1
        tag = "FAIL (A)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def g_lat_zero(L: int) -> float:
    """Periodic-cubic-lattice scalar Laplacian Green function at zero
    separation on Z^3 with side length L. Uses the standard lattice
    momentum kernel hat{k}(m) = 2 sin(pi m / L). Returns the dimensionless
    finite trigonometric-rational sum divided by L^3.
    """
    total = 0.0
    for nx in range(L):
        kx = 2.0 * math.sin(math.pi * nx / L)
        for ny in range(L):
            ky = 2.0 * math.sin(math.pi * ny / L)
            for nz in range(L):
                if nx == 0 and ny == 0 and nz == 0:
                    continue
                kz = 2.0 * math.sin(math.pi * nz / L)
                k2 = kx * kx + ky * ky + kz * kz
                total += 1.0 / k2
    return total / (L * L * L)


def g_lat_zero_naive_momentum(L: int) -> float:
    """Counterfactual: same sum but with the *naive* continuum momentum
    k(m) = 2 pi m / L instead of the lattice momentum hat{k}(m) =
    2 sin(pi m / L). This is the naive-continuum-limit kernel and gives
    a different numerical value at finite L.
    """
    total = 0.0
    for nx in range(L):
        kx = 2.0 * math.pi * nx / L
        for ny in range(L):
            ky = 2.0 * math.pi * ny / L
            for nz in range(L):
                if nx == 0 and ny == 0 and nz == 0:
                    continue
                kz = 2.0 * math.pi * nz / L
                k2 = kx * kx + ky * ky + kz * kz
                total += 1.0 / k2
    return total / (L * L * L)


def g_lat_zero_permuted(L: int, perm: tuple[int, int, int]) -> float:
    """Same sum but with coordinate indices permuted by `perm` before
    forming the lattice-momentum kernel. Should equal g_lat_zero(L) by
    cubic symmetry of the index set.
    """
    a, b, c = perm
    total = 0.0
    for n in [None]:  # dummy
        break
    # Use the same iteration order; the kernel evaluates lattice momentum
    # on the permuted indices.
    for nx in range(L):
        for ny in range(L):
            for nz in range(L):
                if nx == 0 and ny == 0 and nz == 0:
                    continue
                idx = (nx, ny, nz)
                m_x = idx[a]
                m_y = idx[b]
                m_z = idx[c]
                kx = 2.0 * math.sin(math.pi * m_x / L)
                ky = 2.0 * math.sin(math.pi * m_y / L)
                kz = 2.0 * math.sin(math.pi * m_z / L)
                k2 = kx * kx + ky * ky + kz * kz
                total += 1.0 / k2
    return total / (L * L * L)


def main() -> int:
    print("=" * 88)
    print("Audit companion (closed arithmetic) for")
    print("LATTICE_GREEN_FUNCTION_ZERO_ARGUMENT_NARROW_THEOREM_NOTE_2026-05-17")
    print("Goal: verify closed-arithmetic readouts G_lat(0; L) for L in")
    print("{8, 16, 32, 64}, monotone-in-L ordering, cubic-symmetry invariance,")
    print("positivity, and load-bearing role of the lattice-momentum kernel.")
    print("=" * 88)

    # ---------------------------------------------------------------------
    section("Part 0: kernel setup")
    # ---------------------------------------------------------------------
    # The standard lattice scalar Laplacian Green function at zero separation
    # on Z^3 with periodic boundary L^3 is
    #   G_lat(0; L) = (1/L^3) sum_{n != 0} 1 / [hat{k}(n_x)^2 + hat{k}(n_y)^2 + hat{k}(n_z)^2]
    # with hat{k}(m) = 2 sin(pi m / L). Independent of any compact gauge
    # action choice (Wilson, Villain, improved) — that kernel is the
    # inverse of the standard cubic-lattice Laplacian, which is shared by
    # all those actions in the Gaussian / weak-coupling sector.
    print("  kernel:   hat{k}(m) = 2 sin(pi m / L) on Z/(L Z)")
    print("  sum:      G_lat(0; L) = (1/L^3) sum_{n != 0} 1 / hat{k}^2")

    # ---------------------------------------------------------------------
    section("Part 1: closed-arithmetic readouts (T1)")
    # ---------------------------------------------------------------------
    expected = {
        8: 0.224605625390,
        16: 0.238630318605,
        32: 0.245676551187,
        64: 0.249203283894,
    }
    actual: dict[int, float] = {}
    tol = 1.0e-9
    for L in [8, 16, 32, 64]:
        v = g_lat_zero(L)
        actual[L] = v
        diff = abs(v - expected[L])
        check(
            f"(T1) G_lat(0; L={L:2d}) = {expected[L]:.9f} to 1e-9",
            diff < tol,
            detail=f"got {v:.12f}, |diff| = {diff:.3e}",
        )

    # ---------------------------------------------------------------------
    section("Part 2: strict monotone-in-L ordering (T2)")
    # ---------------------------------------------------------------------
    pairs = [(8, 16), (16, 32), (32, 64)]
    for L1, L2 in pairs:
        check(
            f"(T2) G_lat(0; {L1}) < G_lat(0; {L2})",
            actual[L1] < actual[L2],
            detail=f"{actual[L1]:.9f} < {actual[L2]:.9f}",
        )

    # ---------------------------------------------------------------------
    section("Part 3: infinite-volume diagnostic gap (T3)")
    # ---------------------------------------------------------------------
    bkm_literature = 0.2527
    gap = bkm_literature - actual[64]
    check(
        "(T3a) G_lat(0; 64) < 0.2527 (literature BKM, quoted from parent note)",
        actual[64] < bkm_literature,
        detail=f"{actual[64]:.9f} < {bkm_literature}",
    )
    check(
        "(T3b) gap 0.2527 - G_lat(0; 64) < 0.005",
        gap < 5.0e-3,
        detail=f"gap = {gap:.6f}",
    )
    # Positivity of the gap (sanity)
    check(
        "(T3c) gap is strictly positive (finite-L below BKM extrapolation)",
        gap > 0.0,
        detail=f"gap = {gap:.6f}",
    )

    # ---------------------------------------------------------------------
    section("Part 4: cubic-symmetry invariance (T4) at L=8")
    # ---------------------------------------------------------------------
    L_sym = 8
    base = g_lat_zero(L_sym)
    # Generators of S_3 acting on coordinate labels.
    # perm = (a, b, c) means the new (m_x, m_y, m_z) is read out as
    # (idx[a], idx[b], idx[c]) where idx = (nx, ny, nz). The identity is
    # (0, 1, 2). The three transpositions are (1, 0, 2), (2, 1, 0),
    # (0, 2, 1).
    identity = g_lat_zero_permuted(L_sym, (0, 1, 2))
    check(
        "(T4) identity permutation reproduces base (sanity)",
        abs(identity - base) < 1.0e-12,
        detail=f"|identity - base| = {abs(identity - base):.3e}",
    )
    for label, perm in [
        ("(x <-> y)", (1, 0, 2)),
        ("(x <-> z)", (2, 1, 0)),
        ("(y <-> z)", (0, 2, 1)),
    ]:
        permuted = g_lat_zero_permuted(L_sym, perm)
        check(
            f"(T4) cubic symmetry under {label} at L=8: invariant",
            abs(permuted - base) < 1.0e-12,
            detail=f"|permuted - base| = {abs(permuted - base):.3e}",
        )

    # ---------------------------------------------------------------------
    section("Part 5: positivity (C1) and summand positivity")
    # ---------------------------------------------------------------------
    for L in [8, 16, 32, 64]:
        check(
            f"(C1) G_lat(0; L={L:2d}) > 0",
            actual[L] > 0.0,
            detail=f"value = {actual[L]:.9f}",
        )

    # Every summand at L=8 has positive denominator. Verify there is no
    # zero-denominator term in the (n != 0) sum.
    L = 8
    n_terms = 0
    min_k2 = float("inf")
    for nx in range(L):
        for ny in range(L):
            for nz in range(L):
                if nx == 0 and ny == 0 and nz == 0:
                    continue
                kx = 2.0 * math.sin(math.pi * nx / L)
                ky = 2.0 * math.sin(math.pi * ny / L)
                kz = 2.0 * math.sin(math.pi * nz / L)
                k2 = kx * kx + ky * ky + kz * kz
                n_terms += 1
                if k2 < min_k2:
                    min_k2 = k2
    check(
        "L=8 summand positivity: every k^2 > 0 (no zero-denominator term)",
        min_k2 > 0.0,
        detail=f"min k^2 = {min_k2:.6f}",
    )
    check(
        "L=8 zero-mode exclusion: sum has exactly L^3 - 1 = 511 terms",
        n_terms == L * L * L - 1,
        detail=f"n_terms = {n_terms}, expected = {L*L*L - 1}",
    )

    # ---------------------------------------------------------------------
    section("Part 6: counterfactual probe (lattice-momentum kernel is load-bearing)")
    # ---------------------------------------------------------------------
    # Replace hat{k}(m) = 2 sin(pi m / L) by the naive continuum
    # momentum k(m) = 2 pi m / L. At finite L the two kernels give
    # strictly different numerical values. The narrow theorem's
    # closed-arithmetic readout is anchored on the lattice-momentum
    # kernel; the naive-momentum counterfactual demonstrates the kernel
    # choice in (D2) is load-bearing for the value.
    L_cf = 8
    lattice_value = g_lat_zero(L_cf)
    naive_value = g_lat_zero_naive_momentum(L_cf)
    check(
        "counterfactual: naive-momentum kernel gives a different value at L=8",
        abs(naive_value - lattice_value) > 1.0e-3,
        detail=f"lattice = {lattice_value:.6f}, naive = {naive_value:.6f}, "
        f"|diff| = {abs(naive_value - lattice_value):.6f}",
    )
    # The naive-momentum kernel underestimates G_lat(0) at finite L
    # because the naive momenta range over [0, 2 pi) while the lattice
    # momenta range over [0, 2] (peaked at the boundary). Just sanity:
    # naive value should be strictly smaller than the lattice value.
    check(
        "counterfactual: naive-momentum value < lattice-momentum value at L=8",
        naive_value < lattice_value,
        detail=f"{naive_value:.6f} < {lattice_value:.6f}",
    )

    # ---------------------------------------------------------------------
    section("Part 7: derivable corollary (C2) bounded by parent-cited BKM")
    # ---------------------------------------------------------------------
    # All four sample readouts sit below the parent-cited literature BKM
    # value 0.2527 (a finite-`L` boundedness check; the narrow theorem
    # does not derive the infinite-volume limit).
    for L in [8, 16, 32, 64]:
        check(
            f"(C2) G_lat(0; L={L:2d}) < 0.2527 (parent-cited BKM literature)",
            actual[L] < bkm_literature,
            detail=f"{actual[L]:.9f} < {bkm_literature}",
        )

    # ---------------------------------------------------------------------
    section("Summary")
    # ---------------------------------------------------------------------
    print("  Verified at 1e-9 precision (or exact float comparison):")
    print("    (T1) four closed-arithmetic readouts G_lat(0; L) at L in")
    print("         {8, 16, 32, 64}")
    print("    (T2) strict monotone-in-L ordering across the four sample sizes")
    print("    (T3) L=64 readout sits below 0.2527 with gap < 0.005")
    print("    (T4) cubic-symmetry invariance under (x<->y), (x<->z), (y<->z)")
    print("    (C1) positivity at every sample size; summand positivity at L=8")
    print("    L=8 sum has exactly L^3 - 1 = 511 terms (zero-mode excluded)")
    print("    counterfactual: naive-momentum kernel gives a different value")
    print("    (C2) all four sample readouts below parent-cited BKM 0.2527")

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
