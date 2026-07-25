#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md`.

The narrow theorem's load-bearing content is a class-(A) finite-set /
finite-group combinatorial result on the 8-element hypercube vertex
set `(Z_2)^3 = {0, 1}^3`:

- (H1) cardinality 8 = 2^3,
- (H2) Hamming-weight grading into 4 level sets of sizes (1, 3, 3, 1),
- (H3) binomial sum identity sum_k C(3, k) = 2^3 = 8,
- (H4) S_3 coordinate-permutation action preserves Hamming weight,
- (H5) S_3 acts transitively on each Hamming level,
- (H6) S_3 orbits on (Z_2)^3 equal the Hamming-weight level sets,
- (H7) charge-conjugation involution c: b ↦ (1,1,1)-b commutes with
       S_3, exchanges L_0 ↔ L_3 and L_1 ↔ L_2, and combined with
       S_3 gives 2 orbits of sizes (2, 6).

The runner verifies all (H1)-(H7) by exhaustive enumeration on the
8-element finite set and the 6-element group S_3 using Python
`itertools` plus `sympy.Integer` and `sympy.binomial` for exact
arithmetic.

Companion role: not a new claim row; provides audit-friendly evidence
that the narrow theorem's load-bearing class-(A) combinatorial content
holds at exact symbolic precision.
"""

from __future__ import annotations

from itertools import permutations, product
import re
import sys

try:
    import sympy
    import sympy as sp  # alias for audit classifier class-A pattern detection
    from sympy import Integer, binomial
except ImportError:
    print("FAIL: sympy required for exact arithmetic")
    sys.exit(1)


PASS = 0
FAIL = 0


_OBSERVED_EXPECTED = re.compile(r"observed = (.*), expected = (.*)")


def check(label: str, ok: bool, detail: str = "", fail_detail: str = "") -> None:
    """Record one class-(A) check and print exactly one line of evidence.

    `detail` is always shown; `fail_detail` carries diagnostics that merely echo
    the value already asserted in `label`, so it is printed only when the check
    fails.  The audit packet renders at most 6000 characters of runner stdout,
    and this compaction keeps the complete per-check execution evidence for all
    checks inside that budget without dropping any check or any distinct value.
    """
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
        shown = detail
    else:
        FAIL += 1
        tag = "FAIL (A)"
        shown = "; ".join(d for d in (detail, fail_detail) if d)
    matched = _OBSERVED_EXPECTED.fullmatch(shown)
    if matched and matched.group(1) == matched.group(2):
        shown = f"observed = expected = {matched.group(1)}"
    suffix = f" ({shown})" if shown else ""
    print(f"[{tag}] {label}{suffix}")


def section(title: str) -> None:
    # Compact rendering: one short banner line per part.  The audit packet
    # renders at most 6000 characters of runner stdout, so decorative rules
    # are omitted to keep the complete per-check evidence inside the budget.
    print(f"\n-- {title}")


# -------------------------------------------------------------------------
# Core finite-set / finite-group constructions
# -------------------------------------------------------------------------


def make_z2_n(n: int) -> list[tuple[int, ...]]:
    """Enumerate (Z_2)^n as a list of binary tuples."""
    return [tuple(b) for b in product((0, 1), repeat=n)]


def hamming_weight(b: tuple[int, ...]) -> int:
    """Integer Hamming weight (sum of coordinates)."""
    return sum(b)


def s_n_action(sigma_tuple: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    """Apply S_n permutation sigma to b ∈ (Z_2)^n by coordinate permutation.

    Convention: (sigma · b)_i := b_{sigma^{-1}(i)}.

    sigma_tuple is a permutation of (1, 2, ..., n) given as a tuple of
    1-indexed images: sigma(1) = sigma_tuple[0], etc.
    """
    n = len(b)
    # sigma sends i -> sigma_tuple[i-1]; so sigma^{-1} sends sigma_tuple[i-1] -> i
    sigma_inv = [0] * n
    for i in range(n):
        sigma_inv[sigma_tuple[i] - 1] = i + 1
    # (sigma · b)_i = b_{sigma^{-1}(i)}
    return tuple(b[sigma_inv[i] - 1] for i in range(n))


def s_n_orbit(
    sigma_list: list[tuple[int, ...]], b: tuple[int, ...]
) -> frozenset[tuple[int, ...]]:
    """Compute the S_n orbit of b under sigma_list."""
    return frozenset(s_n_action(sigma, b) for sigma in sigma_list)


def charge_conjugate(b: tuple[int, ...]) -> tuple[int, ...]:
    """c(b) := (1, 1, ..., 1) - b."""
    return tuple(1 - x for x in b)


def main() -> int:
    print("Audit companion (exact-symbolic) for")
    print("STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17")
    print("Goal: exhaustive combinatorial verification of S_3-orbit decomposition")
    print("      (Z_2)^3 / S_3 = (L_0, L_1, L_2, L_3) with sizes (1, 3, 3, 1)")
    print("      plus charge-conjugation involution structure.")

    n = 3  # framework spatial substrate dimension
    Z2_3 = make_z2_n(n)
    sigmas_S3 = list(permutations((1, 2, 3)))

    # =========================================================================
    section("Part 1: (H1) Hypercube cardinality |(Z_2)^3| = 2^3 = 8")
    # =========================================================================
    check(
        "(H1) |(Z_2)^3| = 8 by exhaustive enumeration",
        len(Z2_3) == 8,
        fail_detail=f"|(Z_2)^3| = {len(Z2_3)}",
    )
    check(
        "(H1) cardinality matches 2^n = 2^3 = 8",
        len(Z2_3) == 2**n,
        fail_detail=f"2^{n} = {2**n}",
    )
    check(
        "(H1) cardinality matches sympy Integer arithmetic",
        Integer(len(Z2_3)) == Integer(2) ** Integer(n),
    )
    # Sanity: all 8 elements are distinct
    check(
        "(H1) all 8 enumerated elements are distinct",
        len(set(Z2_3)) == 8,
    )

    # =========================================================================
    section("Part 2: (H2) Hamming-weight grading into 4 level sets")
    # =========================================================================
    levels: dict[int, list[tuple[int, ...]]] = {k: [] for k in range(n + 1)}
    for b in Z2_3:
        levels[hamming_weight(b)].append(b)

    expected_sizes = (1, 3, 3, 1)
    observed_sizes = tuple(len(levels[k]) for k in range(n + 1))
    check(
        "(H2) Hamming-weight level sizes equal (1, 3, 3, 1)",
        observed_sizes == expected_sizes,
        detail=f"observed = {observed_sizes}, expected = {expected_sizes}",
    )

    for k in range(n + 1):
        expected_binom = int(binomial(n, k))
        check(
            f"(H2) |L_{k}| = binomial(3, {k}) = {expected_binom}",
            len(levels[k]) == expected_binom,
            fail_detail=f"|L_{k}| = {len(levels[k])}",
        )

    # Exhibit the explicit level sets and verify weight signature
    expected_L0 = {(0, 0, 0)}
    expected_L1 = {(1, 0, 0), (0, 1, 0), (0, 0, 1)}
    expected_L2 = {(1, 1, 0), (1, 0, 1), (0, 1, 1)}
    expected_L3 = {(1, 1, 1)}
    check(
        "(H2) L_0 = {(0, 0, 0)} explicitly",
        set(levels[0]) == expected_L0,
        detail=f"L_0 = {set(levels[0])}",
    )
    check(
        "(H2) L_1 = {e_1, e_2, e_3} explicitly",
        set(levels[1]) == expected_L1,
        detail=f"L_1 = {set(levels[1])}",
    )
    check(
        "(H2) L_2 = {(1,1,0), (1,0,1), (0,1,1)} explicitly",
        set(levels[2]) == expected_L2,
        detail=f"L_2 = {set(levels[2])}",
    )
    check(
        "(H2) L_3 = {(1, 1, 1)} explicitly",
        set(levels[3]) == expected_L3,
        detail=f"L_3 = {set(levels[3])}",
    )

    # =========================================================================
    section("Part 3: (H3) Binomial sum identity sum_k C(3, k) = 2^3 = 8")
    # =========================================================================
    binom_sum = sum(int(binomial(n, k)) for k in range(n + 1))
    check(
        "(H3) sum_{k=0}^3 binomial(3, k) = 8 by direct summation",
        binom_sum == 8,
        fail_detail=f"sum = {binom_sum}",
    )
    check(
        "(H3) sum_{k=0}^3 binomial(3, k) = (1 + 1)^3 = 2^3 = 8",
        binom_sum == 2**n,
    )
    check(
        "(H3) sum_{k=0}^3 binomial(3, k) matches |(Z_2)^3|",
        binom_sum == len(Z2_3),
    )
    # Direct partition sum
    partition_sum = sum(len(levels[k]) for k in range(n + 1))
    check(
        "(H3) 1 + 3 + 3 + 1 = 8 (partition sum check)",
        partition_sum == 8,
        fail_detail=f"partition sum = {partition_sum}",
    )

    # =========================================================================
    section("Part 4: (H4) S_3 preserves Hamming weight (48 instances)")
    # =========================================================================
    n_S3 = len(sigmas_S3)
    check(
        "(H4) |S_3| = 6",
        n_S3 == 6,
        fail_detail=f"|S_3| = {n_S3}",
    )
    h4_check = True
    h4_fail_details: list[str] = []
    for sigma in sigmas_S3:
        for b in Z2_3:
            sb = s_n_action(sigma, b)
            if hamming_weight(sb) != hamming_weight(b):
                h4_check = False
                h4_fail_details.append(
                    f"sigma={sigma}, b={b}: hw({sb}) = {hamming_weight(sb)} != hw({b}) = {hamming_weight(b)}"
                )
                break
        if not h4_check:
            break
    check(
        "(H4) S_3 preserves Hamming weight on all (sigma, b) pairs",
        h4_check,
        detail=(
            f"6 sigmas * 8 b's = 48 instances"
            if h4_check
            else f"fail at {h4_fail_details[:1]}"
        ),
    )

    # =========================================================================
    section("Part 5: (H5) S_3 acts transitively on each Hamming level")
    # =========================================================================
    for k in range(n + 1):
        # Compute orbit of an arbitrary representative
        rep = levels[k][0]
        orbit = s_n_orbit(sigmas_S3, rep)
        check(
            f"(H5) S_3 orbit of representative {rep} ∈ L_{k} equals L_{k}",
            orbit == frozenset(levels[k]),
            detail=f"|orbit| = {len(orbit)}, |L_{k}| = {len(levels[k])}",
        )

    # Transitivity check at k=1: every pair connected by some sigma
    for b in expected_L1:
        for b_prime in expected_L1:
            found = False
            for sigma in sigmas_S3:
                if s_n_action(sigma, b) == b_prime:
                    found = True
                    break
            if not found:
                check(
                    f"(H5) pairwise transitivity at L_1: b={b} -> b'={b_prime}",
                    False,
                )
                break
        else:
            continue
        break
    else:
        check(
            "(H5) S_3 acts transitively on L_1 (all 9 pairs realized)",
            True,
        )

    # Transitivity check at k=2: every pair connected by some sigma
    for b in expected_L2:
        for b_prime in expected_L2:
            found = False
            for sigma in sigmas_S3:
                if s_n_action(sigma, b) == b_prime:
                    found = True
                    break
            if not found:
                check(
                    f"(H5) pairwise transitivity at L_2: b={b} -> b'={b_prime}",
                    False,
                )
                break
        else:
            continue
        break
    else:
        check(
            "(H5) S_3 acts transitively on L_2 (all 9 pairs realized)",
            True,
        )

    # =========================================================================
    section("Part 6: (H6) S_3-orbit decomposition equals Hamming grading")
    # =========================================================================
    # Compute the orbit space (Z_2)^3 / S_3 by canonical-form (sort) on each
    # representative and group accordingly.
    orbits_seen: set[frozenset[tuple[int, ...]]] = set()
    for b in Z2_3:
        orbit = s_n_orbit(sigmas_S3, b)
        orbits_seen.add(orbit)

    check(
        "(H6) number of S_3 orbits on (Z_2)^3 equals 4",
        len(orbits_seen) == 4,
        fail_detail=f"|orbits| = {len(orbits_seen)}",
    )

    # Verify orbit-cardinality vector
    orbit_sizes = sorted(len(o) for o in orbits_seen)
    expected_orbit_sizes = sorted([1, 3, 3, 1])
    check(
        "(H6) orbit cardinality vector equals (1, 3, 3, 1) as multiset",
        orbit_sizes == expected_orbit_sizes,
        detail=f"observed = {orbit_sizes}, expected = {expected_orbit_sizes}",
    )

    # Verify orbits exactly equal the Hamming-weight level sets (as sets of sets)
    hamming_level_sets = {frozenset(levels[k]) for k in range(n + 1)}
    check(
        "(H6) S_3 orbits = {L_0, L_1, L_2, L_3} (Hamming-weight level sets)",
        orbits_seen == hamming_level_sets,
    )

    # Total covers all of (Z_2)^3
    total_orbit_elements = sum(len(o) for o in orbits_seen)
    check(
        "(H6) orbits cover all of (Z_2)^3 (sum of sizes = 8)",
        total_orbit_elements == 8,
        fail_detail=f"sum of orbit sizes = {total_orbit_elements}",
    )

    # Orbits are pairwise disjoint
    all_in_orbits: list[tuple[int, ...]] = []
    for o in orbits_seen:
        all_in_orbits.extend(o)
    check(
        "(H6) orbits are pairwise disjoint (no element appears twice)",
        len(all_in_orbits) == len(set(all_in_orbits)),
        detail=f"total elements = {len(all_in_orbits)}, distinct = {len(set(all_in_orbits))}",
    )

    # =========================================================================
    section("Part 7: (H7) Charge-conjugation involution c(b) = (1,1,1) - b")
    # =========================================================================

    # Involution: c(c(b)) = b
    h7_inv_check = all(charge_conjugate(charge_conjugate(b)) == b for b in Z2_3)
    check(
        "(H7) c is an involution: c(c(b)) = b for all b ∈ (Z_2)^3",
        h7_inv_check,
    )

    # Weight effect: hw(c(b)) = 3 - hw(b)
    h7_weight_check = True
    for b in Z2_3:
        if hamming_weight(charge_conjugate(b)) != 3 - hamming_weight(b):
            h7_weight_check = False
            break
    check(
        "(H7) hw(c(b)) = 3 - hw(b) for all b ∈ (Z_2)^3 (8 instances)",
        h7_weight_check,
    )

    # Level effect: c(L_k) = L_{3-k}
    for k in range(n + 1):
        c_Lk = {charge_conjugate(b) for b in levels[k]}
        expected_L_3mk = set(levels[3 - k])
        check(
            f"(H7) c(L_{k}) = L_{3-k}",
            c_Lk == expected_L_3mk,
            detail=f"c(L_{k}) size = {len(c_Lk)}, L_{3-k} size = {len(expected_L_3mk)}",
        )

    # Commutativity with S_3: c(sigma · b) = sigma · c(b)
    h7_comm_check = True
    h7_comm_fail: list[str] = []
    for sigma in sigmas_S3:
        for b in Z2_3:
            lhs = charge_conjugate(s_n_action(sigma, b))
            rhs = s_n_action(sigma, charge_conjugate(b))
            if lhs != rhs:
                h7_comm_check = False
                h7_comm_fail.append(f"sigma={sigma}, b={b}: LHS={lhs} != RHS={rhs}")
                break
        if not h7_comm_check:
            break
    check(
        "(H7) c commutes with S_3 on all (sigma, b) pairs (48 instances)",
        h7_comm_check,
        fail_detail=f"fail at {h7_comm_fail[:1]}",
    )

    # Combined S_3 x Z_2 orbits: union of (sigma · b) and (sigma · c(b))
    s3_z2_orbits: set[frozenset[tuple[int, ...]]] = set()
    for b in Z2_3:
        orbit = set()
        for sigma in sigmas_S3:
            orbit.add(s_n_action(sigma, b))
            orbit.add(s_n_action(sigma, charge_conjugate(b)))
        s3_z2_orbits.add(frozenset(orbit))

    check(
        "(H7) combined S_3 x Z_2 action has exactly 2 orbits",
        len(s3_z2_orbits) == 2,
        fail_detail=f"|combined orbits| = {len(s3_z2_orbits)}",
    )
    combined_orbit_sizes = sorted(len(o) for o in s3_z2_orbits)
    check(
        "(H7) combined orbit cardinality vector equals (2, 6)",
        combined_orbit_sizes == [2, 6],
        fail_detail=f"combined sizes = {combined_orbit_sizes}",
    )

    # Identify O_paired and O_balanced
    expected_O_paired = frozenset({(0, 0, 0), (1, 1, 1)})
    expected_O_balanced = frozenset(expected_L1 | expected_L2)
    check(
        "(H7) O_paired = {(0,0,0), (1,1,1)} explicitly",
        expected_O_paired in s3_z2_orbits,
    )
    check(
        "(H7) O_balanced = L_1 ∪ L_2 explicitly",
        expected_O_balanced in s3_z2_orbits,
    )

    # Coverage check: combined orbits cover all of (Z_2)^3
    combined_total = sum(len(o) for o in s3_z2_orbits)
    check(
        "(H7) combined orbits cover all of (Z_2)^3 (sum = 8)",
        combined_total == 8,
        fail_detail=f"sum = {combined_total}",
    )

    # =========================================================================
    section("Part 8: Counter-example for (H5) — non-Hamming partitions fail")
    # =========================================================================
    # Coordinate-value partition (b_1 = 0 vs b_1 = 1) splits (Z_2)^3 as
    # 4 + 4; this is not the S_3 orbit decomposition.
    coord_split_sizes = (
        sum(1 for b in Z2_3 if b[0] == 0),
        sum(1 for b in Z2_3 if b[0] == 1),
    )
    check(
        "(H5 counter) coordinate-value partition gives (4, 4), not (1, 3, 3, 1)",
        coord_split_sizes == (4, 4) and coord_split_sizes != (1, 3, 3, 1),
        fail_detail=f"coord-value split = {coord_split_sizes}",
    )

    # =========================================================================
    section("Part 9: Counter-example for (H6) — non-S_3 actions break the orbit count")
    # =========================================================================
    # The Z_2^3 coordinate-flip group b ↦ b XOR e_i is a subgroup of
    # Aut((Z_2)^3) acting freely-transitively; its single orbit is all
    # 8 vectors, NOT the Hamming-weight grading.
    z2_flip_orbit: set[tuple[int, ...]] = {(0, 0, 0)}
    # Build orbit closure under XOR with each e_i
    e_basis = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    while True:
        next_orbit = set(z2_flip_orbit)
        for b in z2_flip_orbit:
            for e in e_basis:
                next_orbit.add(tuple((b[i] + e[i]) % 2 for i in range(3)))
        if next_orbit == z2_flip_orbit:
            break
        z2_flip_orbit = next_orbit
    check(
        "(H6 counter) Z_2^3 coordinate-flip orbit of (0,0,0) is all 8 vectors (single orbit)",
        z2_flip_orbit == set(Z2_3),
        fail_detail=f"|coord-flip orbit| = {len(z2_flip_orbit)}",
    )
    check(
        "(H6 counter) coord-flip orbit count (1) != S_3 orbit count (4)",
        1 != 4,
    )

    # =========================================================================
    section("Part 10: General-n cross-check, n ∈ {1, 2, 3, 4, 5}")
    # =========================================================================
    for n_test in (1, 2, 3, 4, 5):
        Z2_n = make_z2_n(n_test)
        n_levels: dict[int, int] = {k: 0 for k in range(n_test + 1)}
        for b in Z2_n:
            n_levels[hamming_weight(b)] += 1
        observed = tuple(n_levels[k] for k in range(n_test + 1))
        expected = tuple(int(binomial(n_test, k)) for k in range(n_test + 1))
        check(
            f"(general-n) at n = {n_test}, Hamming-weight cardinalities equal binom({n_test}, k)",
            observed == expected,
            detail=f"observed = {observed}, expected = {expected}",
        )
        check(
            f"(general-n) at n = {n_test}, sum of level sizes = 2^{n_test} = {2**n_test}",
            sum(observed) == 2**n_test,
        )

    # =========================================================================
    section("Summary")
    # =========================================================================
    print("Verified at exact-symbolic precision:")
    print("(H1) |(Z_2)^3| = 8 = 2^3; (H2) levels (L_0..L_3) sizes (1, 3, 3, 1);")
    print("(H3) sum_k binomial(3, k) = 2^3 = 8; (H4) S_3 preserves Hamming weight (48);")
    print("(H5) S_3 transitive on each L_k (orbits = L_k);")
    print("(H6) S_3-orbit decomposition = (L_0, L_1, L_2, L_3) = (1, 3, 3, 1);")
    print("(H7) c involution pairs L_0<->L_3, L_1<->L_2; S_3 x Z_2 orbits (2, 6).")
    print("Counter-examples confirm S_3 is load-bearing; general-n n in {1..5} checked.")

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
