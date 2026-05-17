"""
Runner: Klein-four APBC orbit partition closed-form narrow theorem.

Source note:
  docs/OBSERVABLE_PRINCIPLE_KLEIN_FOUR_APBC_ORBIT_PARTITION_CLOSED_FORM_NARROW_THEOREM_NOTE_2026-05-17.md

Closed-form claim (Theorem 2 of the source note):
  For every even L_t = 2m with m >= 1, the Klein-four group
    K_4 = {1, sigma_-, sigma_*, sigma_{-*}}
  acting on the APBC phase set
    Phi(L_t) = { z_n = exp(i (2n+1) pi / L_t) : n = 0, ..., L_t - 1 }
  partitions Phi(L_t) into exactly ceil(L_t / 4) orbits.

  The orbit invariant is sin^2(arg z); orbits are level sets of
    s_n := sin^2((2n+1) pi / (2m))
  on n in {0, ..., 2m - 1}.

Corollaries:
  (2.1.1) Single-orbit iff L_t in {2, 4}.
  (2.1.2) Orbit sizes: at L_t = 2, size 2 (the {+i, -i} pair); at L_t = 4,
          size 4 with sin^2 = 1/2 uniformly.
  (2.1.3) L_t = 4 is the unique minimal RESOLVED orbit (single orbit, size > 2).

This runner verifies the theorem and corollaries at EXACT precision using
SymPy symbolic and Python Fraction arithmetic. No floating-point comparison.

Layout of checks (matches the source note's §7 table):
  T1  : Klein-four group composition table.
  T2  : Lemma 1.4 sin^2 is a complete Klein-four invariant on S^1.
  T3  : K_4 preserves Phi(L_t) for every even L_t in {2, ..., 64}.
  T4  : Closed-form orbit count ceil(L_t/4) matches direct enumeration for
        every even L_t in {2, ..., 64}.
  T5  : Trigonometric collapse identities sin^2(theta + pi) = sin^2(theta),
        sin^2(pi - theta) = sin^2(theta).
  T6  : No-further-collapse argument via cos(2 alpha) = cos(2 beta).
  T7  : Corollary 2.1.1 single-orbit characterization across L_t in {2, ..., 200}.
  T8  : Corollary 2.1.2 orbit sizes at L_t in {2, 4} exact (SymPy).
  T9  : Corollary 2.1.3 unique resolved orbit characterization.
  T10 : Observation 4.1 Phi_8(x) = x^4 + 1 cyclotomic identification.
  T11 : Source-note boundary check (claim type, status authority, no overclaim).
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


# --------------------------------------------------------------------------- #
# Setup: APBC phase set, Klein-four action, orbit invariant.
# --------------------------------------------------------------------------- #


def apbc_arguments_rational(lt: int):
    """Return the APBC arguments as exact SymPy Rational multiples of pi.

    Phi(L_t) = { exp(i (2n+1) pi / L_t) : n = 0, ..., L_t - 1 }.
    We return the rational ratios (2n+1) / L_t for n in {0, ..., L_t - 1}.
    """
    return [sp.Rational(2 * n + 1, lt) for n in range(lt)]


def sin_sq_of(ratio):
    """sin^2(ratio * pi) as an exact SymPy expression."""
    return sp.sin(ratio * sp.pi) ** 2


def klein_four_action_on_ratio(ratio):
    """
    Klein-four action on z = exp(i ratio pi), in terms of the rational
    argument ratio = arg(z) / pi:
      identity:  ratio
      sigma_-:   ratio + 1            (z -> -z)
      sigma_*:   -ratio                (z -> z*)
      sigma_-*:  -ratio + 1 = 1 - ratio (z -> -z*)
    We reduce mod 2 to keep ratio in [0, 2).
    """
    g = []
    g.append(ratio % 2)
    g.append((ratio + 1) % 2)
    g.append((-ratio) % 2)
    g.append((1 - ratio) % 2)
    return g


def klein_four_orbit_of_ratio(ratio, phase_set):
    """Compute the K_4 orbit of `ratio` within `phase_set` (set of ratios)."""
    images = klein_four_action_on_ratio(ratio)
    return frozenset(r for r in images if r in phase_set)


def enumerate_orbits_direct(lt: int):
    """Enumerate K_4 orbits on Phi(L_t) by direct computation.

    Returns a sorted list of frozensets (each orbit), unique.
    """
    ratios = apbc_arguments_rational(lt)
    phase_set = set(ratios)
    seen = set()
    orbits = []
    for r in ratios:
        if r in seen:
            continue
        orb = klein_four_orbit_of_ratio(r, phase_set)
        orbits.append(orb)
        seen.update(orb)
    return orbits


def sin_sq_levels_distinct_count(lt: int) -> int:
    """Number of distinct exact sin^2((2n+1)pi/L_t) values for n=0..L_t-1."""
    ratios = apbc_arguments_rational(lt)
    levels = set()
    for r in ratios:
        val = sp.simplify(sin_sq_of(r))
        # Force a canonical form via radical simplification.
        levels.add(sp.nsimplify(val, rational=False))
    return len(levels)


def closed_form_orbit_count(lt: int) -> int:
    """ceil(L_t / 4) for even L_t."""
    assert lt % 2 == 0 and lt >= 2
    # ceil(L_t / 4):
    return (lt + 3) // 4


# --------------------------------------------------------------------------- #
# Check helper.
# --------------------------------------------------------------------------- #


_PASS = 0
_FAIL = 0


def check(name: str, cond: bool, detail: str = ""):
    global _PASS, _FAIL
    status = "PASS" if cond else "FAIL"
    if cond:
        _PASS += 1
    else:
        _FAIL += 1
    print(f"  [{status}] {name}" + (f"  ({detail})" if detail else ""))


# --------------------------------------------------------------------------- #
# T1: Klein-four group composition table.
# --------------------------------------------------------------------------- #


def test_t1_klein_four_group_axioms():
    print("\n" + "=" * 78)
    print("T1: Klein-four group composition table on K_4 = {1, sigma_-, sigma_*, sigma_-*}")
    print("=" * 78)

    # Represent each generator as a function on the unit circle parameter
    # ratio (= arg / pi), reduced mod 2.
    def ident(r):
        return r % 2

    def s_neg(r):
        return (r + 1) % 2

    def s_conj(r):
        return (-r) % 2

    def s_negconj(r):
        return (1 - r) % 2

    gens = {"1": ident, "s-": s_neg, "s*": s_conj, "s-*": s_negconj}

    # Composition table: gens[a](gens[b](r)) should equal gens[c](r) where c
    # is the Klein-four product a*b.
    expected = {
        ("1", "1"): "1",
        ("1", "s-"): "s-",
        ("1", "s*"): "s*",
        ("1", "s-*"): "s-*",
        ("s-", "1"): "s-",
        ("s-", "s-"): "1",
        ("s-", "s*"): "s-*",
        ("s-", "s-*"): "s*",
        ("s*", "1"): "s*",
        ("s*", "s-"): "s-*",
        ("s*", "s*"): "1",
        ("s*", "s-*"): "s-",
        ("s-*", "1"): "s-*",
        ("s-*", "s-"): "s*",
        ("s-*", "s*"): "s-",
        ("s-*", "s-*"): "1",
    }

    test_ratios = [sp.Rational(1, 7), sp.Rational(3, 11), sp.Rational(2, 5)]

    bad = 0
    for (a, b), c in expected.items():
        for r in test_ratios:
            lhs = gens[a](gens[b](r))
            rhs = gens[c](r)
            if sp.simplify(lhs - rhs) != 0:
                bad += 1
                print(f"    MISMATCH: {a} o {b} != {c} at r={r}: lhs={lhs}, rhs={rhs}")

    check(
        "all 16 Klein-four composition entries match on three test ratios",
        bad == 0,
        f"mismatches = {bad}",
    )


# --------------------------------------------------------------------------- #
# T2: Lemma 1.4: sin^2(arg z) is a complete K_4 invariant on S^1.
# --------------------------------------------------------------------------- #


def test_t2_invariance_lemma_symbolic():
    print("\n" + "=" * 78)
    print("T2: Lemma 1.4 — sin^2(arg z) is a complete Klein-four invariant on S^1")
    print("=" * 78)

    omega = sp.symbols("omega", real=True)
    f = sp.sin(omega) ** 2

    # Action on omega: omega -> omega, omega + pi, -omega, pi - omega.
    images = [omega, omega + sp.pi, -omega, sp.pi - omega]

    bad = 0
    for img in images:
        diff = sp.simplify(sp.sin(img) ** 2 - f)
        if diff != 0:
            bad += 1
            print(f"    NON-INVARIANT under omega -> {img}: diff = {diff}")

    check(
        "sin^2(arg z) is invariant under all four Klein-four images of omega (symbolic)",
        bad == 0,
        f"non-invariant cases = {bad}",
    )

    # Completeness: sin^2(omega) = sin^2(omega') ⇔ omega' in K_4-orbit of omega.
    # Verify on a non-degenerate sample omega = pi/7.
    omega0 = sp.Rational(1, 7) * sp.pi
    val0 = sp.simplify(sp.sin(omega0) ** 2)
    orbit_vals = [sp.simplify(sp.sin(img.subs(omega, omega0)) ** 2) for img in images]
    all_eq = all(sp.simplify(v - val0) == 0 for v in orbit_vals)
    check(
        "K_4 orbit values of sin^2 are all equal at the non-degenerate test point omega = pi/7",
        all_eq,
        "exact SymPy",
    )

    # Off-orbit point omega' = 2 pi/7 should give DIFFERENT sin^2.
    omega_off = sp.Rational(2, 7) * sp.pi
    val_off = sp.simplify(sp.sin(omega_off) ** 2)
    diff = sp.simplify(val0 - val_off)
    check(
        "off-orbit point omega = 2 pi/7 has DIFFERENT sin^2 from in-orbit pi/7",
        sp.simplify(diff) != 0,
        f"diff = {sp.nsimplify(diff)}",
    )


# --------------------------------------------------------------------------- #
# T3: K_4 preserves Phi(L_t) for every even L_t in scan range.
# --------------------------------------------------------------------------- #


def test_t3_klein_four_preserves_phi(scan_max=64):
    print("\n" + "=" * 78)
    print(f"T3: K_4 preserves Phi(L_t) for even L_t in [2, {scan_max}]")
    print("=" * 78)

    bad = []
    for lt in range(2, scan_max + 1, 2):
        ratios = apbc_arguments_rational(lt)
        phase_set = set(ratios)
        ok = True
        for r in ratios:
            images = set(klein_four_action_on_ratio(r))
            if not images.issubset(phase_set):
                ok = False
                break
        if not ok:
            bad.append(lt)

    check(
        f"K_4 preserves Phi(L_t) for all 32 even L_t in [2, {scan_max}]",
        not bad,
        f"failing L_t = {bad}" if bad else "all pass",
    )


# --------------------------------------------------------------------------- #
# T4: Closed-form orbit count ceil(L_t/4) matches direct enumeration.
# --------------------------------------------------------------------------- #


def test_t4_closed_form_orbit_count(scan_max=64):
    print("\n" + "=" * 78)
    print(f"T4: Closed-form orbit count ceil(L_t/4) vs direct enumeration, "
          f"even L_t in [2, {scan_max}]")
    print("=" * 78)

    mismatches = []
    for lt in range(2, scan_max + 1, 2):
        orbits = enumerate_orbits_direct(lt)
        predicted = closed_form_orbit_count(lt)
        if len(orbits) != predicted:
            mismatches.append((lt, len(orbits), predicted))
        if lt <= 16:
            print(f"  L_t={lt:2d}: orbits={len(orbits):2d}, predicted ceil(L_t/4)={predicted:2d}, "
                  f"orbit sizes={sorted(len(o) for o in orbits)}")

    check(
        f"closed-form ceil(L_t/4) matches direct enumeration for all 32 even L_t in [2, {scan_max}]",
        not mismatches,
        f"mismatches = {mismatches}" if mismatches else "all match",
    )


# --------------------------------------------------------------------------- #
# T5: Symbolic verification of the two collapse identities.
# --------------------------------------------------------------------------- #


def test_t5_collapse_identities_symbolic():
    print("\n" + "=" * 78)
    print("T5: Trigonometric collapse identities (symbolic SymPy)")
    print("=" * 78)

    theta = sp.symbols("theta", real=True)
    id1 = sp.simplify(sp.sin(theta + sp.pi) ** 2 - sp.sin(theta) ** 2)
    id2 = sp.simplify(sp.sin(sp.pi - theta) ** 2 - sp.sin(theta) ** 2)

    check(
        "sin^2(theta + pi) - sin^2(theta) simplifies to 0 (period-pi collapse)",
        id1 == 0,
        f"residual = {id1}",
    )
    check(
        "sin^2(pi - theta) - sin^2(theta) simplifies to 0 (reflection collapse)",
        id2 == 0,
        f"residual = {id2}",
    )


# --------------------------------------------------------------------------- #
# T6: No-further-collapse argument via cos(2 alpha) = cos(2 beta).
# --------------------------------------------------------------------------- #


def test_t6_no_further_collapse():
    print("\n" + "=" * 78)
    print("T6: §3.3 no-further-collapse: sin^2 equality forces n = n' or n' = m-1-n")
    print("=" * 78)

    # We check at SymPy precision on representative odd and even m values.
    bad = []
    for m in (3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
        levels = {}
        for n in range(m):
            ratio = sp.Rational(2 * n + 1, 2 * m)
            val = sp.simplify(sp.sin(ratio * sp.pi) ** 2)
            key = sp.nsimplify(val, rational=False)
            levels.setdefault(key, []).append(n)
        # Each level value should correspond to either {n} (fixed by iota) or
        # {n, m-1-n} for some n in {0, ..., m-1}.
        for k, ns in levels.items():
            ns_sorted = sorted(ns)
            if len(ns_sorted) == 1:
                n0 = ns_sorted[0]
                # Fixed point: must satisfy n0 = m - 1 - n0, i.e., m odd, n0 = (m-1)/2.
                if not (m % 2 == 1 and n0 == (m - 1) // 2):
                    bad.append((m, k, ns_sorted, "fixed-point claim failed"))
            elif len(ns_sorted) == 2:
                n0, n1 = ns_sorted
                if n0 + n1 != m - 1:
                    bad.append((m, k, ns_sorted, "iota-pair claim failed"))
            else:
                bad.append((m, k, ns_sorted, "more than 2 in a level — extra collapse!"))

    check(
        "every sin^2 level collapse is either trivial (fixed) or iota-paired; no extra",
        not bad,
        f"violations = {bad}" if bad else "all clean",
    )


# --------------------------------------------------------------------------- #
# T7: Corollary 2.1.1 single-orbit characterization.
# --------------------------------------------------------------------------- #


def test_t7_single_orbit_characterization(scan_max=200):
    print("\n" + "=" * 78)
    print(f"T7: Corollary 2.1.1 — single-orbit L_t ∈ {{2, 4}} across even L_t in [2, {scan_max}]")
    print("=" * 78)

    single_orbit_lts = []
    for lt in range(2, scan_max + 1, 2):
        orbits = enumerate_orbits_direct(lt)
        if len(orbits) == 1:
            single_orbit_lts.append(lt)

    check(
        f"the only even L_t in [2, {scan_max}] with a single K_4 orbit are L_t = 2 and L_t = 4",
        single_orbit_lts == [2, 4],
        f"found single-orbit L_t = {single_orbit_lts}",
    )


# --------------------------------------------------------------------------- #
# T8: Corollary 2.1.2 orbit sizes at L_t in {2, 4} exact.
# --------------------------------------------------------------------------- #


def test_t8_orbit_sizes_at_2_and_4():
    print("\n" + "=" * 78)
    print("T8: Corollary 2.1.2 — orbit sizes at L_t ∈ {2, 4}")
    print("=" * 78)

    # L_t = 2: orbit size 2, sin^2(pi/2) = 1 uniform.
    o2 = enumerate_orbits_direct(2)
    assert len(o2) == 1
    sizes2 = [len(o) for o in o2]
    sin_sq_2 = {sp.simplify(sp.sin(r * sp.pi) ** 2) for r in list(o2[0])}
    check(
        "L_t = 2 has a single orbit of size 2",
        sizes2 == [2],
        f"sizes = {sizes2}",
    )
    check(
        "L_t = 2 orbit has uniform sin^2 = 1 (exact SymPy)",
        sin_sq_2 == {sp.Integer(1)},
        f"sin^2 values = {sin_sq_2}",
    )

    # L_t = 4: orbit size 4, sin^2(pi/4) = 1/2 uniform.
    o4 = enumerate_orbits_direct(4)
    assert len(o4) == 1
    sizes4 = [len(o) for o in o4]
    sin_sq_4 = {sp.simplify(sp.sin(r * sp.pi) ** 2) for r in list(o4[0])}
    check(
        "L_t = 4 has a single orbit of size 4",
        sizes4 == [4],
        f"sizes = {sizes4}",
    )
    check(
        "L_t = 4 orbit has uniform sin^2 = 1/2 (exact SymPy)",
        sin_sq_4 == {sp.Rational(1, 2)},
        f"sin^2 values = {sin_sq_4}",
    )


# --------------------------------------------------------------------------- #
# T9: Corollary 2.1.3 unique resolved orbit characterization.
# --------------------------------------------------------------------------- #


def test_t9_unique_resolved_orbit(scan_max=200):
    print("\n" + "=" * 78)
    print(f"T9: Corollary 2.1.3 — L_t = 4 is unique with single orbit of size > 2 in [2, {scan_max}]")
    print("=" * 78)

    resolved = []
    for lt in range(2, scan_max + 1, 2):
        orbits = enumerate_orbits_direct(lt)
        if len(orbits) == 1 and len(orbits[0]) > 2:
            resolved.append(lt)

    check(
        f"L_t = 4 is the unique even L_t in [2, {scan_max}] with a single resolved orbit (size > 2)",
        resolved == [4],
        f"resolved single-orbit L_t = {resolved}",
    )


# --------------------------------------------------------------------------- #
# T10: Cyclotomic identification Phi_8(x) = x^4 + 1 at L_t = 4.
# --------------------------------------------------------------------------- #


def test_t10_cyclotomic_identification_at_4():
    print("\n" + "=" * 78)
    print("T10: Observation 4.1 — Phi_8(x) = x^4 + 1, sin^2(arg root) = 1/2 uniform")
    print("=" * 78)

    x = sp.symbols("x")
    poly = x ** 4 + 1
    roots = sp.solve(poly, x)
    # Confirm we got 4 roots.
    check(
        "x^4 + 1 has exactly 4 complex roots",
        len(roots) == 4,
        f"|roots| = {len(roots)}",
    )

    # All four roots on unit circle.
    abs_ok = all(sp.simplify(sp.Abs(r) - 1) == 0 for r in roots)
    check(
        "all four roots of x^4 + 1 lie on the unit circle",
        abs_ok,
        "|root| = 1 exact",
    )

    # All four arguments give sin^2(arg) = 1/2.
    sin_sq_vals = set()
    for r in roots:
        # arg(r) for complex unit-modulus r.
        omega = sp.atan2(sp.im(r), sp.re(r))
        v = sp.simplify(sp.sin(omega) ** 2)
        sin_sq_vals.add(sp.simplify(v))

    check(
        "all four roots of Phi_8 satisfy sin^2(arg) = 1/2 (exact SymPy)",
        sin_sq_vals == {sp.Rational(1, 2)},
        f"sin^2 values = {sin_sq_vals}",
    )

    # Cross-check: roots of x^4 + 1 are exactly Phi(4) = {e^{i (2n+1) pi / 4}}.
    # Compare by Cartesian form (re, im) after canonicalisation with sp.cancel
    # + sp.expand_complex; SymPy roots from solve come back in
    # ((-1)**(1/4)) form, which simplifies cleanly via rewrite as cos + i sin.
    def canonical_complex(z):
        z = sp.expand_complex(z)
        re = sp.simplify(sp.re(z))
        im = sp.simplify(sp.im(z))
        return (re, im)

    expected_set = {
        canonical_complex(sp.cos(sp.Rational(2 * n + 1, 4) * sp.pi)
                          + sp.I * sp.sin(sp.Rational(2 * n + 1, 4) * sp.pi))
        for n in range(4)
    }
    actual_set = {canonical_complex(r) for r in roots}
    check(
        "roots of x^4 + 1 coincide with Phi(4) APBC phase set (canonical (re, im) form)",
        actual_set == expected_set,
        f"matched {len(actual_set & expected_set)} of 4",
    )


# --------------------------------------------------------------------------- #
# T11: Source-note boundary check.
# --------------------------------------------------------------------------- #


def test_t11_source_note_boundary():
    print("\n" + "=" * 78)
    print("T11: Source-note boundary check (claim type, status authority, no overclaim)")
    print("=" * 78)

    here = Path(__file__).resolve().parent.parent
    note_path = here / "docs" / (
        "OBSERVABLE_PRINCIPLE_KLEIN_FOUR_APBC_ORBIT_PARTITION_CLOSED_FORM_NARROW_THEOREM_NOTE_2026-05-17.md"
    )
    text = note_path.read_text()

    required_strings = [
        "**Claim type:** bounded_theorem",
        "**Status authority:** independent audit lane only",
        "source-note proposal",
        "does not promote",
        "audited_conditional",  # acknowledges parent's audit status without promoting
    ]
    missing = [s for s in required_strings if s not in text]
    check(
        "all required source-note boundary strings are present",
        not missing,
        f"missing = {missing}" if missing else "all present",
    )

    # Forbidden overclaim PHRASES (not bare strings — the note legitimately
    # mentions e.g. "audited_clean" as a string being checked-against in this
    # very runner row). We only ban declarative overclaim phrasings here.
    forbidden_phrases = [
        "this note retires P1",
        "this note retires the P1",
        "this note retains the parent",
        "this note overturns",
        "this note promotes",
        "this note closes P1",
        "this note proves P1",
        "this note sets audit",
    ]
    present_forbidden = [s for s in forbidden_phrases if s in text]
    check(
        "no forbidden declarative overclaim phrases present in the source note",
        not present_forbidden,
        f"forbidden present = {present_forbidden}" if present_forbidden else "none",
    )


# --------------------------------------------------------------------------- #
# Main driver.
# --------------------------------------------------------------------------- #


def main():
    print("=" * 78)
    print("Klein-four APBC orbit partition closed-form narrow theorem — runner")
    print("Source: docs/OBSERVABLE_PRINCIPLE_KLEIN_FOUR_APBC_ORBIT_PARTITION_"
          "CLOSED_FORM_NARROW_THEOREM_NOTE_2026-05-17.md")
    print("=" * 78)

    test_t1_klein_four_group_axioms()
    test_t2_invariance_lemma_symbolic()
    test_t3_klein_four_preserves_phi(scan_max=64)
    test_t4_closed_form_orbit_count(scan_max=64)
    test_t5_collapse_identities_symbolic()
    test_t6_no_further_collapse()
    test_t7_single_orbit_characterization(scan_max=200)
    test_t8_orbit_sizes_at_2_and_4()
    test_t9_unique_resolved_orbit(scan_max=200)
    test_t10_cyclotomic_identification_at_4()
    test_t11_source_note_boundary()

    print("\n" + "=" * 78)
    print(f"THEOREM PASS={_PASS} FAIL={_FAIL}")
    print("=" * 78)
    return 0 if _FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
