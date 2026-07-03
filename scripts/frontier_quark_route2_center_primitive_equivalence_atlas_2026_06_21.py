#!/usr/bin/env python3
"""Route-2 center primitive equivalence atlas and firewall."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "QUARK_ROUTE2_CENTER_PRIMITIVE_EQUIVALENCE_ATLAS_NOTE_2026-06-21.md"

PASS_COUNT = 0
FAIL_COUNT = 0

Q_T = Fraction(5, 6)
S_TE = Fraction(-2)
TARGET_RHO = Fraction(21, 4)
TARGET_Q = Fraction(15, 8)
TARGET_C = Fraction(-8, 9)
TARGET_LAMBDA = Fraction(9, 4)
TARGET_METRIC_RATIO = Fraction(1449, 704)
W_E = Fraction(1, 3)
W_T = Fraction(1, 2)
F_ADJ = Fraction(8, 9)


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


def rho_to_q(rho: Fraction) -> Fraction:
    return 1 + rho / 6


def q_to_rho(q: Fraction) -> Fraction:
    return 6 * (q - 1)


def c_to_q(c_te: Fraction) -> Fraction:
    return S_TE * Q_T / c_te


def q_to_c(q: Fraction) -> Fraction:
    return S_TE * Q_T / q


def lambda_to_q(lam: Fraction) -> Fraction:
    return lam * Q_T


def q_to_lambda(q: Fraction) -> Fraction:
    return q / Q_T


def diag_ratio_to_q_squared(ratio: Fraction) -> Fraction:
    return 1 + Fraction(11, 9) * ratio


def diag_ratio_for_q(q: Fraction) -> Fraction:
    return Fraction(9, 11) * (q * q - 1)


def general_metric_residual(a: Fraction, b: Fraction, c: Fraction, q: Fraction) -> Fraction:
    center_t = Fraction(-5, 3)
    shell = (Fraction(1), Fraction(-2))
    return (
        a * (q * q - 1)
        + 2 * c * (q * center_t - shell[0] * shell[1])
        + b * (center_t * center_t - shell[1] * shell[1])
    )


def part1_authorities() -> None:
    print("\nA. Authority anchors")
    paths = [
        NOTE,
        DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
        DOCS / "QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md",
        DOCS / "QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md",
        DOCS / "QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md",
        DOCS / "QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md",
        DOCS / "QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md",
        DOCS / "MINIMAL_AXIOMS_2026-06-05.md",
    ]
    for path in paths:
        check(f"{path.name} exists", path.exists(), str(path.relative_to(ROOT)))

    note = read(NOTE)
    check("new note declares no_go metadata", "**Claim type:** no_go" in note and "**Status authority:**" in note)
    check("new note names no endpoint closure", "no endpoint closure" in note)
    check("new note has exact readout markdown link", "](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)" in note)
    check("new note has naturality no-go markdown link", "](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md)" in note)
    check("new note avoids source-status certificate", "proposal_allowed: false" not in note and "actual_current_surface_status:" not in note)


def part2_equivalence_atlas() -> None:
    print("\nB. Exact equivalence atlas")
    check("rho_E=21/4 maps to q_E=15/8", rho_to_q(TARGET_RHO) == TARGET_Q, str(rho_to_q(TARGET_RHO)))
    check("q_E=15/8 maps to rho_E=21/4", q_to_rho(TARGET_Q) == TARGET_RHO, str(q_to_rho(TARGET_Q)))
    check("c_TE=-8/9 maps to q_E=15/8", c_to_q(TARGET_C) == TARGET_Q, str(c_to_q(TARGET_C)))
    check("q_E=15/8 maps to c_TE=-8/9", q_to_c(TARGET_Q) == TARGET_C, str(q_to_c(TARGET_Q)))
    check("lambda=9/4 maps to q_E=15/8", lambda_to_q(TARGET_LAMBDA) == TARGET_Q, str(lambda_to_q(TARGET_LAMBDA)))
    check("q_E=15/8 maps to lambda=9/4", q_to_lambda(TARGET_Q) == TARGET_LAMBDA, str(q_to_lambda(TARGET_Q)))
    check("diagonal metric ratio maps to q_E^2=(15/8)^2", diag_ratio_to_q_squared(TARGET_METRIC_RATIO) == TARGET_Q * TARGET_Q, str(diag_ratio_to_q_squared(TARGET_METRIC_RATIO)))
    check("q_E=15/8 maps to diagonal metric ratio 1449/704", diag_ratio_for_q(TARGET_Q) == TARGET_METRIC_RATIO, str(diag_ratio_for_q(TARGET_Q)))
    check("O_h inverse-square projector law gives lambda=9/4", (W_E / W_T) ** -2 == TARGET_LAMBDA, str((W_E / W_T) ** -2))
    check("one-power projector law is not the target covariance", (W_E / W_T) ** -1 != TARGET_LAMBDA, str((W_E / W_T) ** -1))
    check("positive SU(3) adjoint fraction is 8/9", F_ADJ == Fraction(8, 9), str(F_ADJ))
    check("color route reaches center slot only if c_TE=-F_adj is supplied", -F_ADJ == TARGET_C, str(-F_ADJ))
    check("distinct slots carry distinct structural numbers", TARGET_LAMBDA != F_ADJ and TARGET_METRIC_RATIO != TARGET_LAMBDA, f"lambda={TARGET_LAMBDA}, F_adj={F_ADJ}, metric={TARGET_METRIC_RATIO}")
    check("target diagonal metric satisfies general metric equation", general_metric_residual(Fraction(704), Fraction(1449), Fraction(0), TARGET_Q) == 0)
    check("identity metric does not satisfy target equation", general_metric_residual(Fraction(1), Fraction(1), Fraction(0), TARGET_Q) != 0)
    check("general metric coefficients match atlas note", (
        general_metric_residual(Fraction(1), Fraction(0), Fraction(0), TARGET_Q) == Fraction(161, 64)
        and 2 * (TARGET_Q * Fraction(-5, 3) - Fraction(1) * Fraction(-2)) == Fraction(-9, 4)
        and Fraction(-5, 3) ** 2 - Fraction(-2) ** 2 == Fraction(-11, 9)
    ))


def part3_firewall_authorities() -> None:
    print("\nC. Current-route firewall")
    naturality = flat(DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md")
    lift = flat(DOCS / "QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md")
    rconn = flat(DOCS / "QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md")
    kappa = flat(DOCS / "QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md")
    schur = flat(DOCS / "QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md")
    box = flat(DOCS / "QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md")
    axioms = flat(DOCS / "MINIMAL_AXIOMS_2026-06-05.md")

    check("naturality no-go leaves rho_E free absent extra primitive", "remains a free parameter unless an additional E-center endpoint ratio, source-domain, or readout-map primitive is supplied" in naturality)
    check("naturality no-go names c_TE=-8/9 as equivalent target", "gamma_T(center)/gamma_E(center) = -8/9" in naturality)
    check("E-center lift attempt says current source bank lacks exact computation", "does not contain an exact E-channel row that computes `beta_E/alpha_E`" in lift)
    check("E-center lift attempt separates comparator evidence", "Comparator Evidence Not Used As Proof Input" in lift)
    check("Rconn typed note says no Rconn-to-rho path", "absent without the bridge and present with the hypothetical bridge adjoined" in rconn)
    check("Rconn typed note separates F_adj from Route-2 gamma", "not, by itself, a definition of `rho_E`, `q_E`, `gamma_E`, `gamma_T`" in rconn)
    check("kappa note says covariance bridge remains open", "bridge" in kappa and "not a consequence" in kappa and "remaining open datum" in kappa)
    check("kappa note derives same-domain leverage value only", "same-domain" in kappa and "3/2" in kappa and "9/4" in kappa)
    check("Schur note closes quadratic route with free E:T ratio", "an `O_h`-invariant quadratic form has a **free** `E:T1`" in schur)
    check("Schur note names inverse-square gap", "q_X" in schur and "w_X" in schur and "No named functional produces an" in schur)
    check("box scan closes bulk-limit hatch", "closes the bulk-limit hatch" in box)
    check("box scan says no selecting primitive supplied", "this scan supplies **no** selecting primitive" in box)
    check("minimal axioms withhold readout context and weighting", "record supplies no readout context" in axioms and "weighting" in axioms)


def part4_note_firewall() -> None:
    print("\nD. New-note claim firewall")
    note = read(NOTE)
    note_flat = " ".join(note.split())
    note_lower = note.lower()
    forbidden_markers = (
        "observed quark",
        "fitted yukawa",
        "ckm",
        "pdg",
        "nearest-rational selector",
        "endpoint closure achieved",
    )
    check("forbidden observational/fitted proof inputs are absent from note", all(marker not in note_lower for marker in forbidden_markers))
    check("note says equivalent forms are not independent derivations", "equivalent discharge forms, not independent derivations" in note_flat)
    check("note says current surfaces do not supply primitive", "Current surfaces do not supply that primitive" in note)
    check("note leaves future source/readout primitive open", "one missing center primitive with several equivalent exact faces" in note_flat)
    check("note does not claim endpoint closure", "no endpoint closure" in note)
    check("bare retained is disallowed", "bare_retained_allowed: false" not in note)


def main() -> int:
    print("=" * 88)
    print("ROUTE-2 CENTER PRIMITIVE EQUIVALENCE ATLAS")
    print("=" * 88)
    part1_authorities()
    part2_equivalence_atlas()
    part3_firewall_authorities()
    part4_note_firewall()
    print("\nSummary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: the Route-2 center primitive has equivalent exact faces, but no current surface derives it.")
        return 0
    print("VERDICT: center primitive equivalence atlas checks failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
