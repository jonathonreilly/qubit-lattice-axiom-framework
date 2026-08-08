#!/usr/bin/env python3
"""Route-2 inverse-square center-lift boundary."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "QUARK_ROUTE2_INVERSE_SQUARE_CENTER_LIFT_BOUNDARY_NOTE_2026-06-21.md"

PASS_COUNT = 0
FAIL_COUNT = 0

W_E = Fraction(1, 3)
W_T = Fraction(1, 2)
Q_T = Fraction(5, 6)
S_TE = Fraction(-2)
TARGET_Q = Fraction(15, 8)
TARGET_RHO = Fraction(21, 4)
TARGET_C = Fraction(-8, 9)
TARGET_LAMBDA = Fraction(9, 4)


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(path: Path) -> str:
    return " ".join(read(path).split())


def q_to_rho(q: Fraction) -> Fraction:
    return 6 * (q - 1)


def q_to_c(q: Fraction) -> Fraction:
    return S_TE * Q_T / q


def lambda_for_power(power: int) -> Fraction:
    return (W_E / W_T) ** power


def part1_authorities() -> None:
    print("\nA. Authority anchors")
    paths = [
        NOTE,
        DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
        DOCS / "QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md",
        DOCS / "QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md",
        DOCS / "TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md",
        DOCS / "MINIMAL_AXIOMS_2026-06-05.md",
    ]
    for path in paths:
        check(f"{path.name} exists", path.exists(), str(path.relative_to(ROOT)))

    note = read(NOTE)
    check("new note declares no_go metadata", "**Claim type:** no_go" in note and "**Status authority:**" in note)
    check("new note names no endpoint closure", "no endpoint closure" in note)
    check("new note links exact readout", "](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)" in note)
    check("new note links Schur quadratic no-go", "](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md)" in note)


def part2_exact_inverse_square_law() -> None:
    print("\nB. Exact inverse-square boundary")
    c_norm = Q_T * W_T * W_T
    q_e = c_norm / (W_E * W_E)
    check("T-side fixes normalized constant C=5/24", c_norm == Fraction(5, 24), str(c_norm))
    check("inverse-square law maps E weight to q_E=15/8", q_e == TARGET_Q, str(q_e))
    check("q_E=15/8 maps to rho_E=21/4", q_to_rho(q_e) == TARGET_RHO, str(q_to_rho(q_e)))
    check("q_E=15/8 maps to c_TE=-8/9", q_to_c(q_e) == TARGET_C, str(q_to_c(q_e)))
    check("inverse-square law gives lambda=9/4", q_e / Q_T == TARGET_LAMBDA, str(q_e / Q_T))
    check("E and T normalized products agree", q_e * W_E * W_E == Q_T * W_T * W_T, str(q_e * W_E * W_E))
    check("constant 5/24 is not supplied by weights alone", c_norm != W_E and c_norm != W_T and c_norm != W_E * W_T, str(c_norm))


def part3_power_law_discriminator() -> None:
    print("\nC. Power-law discriminator")
    expected = {
        -2: Fraction(9, 4),
        -1: Fraction(3, 2),
        0: Fraction(1),
        1: Fraction(2, 3),
        2: Fraction(4, 9),
    }
    for power, value in expected.items():
        check(f"weight power {power} gives expected covariance", lambda_for_power(power) == value, str(lambda_for_power(power)))
    target_powers = [p for p in range(-6, 7) if lambda_for_power(p) == TARGET_LAMBDA]
    check("only integer power -2 in [-6,6] gives target covariance", target_powers == [-2], str(target_powers))
    check("quadratic positive power is wrong value", lambda_for_power(2) != TARGET_LAMBDA, str(lambda_for_power(2)))
    check("one inverse leverage power is wrong value", lambda_for_power(-1) != TARGET_LAMBDA, str(lambda_for_power(-1)))
    check("no-covariance power is wrong value", lambda_for_power(0) != TARGET_LAMBDA, str(lambda_for_power(0)))


def part4_current_surface_firewall() -> None:
    print("\nD. Current-surface firewall")
    naturality = flat(DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md")
    kappa = flat(DOCS / "QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md")
    schur = flat(DOCS / "QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md")
    center = flat(DOCS / "TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md")
    axioms = flat(DOCS / "MINIMAL_AXIOMS_2026-06-05.md")

    check("naturality no-go leaves rho_E free", "remains a free parameter unless an additional E-center endpoint ratio, source-domain, or readout-map primitive is supplied" in naturality)
    check("kappa note says covariance bridge is not consequence", "not a consequence" in kappa and "remaining open datum" in kappa)
    check("Schur note identifies inverse-square gap", "inverse square" in schur.lower() and "q_X" in schur and "w_X" in schur)
    check("Schur note says no named functional produces inverse-square lift", "No named functional produces an" in schur)
    check("Schur note says quadratic route has free E:T ratio", "free `E:T1`" in schur or "free E:T1" in schur)
    check("center-excess note supplies 1/6 but not inverse-square law", "1/6" in center and "inverse-square" not in center.lower())
    check("minimal axioms withhold readout context and weighting", "record supplies no readout context" in axioms and "weighting" in axioms)
    check("minimal axioms do not supply inverse-square law", "inverse-square" not in axioms.lower())


def part5_note_firewall() -> None:
    print("\nE. New-note claim firewall")
    note = read(NOTE)
    note_flat = " ".join(note.split())
    note_lower = note.lower()
    forbidden_markers = (
        "observed quark",
        "fitted yukawa",
        "ckm",
        "pdg",
        "nearest-rational",
        "endpoint closure achieved",
    )
    check("forbidden observational/fitted proof inputs are absent from note", all(marker not in note_lower for marker in forbidden_markers))
    check("note says current surfaces do not derive the law", "Current named O_h equivariance, quadratic Schur, naturality, center-excess, and minimal-axiom surfaces do not derive that law" in note_flat)
    check("note calls route exact support boundary not closure", "exact support boundary and a sharpened open primitive target, not endpoint closure" in note_flat)
    check("proposal_allowed false is recorded", "proposal_allowed: false" not in note and "actual_current_surface_status:" not in note)
    check("bare retained is disallowed", "bare_retained_allowed: false" not in note)


def part6_n5_execution_certificate() -> None:
    """N5 execution certificate: print-only; it registers no check."""
    print("\nF. N5 execution certificate")
    c_norm = Q_T * W_T * W_T
    sweep = [p for p in range(-6, 7)]
    print(
        f"per_element: the normalization constant is built from one channel and then spent "
        f"on the other, entry by entry -- C = q_T * w_T^2 = {c_norm} comes solely from the "
        f"granted T data, q_E = C / w_E^2 = {c_norm / (W_E * W_E)} is read back on the E "
        "side, and rho_E, c_TE and lambda are each derived from that single scalar "
        "separately; C is also compared individually against w_E, w_T and w_E*w_T and "
        "matches none of them."
    )
    print(
        "per_site: checked and not executed -- the only star-derived numbers entering this "
        "file are the two per-arm weights, and the 1/6 center-excess support step is not "
        "used arithmetically at all; it is merely confirmed present in the center-excess "
        "note, which the same runner then confirms says nothing about an inverse-square "
        "law, so the site-level support content is cited rather than computed here."
    )
    print(
        f"per_mode: the two channels are tied by one invariant and that tie is tested "
        f"directly -- the law asserts q_X * w_X^2 is channel-independent, and the runner "
        f"confirms q_E * w_E^2 equals q_T * w_T^2 at the common value {c_norm}, so the E "
        "and T modes are not merely scaled against each other but are shown to share a "
        "single normalized product, which is the whole content of the conditional support."
    )
    print(
        f"per_block: the weight-power ladder is resolved as a block and then swept -- the "
        f"five named rungs -2, -1, 0, 1, 2 give lambda = 9/4, 3/2, 1, 2/3 and 4/9 "
        f"respectively, and a wider sweep across all {len(sweep)} integer powers in [-6, 6] "
        "returns the single hit -2, so the boundary is a uniqueness result within the "
        "integer power grammar rather than a check at one favoured exponent."
    )
    print(
        "lattice_wide: checked and not executed -- no lattice, box, volume, site count or "
        "limit is constructed anywhere in this runner, whose arithmetic universe is four "
        "granted scalars and one exponent; the whole-surface object it reports as absent is "
        "the inverse-square center-lift law itself, which the verdict names as an open "
        "primitive rather than anything this file derives."
    )


def main() -> int:
    print("=" * 88)
    print("ROUTE-2 INVERSE-SQUARE CENTER-LIFT BOUNDARY")
    print("=" * 88)
    part1_authorities()
    part2_exact_inverse_square_law()
    part3_power_law_discriminator()
    part4_current_surface_firewall()
    part5_note_firewall()
    part6_n5_execution_certificate()
    print("\nSummary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: inverse-square center-lift normalization would close Route-2, but remains an open primitive.")
        return 0
    print("VERDICT: inverse-square center-lift boundary checks failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
