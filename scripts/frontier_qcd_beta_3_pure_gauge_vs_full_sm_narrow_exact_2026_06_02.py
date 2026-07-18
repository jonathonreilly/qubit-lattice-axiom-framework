#!/usr/bin/env python3
"""Exact-symbolic verifier for
`QCD_BETA_3_PURE_GAUGE_VS_FULL_SM_NARROW_THEOREM_NOTE_2026-06-02`.

Given (X0) graph-first SU(3)_c with N_color=3, (X1) N_quark in
{0 (pure gauge), 6 (explicitly supplied full-SM inventory)}, (X2) linked
N_gen = 3 bookkeeping, and (X3) explicitly supplied
Peskin-Schroeder b = (11/3) C_2(adj SU(N)) - (4/3) T(F) n_f with
C_2(adj SU(N)) = N, T(F) = 1/2, n_f counting Dirac quark flavors, and no
scalar (Higgs is SU(3)-singlet), verifies (P1) b_3 = (11 N_color - 2
N_quark)/3, (P2a) 11 at
(3,0), (P2b) 7 at (3,6), (P2) Delta b_3 = 4 = (2/3)*6, (P3) per-sector
+11 -4 = +7, plus (C1)-(C5), SU(2) sister cross-check, convention flip.
Mirrors the bounded SU(2)_L sister
audit_companion_su2_weak_beta_coefficient_narrow_exact_2026_05_10.py.
"""

from __future__ import annotations
import sys

try:
    from sympy import Rational, Symbol, simplify
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


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


def main() -> int:
    print("=" * 88)
    print("Exact-symbolic verifier for")
    print("QCD_BETA_3_PURE_GAUGE_VS_FULL_SM_NARROW_THEOREM_NOTE_2026-06-02")
    print("Goal: b_3(n_f=0) = 11, b_3(n_f=6) = 7, Delta b_3 = 4")
    print("=" * 88)

    # ---------------------------------------------------------------------
    section("Part 0: symbolic setup and (X3) Peskin-Schroeder application")
    # ---------------------------------------------------------------------
    N_color = Symbol("N_color", positive=True, integer=True)
    N_quark = Symbol("N_quark", nonnegative=True, integer=True)

    # (X3) explicit external kernel: C_2(adj SU(N)) = N; T(F) = 1/2.
    # n_f counts Dirac quark flavors; no scalar contribution because the
    # SM Higgs is SU(3)-singlet.
    C2_adj_SU3 = N_color
    T_F = Rational(1, 2)

    # Peskin-Schroeder Eq. 16.135 specialized to QCD:
    b_3_psv = (
        Rational(11, 3) * C2_adj_SU3
        - Rational(4, 3) * T_F * N_quark
    )

    # ---------------------------------------------------------------------
    section("Part 1: (P1) symbolic closed form parametric in (N_color, N_quark)")
    # ---------------------------------------------------------------------
    # Unfactored form: b_3 = (11/3) N_color - (2/3) N_quark.
    b_3_claimed_P1 = (
        Rational(11, 3) * N_color
        - Rational(2, 3) * N_quark
    )
    check(
        "(P1) PSv-applied b_3 = (11/3) N_color - (2/3) N_quark",
        simplify(b_3_psv - b_3_claimed_P1) == 0,
        detail=f"diff = {simplify(b_3_psv - b_3_claimed_P1)}",
    )

    # Factored form: b_3 = (11 N_color - 2 N_quark) / 3.
    b_3_claimed_factored = (11 * N_color - 2 * N_quark) / Rational(3)
    check(
        "(P1') factored: b_3 = (11 N_color - 2 N_quark) / 3",
        simplify(b_3_psv - b_3_claimed_factored) == 0,
        detail=f"diff = {simplify(b_3_psv - b_3_claimed_factored)}",
    )

    # ---------------------------------------------------------------------
    section("Part 2: (P2a) pure-gauge instance (3, 0) -> 11")
    # ---------------------------------------------------------------------
    pure_gauge = {N_color: 3, N_quark: 0}
    b_3_pure_gauge = simplify(b_3_psv.subs(pure_gauge))
    check(
        "(P2a) pure-gauge b_3 = 11 at (N_color, N_quark) = (3, 0)",
        b_3_pure_gauge == Rational(11),
        detail=f"b_3 = {b_3_pure_gauge}",
    )
    check(
        "(P2a alt) factored form at (3, 0) also equals 11",
        simplify(b_3_claimed_factored.subs(pure_gauge)) == Rational(11),
        detail="cross-check via (P1')",
    )

    # ---------------------------------------------------------------------
    section("Part 3: (P2b) full-SM instance (3, 6) -> 7")
    # ---------------------------------------------------------------------
    full_sm = {N_color: 3, N_quark: 6}
    b_3_full_sm = simplify(b_3_psv.subs(full_sm))
    check(
        "(P2b) full-SM b_3 = 7 at (N_color, N_quark) = (3, 6)",
        b_3_full_sm == Rational(7),
        detail=f"b_3 = {b_3_full_sm}",
    )
    check(
        "(P2b alt) factored form at (3, 6) also equals 7",
        simplify(b_3_claimed_factored.subs(full_sm)) == Rational(7),
        detail="cross-check via (P1')",
    )

    # Check the supplied full-SM bookkeeping decomposition 6 = 3 * 2.
    N_gen_sym = Symbol("N_gen", positive=True, integer=True)
    N_pair_sym = Symbol("N_pair", positive=True, integer=True)
    check(
        "(X1b) N_quark = N_gen * N_pair = 3 * 2 = 6",
        simplify((N_gen_sym * N_pair_sym).subs({N_gen_sym: 3, N_pair_sym: 2}))
        == Rational(6),
        detail="3 * 2 = 6",
    )

    # ---------------------------------------------------------------------
    section("Part 4: (P2) pure-gauge vs full-SM difference Delta b_3 = 4")
    # ---------------------------------------------------------------------
    delta_b_3 = simplify(b_3_pure_gauge - b_3_full_sm)
    check(
        "(P2) Delta b_3 = b_3(0) - b_3(6) = 11 - 7 = 4",
        delta_b_3 == Rational(4),
        detail=f"Delta b_3 = {delta_b_3}",
    )

    # Symbolic: b_3(N_color, 0) - b_3(N_color, N_quark) = (2/3) N_quark, parametric.
    delta_b_3_sym = simplify(b_3_psv.subs({N_quark: 0}) - b_3_psv)
    check(
        "Symbolic: b_3(N_color, 0) - b_3(N_color, N_quark) = (2/3) N_quark",
        simplify(delta_b_3_sym - Rational(2, 3) * N_quark) == 0,
        detail=f"diff = {simplify(delta_b_3_sym - Rational(2, 3) * N_quark)}",
    )

    # ---------------------------------------------------------------------
    section("Part 5: (P3) per-sector decomposition")
    # ---------------------------------------------------------------------
    gauge_contrib_sym = Rational(11, 3) * N_color
    matter_contrib_sym = -Rational(2, 3) * N_quark

    # Full-SM: gauge +11, matter -4, sum +7.
    gauge_at_fw = simplify(gauge_contrib_sym.subs(full_sm))
    matter_at_fw = simplify(matter_contrib_sym.subs(full_sm))
    check(
        "(P3) full-SM gauge contribution +11",
        gauge_at_fw == Rational(11),
        detail=f"(11/3) * 3 = {gauge_at_fw}",
    )
    check(
        "(P3) full-SM matter contribution -4",
        matter_at_fw == Rational(-4),
        detail=f"-(2/3) * 6 = {matter_at_fw}",
    )
    check(
        "(P3) full-SM sum: 11 + (-4) = 7",
        gauge_at_fw + matter_at_fw == Rational(7),
        detail=f"{gauge_at_fw} + {matter_at_fw} = {gauge_at_fw + matter_at_fw}",
    )

    # Pure-gauge: gauge +11, matter 0, sum +11.
    gauge_at_pg = simplify(gauge_contrib_sym.subs(pure_gauge))
    matter_at_pg = simplify(matter_contrib_sym.subs(pure_gauge))
    check(
        "(P3) pure-gauge sum: 11 + 0 = 11 (matter contribution vanishes at n_f=0)",
        (gauge_at_pg + matter_at_pg) == Rational(11) and matter_at_pg == Rational(0),
        detail=f"gauge={gauge_at_pg}, matter={matter_at_pg}",
    )

    # ---------------------------------------------------------------------
    section("Part 6: (C1)-(C5) corollaries")
    # ---------------------------------------------------------------------
    # (C1) Per-sector decomposition exact at full SM: 11 + (-4) = 7.
    check(
        "(C1) per-sector exact: 11 + (-4) = 7",
        Rational(11) + Rational(-4) == Rational(7),
        detail="11 - 4 = 7",
    )

    # (C2) Ratio b_3(n_f=0) : b_3(n_f=6) = 11 : 7.
    check(
        "(C2) ratio b_3(0) : b_3(6) = 11 : 7",
        (b_3_pure_gauge / b_3_full_sm) == Rational(11, 7),
        detail=f"11/7 = {b_3_pure_gauge / b_3_full_sm}",
    )

    # (C3) Linear slope -(2/3) N_quark, parametric in N_color.
    c3_lhs = simplify(b_3_psv - b_3_psv.subs({N_quark: 0}))
    check(
        "(C3) b_3(N_quark) - b_3(0) = -(2/3) N_quark, parametric in N_color",
        simplify(c3_lhs - (-Rational(2, 3) * N_quark)) == 0,
        detail=f"diff = {simplify(c3_lhs - (-Rational(2, 3) * N_quark))}",
    )
    check(
        "(C3 alt) at (3, 6): b_3(6) - b_3(0) = -4",
        simplify(c3_lhs.subs(full_sm)) == Rational(-4),
        detail=f"{simplify(c3_lhs.subs(full_sm))}",
    )

    # (C4) Asymptotic-freedom threshold N_quark < (11/2) N_color.
    threshold_at_3 = simplify(Rational(11, 2) * Rational(3))
    check(
        "(C4) AF threshold at N_color=3: N_quark < 33/2 = 16.5",
        threshold_at_3 == Rational(33, 2),
        detail=f"threshold = {threshold_at_3}",
    )
    check(
        "(C4) framework N_quark=6 < 16.5 -> AF holds; bound recovers N_quark <= 16",
        (6 < threshold_at_3)
        and simplify(b_3_psv.subs({N_color: 3, N_quark: 16})) > 0
        and simplify(b_3_psv.subs({N_color: 3, N_quark: 17})) < 0,
        detail="b_3(16)=1/3 > 0, b_3(17)=-1/3 < 0 -> AF cuts at n_f = 16",
    )

    # (C5) Counterfactual (3, 12): b_3 = 3.
    b_3_cf = simplify(b_3_psv.subs({N_color: 3, N_quark: 12}))
    check(
        "(C5) counterfactual (3, 12) -> 3 (N_pair=4 -> N_quark=12); parametric confirmed",
        b_3_cf == Rational(3),
        detail=f"b_3 = (33 - 24)/3 = {b_3_cf}",
    )

    # ---------------------------------------------------------------------
    section("Part 7: cross-checks (Rational arithmetic, sister, convention-flip)")
    # ---------------------------------------------------------------------
    # Direct Rational arithmetic on both instances.
    pg_total_num = Rational(11, 3) * 3 + (-Rational(2, 3) * 0)
    sm_total_num = Rational(11, 3) * 3 + (-Rational(2, 3) * 6)
    check(
        "Rational arithmetic: pure-gauge = 11, full-SM = 7, Delta = 4",
        pg_total_num == Rational(11)
        and sm_total_num == Rational(7)
        and (pg_total_num - sm_total_num) == Rational(4),
        detail=f"pg={pg_total_num}, sm={sm_total_num}, delta={pg_total_num - sm_total_num}",
    )

    # Sister cross-check: the same (X3) kernel at SU(2) pure gauge
    # gives the matter-free piece of the bounded SU(2)_L sister.
    b_2_pg_matter_free = simplify(b_3_psv.subs({N_color: 2, N_quark: 0}))
    check(
        "sister cross-check: SU(2) pure-gauge matter-free = +22/3",
        b_2_pg_matter_free == Rational(22, 3),
        detail=f"(11/3) * 2 = {b_2_pg_matter_free}",
    )

    # Convention-flip: under alternative `beta < 0 <-> AF` sign convention,
    # b_3 -> -b_3 uniformly; |Delta b_3| = 4 preserved.
    b_3_pg_flip = simplify(-b_3_psv.subs(pure_gauge))
    b_3_sm_flip = simplify(-b_3_psv.subs(full_sm))
    delta_flip = simplify(b_3_pg_flip - b_3_sm_flip)
    check(
        "convention-flip: b_3 -> -b_3, |Delta b_3| = 4 preserved",
        abs(delta_flip) == Rational(4)
        and b_3_sm_flip == Rational(-7)
        and b_3_pg_flip == Rational(-11),
        detail=f"pg_flip={b_3_pg_flip}, sm_flip={b_3_sm_flip}, |delta|={abs(delta_flip)}",
    )

    section("Summary")
    print("  Verified: (P1)/(P1') parametric form; (P2a) pg=11; (P2b) sm=7;")
    print("  (P2) Delta=4; (P3) per-sector; (C1)-(C5); SU(2) cross-check;")
    print("  convention-flip; Rational-arithmetic sanity.")
    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
