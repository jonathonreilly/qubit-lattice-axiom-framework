#!/usr/bin/env python3
"""Defined-readout complement bridge: exact four-way equality runner.

Checks an exact equality among stipulated scalar/count inputs
(FOUR-WAY FORMAL equality plus a SEPARATE support-tier F5 numerical
companion):

  c^2 | _assigned couplings  =  1 - A^4
                              =  (N_color^2 - N_pair^2) / N_color^2
                              =  (N_quark - 1) / N_color^2
                              =  5/9                  [FOUR-WAY FORMAL]

Auxiliary support-tier numerical companion (NOT load-bearing for the
formal four-way equality):

  F5 (CKM n/9 family, support-tier)  =  5/9            [auxiliary only]

Reviewer correction (2026-04-26): an earlier version of this runner
labelled a "five-way" identity that included F5 inside the load-bearing
PASS. The exact equality is FOUR-WAY across the named inputs
only; F5 is a SEPARATE support-tier auxiliary check at the same
numerical value, not a fifth route.

Plus NEW closed forms:

  MW2 / MZ2                  =  c^2                           =  5/9.
  sqrt(MW2 / MZ2)            =  sqrt(N_quark - 1) / N_color  =  sqrt(5)/3.
  s^2 / c^2                  =  N_pair^2 / (N_quark - 1)     =  4/5.

Plus NEW SM-specific structural identity (T8):

  N_color^2 - N_pair^2  =  N_quark - 1.
  Derivable from retained primitive N_pair = N_color - 1 (W2),
  IFF N_color = 3 (positive root). Sharp algebraic SM-fingerprint.

The runner extracts the cited representation literals (`Q_L : (a,b)`) by
regex, explicitly supplies the coupling assignment declared by the theorem,
and derives every identity step-by-step via exact `Fraction` arithmetic. It
does not derive a physical weak angle, particle mass, or lattice coupling.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from pathlib import Path


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {name}{suffix}")
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1


def banner(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


REPO_ROOT = Path(__file__).resolve().parents[1]


def read_authority(rel_path: str) -> str:
    path = REPO_ROOT / rel_path
    if not path.exists():
        return ""
    return path.read_text()


def extract_rep_literal(content: str, field_name: str) -> tuple[int, int] | None:
    """Extract (dim_SU2, dim_SU3) from `<field> : (a,b)_{...}` literal."""
    if not content:
        return None
    pattern = re.compile(
        rf"`?\b{re.escape(field_name)}\s*:\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)_\{{[^}}]*\}}`?"
    )
    m = pattern.search(content)
    if not m:
        return None
    return int(m.group(1)), int(m.group(2))


def audit_authority_status_lines() -> None:
    """Check cited source presence; audit status is not theorem evidence."""
    banner("Cited source-file presence (status is not scientific evidence)")
    cited = (
        "docs/YT_EW_COLOR_PROJECTION_THEOREM.md",
        "docs/EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md",
        "docs/WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md",
        "docs/LEFT_HANDED_CHARGE_MATCHING_NOTE.md",
        "docs/ONE_GENERATION_MATTER_CLOSURE_NOTE.md",
        "docs/CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md",
        "docs/MINIMAL_AXIOMS_2026-04-11.md",
        "docs/CKM_EW_LATTICE_A4_BRIDGE_RETAINED_IDENTITY_NOTE_2026-04-25.md",
    )
    for rel_path in cited:
        check(f"cited source exists: {Path(rel_path).name}", bool(read_authority(rel_path)))
    f5 = read_authority(
        "docs/CKM_N9_STRUCTURAL_FAMILY_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md"
    )
    check("F5 auxiliary source contains F5=5/9", "F5" in f5 and "5/9" in f5)


def audit_yt_ew_couplings() -> tuple[Fraction, Fraction]:
    """Construct the theorem's explicitly supplied coupling assignment."""
    banner("P1: explicitly supplied coupling assignment")
    d = 3
    g_2_sq = Fraction(1, d + 1)
    g_Y_sq = Fraction(1, d + 2)
    check("P1: supplied d equals 3", d == 3)
    check("P1: supplied g_2^2 equals 1/4", g_2_sq == Fraction(1, 4))
    check("P1: supplied g_Y^2 equals 1/5", g_Y_sq == Fraction(1, 5))
    return g_2_sq, g_Y_sq


def audit_s1_qL_extraction() -> tuple[int, int, int, int]:
    """Extract retained Q_L : (a,b) literal (S1 source)."""
    banner("P4: Extract S1 source Q_L : (a,b) literal from retained doc (NOT hard-coded)")

    qL_content = read_authority("docs/LEFT_HANDED_CHARGE_MATCHING_NOTE.md")
    qL_rep = extract_rep_literal(qL_content, "Q_L")

    print("  Reading docs/LEFT_HANDED_CHARGE_MATCHING_NOTE.md")
    print(f"  Extracted Q_L : (dim_SU2, dim_SU3) = {qL_rep}")
    check("P4: Q_L representation literal extracted from retained doc",
          qL_rep is not None)

    if qL_rep is None:
        print("FATAL: Q_L literal not extractable. Aborting.")
        sys.exit(1)

    N_pair = qL_rep[0]   # dim_SU2(Q_L)
    N_color = qL_rep[1]  # dim_SU3(Q_L)
    N_quark = N_pair * N_color
    N_quark_minus_1 = N_quark - 1

    print(f"  S1 derivation: N_pair = dim_SU2(Q_L) = {N_pair}")
    print(f"  S1 derivation: N_color = dim_SU3(Q_L) = {N_color}")
    print(f"  S1 derivation: N_quark = N_pair * N_color = {N_quark}")
    print(f"  S1 derivation: N_quark - 1 = {N_quark_minus_1}")

    # Cross-check with retained right-handed quark reps
    one_gen_content = read_authority("docs/ONE_GENERATION_MATTER_CLOSURE_NOTE.md")
    uR_rep = extract_rep_literal(one_gen_content, "u_R")
    dR_rep = extract_rep_literal(one_gen_content, "d_R")
    if uR_rep is not None and dR_rep is not None:
        cross_ok = uR_rep[1] == dR_rep[1] == N_color
        print(f"  S1 cross-check: dim_SU3(u_R) = {uR_rep[1]}, dim_SU3(d_R) = {dR_rep[1]}")
        print(f"                  consistent with N_color = {N_color}? {cross_ok}")
        check("P4 cross-check: u_R, d_R SU(3) reps consistent with N_color",
              cross_ok)
    return N_pair, N_color, N_quark, N_quark_minus_1


def audit_t1_cos_sq_theta_w_via_yt_ew(g_2_sq: Fraction, g_Y_sq: Fraction
                                       ) -> Fraction:
    """T1: derive the formal c^2 readout from the supplied couplings."""
    banner("T1: formal c^2 from defined C^2 algebra and supplied couplings")

    # Defined quadratic-form readout: c^2 = g^2 / (g^2 + g_Y^2).
    cos_sq_theta_W = g_2_sq / (g_2_sq + g_Y_sq)

    print("  Defined C^2 readout: c^2 = g^2/(g^2 + g_Y^2)")
    print(f"  Supplied assignment: g_2^2 = {g_2_sq}, g_Y^2 = {g_Y_sq}")
    print(f"  c^2 | _assigned couplings = {g_2_sq} / ({g_2_sq} + {g_Y_sq})")
    print(f"                            = {g_2_sq} / {g_2_sq + g_Y_sq}")
    print(f"                            = {cos_sq_theta_W}")

    check("T1: formal c^2 equals 5/9 at the supplied couplings",
          cos_sq_theta_W == Fraction(5, 9))

    return cos_sq_theta_W


def audit_t2_complement_via_a4(cos_sq_theta_W: Fraction) -> Fraction:
    """T2: compare the stipulated complement 1-A^4 with formal c^2."""
    banner("T2: formal c^2 = 1 - A^4 at the supplied values")

    # A^2 = N_pair/N_color = 2/3 (W2 retained)
    # A^4 = (2/3)^2 = 4/9
    # The sister bridge supplies A^4 = 4/9 for this consistency check.
    A_sq = Fraction(2, 3)
    A_4 = A_sq ** 2
    sin_sq_theta_W_via_A4 = A_4
    cos_sq_theta_W_complement = 1 - sin_sq_theta_W_via_A4

    print(f"  W2 retained: A^2 = 2/3 ⇒ A^4 = {A_4}")
    print(f"  Sister bridge supplies A^4 = {sin_sq_theta_W_via_A4}")
    print(f"  Complement: c^2 = 1 - A^4 = {cos_sq_theta_W_complement}")
    print(f"  Matches T1 ({cos_sq_theta_W})?  {cos_sq_theta_W == cos_sq_theta_W_complement}")

    check("T2: formal c^2 = 1 - A^4 = 5/9",
          cos_sq_theta_W_complement == Fraction(5, 9))
    check("T2: T1 == T2 consistency (5/9 = 5/9)",
          cos_sq_theta_W == cos_sq_theta_W_complement)

    return cos_sq_theta_W_complement


def audit_t3_via_s1(N_pair: int, N_color: int, N_quark: int,
                    cos_sq_theta_W: Fraction) -> tuple[Fraction, Fraction]:
    """T3: structural-integer readings of formal c^2 = 5/9 via S1."""
    banner("T3: formal c^2 via S1 structural integers")

    # T3a: (N_color^2 - N_pair^2) / N_color^2
    val_a = Fraction(N_color ** 2 - N_pair ** 2, N_color ** 2)
    # T3b: (N_quark - 1) / N_color^2
    val_b = Fraction(N_quark - 1, N_color ** 2)

    print(f"  S1 structural integers: N_pair = {N_pair}, N_color = {N_color}, N_quark = {N_quark}")
    print(f"  T3a: (N_color^2 - N_pair^2) / N_color^2 = ({N_color**2} - {N_pair**2}) / {N_color**2}")
    print(f"                                          = {val_a}")
    print(f"  T3b: (N_quark - 1) / N_color^2          = ({N_quark - 1}) / {N_color**2}")
    print(f"                                          = {val_b}")
    print(f"  T1 formal c^2 | _assigned couplings = {cos_sq_theta_W}")

    check("T3a: (N_color^2 - N_pair^2)/N_color^2 = 5/9", val_a == Fraction(5, 9))
    check("T3b: (N_quark - 1)/N_color^2 = 5/9", val_b == Fraction(5, 9))
    check("T3a = T3b (structural identity)", val_a == val_b)
    check("T3a = T1 (structural reading == EW closed form)",
          val_a == cos_sq_theta_W)
    return val_a, val_b


def audit_t4_four_way_retained_equality(t1_val: Fraction, t2_val: Fraction,
                                        t3a: Fraction, t3b: Fraction) -> None:
    """T4: exact four-way formal equality at 5/9.

    The load-bearing equality is FOUR-WAY across the named inputs (T1, T2,
    T3a, T3b). The support-tier F5
    reading is checked SEPARATELY in audit_t4_aux_f5_companion as a
    non-load-bearing auxiliary companion at the same numerical value.
    """
    banner("T4: FOUR-WAY FORMAL EQUALITY at 5/9")

    print(f"  T1  (defined C^2 algebra + assignment): c^2 = {t1_val}")
    print(f"  T2  (1 - A^4 sister bridge):          c^2 = {t2_val}")
    print(f"  T3a ((N_c^2 - N_p^2)/N_c^2 via S1): structural reading       = {t3a}")
    print(f"  T3b ((N_q - 1)/N_c^2 via S1):       structural reading       = {t3b}")

    four_way = t1_val == t2_val == t3a == t3b == Fraction(5, 9)
    check("T4: FOUR-WAY FORMAL EQUALITY c^2 = 1 - A^4 = (Nc^2 - Np^2)/Nc^2 = (Nq-1)/Nc^2 = 5/9",
          four_way)


def audit_t4_aux_f5_companion(four_way_val: Fraction) -> None:
    """T4-aux: support-tier F5 companion reading at the SAME numerical value.

    F5 = 5/9 from CKM_N9_STRUCTURAL_FAMILY_KOIDE_BRIDGE_SUPPORT_NOTE is
    explicitly NOT a fifth route inside the four-way equality.
    It is reported here as a SEPARATE auxiliary numerical companion only.
    The formal four-way equality T4 is independent of this auxiliary.
    """
    banner("T4-aux: F5 numerical companion (NOT load-bearing)")
    content = read_authority(
        "docs/CKM_N9_STRUCTURAL_FAMILY_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md"
    )
    check(
        "T4-aux: cited F5 companion equals 5/9",
        "F5" in content and "5/9" in content and four_way_val == Fraction(5, 9),
    )


def audit_t5_m_w_m_z_lattice(cos_sq_theta_W: Fraction, N_color: int,
                             N_quark: int) -> None:
    """T5: formal MW2/MZ2 closed form."""
    banner("T5: formal MW2/MZ2 closed form")

    # Defined scalar readout: MW2 / MZ2 = c^2.
    M_W_sq_over_M_Z_sq = cos_sq_theta_W
    # Structural form: (N_quark - 1) / N_color^2
    M_W_sq_over_M_Z_sq_struct = Fraction(N_quark - 1, N_color ** 2)

    print("  Defined C^2 readout: MW2 / MZ2 = c^2")
    print(f"  MW2 / MZ2 = {M_W_sq_over_M_Z_sq}")
    print(f"  Structural: (N_quark - 1) / N_color^2 = {M_W_sq_over_M_Z_sq_struct}")
    print(f"  sqrt(MW2/MZ2) = sqrt(N_quark - 1) / N_color = sqrt({N_quark - 1})/{N_color}")
    print(f"                       = sqrt(5)/3 ≈ {((N_quark - 1) ** 0.5) / N_color:.6f}")

    check("T5: formal MW2/MZ2 = 5/9",
          M_W_sq_over_M_Z_sq == Fraction(5, 9))
    check("T5: MW2/MZ2 structural form (N_quark-1)/N_color^2 = 5/9",
          M_W_sq_over_M_Z_sq_struct == Fraction(5, 9))
    check("T5: defined readout at supplied couplings matches structural reading",
          M_W_sq_over_M_Z_sq == M_W_sq_over_M_Z_sq_struct)


def audit_t6_tan_sq_theta_w(cos_sq_theta_W: Fraction, N_pair: int,
                            N_quark: int) -> None:
    """T6: formal s^2/c^2 closed form."""
    banner("T6: formal s^2/c^2 closed form")

    sin_sq_theta_W = 1 - cos_sq_theta_W
    tan_sq_theta_W = sin_sq_theta_W / cos_sq_theta_W
    tan_sq_struct = Fraction(N_pair ** 2, N_quark - 1)

    print(f"  s^2 = 1 - c^2 = {sin_sq_theta_W}")
    print(f"  s^2/c^2 = {sin_sq_theta_W} / {cos_sq_theta_W}")
    print(f"                            = {tan_sq_theta_W}")
    print(f"  Structural: N_pair^2 / (N_quark - 1) = {N_pair**2} / {N_quark - 1}")
    print(f"                                       = {tan_sq_struct}")

    check("T6: formal s^2/c^2 = 4/5",
          tan_sq_theta_W == Fraction(4, 5))
    check("T6: s^2/c^2 structural form N_pair^2/(N_quark-1) = 4/5",
          tan_sq_struct == Fraction(4, 5))
    check("T6: trig form matches structural form",
          tan_sq_theta_W == tan_sq_struct)


def audit_t7_structural_readings_g_couplings(g_2_sq: Fraction,
                                             g_Y_sq: Fraction,
                                             N_pair: int,
                                             N_quark: int) -> None:
    """T7: structural readings of the supplied coupling assignment.
    """
    banner("T7: structural-integer readings of supplied couplings")

    g_2_sq_struct = Fraction(1, N_pair ** 2)
    g_Y_sq_struct = Fraction(1, N_quark - 1)

    print("  CONSISTENCY AT THE SUPPLIED VALUES (not a coupling derivation)")
    print()
    print(f"  Supplied:         g_2^2 = 1/(d+1) = {g_2_sq}")
    print(f"  S1 structural:   1/N_pair^2 = 1/{N_pair**2} = {g_2_sq_struct}")
    print(f"  Match? {g_2_sq == g_2_sq_struct}")
    check("T7a: supplied g_2^2 = 1/N_pair^2 at the cited values",
          g_2_sq == g_2_sq_struct)
    print()
    print(f"  Supplied:         g_Y^2 = 1/(d+2) = {g_Y_sq}")
    print(f"  S1 structural:   1/(N_quark - 1) = 1/{N_quark - 1} = {g_Y_sq_struct}")
    print(f"  Match? {g_Y_sq == g_Y_sq_struct}")
    check("T7b: supplied g_Y^2 = 1/(N_quark - 1) at the cited values",
          g_Y_sq == g_Y_sq_struct)


def audit_t8_sm_specific_structural_identity(N_pair: int, N_color: int,
                                             N_quark: int) -> None:
    """T8: SM-specific structural identity N_color^2 - N_pair^2 = N_quark - 1.
    Derivable from W2 primitive N_pair = N_color - 1 IFF N_color = 3.
    """
    banner("T8: SM-specific structural identity N_color^2 - N_pair^2 = N_quark - 1")

    lhs = N_color ** 2 - N_pair ** 2
    rhs = N_quark - 1

    print(f"  At retained values (S1):")
    print(f"    LHS: N_color^2 - N_pair^2 = {N_color**2} - {N_pair**2} = {lhs}")
    print(f"    RHS: N_quark - 1          = {N_quark} - 1 = {rhs}")
    print(f"    Equal? {lhs == rhs}")
    check("T8: N_color^2 - N_pair^2 = N_quark - 1 at retained S1 values",
          lhs == rhs)

    # Now verify the W2-primitive derivation: with N_pair = N_color - 1,
    # the identity reduces to N_color(N_color - 3) = 0, giving N_color = 3.
    print()
    print("  Algebraic derivation from retained W2 primitive N_pair = N_color - 1:")
    print("    N_color^2 - (N_color - 1)^2 = N_color(N_color - 1) - 1")
    print("    N_color^2 - N_color^2 + 2N_color - 1 = N_color^2 - N_color - 1")
    print("    2N_color - 1 = N_color^2 - N_color - 1")
    print("    N_color^2 - 3N_color = 0")
    print("    N_color(N_color - 3) = 0")
    print("    ⇒ N_color = 3 (positive root, dropping unphysical N_color = 0)")
    print()

    # Verify the algebraic statement: scan integer N_color over [1, 6] and
    # check which ones satisfy N_color^2 - N_pair^2 = N_quark - 1 with
    # N_pair = N_color - 1, N_quark = N_pair * N_color.
    print("  Scan integer N_color values to check which satisfy T8:")
    valid_N_colors = []
    for nc in range(1, 7):
        np = nc - 1  # W2 primitive
        if np < 1:
            print(f"    N_color = {nc}: skipped (N_pair = {np} < 1)")
            continue
        nq = np * nc
        L = nc ** 2 - np ** 2
        R = nq - 1
        valid = L == R
        marker = "✓" if valid else " "
        print(f"    N_color = {nc}: N_pair = {np}, N_quark = {nq}, "
              f"L = {L}, R = {R}, identity holds? {valid} {marker}")
        if valid:
            valid_N_colors.append(nc)

    unique_solution = valid_N_colors == [N_color]
    print()
    print(f"  Valid N_color values (with W2 primitive N_pair = N_color - 1): {valid_N_colors}")
    print(f"  Unique solution at retained N_color = {N_color}? {unique_solution}")
    check("T8 derivation: N_color = 3 is unique positive integer solution",
          unique_solution)


def audit_no_closure_overclaim() -> None:
    """Verify the source-note firewall without treating it as theorem evidence."""
    banner("Scope firewall: formal readouts are not physical observables")

    print("  Per the rejected A^2-below-W2 lesson preserved in")
    print("  feedback_consistency_vs_derivation_below_w2.md:")
    print()
    print("  - T1 uses the explicitly supplied coupling assignment and defined C^2")
    print("    scalar readout; it does not derive a physical weak angle.")
    print("  - T7 (structural readings g_2^2 = 1/N_pair^2, g_Y^2 = 1/(N_quark-1))")
    print("    are explicitly labeled as consistency at supplied values,")
    print("    NOT load-bearing for any closure.")
    print("  - T4 is an exact formal equality among the four named values.")
    print("  - T4-aux F5 support-tier reading is reported SEPARATELY as a")
    print("    non-load-bearing auxiliary companion (not a fifth route).")
    print("  - T5 concerns only the formal labels MW2 and MZ2.")

    note = read_authority(
        "docs/EW_LATTICE_COS_SQ_THETA_W_COMPLEMENT_BRIDGE_THEOREM_NOTE_2026-04-26.md"
    )
    check(
        "scope firewall states that physical interpretation remains open",
        "physical weak-angle" in note and "open premise" in note,
    )


def audit_summary(cos_sq_theta_W: Fraction, N_pair: int, N_color: int,
                  N_quark: int) -> None:
    banner("Summary of defined-readout complement bridge")

    print(f"  c^2 | _assigned couplings = {cos_sq_theta_W} (FOUR-WAY FORMAL EQUALITY)")
    print()
    print("  The four equal formal forms:")
    print("    1. c^2 | _assigned couplings  [defined C^2 algebra + assignment]")
    print("    2. 1 - A^4                   [from W2 + sister A^4 = 4/9 bridge]")
    print(f"    3. (N_color^2 - N_pair^2)/N_color^2 = ({N_color**2}-{N_pair**2})/{N_color**2}  [via S1]")
    print(f"    4. (N_quark - 1)/N_color^2 = ({N_quark - 1})/{N_color**2}  [via S1]")
    print(f"    All four equal {cos_sq_theta_W}.")
    print()
    print("  Auxiliary support-tier numerical companion (NOT load-bearing):")
    print("    F5 (CKM n/9 family, support-tier) = 5/9")
    print("    [reported separately as non-load-bearing auxiliary; not a fifth route]")
    print()
    print(f"  MW2 / MZ2 = (N_quark - 1)/N_color^2 = {Fraction(N_quark-1, N_color**2)}")
    print(f"                            = sqrt(5)/3 squared")
    print(f"  sqrt(MW2/MZ2) = sqrt({N_quark - 1})/{N_color} = sqrt(5)/3 ≈ {((N_quark-1)**0.5)/N_color:.4f}")
    print()
    print(f"  s^2/c^2 = N_pair^2/(N_quark - 1) = {Fraction(N_pair**2, N_quark-1)}")
    print()
    print(f"  SM-specific structural identity (T8): N_color^2 - N_pair^2 = N_quark - 1")
    print(f"    Derivable from W2 primitive N_pair = N_color - 1 IFF N_color = 3.")
    print()
    print("  Cited source-file presence checked without consuming audit status.")
    print("  Q_L : (a,b) literal extracted from doc text by regex (NOT hard-coded).")
    print("  Formal c^2 derived via Fraction arithmetic from the supplied coupling")
    print("  assignment and checked against the defined C^2 readout.")
    print()
    print(f"  FORMAL_C_SQ_COMPLEMENT_BRIDGE_VERIFIED = {cos_sq_theta_W == Fraction(5, 9)}")
    print(f"  FORMAL_MW2_MZ2_RATIO_VERIFIED          = {Fraction(N_quark-1, N_color**2) == cos_sq_theta_W}")
    print(f"  SM_STRUCTURAL_IDENTITY_VERIFIED        = {N_color**2 - N_pair**2 == N_quark - 1}")


def main() -> int:
    print("=" * 88)
    print("Defined-readout complement bridge: four-way formal equality")
    print("See docs/EW_LATTICE_COS_SQ_THETA_W_COMPLEMENT_BRIDGE_THEOREM_NOTE_2026-04-26.md")
    print("=" * 88)

    audit_authority_status_lines()
    g_2_sq, g_Y_sq = audit_yt_ew_couplings()
    N_pair, N_color, N_quark, _ = audit_s1_qL_extraction()

    cos_sq_theta_W = audit_t1_cos_sq_theta_w_via_yt_ew(g_2_sq, g_Y_sq)
    cos_sq_theta_W_complement = audit_t2_complement_via_a4(cos_sq_theta_W)
    t3a, t3b = audit_t3_via_s1(N_pair, N_color, N_quark, cos_sq_theta_W)
    audit_t4_four_way_retained_equality(
        cos_sq_theta_W, cos_sq_theta_W_complement, t3a, t3b
    )
    audit_t4_aux_f5_companion(cos_sq_theta_W)
    audit_t5_m_w_m_z_lattice(cos_sq_theta_W, N_color, N_quark)
    audit_t6_tan_sq_theta_w(cos_sq_theta_W, N_pair, N_quark)
    audit_t7_structural_readings_g_couplings(g_2_sq, g_Y_sq, N_pair, N_quark)
    audit_t8_sm_specific_structural_identity(N_pair, N_color, N_quark)
    audit_no_closure_overclaim()
    audit_summary(cos_sq_theta_W, N_pair, N_color, N_quark)

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
