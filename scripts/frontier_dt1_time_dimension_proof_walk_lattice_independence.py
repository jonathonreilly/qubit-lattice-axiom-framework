#!/usr/bin/env python3
"""Conditional anomaly/parity arithmetic with supplied reconstruction and clock cap.

No full-chain lattice-independence or physical time derivation is checked.
Metadata checks concern source identity/presence only.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    ROOT
    / "docs"
    / "DT1_TIME_DIMENSION_PROOF_WALK_LATTICE_INDEPENDENCE_BOUNDED_NOTE_2026-05-08.md"
)

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tag = "PASS" if ok else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{tag}] {name}{suffix}")
    return ok


def metadata(name: str, ok: bool, detail: str = "") -> bool:
    global FAIL
    print(f"  [METADATA {'OK' if ok else 'FAIL'}] {name} {detail}")
    if not ok:
        FAIL += 1
    return ok


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


NOTE_TEXT = NOTE_PATH.read_text()
NOTE_FLAT = re.sub(r"\s+", " ", NOTE_TEXT)


def check_note_structure() -> None:
    section("source metadata, not mathematical evidence")
    for marker in ["Claim type:** bounded_theorem", "Proposal allowed:** false",
                   "P-HY", "P-COMP", "P-REC", "B-AXIS",
                   "full-chain", "d_t<=1", "doubled representations"]:
        metadata(f"scope marker: {marker}", marker in NOTE_TEXT)


def check_honest_scope() -> None:
    metadata("full-chain independence withdrawn", "withdraws the older full-chain assertion" in NOTE_TEXT)


def check_dependencies_exist() -> None:
    for rel in ["MINIMAL_AXIOMS_2026-06-29.md", "ANOMALY_FORCES_TIME_THEOREM.md",
                "CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md",
                "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md",
                "LH_ANOMALY_TRACE_CATALOG_THEOREM_NOTE_2026-04-25.md",
                "ONE_TIME_DIMENSION_DT1_REDUCES_TO_EMERGENT_DYNAMICS_GATE_OPEN_GATE_NOTE_2026-06-17.md",
                "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"]:
        metadata(f"dependency exists: {rel}", (ROOT / "docs" / rel).exists())


def check_exact_lh_anomaly_traces() -> None:
    section("exact LH-anomaly traces (Step 1 input)")
    # Left-handed content of one generation:
    # Q_L = (2, 3)_{+1/3}: SU(2) doublet, SU(3) triplet, Y = +1/3, mult 6
    # L_L = (2, 1)_{-1}:   SU(2) doublet, SU(3) singlet, Y = -1,   mult 2
    y_QL = Fraction(1, 3)
    y_LL = Fraction(-1)
    n_QL = 6
    n_LL = 2
    dynkin_fund = Fraction(1, 2)

    tr_y_lh = n_QL * y_QL + n_LL * y_LL
    check("Tr[Y]_LH = 0", tr_y_lh == 0, str(tr_y_lh))

    # Tr[SU(2)^2 Y]_LH = T(fund_SU2) * (n_color_QL * y_QL + n_color_LL * y_LL)
    # SU(2) doublet T = 1/2; trace runs over color-replicated doublets
    tr_su2_y_lh = dynkin_fund * (3 * y_QL + 1 * y_LL)
    check("Tr[SU(2)^2 Y]_LH = 0", tr_su2_y_lh == 0, str(tr_su2_y_lh))

    # Tr[SU(3)^2 Y]_LH = T(fund_SU3) * (2 * y_QL)
    # SU(3) triplet T = 1/2; trace runs over isospin-replicated triplets
    tr_su3_y_lh = dynkin_fund * (2 * y_QL)
    check("Tr[SU(3)^2 Y]_LH = 1/3", tr_su3_y_lh == Fraction(1, 3), str(tr_su3_y_lh))

    tr_y_cubed_lh = n_QL * y_QL ** 3 + n_LL * y_LL ** 3
    check("Tr[Y^3]_LH = -16/9", tr_y_cubed_lh == Fraction(-16, 9), str(tr_y_cubed_lh))

    # The two nonzero LH traces are the inconsistency that drives Steps 2-4.
    nonzero_anomaly_traces = (tr_su3_y_lh, tr_y_cubed_lh)
    any_nonzero = any(t != 0 for t in nonzero_anomaly_traces)
    check("LH content is anomalous (drives Steps 2-4)", any_nonzero)


def check_full_spectrum_anomaly_cancellation() -> None:
    section("full SM spectrum cancels anomaly (Step 2 output)")
    y = {
        "Q_L": Fraction(1, 3),
        "L_L": Fraction(-1),
        "u_R": Fraction(4, 3),
        "d_R": Fraction(-2, 3),
        "e_R": Fraction(-2),
        "nu_R": Fraction(0),
    }
    mult = {"Q_L": 6, "L_L": 2, "u_R": 3, "d_R": 3, "e_R": 1, "nu_R": 1}

    # Tr[Y] (LH minus RH for chirality-signed convention)
    tr_y = (
        mult["Q_L"] * y["Q_L"]
        + mult["L_L"] * y["L_L"]
        - mult["u_R"] * y["u_R"]
        - mult["d_R"] * y["d_R"]
        - mult["e_R"] * y["e_R"]
        - mult["nu_R"] * y["nu_R"]
    )
    check("Tr[Y] = 0 on full spectrum", tr_y == 0, str(tr_y))

    dynkin_fund = Fraction(1, 2)
    tr_su3_y = dynkin_fund * (2 * y["Q_L"] - y["u_R"] - y["d_R"])
    check(
        "Tr[SU(3)^2 Y] = 0 per color on full spectrum",
        tr_su3_y == 0,
        str(tr_su3_y),
    )

    tr_y_cubed = (
        mult["Q_L"] * y["Q_L"] ** 3
        + mult["L_L"] * y["L_L"] ** 3
        - mult["u_R"] * y["u_R"] ** 3
        - mult["d_R"] * y["d_R"] ** 3
        - mult["e_R"] * y["e_R"] ** 3
        - mult["nu_R"] * y["nu_R"] ** 3
    )
    check("Tr[Y^3] = 0 on full spectrum", tr_y_cubed == 0, str(tr_y_cubed))


def check_clifford_volume_classification() -> None:
    section("Clifford volume-element parity (Step 3 input)")
    # omega = gamma_1 ... gamma_n satisfies
    #   omega gamma_mu = (-1)^{n-1} gamma_mu omega
    # n even: anticommutes with all generators -> chirality gamma_5 exists.
    # n odd: volume commutes; this does not exclude other gradings on doubled representations.
    for n in range(1, 9):
        sign = (-1) ** (n - 1)
        # We define "anticommutes" iff sign == -1.
        anticommutes = sign == -1
        chirality_exists = anticommutes
        if n % 2 == 0:
            check(
                f"n={n} (even): omega anticommutes with gamma_mu, volume anticommutes",
                chirality_exists,
            )
        else:
            check(
                f"n={n} (odd): omega is central, volume is central (no claim about doubled representations)",
                not chirality_exists,
            )


def check_d_s_from_a2_then_d_t_odd() -> None:
    section("supplied d_s=3 and volume grading imply odd d_t")
    # A2 supplies d_s = 3 directly. Not derived here.
    d_s = 3
    print("INFO: current Lattice axiom supplies d_s=3; legacy A2 label is historical.")

    # The supplied volume-element grading requires d_s + d_t even.
    for d_t in range(0, 8):
        n_total = d_s + d_t
        chirality_ok = (n_total % 2) == 0
        if d_t % 2 == 1:
            check(
                f"d_t = {d_t} (odd): d_s + d_t = {n_total} even, volume grading OK",
                chirality_ok,
            )
        else:
            check(
                f"d_t = {d_t} (even): d_s + d_t = {n_total} odd, volume grading fails",
                not chirality_ok,
            )


def check_single_clock_excludes_dt_gt_1() -> None:
    print("INFO: d_t=1 single-clock exclusion is a separate supplied premise, not tested here.")


def check_d_t_unique_one() -> None:
    section("uniqueness: d_t = 1 (Step 5 combine)")
    d_s = 3
    survivors = []
    for d_t in range(0, 8):
        chirality_ok = ((d_s + d_t) % 2) == 0   # Step 3 (Clifford)
        odd_ok = (d_t % 2) == 1                 # Step 3 conclusion (parity)
        single_clock_ok = d_t <= 1              # Step 4 (cited theorem)
        if chirality_ok and odd_ok and single_clock_ok:
            survivors.append(d_t)
    check("conditional filter with supplied single clock", survivors == [1], str(survivors))
    check("oddness alone leaves multiple tested dimensions", [d for d in range(8) if (3+d)%2==0] == [1,3,5,7])


def check_lattice_action_boundary() -> None:
    print("INFO: absence of lattice-action runtime inputs does not certify transitive premise independence.")


def check_no_status_promotion_language() -> None:
    metadata("audit authority disclosed", "independent audit lane" in NOTE_TEXT)


def main() -> int:
    print("frontier_dt1_time_dimension_proof_walk_lattice_independence.py")
    check_note_structure()
    check_honest_scope()
    check_dependencies_exist()
    check_exact_lh_anomaly_traces()
    check_full_spectrum_anomaly_cancellation()
    check_clifford_volume_classification()
    check_d_s_from_a2_then_d_t_odd()
    check_single_clock_excludes_dt_gt_1()
    check_d_t_unique_one()
    check_lattice_action_boundary()
    check_no_status_promotion_language()
    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("VERDICT: conditional arithmetic checks and source metadata pass.")
        print("Oddness alone does not select d_t=1; the separate single-clock")
        print("premise and its dynamics are not derived by this runner.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
